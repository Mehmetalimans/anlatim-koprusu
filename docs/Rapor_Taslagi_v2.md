# Anlatım Köprüsü - Proje Raporu

**Grup 14 | 17 Ekim 2026 | Çevrimdışı kabul sonrası taslak v2**

Uygulama kodu ve üç ders içeriği birleştirilmiş; temiz kurulum, çevrimdışı servis ve arayüz kontrolleri yapılmıştır. Bu rapor canlı model doğruluğu veya ölçülmüş öğrenme kazanımı iddia etmez. Gerçek API ve içerik değerlendirmeleri tamamlanınca son teslim sürümüne dönüştürülecektir.

## 1. Problem, kullanıcı ve sosyal etki

Hedef problem, üniversite öğrencilerinin akademik terimler ve yoğun ifadeler nedeniyle bir ders metninde takılmasıdır. Anlatım Köprüsü, öğrencinin seçtiği ifadeye odaklanır ve açıklamayı kaynak bağlamıyla birlikte sunar. Hedef kitle 18 yaş üstü üniversite öğrencileri; arayüz ve öğrenme çıktıları Türkçedir. Kullanıcı ihtiyacı henüz öğrenci araştırmasıyla doğrulanmamıştır.

SDG 4 bağlantısı, anlaşılır öğrenme desteğine erişim hedefidir. BM'nin 4.3 hedefi üniversite dahil nitelikli yükseköğretime eşit erişimi kapsar [1]. Projenin bu hedefe katkısı bir tasarım amacı olarak ele alınır; eğitim eşitsizliğini azalttığı veya başarıyı artırdığı ölçülmüş bir sonuç değildir.

## 2. Çözüm ve kullanıcı akışı

Öğrenci üç örnekten birini seçer veya en fazla 6.000 karakterlik metin girer. Zorlandığı ifadeyi kaynaktan kopyalar. Açıklama, terim kartları, kaynak referansları ve ayrı etiketli ek örnek üzerinden çalışır. Ardından yeni bir duruma ilişkin dört seçenekli soruyu cevaplar ve kısa gerekçesini yazar. Seçenek sonucu ile gerekçeye ilişkin geri bildirim ayrı ele alınır.

Kaynak ve açıklama yan yana gösterilir. Kod blokları görüntülenir, çalıştırılmaz; matematik işaretleri uygun görünümle sunulur. Girdi veya çalışma modu değişince eski çalışma temizlenir. Yetersiz kaynak sonucunda cevap formu açılmaz. Hesap sistemi, PDF yükleme, ses ve internette yayınlama ilk kapsamın dışındadır.

## 3. Uygulama ve model erişimi

İrem'in `3e9a4ac` teslimi kabul dalında içeriklerle birleştirilmiştir. Temiz yerel ortam Python 3.12.14, Streamlit 1.66.0 ve Pydantic 2.14.1 ile kurulmuştur. Üç ders ayrı JSON dosyalarında yüklenir; toplu değerlendirme verisi içerik yükleyicisinin dışında tutulur. Sözleşme ve servis imzaları korunmuştur.

Gemini REST istemcisi kodda mevcuttur. Varsayılan model adı `gemini-3.5-flash-lite` olarak yapılandırılmıştır; bu, doğrulanmış erişim bilgisi değildir. Mehmet Ali'nin ortamında anahtar olmadığından gerçek API kontrolü çağrı yapmadan durmuştur. İrem'in anahtar aldığı bilgisi paylaşılmıştır; gerçek çağrı kaydı ve kullanılan model ayrıca doğrulanmayı beklemektedir.

## 4. Prompt tasarımı

`generate_bridge` açıklama ve soru, `evaluate_attempt` gerekçe geri bildirimi üretir. Kaynak ve öğrenci metni JSON veri olarak sistem talimatından ayrılır. Zero-shot ve örnek içeren iki üretim promptu kodda bulunur. Gerekçe yeterliyse modelin eksik uydurmaması için boş iyileştirme listesine izin verilir. Aynı üç girdide gerçek prompt karşılaştırması henüz yapılmamıştır.

---

## 5. Testler ve elde edilen kanıtlar

İrem'in teknik testleri ve Mehmet Ali'nin bağımsız servis/Streamlit kontrolleri birlikte çalıştırılmıştır: 68 otomatik test geçmiş, başarısız test kalmamıştır. Testler sırasında gerçek ağ çağrıları engellenmiş; model yanıtları için kontrollü örnekler kullanılmıştır. Sonuçlar öğrenme veya gerçek model başarısı puanı değildir.

Kontroller; üç içeriğin şemaya uygun yüklenmesini, girdi sınırlarını, Türkçe harf/boşluk eşleşmesini, kod bloklarını, geçersiz referansları, seçenek sonucunun kodla hesaplanmasını, cevap formunu, yeniden denemeyi, durum sıfırlamayı ve hata yönetimini kapsar. Talimat içeren metnin veri alanında kalması kontrol edilmiştir; bu kontrol gerçek modelin bütün saldırılara dirençli olduğunu kanıtlamaz.

Üç regresyon önce yeniden üretilmiş, sonra düzeltilmiştir: canlı moda geçerken geliştirme sonucunun kalması, geliştirme sonucu türü değişince eski sorunun kalması ve sorudaki kod bloğunun düz metin gösterilmesi. Tarayıcıda etiketli geliştirme verisiyle cevap ve geri bildirim akışı da denenmiştir. Geliştirme geri bildirimi sabit örnektir; gerçek gerekçeyi anlayan AI davranışı olarak değerlendirilmemiştir.

## 6. İçerik doğruluğu ve etik sınırlar

Fizik 2 metninde potansiyel/enerji ayrımı, işaret ve birimler korunur [2]. ECON 100 metni fırsat maliyetini vazgeçilen en iyi alternatif üzerinden açıklar [3]. Python metninde başlangıç dahil, bitiş hariç kuralı ve kod girintileri korunur [4]. Güncel metinler 142, 130 ve 128 kelimedir. İnsan incelemesine yardımcı olmak için 12 şık/gerekçe denemesi ve 12 girdi senaryosu hazırlanmıştır.

Pydantic biçim doğrulaması anlam doğruluğunu garanti etmez. Kodun hesapladığı şık sonucu, modelin ürettiği anahtara dayanacağından canlı demo anahtarları ayrıca incelenmelidir. AI hatalı açıklama veya ilgisiz geri bildirim verebilir. Kaynak görünürlüğü ve üretilmiş örneklerin etiketlenmesi bu incelemeyi destekler. Genel yeterlilik puanı verilmez; kişisel/gizli notlar demo girdisi olarak kullanılmaz. API anahtarı yerel ortamda tutulur ve repoya eklenmez.

## 7. Kalan işler ve teslim

İrem teknik geliştirme ve model erişimini; Mehmet Ali içerik, bağımsız kabul ve teslim belgelerini takip eder. Gerçek API erişimi, üç derste canlı çıktıların anlam incelemesi, gerekçeye duyarlı geri bildirim, prompt karşılaştırması ve İngilizce video henüz tamamlanmamıştır. Yirmi kabul başlığına ilişkin ayrıntılı kapsam ve bekleyenler repo içindeki kabul raporunda tutulur. Son teslim paketi gerçek sonuçlarla güncellenmiş rapor, kod/README, İngilizce sunum ve yaklaşık beş dakikalık İngilizce demo içerecektir.

## Kaynaklar

1. [Birleşmiş Milletler, SDG 4 ve hedef 4.3](https://sdgs.un.org/goals/goal4)
2. [OpenStax, University Physics Volume 2, 7.2](https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference)
3. [OpenStax, Principles of Economics 3e, 2.1](https://openstax.org/books/principles-economics-3e/pages/2-1-how-individuals-make-choices-based-on-their-budget-constraint)
4. [Python resmî öğreticisi, range](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

Repo: https://github.com/Mehmetalimans/anlatim-koprusu
