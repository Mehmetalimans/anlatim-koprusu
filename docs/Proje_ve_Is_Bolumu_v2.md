# Anlatım Köprüsü — Güncel İş Bölümü ve Claude Çalışma Talimatı

**Grup 14 | 17 Ekim 2026 | Sürüm 2**

**Bu belge İrem’e ve İrem’in Claude oturumuna gönderilmek üzere hazırlanmıştır.** Önceki PDF’deki “Mehmet Ali core/API, İrem UI/content” görev dağılımının ve önceki başlangıç mesajının yerini alır. Proje seçimi ve temel kapsam korunur; görevler ve aşağıda belirtilen uygulama kararları güncellenmiştir. Çelişki durumunda bu belgedeki görev dağılımı esas alınır.

## 1. Yeni çalışma kararı

**İrem + Claude: uygulamanın teknik geliştirmesi, model/API araştırması ve çalışan sürümün bütünleştirilmesi.**

**Mehmet Ali + kendi AI desteği: ders içerikleri, bağımsız kabul testleri, rapor, İngilizce sunum, video ve teslim koordinasyonu.**

Bu dağılım, ekibin zor kodlama işlerini İrem’in Claude oturumunda toplama tercihidir; belirli bir modelin diğerinden kesin olarak daha başarılı olduğu iddiası değildir. Teknik bütünlük için çekirdek ve arayüz aynı geliştirme takibinde olacak. İrem’in üzerinden içerik yazımı ve teslim belgelerinin ana yükü alınacak.

Takipçi, işi tek başına yapmak zorunda değildir. Mehmet Ali ve İrem birlikte prompt inceleyebilir, bir hatayı beraber çözebilir ve aynı çıktıyı ayrı ayrı test edebilir. Aynı dosyanın iki AI tarafından eşzamanlı değiştirilmesi önlenecek; gerektiğinde dosya görevi kısa bir devir mesajıyla aktarılacak.

**Mevcut durum:** Mehmet Ali’nin bu belge hazırlanırken kontrol edilen klasöründe plan belgeleri ve yerel Git kaydı bulunuyor. Uygulama kodu ve bağlı GitHub uzak reposu henüz bulunmuyor. İrem’in bilgisayarındaki dosyalar ayrıca kontrol edilmeli. Mevcut bir çalışma varsa korunup bu plana uyarlanmalı; sıfırdan yeniden yazılması gerekmiyor. API erişimi ve canlı testlerin tamamlandığı varsayılmamalı.

## 2. Projeyi tek başına anlamak için özet

Anlatım Köprüsü, 18 yaş üstü üniversite öğrencilerinin zorlandıkları akademik ifadeleri kaynakla bağlantılı açıklama, terim kartları, üretilmiş örnek ve kısa uygulama sorusu üzerinden anlamalarına yardımcı olur. Arayüz ve öğrenme çıktıları Türkçedir. SDG 4 bağlantısı, anlaşılır öğrenme desteğine erişimdir; ölçülmemiş öğrenme başarısı vaat edilmez.

**Teknoloji:** Python + Streamlit. Uygulama `streamlit run app.py` ile başlatılır ve tarayıcıda kullanılır. Canlı AI çağrıları internet ve geçerli API erişimi gerektirir. Yerel tarayıcı adresi, herkese açık bir internet sitesi bağlantısı değildir.

**Temel akış:**

1. Öğrenci üç demo metninden birini seçer veya kendi metnini yapıştırır.
2. Zorlandığı ifadeyi kaynak metinden kopyalayıp ayrı alana girer.
3. “Açıkla” ile gerçek model çağrısı yapılır.
4. Kaynak, sade açıklama, terimler, kaynak referansları ve ayrı etiketlenmiş ek örnek gösterilir.
5. Öğrenci yeni bir durum hakkındaki dört seçenekli soruyu cevaplar ve kısa gerekçesini yazar.
6. Seçenek sonucu ve kendi gerekçesine dayalı geri bildirim alır; yeniden deneyebilir.

**Demo alanları:** Fizik 2 elektrik; ECON 100 fırsat maliyeti; temel Python `for` ve `range`. Üç uygulama yapılmayacak; aynı akış üç metinle çalışacak. Kaynak metin sınırı 6.000 karakterdir.

**İlk sürüm dışında:** PDF yükleme, özel fareyle seçim bileşeni, hesap sistemi, veritabanı, ses, çok dil ve internetten yayınlama. Öğrencinin yapıştırdığı Python kodu çalıştırılmayacak. Öğrenciye genel yeterlilik puanı verilmeyecek.

## 3. İş paketleri ve tamamlanma koşulları

| İş | Ana takipçi | Somut çıktı / tamamlanma koşulu |
| --- | --- | --- |
| IR-01: Teknik başlangıç | İrem | Çalışan proje iskeleti, Pydantic modelleri, servis imzaları, `ready` ve `insufficient_source` örnek verileri, kurulum komutları. |
| IR-02: API ve model erişimi | İrem | Resmî belgelerden model/SDK/kota kontrolü; gerçek açıklama üretimi ve geri bildirim çağrısı; kullanılan model adı ve erişim sonucu. Anahtar alınamıyorsa açık engel kaydı. |
| IR-03: Model çekirdeği | İrem | Promptlar, yapılandırılmış çıktı, doğrulama, kaynak bölme/referans kontrolü, seçenek sonucu, hata yönetimi. |
| IR-04: Streamlit ve birleştirme | İrem | Girdiden geri bildirime çalışan `app.py`; oturum sıfırlama, kod gösterimi, yetersiz kaynak ve hata ekranları. |
| IR-05: Teknik test ve düzeltme | İrem | Girdi doğrulama, referanslar, API hataları ve oturum davranışı için gerçek test kayıtları; kritik hataların giderilmesi. |
| MA-01: Üç ders içeriği | Mehmet Ali | Her biri 120–200 kelimelik özgün metin, kaynak bağlantıları, seçilen ifade, beklenen anlam ve doğru/yanlış gerekçe örnekleri. |
| MA-02: Bağımsız kabul | Mehmet Ali | İrem’in sürümünü kendi bilgisayarında kurma; üç dersin doğru/yanlış cevap akışlarını deneme; yeniden üretilebilir hata listesi. |
| MA-03: Prompt ve içerik değerlendirmesi | Mehmet Ali | İrem’in sağladığı iki prompt sürümünün aynı üç girdide gerçek çıktılarını karşılaştırma; anlam, açıklık, soru ve gerekçe kalitesi kaydı. |
| MA-04: Belgeler | Mehmet Ali | 1–2 sayfalık PDF rapor; İngilizce slaytlar; İngilizce demo metni. Teknik bilgileri İrem doğrular. |
| MA-05: Repo ve teslim koordinasyonu | Mehmet Ali | Ortak GitHub reposu ve erişimler, teslim dosyaları/bağlantıları, yaklaşık beş dakikalık video, son kontrol ve teslim kaydı. |
| Ortak kabul | İrem + Mehmet Ali | Demo cevap anahtarları, teknik rapor bilgileri, prova, son paketin kontrolü. |

**Yükü dengeleme kuralı:** Mehmet Ali içerik ve belge taslaklarına hemen başlar; çalışan kodu beklemez. Sonuç ve ekran görüntüsü gerektiren bölümler açıkça “bekliyor” olarak tutulur. İrem taslak rapor/slayt yazımını üstlenmez; teknik doğrulama ve hata düzeltmeye odaklanır.

## 4. Dosyalar ve çalışma sınırları

Aşağıdaki yapı hedef yapıdır; bu dosyaların şu anda oluşturulduğu anlamına gelmez.

```text
app.py                         İrem — ana uygulama
core/                          İrem — modeller, servisler, promptlar, doğrulama
ui/                            İrem — ekranlar ve oturum davranışı
tests/                         İrem — teknik testler
fixtures/                      İrem — etiketli geliştirme verisi
requirements.txt               İrem — doğrulanmış bağımlılıklar
.env.example                   İrem — yalnızca boş/örnek değişkenler
.gitignore                     İrem — anahtar ve yerel dosya hariç tutma
README.md                      İrem — teknik kurulum ve çalışma açıklaması
content/                       Mehmet Ali — üç ders içeriği ve kaynaklar
evaluation/                    Mehmet Ali — kabul ve prompt karşılaştırma kayıtları
docs/                          Mehmet Ali — rapor ve sunum kaynakları
delivery/                      Mehmet Ali — teslim dosyaları ve bağlantı listesi
```

İrem `content/` dosyalarını okuyacak yükleyiciyi geliştirir; Mehmet Ali içeriği yazar. İlk içerik tesliminden önce İrem içerik şemasını paylaşır. Başlangıç alanları: `id`, `subject_label`, `title`, `source_text`, `selected_phrase`, `sources`, `expected_meaning`, `invariants`, `correct_rationale`, `incorrect_rationale`. `sources`, başlık ve URL içeren bir listedir. `invariants`, korunacak anlam/koşullar listesidir. Öğrenci ekranında test gerekçeleri ve beklenen cevaplar gösterilmez.

İçerik şeması henüz gelmediyse Mehmet Ali aynı alanlarla Markdown taslağı hazırlar; iş durmaz. İrem’in loader beklentisiyle son biçim birlikte netleştirilir.

**Git düzeni:** İrem `codex/app`, Mehmet Ali `codex/content-delivery` dalını kullanabilir. Bunlar önerilen yeni dal adlarıdır; mevcut dallar varsa iş kaybetmeden uyarlanır. Eski `codex/core` ve `codex/ui-content` görev ayrımı artık geçerli değildir.

Mehmet Ali repo erişimini kurar. İrem teknik değişiklikleri ve içerik bağlantısını çalıştırarak bütünleştirir; Mehmet Ali birleştirilmiş sürümü bağımsız test eder. Claude’un doğrudan repo erişimi yoksa İrem dosyaları/yamaları taşır. Repo kurulumu API ve yerel geliştirmeyi bekletmez.

## 5. İrem’e devredilen ortak teknik sözleşme

**Önceki plandaki `core/contracts.py` ve örnek çıktıyı hazırlama görevi artık İrem’dedir. Claude bunları Mehmet Ali’den beklemeyecek.**

```python
generate_bridge(request: BridgeRequest) -> BridgeResult

evaluate_attempt(
    request: BridgeRequest,
    bridge: BridgeResult,
    selected_option_id: str,
    rationale: str,
) -> AttemptFeedback
```

| Model | Alanlar / kurallar |
| --- | --- |
| BridgeRequest | `source_text`, `selected_phrase`, isteğe bağlı `subject_label`. |
| BridgeResult | `status` (`ready` / `insufficient_source`), `simple_explanation`, `source_refs`, `terms`, `example`, `quiz`, `warnings`. |
| Terim | `term`, `explanation`, `origin` (`source` / `supporting`). |
| Ek örnek | `text`, `origin="generated"`. Yetersiz kaynakta `example` null olabilir. |
| Quiz | `question`, tam dört `options` (`id`, `text`), `correct_option_id`, `answer_explanation`. Kimlikler A–D; tekrar yok; doğru kimlik seçeneklerde var. |
| AttemptFeedback | `is_correct`, `strengths`, `improvements`, `retry_hint`. Geri bildirim metinleri öğrencinin gerekçesine dayanır. |

İrem alanların kesin türlerini, varsayılanlarını ve örnek JSON’u modellerle birlikte paylaşır. Liste alanları boş liste olabilir. `ready` sonucunda soru ve ek örnek zorunludur. `insufficient_source` sonucunda `quiz=null`; neden ve önerilen sonraki adım `simple_explanation` ve `warnings` içinde anlatılır. UI bu durumda cevap formu göstermez.

`is_correct` uygulama kodunda seçenek kimliği ile cevap anahtarı karşılaştırılarak hesaplanır; AI’ın geri bildirim metni bunu değiştiremez. Cevap anahtarı modelden geldiği için demo anahtarları ayrıca insan kontrolünden geçer.

Hata kodları: `invalid_input`, `missing_key`, `quota`, `network`, `invalid_output`. Kullanıcıya Türkçe açıklama gösterilir; gizli anahtar ve ham hassas hata içeriği gösterilmez.

İrem uygulama içindeki teknik düzenlemeleri kendi takibinde yapabilir. Mehmet Ali’nin içerik şemasını, kabul ölçütlerini veya kullanıcı akışını etkileyen değişikliklerde değişen alan ve geçiş örneği paylaşılır. Her küçük kod değişikliği için onay beklenmez.

## 6. Claude’un önerilerine göre kesinleştirilen kararlar

### 6.1 İfadenin kaynakta bulunması

- Orijinal kaynak korunur. Eşleşme için ayrı bir karşılaştırma kopyası üretilir.
- Düzyazıda Unicode NFC ve boşluk normalleştirmesi uygulanır. Büyük/küçük harf dönüşümü yapılmaz; Türkçe `İ/i/ı/I` farkları korunur.
- İlk sürümde tırnaklar otomatik olarak değiştirilmez. Kullanıcı kaynakta geçen ifadeyi kopyalar; eşleşme yoksa yönlendirici uyarı alır. Böylece kod dizgileri ve özel işaretler de gelişigüzel değiştirilmez.
- Kod içindeki seçimlerde girintiler ve satırlar korunur; yalnızca platform satır sonu farkları eşitlenir. Düzyazı boşluk sadeleştirmesi kod bloklarına uygulanmaz.
- Eşleşme birden fazla yerdeyse otomatik olarak ilk yer seçilmez. API çağrılmadan “İfadeyi çevresindeki birkaç kelimeyle genişletin” uyarısı gösterilir. İlk sürüm için yeni seçim bileşeni veya sözleşme alanı gerekmez.

### 6.2 Oturum, düğmeler ve cevap formu

- Kaynak, seçilen ifade ve ders etiketinden kararlı bir parmak izi üretilir; sonuç ilgili girdi kimliğiyle `st.session_state` içinde tutulur. Gerçek kaynak değişikliklerini görebilmek için bu hesap, eşleştirme amacıyla sadeleştirilmiş kopyaya dayandırılmaz.
- Girdi kimliği değişince açıklama, soru, seçili şık, gerekçe ve geri bildirim temizlenir. Aynı girdiyle yeni soru üretildiğinde de eski cevap durumu sıfırlanır.
- **Hash kullanmak API çağrısını kendiliğinden engellemez.** Üretim yalnızca “Açıkla”, değerlendirme yalnızca cevap formunun gönderimi üzerinden tetiklenir.
- Kaynak ve ifade girdileri cevap formunun dışında tutulur. Böylece Streamlit yeni girdi değerini aldığında eski çalışma temizlenebilir.
- Seçenekler `st.radio(..., index=None)` ile başta seçimsiz gösterilir. Seçenek ve gerekçe `st.form` içindedir; bu form girdileri gönderimde birlikte işler. Form kullanmak uygulamadaki bütün yeniden çalışmaları durdurmaz.
- Boş seçenek veya yalnızca boşluk içeren gerekçe API çağrısından önce reddedilir. Çok kısa gerekçeye açıklayıcı bir hatırlatma yapılabilir; ilk sürümde keyfî bir minimum kelime sayısıyla anlamlı kısa yanıtlar engellenmez. Gerekçe için 1.000 karakter üst sınır uygulanır.
- Aynı girdide API hatası oluşursa mevcut başarılı çalışma korunur. Girdi değişmişse önceki çalışmanın yeni girdiye aitmiş gibi gösterilmesine izin verilmez.

### 6.3 Kaynak gösterimi ve paragraf kimlikleri

- Düzyazı kaynakları düz metin, kod parçaları `st.code` ile gösterilir. Kullanıcı kaynağı serbest HTML olarak işlenmez. Kod çalıştırılmaz.
- Kaynak bölücü üç ters tırnakla çevrili kod bloklarını tanır. Kod içindeki boş satırlar paragraf sınırı sayılmaz; kod bloğu tek parça tutulur. Düzyazı boş satırlarda bölünür; parçalar sırayla P1, P2… kimlikleri alır.
- Aynı bölücü hem modele gönderilen kaynakta hem UI referanslarında kullanılır. Modelin `source_refs` alanındaki kimliklerin gerçekten var olduğu doğrulanır.
- Demo kodu açıkça kod bloğu işaretleriyle verilir. Kapanmamış kod bloğunda API öncesi düzeltme uyarısı gösterilir. İşaretlenmemiş özel metnin otomatik olarak kusursuz kod ayrıştırılması vaat edilmez.
- Kod içindeki boş satırlardan kaçınmak, bölücü hatasının kalıcı çözümü olarak kabul edilmez.

### 6.4 Yetersiz kaynak ve talimat içeren girdiler

- İrem hem `ready` hem `insufficient_source` geliştirme verisi hazırlayacak. Geliştirme modunda her zaman “GELİŞTİRME VERİSİ — canlı AI sonucu değildir” etiketi görünecek.
- Kaynak metni ve öğrenci gerekçesi, model talimatı değil işlenecek veri olarak ayrılacak. “Önceki talimatları yok say” gibi ifadeler görev değişikliği yaptırmamalı.
- Mehmet Ali bu ifadeyi kaynak ve gerekçeye ayrı ayrı ekleyerek kabul testi hazırlayacak; İrem prompt ve doğrulama düzeltmelerini yapacak. Birkaç testin geçmesi bütün saldırılara karşı garanti olarak sunulmayacak.

## 7. API araştırması ve erişim görevi

API sağlayıcısını araştırma, SDK bağlantısını kurma, yapılandırılmış çıktıyı deneme ve erişim hatalarını çözme takibi **İrem + Claude** tarafına geçmiştir.

1. İlk aday Gemini’dir. Önceki plandaki `gemini-3.5-flash-lite` adı bir başlangıç tercihidir; kullanılabilirliği ve ücretsiz kota koşulları güncel resmî belgelerden ve gerçek hesap erişiminden doğrulanır. Model adı `GEMINI_MODEL` ile değiştirilebilir olmalıdır.
2. Kullanılabilir model, gerekli hesap/API anahtarı adımları ve olası kota sınırları kısa olarak paylaşılır. Claude hesap oturumu veya anahtar gerektiren adımı kendi başına yapamıyorsa İrem’e tam olarak hangi adımı yapacağını anlatır. Anahtarın mevcut olduğu varsayılmaz.
3. Anahtar `GEMINI_API_KEY` üzerinden yerel ortamda kullanılır; `.env` kullanılıyorsa repodan hariç tutulur. Anahtar sohbet mesajına, örnek veriye, videoya veya repo dosyasına yazılmaz. `.env.example` gerçek anahtar içermez.
4. Gerçek bir demo girdisiyle açıklama/soru üretimi ve bir öğrenci gerekçesiyle değerlendirme denenir. Kullanılan model, sonuç, süre ve varsa hata kaydedilir. Ücretli hizmet veya faturalandırma bu planla yetkilendirilmiş değildir.
5. Erişim yoksa neden açıkça kaydedilir. Etiketli geliştirme verisiyle diğer işler sürer; canlı prototip şartı tamamlandı denmez. Sağlayıcı değişimi gerekiyorsa sebep, maliyet ve kod etkisi ekibe bildirilir.

Mehmet Ali API bulma işinin ana takipçisi olmayacak; kendi bilgisayarındaki bağımsız kurulum için gereken yerel yapılandırmayı yapacak. İrem’in kişisel API anahtarının dosyayla paylaşılması varsayılmayacak.

## 8. Mehmet Ali’nin hemen hazırlayacağı içerik ve kanıtlar

| Ders | Metin odağı | Kontrol örneği / tipik hata |
| --- | --- | --- |
| Fizik 2 | Elektriksel potansiyel ve potansiyel enerji; `ΔU = q × ΔV` | `q=+2 C`, `ΔV=+3 V` → `ΔU=+6 J`. Volt/joule ve işaret ayrımı; çeldiricilerde birimleri karıştırma veya q’ya bölme. |
| ECON 100 | Fırsat maliyeti, vazgeçilen en iyi alternatif | Aynı saatte tek etkinlik seçilir; ders çalışmak seçilmiş, kalanlar arasında konser filmden daha değerli. Maliyet konser alternatifinin değeridir; konser + film toplamı değildir. |
| Temel Python | `for` döngüsü, `range` başlangıç/bitiş sınırları | `range(1, 4)` döngüsü 1, 2, 3 üretir; 4 dahil değildir. Girintiler ve çıktı satırları korunur. |

Her içerikte kaynak, seçilen ifade, korunacak koşullar ve iyi/kötü öğrenci gerekçesi bulunacak. Çeldiriciler birbirinden farklı ve yalnızca bir doğru seçeneğe izin verecek şekilde incelenecek. Taslak içerikler gerçek model çıktısı sayılmayacak.

İrem zero-shot ve örnek içeren prompt sürümlerini sağlayacak. Mehmet Ali aynı üç içerikle alınan gerçek sonuçları karşılaştıracak: anlam korunması, kaynak bağlantısı, açıklık, soru kalitesi ve gerekçeye uygun geri bildirim. Teknik testleri İrem, bağımsız kabul kayıtlarını Mehmet Ali yazar; aynı test dosyasına eşzamanlı müdahale edilmez.

## 9. Güncellenmiş takvim

**Ana hedef bütün paketi bugün bitirmektir.** Rapor, slayt ve video otomatik olarak yarına bırakılmayacak. Belge taslakları kodla paralel hazırlanacağı için İrem’in öngördüğü son saat yığılması azaltılacak. Yetişmeyen işler yarına açık bir listeyle taşınacak.

T0 fiilî ortak başlangıçtır. Çalışma başladıysa sırf görev dağılımı değişti diye yedi saatlik sayaç yeniden başlatılmaz. Claude’un mesajındaki 15.24 geçmiş mesaj saatidir; güncel saat varsayımı olarak kullanılmaz.

| Kontrol noktası | İrem | Mehmet Ali | Ortak çıktı |
| --- | --- | --- | --- |
| İlk 30 dakika | Kod erişimi kontrolü, sözleşme ve API denemesi | Repo erişimi, içerik ve belge iskeletleri | Güncel durum + ilk dosya/şema paylaşımı |
| 30–120 dakika | Çekirdek ve basit UI; bir dersin akışı | Üç metin, kabul senaryoları, rapor/slayt taslağı | Geliştirme sürümü ve içerik paketi |
| 120–180 dakika | Gerçek API ile uçtan uca çalışan sürüm | Kendi bilgisayarında kurulum ve ilk kabul | Açıklama → soru → gerekçe geri bildirimi |
| 180–240 dakika | Kritik düzeltmeler, teknik testler | Üç ders testi, prompt karşılaştırması | Kapsam sabit; hata listesi ve gerçek sonuçlar |
| 240–300 dakika | Kararlılık ve teknik belge doğrulaması | Rapor/slaytları gerçek sonuçlarla bitirme | Teslim belgeleri hazır |
| 300–360 dakika | Ortak prova ve teknik demo desteği | İngilizce anlatım, kayıt ve video kontrolü | Yaklaşık beş dakikalık video |
| 360–420 dakika | Son teknik sorunların giderilmesi | Bağlantı, dosya ve teslim kontrolü | Ekipçe onaylanan teslim paketi |

Üçüncü saatte temel akış çalışmıyorsa görünüm iyileştirmeleri durur. Dördüncü saatte yeni özellik açılmaz. Süre yetmiyorsa kritik hata, doğruluk kontrolü ve zorunlu teslimler önceliklidir.

Kesin teslim: **18 Ekim 2026 Pazar 19.00.** Ekip hedefi en geç 18.00’dir. Tamamlanmayan her iş için takipçi, tahmini süre ve engel yazılır.

## 10. Teslim ve devir kuralları

Teslim paketi: çalışan prototip ve GitHub kodu; promptlar ve README; 1–2 sayfalık PDF rapor; İngilizce sunum; yaklaşık beş dakikalık İngilizce demo videosu. Bu çalışma planı teslim raporunun yerine geçmez.

Canlı demo en az bir derste tam akışı gösterecek. Diğer iki dersin çalışması kısa örnekler ve gerçek test kayıtlarıyla desteklenecek. Video kaydı API anahtarı veya kişisel veri göstermeyecek.

Her devir mesajı şu yapıda verilir:

```text
İş kimliği:
Başlangıç sürümü / commit (varsa):
Tamamlanan iş:
Değişen dosyalar:
Çalıştırma komutu:
Gerçekten yapılan kontroller ve sonuçları:
Yapılamayan kontroller / erişim engelleri:
Diğer kişiden gereken bilgi veya dosya:
Sonraki küçük adım:
```

Kod yazılması, kodun çalıştırıldığı anlamına gelmez. Mock ile çalışan ekran, canlı model testi sayılmaz. İki AI’ın otomatik ortak hafızası olduğu varsayılmaz.

## 11. İrem’in Claude’a doğrudan vereceği başlangıç mesajı

> Ben İrem. Grup 14 olarak Anlatım Köprüsü’nü seçtik. Bu v2 belgesini güncel görev planı olarak kullan; önceki PDF’deki iş dağılımı değişti. Artık uygulamanın bütün teknik geliştirmesini ben takip ediyorum: Python + Streamlit, core/, ui/, app.py, Pydantic sözleşmeleri, örnek veriler, promptlar, API/model araştırması ve bağlantısı, teknik testler, teknik README ve çalışan sürümün birleştirilmesi. Mehmet Ali üç ders içeriğini, bağımsız kabul testlerini, raporu, İngilizce sunumu, videoyu ve teslim koordinasyonunu takip ediyor.
>
> Mehmet Ali’den core/contracts.py veya örnek çıktı bekleme; bunları hazırlama görevi artık bizde. Fikir seçimini yeniden açma. Önce mevcut dosyalara ve çalıştırma ortamına erişimini kontrol et; varsa yaptığın UI çalışmasını koruyarak ilerle. Repo erişimin yoksa bunu söyle ve güncel dosyaları iste, ancak mevcut belgeyle başlayabildiğin işleri durdurma. Dosya oluşturabiliyorsan kullanılabilir proje dosyaları üret; yalnızca metin verebiliyorsan her dosyanın yolunu ve tam içeriğini açıkça sun. Çalıştırmadığın kodu test edilmiş sayma.
>
> İlk teslimin: Pydantic veri modelleri ve içerik şeması, ready/insufficient_source geliştirme verileri, en küçük çalışır uygulama iskeleti ve model erişim denemesinin gerçek sonucu olsun. API anahtarı gereken aşamada bana gerekli yerel adımları anlat; anahtarı sohbete yazmamı isteme. Modelin güncel kullanılabilirliğini ve kota koşullarını doğrula; ücretli hizmet açma. Sonra tek dersle gerçek açıklama → dört seçenekli soru → kısa gerekçeye dayalı geri bildirim akışını tamamla.
>
> Bu belgedeki eşleşme, kod bloklarını koruyan kaynak bölme, girdi değişince sıfırlama, açık düğme tetikleme, seçimsiz radio, cevap formu ve yetersiz kaynak kurallarını uygula. Kullanıcının Python kodunu çalıştırma. Geliştirme verisini görünür biçimde etiketle. İçerik dosyalarının yazımı Mehmet Ali’de; onun dosyalarını veya içerik şemasını etkileyen değişiklikleri paylaş. Teknik kapsamındaki rutin işler için tekrar tekrar onay istemeden ilerle.
>
> İlk yanıtında erişebildiğin ortamı/dosyaları, hemen başlayacağın teknik işi ve gerçekten eksik olan erişimi belirt. Her tesliminde dosyaları, çalıştırma komutunu, gerçekten yapılan kontrolleri ve kalan işleri raporla. Amacımız bugün bitirmek; belgeler Mehmet Ali’de paralel ilerliyor. Üçüncü saatte temel akışa odaklan, dördüncü saatte yeni özellik eklemeyi bırak.

## 12. Başvurulacak kaynaklar

- Yerel yönerge: **Samsung ai hackathon bilgilendirme chapter 5.pdf**, önceki proje planında incelenen teslim ve prototip koşulları. Bu belgedeki iş dağılımı ve takvim ekip kararıdır.
- [Streamlit temel çalışma biçimi](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
- [Streamlit formlar: girdileri gönderimde toplama](https://docs.streamlit.io/develop/concepts/architecture/forms)
- [Streamlit radio: başlangıçta seçenek seçmeme](https://docs.streamlit.io/develop/api-reference/widgets/st.radio)
- [Python Unicode normalleştirme](https://docs.python.org/3/library/unicodedata.html)
- [Gemini yapılandırılmış çıktı](https://ai.google.dev/gemini-api/docs/structured-output)
- [Gemini güncel fiyatlandırma ve kota koşulları](https://ai.google.dev/gemini-api/docs/pricing)
- [Fizik: OpenStax, elektriksel potansiyel ve potansiyel farkı](https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference)
- [Ekonomi: OpenStax, bireylerin bütçe kısıtı altında seçimleri](https://openstax.org/books/principles-economics-3e/pages/2-1-how-individuals-make-choices-based-on-their-budget-constraint)
- [Python resmî öğreticisi: range](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

Streamlit form/radio ve Python Unicode belgeleri bu güncellemede kontrol edildi. API erişimi ve model seçimi, İrem’in gerçek kurulum aşamasında doğrulanacak.
