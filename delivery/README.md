# Grup 14 - Teslim dosyaları

Bu klasörde 17 Ekim 2026 tarihli uygulama ve gerçek test kayıtlarına göre hazırlanmış rapor ve İngilizce sunum bulunur. Belgeler, bilinen sınırlamaları açıkça belirtir; kusursuz model çıktısı veya ölçülmüş öğrenme kazanımı iddia etmez.

## Teslim için kullanılacak dosyalar

- [İki sayfalık proje raporu - PDF](Anlatim_Koprusu_Proje_Raporu.pdf)
- [İngilizce sunum - PowerPoint, altı slayt](Anlatim_Koprusu_English_Presentation.pptx)
- [Raporun düzenlenebilir metni](../docs/Proje_Raporu.md)
- [Sunum metni ve konuşmacı notları](../docs/Sunum_Icerigi_EN.md)
- [Kod, promptlar ve kurulum README'si](../README.md)
- [Gerçek canlı değerlendirme sonuçları](../evaluation/Canli_Sonuclar_20261017.md)
- [Son bağımsız teknik test kaydı - 69 test](../evaluation/offline_acceptance_69.xml)
- [Dosya ve içerik bütünlüğü kontrolü](../evaluation/materials_check_result.json)

## Repo ve uygulama

Teslimde kullanılacak dal: `codex/acceptance`.

https://github.com/Mehmetalimans/anlatim-koprusu/tree/codex/acceptance

Kod snapshot'ı: `06a6c25`; sonraki belge commit'leri uygulama davranışını değiştirmez. Varsayılan `main` dalı henüz bu prototipi içermediğinden incelemeye yukarıdaki doğrudan dal bağlantısıyla başlanmalıdır. Repo erişimi hedef değerlendiriciler için ayrıca kontrol edilmelidir.

Kurulum ve çalıştırma README'dedir. Canlı kullanımda yerel Gemini anahtarı gerekir. `.env.example` paylaşılır; gerçek `.env` teslim edilmez. Geliştirme modu sabit örnek gösterir ve canlı AI çıktısı değildir.

## Sonuçların kapsamı

- Bağımsız yeniden çalıştırmada 69/69 otomatik test geçti; gerçek ağ çağrısı yapılmadı.
- İrem'in 16 üretim ve 50 geri bildirim kaydı ile üç ders/iki prompt karşılaştırması repodadır. Her son karşılaştırma hücresinde tek üretim vardır.
- Son geri bildirimde doğru şık/yanlış gerekçe alt grubunda bir hata kaçmıştır. Bir fizik açıklamasında U ile enerji değişimi ifadesi karışmıştır.
- Son üretim ve geri bildirim revizyonları aynı yeni sorularda birlikte henüz kaydedilmemiştir. Manuel yeni metinle son canlı akış kontrolü ve video hazırlanmalıdır.
- Öğrenci öğrenme kazanımı ölçülmemiştir.

## Ayrı teslim edilecek video

Yönerge, İngilizce sunumla ekran paylaşımında canlı uygulama demosunu içeren yaklaşık beş dakikalık video da ister. Video bu dosya paketinde henüz yoktur. Son video YouTube liste dışı veya erişime açık Drive bağlantısıyla paylaşılmalıdır.

`Taslagi`, `Draft`, `v1` ve `v2` adlarını taşıyan eski PDF/PPTX dosyaları tarihsel hazırlıklardır. Yukarıda adları verilen güncel rapor ve sunum kullanılmalıdır.
