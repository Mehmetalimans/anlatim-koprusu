# İrem / Claude için kabul devri

**17 Ekim 2026 | Grup 14 | Anlatım Köprüsü**

İrem'in `codex/app` dalındaki `3e9a4ac` teslimi, Mehmet Ali'nin içerikleriyle **`codex/acceptance`** dalında birleştirildi. İrem'in dalına doğrudan değişiklik gönderilmedi. Python + Streamlit, ortak veri modelleri ve servis imzaları korunuyor.

## Hazır olanlar

- `content/fizik2_potansiyel.json`, `content/econ100_firsat_maliyeti.json`, `content/python_for_range.json`: yükleyicinin beklediği `LessonContent` alanlarıyla üç özgün metin. Üçü de uygulamada seçilebiliyor.
- Toplu `content/demo_inputs.json`, yükleyiciye ders gibi görünmemesi için **`evaluation/demo_inputs.json`** konumuna taşındı. Değerlendirme araçları güncellendi.
- İrem'in testleri ve bağımsız testler birlikte **68/68 geçti**. Ağ kapatılarak çalıştırıldı; canlı model testi değildir.
- Temiz kurulum ve gerçek tarayıcıda etiketli geliştirme verisiyle cevap akışı denendi.
- Kaynak/açıklama yan yana, kod ve matematik gösterimi düzenlendi. Mod veya geliştirme sonucu türü değişince eski çalışma temizleniyor. Üç regresyon önce başarısız testlerle yeniden üretildi.
- Prompt örneği kaynakla uyumlu hale getirildi; yeterli gerekçede boş iyileştirme listesine izin verildi. Sabit Python geri bildirimindeki koşul netleştirildi.
- İki sayfalık rapor ve altı slaytlık İngilizce sunum v2, çevrimdışı sonuçlarla güncellendi.

## İlk adımlar

1. `git status` ile kendi yerel değişikliklerini kontrol et; kaydedilmemiş işin üzerine yazma. `git fetch origin` sonrası `codex/acceptance` dalını incele. Devam eden `codex/app` çalışmasını bununla uzlaştır; eski dosyaları körlemesine kopyalama.
2. [Kabul kaydını](../evaluation/Kabul_Sonuclari_20261017.md) ve `evaluation/test_acceptance_offline.py` dosyasını oku. Aynı 68 testi çalıştır; ortak sözleşmeyi yeniden tasarlama.
3. Yerel `.env` ile gerçek API erişimini doğrula. Anahtarı sohbete, commit'e veya videoya ekleme. Varsayılan `gemini-3.5-flash-lite` doğrulanmadı; erişebildiğin gerçek model adını kaydet, gerekirse `GEMINI_MODEL` ayarını düzelt.

```powershell
python scripts/check_gemini.py --content content/econ100_firsat_maliyeti.json
python scripts/check_gemini.py --content content/fizik2_potansiyel.json
python scripts/check_gemini.py --content content/python_for_range.json
```

Betikteki hazır gerekçe, modelin yeni sorusuyla uyuşmayabilir. Betiği bağlantı/şema kontrolü için kullan; otomatik anlam doğruluğu kanıtı sayma. Arayüzde üretilen soruyu okuyup o soruya uygun cevap ve gerekçe yaz.

## Canlı görevler — öncelik sırasıyla

1. **Erişim kanıtı:** gerçek model adı, commit, zaman, prompt sürümü, başarılı üretim ve geri bildirim adımları. Anahtar içermeyen kayıt ver. Anahtar almak başarılı çağrı kanıtı değildir.
2. **Üç ders:** her birinde açıklama, referanslar, ek örnek ve dört seçenekli soru üret. Fizikte işaret/birim, ekonomide en iyi alternatif, Python'da girinti/bitiş sınırını kontrol et. Tek doğru seçenek olduğundan emin ol.
3. **Gerekçeye duyarlı değerlendirme:** doğru şık/doğru gerekçe; yanlış/yanlış; doğru/yanlış; yanlış şık/doğru ilke kombinasyonları. Şık sonucu koddan, geri bildirim gerçek gerekçeden gelmeli. Sabit geliştirme geri bildirimi bu testi karşılamaz. Kontrollü sorular için `evaluation/feedback_reference_cases.json` kullanılabilir; canlı soruya eski cevapları uygulama.
4. **Prompt karşılaştırması:** aynı üç metinde aynı modelle zero-shot ve örnekli sürümü çalıştır. Gerçek sürüm adlarını kaydet. `evaluation/prompt_comparison_records.json` dosyasını gerçek çıktı ve gözlemlerle doldur.
5. **Yetersiz bağlam ve talimat içeren metin:** kontrollü testlere ek olarak gerçek model davranışını incele. Hataları ve başarısız denemeleri de kaydet.

Devir yanıtında değişen dosyalar, commit/model adı, gerçekten çalıştırılan kontroller, anahtar içermeyen sonuç kayıtları ve kalan sorunlar bulunmalı. Yapılmayan canlı testler açıkça bekleyen kalmalı.

## Mehmet Ali'nin devamı

Gerçek çıktılar gelince anlam/kabul incelemesi, belgelerin son sürümü, İngilizce prova ve video tamamlanacak. Güncel dosyalar [teslim dizininde](../delivery/README.md). Yeni özellik açmadan ana akış ve canlı kabul tamamlanmalı.

## Claude'a kopyalanacak başlangıç

> Ben İrem. Anlatım Köprüsü için teknik görevleri sürdürüyoruz. Mehmet Ali `codex/app` teslimimizi `codex/acceptance` dalında içerik ve bağımsız kabul düzeltmeleriyle birleştirdi. Önce güncel dalı, `docs/Irem_Kabul_Devir_Notu.md` ve `evaluation/Kabul_Sonuclari_20261017.md` dosyalarını incele; 68 çevrimdışı testin kapsamını koru. Fikir seçimini yeniden başlatma, ortak sözleşmeyi tek taraflı değiştirme ve içerikleri eski toplu şemaya döndürme. Önceliğin kendi yerel anahtarımızla gerçek API erişimini, üç dersin içerik doğruluğunu, gerekçeye duyarlı geri bildirimi ve iki promptun karşılaştırmasını kaydetmek. Anahtar aldıysak bunu başarılı çağrı sayma; gerçek model ve sonuç kaydı oluştur. Anahtarı paylaşma. Yapılanları ve kalan sorunları gerçek test kanıtlarıyla bildir.
