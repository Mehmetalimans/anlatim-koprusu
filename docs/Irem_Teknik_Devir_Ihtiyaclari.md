# Mehmet Ali'den İrem'e - İlk teknik devirde gerekenler

Mehmet Ali tarafında üç ders içeriği, kabul testi planı, rapor ve İngilizce sunum/demo taslakları hazırlanıyor. Aşağıdaki bilgiler geldiğinde içerik dosyalarını son şemaya dönüştürüp bağımsız kabul testlerine geçebiliriz.

## Tek mesajda paylaşılacak teknik paket

1. Çalışan dal ve commit; mevcut kod dosyaları.
2. Python sürümü, bağımlılık dosyası ve doğrulanmış kurulum/çalıştırma komutları.
3. `core/contracts.py` ve üç ders için kesin içerik dosyası şeması. Alan türlerini ve kısa JSON örneğini ekle.
4. `ready` ve `insufficient_source` çıktı örnekleri; bunların geliştirme verisi mi canlı sonuç mu olduğunu belirt.
5. Sağlayıcı, gerçek model adı ve yerel ortam değişkeni adları. API anahtarını paylaşma.
6. Gerçek API denemesinde çalışan akışlar ve açık erişim/kota engelleri.
7. Zero-shot ve örnek içeren prompt sürümleri; karşılaştırma için aynı girdinin nasıl verileceği.
8. Yapılmış teknik testler ve sonuçları; yapılmayanlar ayrı listelensin.

## Hazır içerikler

`content/Demo_Icerikleri_v1.md` içindeki kaynak metinler hazırdır. Fizik, ekonomi ve Python için kelime/ifade kontrolleri yapılmıştır. Kaynakların son API veri biçimine dönüşümü, senin içerik şemanı paylaşmandan sonra Mehmet Ali tarafından yapılacaktır.

Ortak plandaki `BridgeRequest` alanlarıyla üç girdi ayrıca `evaluation/demo_inputs.json` içinde hazırdır. Her öğenin `request` alanı kullanılabilir; JSON'un bütün üst yapısı uygulamanın kesin içerik yükleme şeması olarak dayatılmıyor. Geri bildirim için üç sabit soru ve 12 öğrenci denemesi `evaluation/feedback_reference_cases.json` içindedir. Kullanım açıklaması: `evaluation/Referans_Paketini_Kullanma.md`.

## Bağımsız kabul

`evaluation/Kabul_Test_Plani.md` içinde 20 senaryo var. Teknik sürüm gelince Mehmet Ali kendi bilgisayarında kurup gözlemleri kaydedecek. Kontroller sadece geliştirme verisiyle geçerse canlı prototip kabulü verilmez.

Bu dosya bir GitHub devir notudur; mesajın İrem'e veya Claude'a otomatik gönderildiği anlamına gelmez.
