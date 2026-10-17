"""Check authored materials and delivery files. Never call a model or execute user code."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from urllib.parse import unquote, urlsplit
import argparse
import hashlib
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def run_checks():
    checks = []

    def check(name, passed, detail):
        checks.append({'name': name, 'passed': bool(passed), 'detail': detail})

    def load(relative):
        return json.loads((ROOT / relative).read_text(encoding='utf-8'))

    source_file = ROOT / 'content/Demo_Icerikleri_v1.md'
    markdown = source_file.read_text(encoding='utf-8')
    originals = re.findall(r'### Kaynak metin\n\n(.*?)\n### Beklenen anlam', markdown, re.S)
    data = load('evaluation/demo_inputs.json')
    items = data['items']
    check('demo_count', len(items) == 3, 'Three prepared course inputs')
    ids = [item['id'] for item in items]
    check('unique_demo_ids', len(ids) == len(set(ids)), ids)
    check('markdown_source_count', len(originals) == len(items), len(originals))

    for index, item in enumerate(items):
        request = item['request']
        source = request['source_text']
        phrase = request['selected_phrase']
        prose = re.sub(r'```.*?```', '', source, flags=re.S)
        count = len(prose.split())
        check(item['id'] + ':word_limit', 120 <= count <= 200, count)
        check(item['id'] + ':source_limit', 0 < len(source) <= 6000, len(source))
        check(item['id'] + ':single_phrase', bool(phrase) and source.count(phrase) == 1, phrase)
        check(item['id'] + ':markdown_match', index < len(originals) and source == originals[index].strip(), 'JSON matches the authored Markdown source')
        check(item['id'] + ':source_urls', bool(item['sources']) and all(urlsplit(s['url']).scheme == 'https' for s in item['sources']), 'URL syntax only, not remote access')

    content_record = load('evaluation/Icerik_Kontrol_Sonuclari_v2.json')
    canonical = source_file.read_bytes().replace(b'\r\n', b'\n')
    check('content_record_hash', hashlib.sha256(canonical).hexdigest() == content_record['content_file_sha256'], 'Normalize CRLF to LF before checking')

    references = load('evaluation/feedback_reference_cases.json')['cases']
    check('feedback_demo_ids', {c['demo_id'] for c in references} == set(ids), 'Each course has a reference question')
    attempt_count = 0
    attempt_ids = []
    for case in references:
        quiz = case['bridge_fixture']['quiz']
        option_ids = [o['id'] for o in quiz['options']]
        check(case['demo_id'] + ':option_ids', len(option_ids) == 4 and set(option_ids) == set('ABCD'), option_ids)
        check(case['demo_id'] + ':key_present', quiz['correct_option_id'] in option_ids, quiz['correct_option_id'])
        combinations = set()
        for attempt in case['attempts']:
            attempt_count += 1
            attempt_ids.append(attempt['id'])
            computed = attempt['selected_option_id'] == quiz['correct_option_id']
            reason_good = attempt['rationale_assessment'] == 'conceptually_correct'
            combinations.add((computed, reason_good))
            check(attempt['id'] + ':option_outcome', computed == attempt['expected_is_correct'], 'Reference key comparison only, not the app implementation')
            check(attempt['id'] + ':reason_limit', 0 < len(attempt['rationale'].strip()) <= 1000, len(attempt['rationale']))
            check(attempt['id'] + ':not_run', attempt['execution_status'] == 'not_run', 'No app or model execution claimed')
        check(case['demo_id'] + ':all_combinations', combinations == {(True, True), (True, False), (False, True), (False, False)}, 'Four choice/reason combinations')
    check('feedback_attempt_count', attempt_count == 12, attempt_count)
    check('unique_attempt_ids', len(attempt_ids) == len(set(attempt_ids)), len(attempt_ids))

    inputs = load('evaluation/input_reference_cases.json')['cases']
    check('input_scenario_count', len(inputs) == 12, len(inputs))
    check('unique_input_ids', len({c['id'] for c in inputs}) == len(inputs), len(inputs))
    by_id = {c['id']: c for c in inputs}
    for id_, length in [('source_exactly_6000', 6000), ('source_6001', 6001)]:
        check(id_ + ':fixture_length', len(by_id[id_]['request']['source_text']) == length, length)
    check('input_scenarios_pending', all(c['execution_status'] == 'not_run' for c in inputs), 'Fixtures are specified expectations, not app test results')
    check('code_blank_line_fixture', '\n\nprint("bitiş")' in by_id['fenced_code_blank_line']['request']['source_text'], 'A blank line remains inside the code fence')

    comparisons = load('evaluation/prompt_comparison_records.json')['records']
    expected_pairs = {(id_, variant) for id_ in ids for variant in ['zero_shot', 'with_example']}
    check('comparison_grid', len(comparisons) == 6 and {(c['demo_id'], c['prompt_variant']) for c in comparisons} == expected_pairs, 'Six planned real runs')
    check('comparisons_live', all(c['execution_status'] == 'run_live' and c['actual_output'] is not None
                                  and (ROOT / c['log_file']).is_file() for c in comparisons),
          'Filled only from key-free live logs in evaluation/live')
    for c in comparisons:
        if c.get('actual_output'):
            log = load(c['log_file'])
            variant = 'few_shot' if c['prompt_variant'] == 'with_example' else 'zero_shot'
            match = [x for x in log['cases'] if x['case_id'] == c['demo_id'] and x['prompt_version'] == variant]
            check(c['id'] + ':matches_log', bool(match) and match[0]['result'] == c['actual_output'], 'Output copied verbatim from log')
    live_text = ' '.join(f.read_text(encoding='utf-8') for f in (ROOT / 'evaluation' / 'live').glob('*.json'))
    check('live_logs_no_key', not re.search(r'AIza[0-9A-Za-z_-]{10,}|AQ\.[0-9A-Za-z_-]{20,}', live_text), 'No API key in live logs')

    folders = ['content', 'docs', 'evaluation', 'delivery']
    local_links = []
    missing_links = []
    for folder in folders:
        for file in (ROOT / folder).glob('*.md'):
            for href in re.findall(r'!?\[[^\]\n]+\]\(([^)\n]+)\)', file.read_text(encoding='utf-8')):
                href = href.strip('<>')
                if href.startswith(('http:', 'https:', 'mailto:', '#')):
                    continue
                relative = unquote(href.split('#', 1)[0])
                if not relative:
                    continue
                target = file.parent / relative
                local_links.append(str(file.relative_to(ROOT)) + ':' + href)
                if not target.exists():
                    missing_links.append(str(file.relative_to(ROOT)) + ':' + href)
    check('local_document_links', not missing_links, {'checked': len(local_links), 'missing': missing_links})

    pdf = ROOT / 'delivery/Anlatim_Koprusu_Proje_Raporu.pdf'
    try:
        from pypdf import PdfReader
        reader = PdfReader(pdf)
        check('report_page_count', 1 <= len(reader.pages) <= 2, len(reader.pages))
        report_text = '\n'.join(page.extract_text() or '' for page in reader.pages)
        check('report_identity', 'Anlatım Köprüsü - Proje Raporu' in ' '.join(report_text.split()), 'Current report identity')
    except ImportError:
        check('report_pdf_reader', False, 'Install pypdf or use the documented bundled Python runtime')

    pptx = ROOT / 'delivery/Anlatim_Koprusu_English_Presentation.pptx'
    with zipfile.ZipFile(pptx) as z:
        slides = [n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', n)]
        notes = [n for n in z.namelist() if re.fullmatch(r'ppt/notesSlides/notesSlide\d+\.xml', n)]
        check('presentation_slide_count', len(slides) == 6, len(slides))
        check('presentation_notes_count', len(notes) == 6, len(notes))
        check('presentation_xml', all(ET.fromstring(z.read(n)) is not None for n in slides + notes), 'XML parses; visual QA is separate')

    script = (ROOT / 'docs/Demo_Konusmasi_EN_v2.md').read_text(encoding='utf-8')
    spoken = ' '.join(line[2:].strip() for line in script.splitlines() if line.startswith('> '))
    timing = load('evaluation/Prova_Sure_Tahmini_v2.json')
    check('script_word_count', len(spoken.split()) == timing['current_word_count'], len(spoken.split()))
    check('timing_not_measured', 'Estimate only' in timing['timing_status'], 'Word-count estimate only')

    return {
        'checked_at_istanbul': datetime.now(timezone(timedelta(hours=3))).isoformat(),
        'scope': 'Authored data and delivery integrity only. No live model, app flow, semantic scoring or student learning test.',
        'all_passed': all(c['passed'] for c in checks),
        'check_count': len(checks),
        'failed_count': sum(not c['passed'] for c in checks),
        'checks': checks,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', help='Optional JSON result file, relative to repository root')
    args = parser.parse_args()
    try:
        result = run_checks()
    except (KeyError, ValueError, OSError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f'Materials check could not complete: {exc}', file=sys.stderr)
        return 2
    if args.report:
        target = (ROOT / args.report).resolve()
        if not target.is_relative_to(ROOT):
            print('Report path must stay inside the repository.', file=sys.stderr)
            return 2
        target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Material integrity checks: {result['check_count'] - result['failed_count']}/{result['check_count']} passed.")
    print(result['scope'])
    for check in result['checks']:
        if not check['passed']:
            print('FAILED:', check['name'], check['detail'])
    return 0 if result['all_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
