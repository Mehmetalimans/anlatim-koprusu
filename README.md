# Anlatım Köprüsü

Grup 14'ün, üniversite öğrencilerinin akademik metinlerde zorlandıkları ifadeleri kaynakla bağlantılı açıklamalar ve kısa uygulamalarla anlamasına yardımcı olmayı amaçlayan AI projesi.

**Durum:** Bu ilk sürüm içerik, çalışma planı ve kabul testi taslaklarını içerir. Uygulama kodu, API bağlantısı ve canlı model testleri henüz bu repoya eklenmemiştir. Test planındaki beklenen davranışlar gerçekleşmiş sonuç değildir.

## Başlangıç dosyaları

- [Claude / İrem için başlangıç ve devir](docs/CLAUDE_BASLANGIC.md)
- [Güncel proje ve iş bölümü — v2](docs/Proje_ve_Is_Bolumu_v2.md)
- [Fizik 2, ECON 100 ve temel Python içerikleri](content/Demo_Icerikleri_v1.md)
- [Kabul testleri ve prompt karşılaştırması planı](evaluation/Kabul_Test_Plani.md)

## Çalışma dağılımı

| Takipçi | İşler |
| --- | --- |
| İrem + Claude | Python/Streamlit uygulaması, veri modelleri, promptlar, API/model erişimi, arayüz, teknik testler ve teknik birleştirme. |
| Mehmet Ali + AI desteği | Üç ders içeriği, bağımsız kabul testleri, rapor, İngilizce sunum, demo videosu ve teslim koordinasyonu. |
| Birlikte | Anlam doğruluğu, soru anahtarları, önemli kararlar, son prova ve kabul. |

İşin takipçisi olması, yalnız çalışılması gerektiği anlamına gelmez. Aynı dosya iki AI'a eşzamanlı düzenletilmez. Güncel dosya ve commit üzerinden küçük devirler yapılır.

## Hedef uygulama akışı

Kaynak metin seç/yapıştır → zorlanılan ifadeyi kopyala → sade açıklama ve kaynak referanslarını incele → dört seçenekli soruya cevap ve kısa gerekçe yaz → geri bildirim al.

Türkçe arayüz ve çıktılar; 18 yaş üstü üniversite öğrencileri. Üç demo alanında aynı öğrenme akışı kullanılacak. Öğrencinin yapıştırdığı Python kodu çalıştırılmayacak.

## Kurulum durumu

Hedef teknoloji Python + Streamlit'tir. Çalışan uygulama, bağımlılıklar ve doğrulanmış kurulum komutları İrem'in teknik teslimiyle eklenecektir. Henüz `app.py` bulunmadığından bu sürüm çalışır uygulama olarak sunulmaz. Canlı model erişimi internet ve yerel API yapılandırması gerektirecektir.

## GitHub üzerinden devir

İrem teknik çalışma için `codex/app`, Mehmet Ali içerik ve teslim işleri için `codex/content-delivery` dalını kullanır. Güncel `main` temel alınır; mevcut kod varsa önce incelenir ve korunur. Birleştirmeden önce gerçek kontroller ve açık sorunlar paylaşılır.

Özel repoyu Claude'un okuyabilmesi için İrem'in hesabına repo erişimi verilmesi ve kullandığı Claude ortamının bu erişimi desteklemesi gerekir. Yalnızca URL vermek erişim sağlamaz. Repo erişimi yoksa ilgili dosyalar indirilebilir veya Claude'a yüklenebilir. Okuma erişimi, otomatik kod yazma/push yetkisi olduğu anlamına gelmez.

## Teslim hedefi

Hedef paketi 17 Ekim 2026'da bitirmek; yetişmeyen işler için 18 Ekim tampon gündür. Ekip teslim hedefi 18 Ekim 18.00, yönergedeki son saat 19.00'dur. Paket: çalışan prototip ve GitHub, 1–2 sayfalık PDF rapor, İngilizce sunum ve yaklaşık beş dakikalık İngilizce demo videosu.

API anahtarları yerel ortamda tutulur ve repoya eklenmez. Geliştirme verisi ve planlanan testler, canlı sonuç olarak gösterilmez.
