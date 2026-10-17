# Anlatım Köprüsü

Üniversite öğrencilerinin zorlandıkları akademik ifadeleri kaynağa bağlı sade açıklama, terim kartları,
üretilmiş ek örnek ve dört seçenekli uygulama sorusuyla anlamalarına yardımcı olan Streamlit prototipi
(Grup 14, SDG 4). Arayüz ve çıktılar Türkçedir.

## Kurulum

Python 3.10+ gerekir.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate     macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### Gemini API anahtarı (yerel)

1. https://aistudio.google.com/apikey adresinde Google hesabıyla oturum açıp **Create API key** ile anahtar oluşturun.
   Kullanılacak modelin erişimini ve ücretsiz kota durumunu kendi projenizde doğrulayın; mevcut kota bu repoda doğrulanmış değildir.
2. Proje klasöründe `.env.example` dosyasını `.env` adıyla kopyalayın, `GEMINI_API_KEY=` satırının sonuna anahtarı yapıştırın.
3. Anahtarı sohbete, repoya, ekran kaydına yazmayın. `.env` dosyası `.gitignore` ile hariç tutulur.

Demo için kişisel/gizli veri kullanmayın. Kullanılan hizmetin güncel veri koşullarını ve kota sınırlarını
hesabınız üzerinden kontrol edin. `GEMINI_MODEL` varsayılanı bu bilgisayarda gerçek çağrıyla doğrulanmadı.

## Çalıştırma

```bash
python scripts/check_gemini.py   # gerçek API erişim + uçtan uca deneme; sonucu tech_logs/ altına yazar
streamlit run app.py             # tarayıcıda http://localhost:8501 açılır (yerel adres, herkese açık değil)
python -m pytest -q              # teknik testler (alternatif: python -m unittest discover -s tests)
```

Kenar çubuğundaki **Geliştirme verisi** modu modeli çağırmaz; etiketli örnek sonuç gösterir
(“GELİŞTİRME VERİSİ — canlı AI sonucu değildir”). Bu mod canlı model testi sayılmaz.

Geliştirme sonucu sabit Python örneğidir; seçilen başka metne göre yeni çıktı üretmez.
Geri bildirim de sabit örnektir ve yazılan gerekçeyi AI ile değerlendirmez.

## Kabul durumu — 17 Ekim 2026

Üç ders `content/` içinden yükleniyor; **Kendi metnim** ile yeni kaynak ve ifade de girilebiliyor.
Son uygulama sürümünde (`06a6c25`) kontrollü yanıtlarla **69 otomatik test** geçti.
İrem'in paylaştığı canlı kayıtlarda `gemini-3.5-flash-lite` ile 16 üretim ve 50 geri bildirim bulunur;
üç derste zero-shot/örnekli prompt karşılaştırması yapıldı. Bir yanlış gerekçenin övülmesi,
bir fizik açıklamasında U/enerji değişimi ifadesi ve son revizyonların aynı yeni soruda uçtan uca
denenmemiş olması bilinen sınırlardır. Öğrenme kazanımı ölçülmedi. Ayrıntılar:
[kabul kaydı](evaluation/Kabul_Sonuclari_20261017.md),
[İrem/Claude için devir](docs/Irem_Kabul_Devir_Notu.md),
[güncel rapor ve sunum](delivery/README.md).

```bash
python -m pytest -q tests evaluation/test_acceptance_offline.py --junitxml=evaluation/offline_acceptance_results.xml
```

`scripts/check_gemini.py` bağlantı ve çıktı biçimini kontrol eder. Hazır gerekçesi yeni üretilen soruyla
uyuşmayabileceğinden içerik/geri bildirim doğruluğu ayrıca gerçek soru üzerinden incelenmelidir.

Canlı kabul için `scripts/live_eval.py` kullanılır: `gen` üç derste zero_shot/few_shot üretimi ile yetersiz kaynak ve
talimat içeren kaynak denemesini kaydeder; `template` gerçek sorulara göre doldurulacak gerekçe dosyasını üretir;
`feedback` doldurulan gerekçeleri değerlendirir. Kayıtlar `tech_logs/` altına yazılır (repoya girmez); paylaşılan
anahtarsız kayıtlar ve sonuçlar `evaluation/live/` ve [canlı kabul kaydı](evaluation/Canli_Sonuclar_20261017.md) içindedir.

## Yapı

```text
app.py                  Streamlit uygulaması (girdiler form dışında; cevap formu st.form içinde)
core/contracts.py       Pydantic sözleşmesi: BridgeRequest, BridgeResult, AttemptFeedback, LessonContent, hata kodları
core/source.py          Kaynak bölme (P1, P2…; ``` kod blokları tek parça) ve ifade eşleşmesi
core/prompts.py         İki prompt sürümü (zero_shot / few_shot) ve Gemini yanıt şemaları
core/gemini_client.py   Gemini REST istemcisi (standart kütüphane; anahtar başlıkta)
core/services.py        generate_bridge, evaluate_attempt, API öncesi girdi kontrolleri
core/content_loader.py  content/*.json derslerini yükler; yoksa geliştirme taslağına düşer
ui/state.py             Oturum: parmak izi, girdi değişince sıfırlama, cevap formu nonce'u
ui/views.py             Görüntüleme (kullanıcı metni HTML olarak işlenmez, kod çalıştırılmaz)
fixtures/               Etiketli geliştirme verisi (ready / insufficient_source / geri bildirim / taslak girdi)
scripts/check_gemini.py IR-02 erişim denemesi
scripts/live_eval.py    Canlı üretim / gerekçe / prompt karşılaştırma kaydı
tests/test_core.py      Teknik testler
```

## Temel kurallar (v2 belgesi §5–6)

- `is_correct`, seçilen kimlik ile `correct_option_id` karşılaştırılarak **kodda** hesaplanır; model metni bunu değiştiremez.
- Model çıktısı Pydantic ile doğrulanır; geçersiz `source_refs` veya biçim hatasında bir kez yeniden denenir, sonra `invalid_output`.
- İfade eşleşmesi: düzyazıda NFC + boşluk sadeleştirme; harf büyüklüğü ve tırnaklar değiştirilmez; kodda yalnızca satır sonları eşitlenir.
  Birden çok eşleşmede ve eşleşme yokluğunda API çağrılmadan uyarı verilir.
- Kaynak ve gerekçe modele JSON **veri** olarak gönderilir; sistem talimatı kullanıcı metni içermez.
- Hata kodları: `invalid_input`, `missing_key`, `quota`, `network`, `invalid_output` — kullanıcıya Türkçe mesaj, ham hata/anahtar gösterilmez.
- Gerekçe: boş olamaz, en fazla 1.000 karakter. Kaynak: en fazla 6.000 karakter.

## İçerik şeması (content/*.json — Mehmet Ali)

Her ders ayrı bir `.json` dosyasıdır. Örnek: `fixtures/dev_input_python.json`.

| Alan | Tür | Öğrenciye gösterilir mi |
| --- | --- | --- |
| `id` | küçük harf, rakam, `_` `-` | hayır |
| `subject_label` | metin (≤80) | evet |
| `title` | metin (seçim listesinde görünür) | evet |
| `source_text` | metin (≤6.000); kod ``` satırları arasında | evet |
| `selected_phrase` | metin (≤500); kaynakta **tam bir kez** geçmeli | evet (ön dolu) |
| `sources` | `[{"title": ..., "url": ...}]` | hayır (rapor için) |
| `expected_meaning` | metin | hayır |
| `invariants` | metin listesi | hayır |
| `correct_rationale` / `incorrect_rationale` | metin | hayır (`check_gemini.py --content` ile kullanılır) |

Kaynakta Türkçe karakterler ve tırnaklar seçilen ifadeyle birebir aynı olmalıdır. `content/` boşsa uygulama geliştirme taslağını gösterir;
bozuk dosyalar kenar çubuğunda hata olarak listelenir.
