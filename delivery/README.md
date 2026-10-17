# Teslim hazırlığı - Taslak v1

Bu klasördeki PDF ve PPTX, uygulama geliştirmesi sürerken hazırlanan **taslaklardır**. Başlangıç dayanağı `9237a4e` commit'idir. Çalışan uygulama ve gerçek test sonuçları gelmeden son teslim dosyaları olarak kullanılmamalıdır.

## Dosyalar

- [İki sayfalık Türkçe rapor taslağı](Anlatim_Koprusu_Rapor_Taslagi_v1.pdf)
- [Altı slaytlık İngilizce sunum taslağı](Anlatim_Koprusu_English_Deck_Draft_v1.pptx)
- [Raporun düzenlenebilir metni](../docs/Rapor_Taslagi_v1.md)
- [Sunumun düzenlenebilir metni](../docs/Ingilizce_Sunum_Metni_v1.md)
- [Güncel İngilizce demo konuşması ve ekran akışı](../docs/Demo_Konusmasi_EN_v2.md)
- [Mehmet Ali'nin ayrı okuma kartı](../docs/Prova_Mehmet_Ali_EN.md)
- [İrem'in ayrı okuma kartı](../docs/Prova_Irem_EN.md)
- [Öğrenci gözüyle içerik incelemesi](../evaluation/Ogrenci_Gozuyle_Icerik_Incelemesi.md)
- [İrem'den beklenecek ilk teknik devir](../docs/Irem_Teknik_Devir_Ihtiyaclari.md)
- [Güncel yerel içerik kontrolleri](../evaluation/Icerik_Kontrol_Sonuclari_v2.json)
- [Varsayımlara dayalı konuşma süre hesabı](../evaluation/Prova_Sure_Tahmini_v2.json)

Rapor ve PPTX v1, ilk hazırlık durumunu gösteren taslaklardır. Rapordaki 134/130/121 kelime sayıları ilk içerik sürümüne aittir. Öğrenci odaklı düzenlemeden sonra güncel sayılar 142/130/128'dir ve v2 içerik kontrol kaydında tutulur. İngilizce konuşma için güncel dosya v2'dir. Son teslimde PDF ve PPTX gerçek teknik sonuçlarla birlikte güncellenecektir.

## Mevcut durum

| İş | Durum |
| --- | --- |
| Üç ders metni ve referans gerekçeler | Hazır, uygulamaya aktarma şeması bekleniyor |
| Metin uzunlukları ve tekil ifade kontrolleri | Yerel kontrol tamamlandı |
| Örnek fizik hesapları ve range değerleri | Yerel kontrol tamamlandı |
| PDF rapor, İngilizce PPTX ve konuşma | İlk taslak hazır |
| Model/API erişimi ve çalışan uygulama | İrem'in teknik teslimi bekleniyor |
| 20 uygulama kabul senaryosu | Henüz çalıştırılmadı |
| Prompt karşılaştırması | Gerçek çağrılar bekleniyor |
| Video kaydı ve süre provası | Canlı akıştan sonra yapılacak |
| Son rapor/slayt güncellemesi ve teslim formu | Bekliyor |

## Son teslim sürümüne geçiş

1. İrem'in model adı, kurulum bilgileri ve çalışan commit'i alınır.
2. Mehmet Ali kendi bilgisayarında kurulum ve kabul testlerini kaydeder.
3. Prompt karşılaştırmasının gerçek çıktıları ve bulguları eklenir.
4. Rapor ve sunumdaki hazırlık durumları gerçek sonuçlarla güncellenir. Ölçülmemiş öğrenme kazanımı iddia edilmez.
5. İngilizce demo gerçek çağrılarla prova edilir ve kaydedilir. Slaytlar canlı uygulama gösteriminin yerine geçmez.
6. Ekip rapor, kod, sunum ve video bağlantılarının erişimini kontrol eder. Son teslim dosyaları son sürüm olarak ayrı adlandırılır.

İçerik kontrolleri uygulama testleriyle karıştırılmaz. Test planındaki beklenen davranışlar, gerçek sonuç olarak raporlanmaz.
