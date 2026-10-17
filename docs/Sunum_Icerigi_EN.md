# Anlatım Köprüsü - English presentation copy

Group 14 | 17 October 2026 | Evidence snapshot: app commit 06a6c25

## 1. Anlatım Köprüsü

Academic language, explained in context

Group 14  |  SDG 4

Hackathon prototype | 17 October 2026

Speaker notes: Anlatım Köprüsü, Group 14. University students aged 18 and over. Turkish interface and learning output. Python + Streamlit. Evidence snapshot: app commit 06a6c25, 17 October 2026. Model access is recorded on Irem’s computer; learning gains have not been measured. Repository: https://github.com/Mehmetalimans/anlatim-koprusu/tree/codex/acceptance

## 2. A phrase can block understanding

ACADEMIC EXPRESSION

“The value of the best alternative forgone.”

If Deniz chooses studying and would otherwise choose the concert, the concert is the alternative he gives up.

Students can enter their own source text and select a phrase.

Speaker notes: The economics example illustrates the problem; it is team-authored, not a live AI screenshot. A student may know the topic but struggle with academic wording. Intended SDG contribution: understandable learning support; need has not been validated in a student study. Source: https://openstax.org/books/principles-economics-3e/pages/2-1-how-individuals-make-choices-based-on-their-budget-constraint

## 3. The learning cycle

01

Enter a source text and choose a phrase

02

Read the explanation and source references

03

Apply the idea in a new question

04

Write a reason and review the feedback

Feedback addresses the selected answer and the written reason.

Speaker notes: The app supports custom text up to 6000 characters as well as three prepared examples. Select Kendi metnim and enter a source context plus a phrase found once within it. generate_bridge creates explanation, terms, generated example and quiz. evaluate_attempt comments on the rationale; code computes the chosen-option outcome from the model-generated key. Human review of keys remains necessary. Source: app.py, core/services.py and core/contracts.py. Latest generation and latest feedback revisions have not been recorded end-to-end on the same new questions; complete that manual live check before the demo. No user code is executed.

## 4. One workflow across three subjects

Physics 2

Potential and potential energy
Preserve units and charge signs.

ECON 100

Opportunity cost
Identify the best forgone alternative.

Basic Python

for loops and range
Preserve indentation and stop boundaries.

Speaker notes: Three prepared lesson inputs load in the app; custom texts are also accepted. Final generation comparison contains one run for each subject/prompt pair. Physics answer explanations still include one U-versus-energy-change wording problem, and a negative-charge sign question has not been sampled. Sources: https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference ; https://openstax.org/books/principles-economics-3e/pages/2-1-how-individuals-make-choices-based-on-their-budget-constraint ; https://docs.python.org/3/tutorial/controlflow.html#the-range-function . Live evidence: evaluation/live/live_gen_20261017_181507_prompt_r2.json

## 5. Model and prompt design

Gemini model

gemini-3.5-flash-lite

Explanation and question

Feedback on the written reason

Prompt comparison

Same three source texts.

Zero-shot vs one example.

One run per subject and version.

Both produced valid answer keys in this small sample; no overall winner.

Speaker notes: Shared live logs identify gemini-3.5-flash-lite, temperature 0.4, structured output. The repository labels the example-based variant few_shot and uses one osmosis example outside the demo subjects. Sources: core/prompts.py, evaluation/prompt_comparison_records.json and evaluation/Canli_Sonuclar_20261017.md. Final comparison is 3 subjects x 2 prompt versions = 6 calls, one per cell. Review found no answer-key accuracy difference in this sample; the example-based version produced shorter questions. Do not generalize. First revision physics questions copied a definition; r2 requires transfer to a new situation. Feedback r2 adds source text to the data payload. Texts with instructions are treated as data. Schema validation checks structure, not semantic truth.

## 6. Evidence and responsible use

Test evidence

69 automated tests passed.

16 generation + 50 feedback records.

Risks and safeguards

AI can miss faulty reasoning.

Show sources and review keys.

Keep the API key local.

SDG 4: support access to understandable learning materials

One of six faulty reasons was missed in a live subset.
Learning gains have not been measured.

Speaker notes: Independent rerun on commit 06a6c25: 69 automated tests pass with network blocked and recorded/simulated outputs; this is not a model accuracy score. Irem’s logs contain 16 generation and 50 feedback records over two revisions, with a separate connectivity check. In the latest 25 feedback records the code outcome matches the key 25/25; the correct-option/wrong-rationale subset detects the error 5/6, missing an economics list-position justification. A physics answer explanation also confuses U and energy change wording. Latest generation and latest feedback need a combined new-question live check. Source-injection answer-letter effect was inconclusive because requested and correct letters were both A. These are known limits, not hidden failures. Generated examples are labelled; development fixtures are labelled and are not live results. Personal/confidential notes are not demo inputs. The prototype gives no general student competency score. Intended SDG link: equal access to quality tertiary education, target 4.3. Source: https://sdgs.un.org/goals/goal4 ; evidence: evaluation/Canli_Sonuclar_20261017.md and evaluation/live/. A student study is future work.
