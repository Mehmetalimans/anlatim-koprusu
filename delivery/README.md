# Teslim hazırlığı — Çevrimdışı kabul sonrası taslak v2

İrem'in `3e9a4ac` uygulama teslimi üç ders içeriğiyle birleştirildi. Temiz kurulum ve **68 çevrimdışı otomatik test** tamamlandı. Canlı API erişimi, gerçek model anlam incelemesi, prompt karşılaştırması ve video bekliyor. PDF/PPTX son teslim sürümü değildir.

## Güncel dosyalar

- [İki sayfalık Türkçe rapor v2](Anlatim_Koprusu_Rapor_Taslagi_v2.pdf)
- [Altı slaytlık İngilizce sunum v2](Anlatim_Koprusu_English_Deck_Draft_v2.pptx)
- [Raporun düzenlenebilir metni](../docs/Rapor_Taslagi_v2.md)
- [Sunum metni ve notları](../docs/Ingilizce_Sunum_Metni_v2.md)
- [Kabul sonuçları ve bekleyen kapsam](../evaluation/Kabul_Sonuclari_20261017.md)
- [İrem / Claude için sonraki görevler](../docs/Irem_Kabul_Devir_Notu.md)
- [İngilizce demo konuşması](../docs/Demo_Konusmasi_EN_v2.md)
- [Mehmet Ali okuma kartı](../docs/Prova_Mehmet_Ali_EN.md)
- [İrem okuma kartı](../docs/Prova_Irem_EN.md)
- [Konuşma süre tahmini](../evaluation/Prova_Sure_Tahmini_v2.json)
- [68 testin gerçek kaydı](../evaluation/offline_acceptance_results.xml)
- [İçerik/dosya bütünlüğü](../evaluation/materials_check_result.json)
- [Referans paketini kullanma](../evaluation/Referans_Paketini_Kullanma.md)

## Durum

| İş | Gerçek durum |
| --- | --- |
| Üç dersin JSON içeriği | Uygulamaya bağlandı; kaynaklar 142/130/128 kelime |
| Temiz kurulum ve yerel tarayıcı | Tamamlandı |
| Teknik testler | 68 geçti; kontrollü yanıtlar, canlı ağ yok |
| Yirmi kabul başlığı | 10 çevrimdışı tamamlandı, 9 kısmi, 1 bekliyor |
| API anahtarı | İrem'in aldığı bildirildi; başarılı çağrı kaydı doğrulanmadı |
| Canlı içerik/gerekçe değerlendirmesi | Bekliyor |
| İki promptun gerçek karşılaştırması | Bekliyor |
| PDF/PPTX | Çevrimdışı sonuçlarla güncellenmiş v2 taslak |
| Sesli süre provası ve İngilizce video | Bekliyor |
| Hedef kitle erişimi ve teslim formu | Bekliyor |

## Son sürüme geçiş

1. İrem gerçek model ve anahtar içermeyen başarılı çağrı kaydını paylaşır.
2. Üç dersin canlı çıktıları, soru anahtarları ve gerekçeye dayalı geri bildirim incelenir.
3. Aynı girdilerle iki promptun gerçek çıktıları karşılaştırılır.
4. PDF/PPTX gerçek sonuçlarla güncellenir; ölçülmeyen öğrenme kazanımı iddia edilmez.
5. Gerçek arayüzde İngilizce prova ve yaklaşık beş dakikalık video yapılır.
6. Başka bilgisayarda kurulum ve teslim bağlantılarının erişimi kontrol edilir.

`v1` dosyaları tarihsel taslaklardır. Geliştirme verisi canlı çıktı olarak sunulmaz. Dosya bütünlüğü, kontrollü uygulama testi ve gerçek model anlam incelemesi ayrı kanıtlardır.
