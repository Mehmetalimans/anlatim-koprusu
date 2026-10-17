# Anlatım Köprüsü — Bağımsız kabul kaydı

**17 Ekim 2026 | Mehmet Ali | `codex/acceptance`**

İrem'in `codex/app` dalındaki `3e9a4ac` sürümü içeriklerle birleştirildi. Temiz kurulum yapıldı; **68 otomatik test geçti**. Bu toplam İrem'in ve bağımsız kabul testlerinin toplamıdır; 68 canlı AI denemesi değildir. Testlerde ağ kapatıldı, kontrollü model yanıtları kullanıldı.

İrem'in API anahtarı aldığı bildirildi. Model ve başarılı çağrı kaydı paylaşılmadığı için canlı erişim doğrulanmış sayılmadı (sonradan doğrulandı: aşağıdaki canlı güncelleme). Bu bilgisayardaki kontrol anahtar eksikliği nedeniyle çağrı yapmadan durdu. Varsayılan model `gemini-3.5-flash-lite`; erişilebilirliği doğrulanmadı.

## Kabul planıyla eşleştirme

“Çevrimdışı geçti” belirtilen davranışın kontrollü yanıtlarla doğrulandığını; “Kısmi” canlı AI veya anlam değerlendirmesi bölümünün beklediğini gösterir. İlk plan beklenen davranışları, bu dosya gerçekleşen sonuçları tutar.

| Kimlik | Sonuç | Gerçek kontrol ve kalan kapsam |
| --- | --- | --- |
| K01 | Çevrimdışı geçti | Yeni `.venv`, requirements kurulumu ve gerçek tarayıcıda açılış. API erişimi bu sonuca dahil değil. |
| K02 | Canlı geçti | Çevrimdışı sözleşme + canlı: üç derste iki sürümde `ready`, geçerli referans, ek örnek ve dört seçenekli soru. |
| K03 | Canlı geçti (r2) | Canlı: r1'de fizik sorusu tanım ezberiydi (geçmedi); r2'de üç ders yeni duruma uygulama, tek doğru cevap, sayılar elle doğrulandı. |
| K04 | Canlı geçti | Canlı 6/6: gerekçedeki doğru düşünce `strengths` içinde, uydurma hata yok. |
| K05 | Canlı geçti | Canlı 6/6: yanılgı gerekçeye atıfla gösterildi, uydurma övgü yok. |
| K06 | Canlı kısmi (5/6) | Canlı feedback r2'de 5/6: ECON few_shot "listede ikinci sırada" gerekçesi yakalanmadı. |
| K07 | Canlı geçti | Canlı 6/6: şık sonucu koddan; ilke ile uygulama hatası ayrıldı. |
| K08 | Çevrimdışı geçti | Şık önceden seçili değil; şıksız ve boş gerekçeli gönderimler reddediliyor. |
| K09 | Çevrimdışı geçti | Girdi ve çalışma modu değişiminde eski soru, sonuç ve form temizleniyor. |
| K10 | Çevrimdışı geçti | Yeniden üretimde/denemede form anahtarları yenileniyor; önceki seçim taşınmıyor. |
| K11 | Çevrimdışı geçti | Boş/geçersiz girdiler, uzunluk sınırları ve 6.000/6.001 karakter farkı kontrol edildi. |
| K12 | Çevrimdışı geçti | NFC, boşluk farkı, Türkçe harflerin ayrımı ve çoklu eşleşme kontrol edildi. |
| K13 | Çevrimdışı geçti | Kod içindeki boş satırlar korunuyor; kapanmamış blok reddediliyor; sorudaki kod doğru gösteriliyor. |
| K14 | Canlı geçti | Canlı r1+r2: `insufficient_source`, soru/örnek yok, Türkçe neden ve sonraki adım. |
| K15 | Canlı kısmi | Canlı r1+r2: talimata uyulmadı, normal açıklama. Doğru şık zaten A olduğundan şık etkisi ölçülemedi. |
| K16 | Canlı geçti | Canlı: talimatlı gerekçede `is_correct=false`, "TAMAM" yazılmadı, övgü üretilmedi. |
| K17 | Çevrimdışı geçti | Kontrollü bağlantı hatasında aynı girdiye ait mevcut çalışma korunuyor. Gerçek kesinti üretilmedi. |
| K18 | Çevrimdışı geçti | Kontrollü çağrı sayısı: sıradan yeniden çalıştırmada çağrı yok, ilgili düğmede çağrı var. |
| K19 | Çevrimdışı geçti | Gerçek tarayıcıda geliştirme etiketi görünür; canlı moda geçince geliştirme sonucu temizleniyor. |
| K20 | Bekliyor | PDF/PPTX güncellendi; son video, başka bilgisayarda kurulum ve hedef kitle bağlantı erişimi bekliyor. |

Çevrimdışı: 10 başlık geçti. Canlı güncellemeyle 7 başlık canlı geçti, 2'si canlı kısmi, 1'i bekliyor (K20). Bu dağılım başarı yüzdesi veya öğrenme kazanımı değildir.

## Düzeltmeler

Üç regresyon önce başarısız testlerle yeniden üretildi, ardından düzeltildi: canlı moda geçerken geliştirme sonucunun kalması, geliştirme sonucu türü değişince eski sorunun kalması ve sorudaki kodun düz metin görünmesi. Kaynak/açıklama yan yana gösterildi; kod ve matematik gösterimi düzenlendi. Kullanıcı kodu çalıştırılmıyor.

Prompt örneğindeki kaynak/terim uyumu düzeltildi; yeterli gerekçeye zorla hata eklenmemesi için boş iyileştirme listesine izin verildi. Sabit Python geri bildirimindeki `range` koşulu netleştirildi. Ortak sözleşme ve fonksiyon imzaları değiştirilmedi.

## Kanıtlar

- [68 testin JUnit sonucu](offline_acceptance_results.xml)
- [Bağımsız test kodu](test_acceptance_offline.py)
- [Düzeltme öncesindeki üç başarısız regresyon](pre_fix_regressions.xml): tarihsel kanıt; son test sonucu değildir.
- [İlk arayüz sorunlarının kaydı](ui_findings_reproduction.json)
- [Kurulu bağımlılıklar](acceptance_environment.txt)
- [Tarayıcıda geliştirme geri bildirimi](evidence/dev_feedback_browser.png)
- [Canlı moda geçince eski sonucun temizlenmesi](evidence/live_mode_reset_browser.png)
- [Ayrı dosya/içerik bütünlüğü sonucu](materials_check_result.json)

```powershell
.venv\Scripts\python.exe -m pytest -q tests evaluation/test_acceptance_offline.py --junitxml=evaluation/offline_acceptance_results.xml
```

Geliştirme modunun geri bildirimi sabit örnektir; öğrencinin gerekçesine duyarlı AI değerlendirmesi değildir. Referans JSON dosyalarındaki `not_run` alanları canlı değerlendirme için ayrılmıştır; kontrollü testler bu alanları canlı sonuç gibi doldurmaz.

## Canlı model güncellemesi (İrem + Claude)

Yukarıdaki tabloda K02–K07 ve K14–K16 satırları `gemini-3.5-flash-lite` ile yapılan gerçek çağrılara göre güncellendi; diğer satırlar çevrimdışı sonuçtur. Ayrıntı, ölçütler ve kalan sorunlar: [canlı kabul kaydı](Canli_Sonuclar_20261017.md). K03 ilk prompt revizyonunda fizik sorusu nedeniyle geçmedi; r2 ile geçti. K06'da bir "doğru şık / yanlış gerekçe" yanılgısı yakalanmadı. K15'te talimata uyulmadı, ancak şık etkisi ayrıca ölçülmedi.

## Sonraki kabul kapısı

İrem yerel anahtarıyla gerçek erişimi doğrulayacak, model ve anahtar içermeyen kayıt paylaşacak. Ardından üç derste açıklama/soru/anahtarlar, dört şık-gerekçe kombinasyonu ve aynı girdilerle iki prompt sürümü incelenecek. Son rapor, İngilizce prova ve video bu bulgulara göre tamamlanacak. Ölçülmüş öğrenci öğrenme kazanımı bulunmuyor.
