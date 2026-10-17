# Anlatım Köprüsü - Proje Raporu Taslağı

**Grup 14 | 17 Ekim 2026 | Geliştirme taslağı, teslim sürümü değildir**

Bu rapor 17 Ekim'de kontrol edilen repo durumunu yansıtır. İçerik ve test planı hazırdır; uygulama kodu, model erişimi ve uçtan uca test sonuçları henüz repoya eklenmemiştir. Son teslimden önce teknik uygulama ve gerçek sonuçlarla güncellenmelidir.

## 1. Problem, kullanıcı ve sosyal etki

Projenin çıkış problemi, üniversite öğrencilerinin akademik ifadelerdeki yoğun dil ve terimler nedeniyle bir metni anlamakta zorlanabilmesidir. Hedef kullanıcı 18 yaş üstü üniversite öğrencileridir. Türkçe bir arayüzde, öğrencinin seçtiği ifadeye odaklanan ve kaynak bağlamını görünür tutan bir öğrenme desteği tasarlanmıştır. Kullanıcı ihtiyacı henüz kullanıcı araştırmasıyla doğrulanmamıştır.

SDG 4 ile ilişki, öğrenme materyallerini anlaşılır kılarak nitelikli öğrenme desteğine erişimi kolaylaştırma hedefidir. Birleşmiş Milletler'in 4.3 hedefi, üniversite dahil nitelikli yükseköğretime eşit erişimi kapsar [1]. Projenin bu hedefe katkısı tasarım düzeyindedir; öğrenme başarısını artırdığı veya eşitsizliği azalttığı ölçülmüş bir sonuç olarak sunulmaz.

## 2. Çözüm ve kullanıcı akışı

Öğrenci bir örnek metni seçer veya en fazla 6.000 karakterlik kendi metnini yapıştırır; zorlandığı ifadeyi ayrı alana kopyalar. Uygulamanın kaynakla bağlantılı sade açıklama, terim kartları ve açıkça etiketlenmiş bir ek örnek üretmesi planlanmaktadır. Ardından öğrenci, yeni bir duruma ilişkin dört seçenekli soruyu cevaplar ve kısa gerekçesini yazar. Geri bildirim, şık sonucunu ve gerekçedeki düşünceyi ayrı ele alır; genel yeterlilik puanı üretmez.

Üretken AI'ın temel görevi, verilen metin ve ifadeye göre açıklama/soru üretmek ve öğrencinin yazdığı gerekçeye özel geri bildirim vermektir. Kaynak referansları, sadeleştirmenin hangi metin parçalarına dayandığını inceleme olanağı sağlayacaktır. Katkı iddiası bu odaklı öğrenme döngüsüdür; piyasada ilk veya benzersiz sistem olduğu ileri sürülmez.

## 3. Teknik yaklaşım ve kapsam

Hedef teknoloji Python ve Streamlit'tir. Tarayıcı arayüzü yerel bilgisayarda çalışacak; model bağlantısı için internet ve geçerli API erişimi gerekecektir. İlk sağlayıcı adayı Gemini'dir. Kesin model adı, erişim, kota ve yapılandırılmış çıktı desteği İrem'in gerçek çağrısıyla doğrulanacaktır. Bu taslakta doğrulanmış API başarısı veya maliyet bilgisi verilmemektedir.

İki işlem tanımlanmıştır: `generate_bridge` açıklama, terim, kaynak referansı, örnek ve soruyu; `evaluate_attempt` öğrenci gerekçesine bağlı geri bildirimi üretir. Pydantic ile çıktı biçimi doğrulanacak. Şık sonucu uygulama kodunda cevap anahtarına göre hesaplanacak; anahtarın kendisi model çıktısı olduğundan demo soruları insan incelemesinden geçecektir.

Kaynak ve ifade değişince önceki çalışma temizlenecek, model yalnızca ilgili düğme gönderiminde çağrılacak. Kaynak yetersizse soru gösterilmeyecek. İlk kapsamda hesap sistemi, PDF yükleme, ses ve internette yayınlama bulunmaz. Kullanıcının Python kodu çalıştırılmayacaktır.

## 4. Prompt tasarımı ve değerlendirme yöntemi

Açıklama üretimi ve öğrenci gerekçesini değerlendirme ayrı görevler olarak ele alınacaktır. Prompt, kaynak metni ve öğrenci gerekçesini talimatlardan ayıracak; kaynaktaki koşulların korunmasını, destek tanımlarıyla üretilmiş örneklerin etiketlenmesini ve mevcut paragraf kimliklerinin kullanılmasını isteyecektir. Şema kontrolü biçimi doğrular; açıklamanın anlamca doğru olduğunu tek başına garanti etmez.

Zero-shot başlangıç promptu ile örnek içeren geliştirilmiş prompt, aynı üç metin ve seçilen ifadelerde karşılaştırılacaktır. Her denemede model adı, prompt sürümü, gerçek çıktı ve hata kaydedilecektir. İnceleme ölçütleri anlamın korunması, kaynakla ilişki, açıklık, tek savunulabilir doğru seçenek ve gerekçeye uygun geri bildirimdir. Henüz bu karşılaştırmadan elde edilmiş sonuç yoktur.

---

## 5. Demo içerikleri ve mevcut kanıtlar

Üç özgün Türkçe kaynak metni hazırlanmıştır: Fizik 2'de potansiyel ile potansiyel enerji, ECON 100'de fırsat maliyeti ve temel Python'da for/range sınırları. Metinlerin düzyazı bölümleri sırasıyla 134, 130 ve 121 kelimedir; seçilen ifadelerin her kaynakta tek kez geçtiği yerel kontrolle doğrulanmıştır. Örnek fizik çarpımları ve Python range değerleri de kontrol edilmiştir. Bunlar canlı model veya öğrenme başarısı testleri değildir.

Fizikte işaretler, volt/joule ayrımı ve ΔU = q × ΔV korunmalıdır [2]. Ekonomide vazgeçilen en iyi alternatif, bütün seçeneklerin toplamına dönüştürülmemelidir [3]. Python'da başlangıç dahil, bitiş hariç kuralı ve girintiler korunmalıdır [4]. Her ders için yeni duruma aktarım sorusu ve doğru/yanlış gerekçe örnekleri hazırlanmıştır.

Kabul planında 20 senaryo bulunur. Bunlar üç ders akışı, çelişkili şık/gerekçe, girdi değişince sıfırlama, sınırlar, kod blokları, yetersiz kaynak, talimat içeren girdiler ve API hatalarını kapsar. Bu 20 senaryonun tamamı uygulama üzerinde çalıştırılmayı beklemektedir; geçme oranı hesaplanmamıştır.

## 6. Etik, riskler ve sınırlılıklar

Başlıca riskler anlamı bozan sadeleştirme, yanlış kaynak eşleştirmesi ve hatalı soru anahtarıdır. Önlemler olarak kaynağın görünür tutulması, üretilmiş desteğin etiketlenmesi, geçerli referansların kontrolü ve demo çıktılarının insan incelemesi planlanmıştır. Öğrenci gerekçesinin içindeki talimatlar uygulamanın görevini değiştirmemelidir; ilgili testlerin sonucu ayrıca kaydedilecektir.

API anahtarları repoya eklenmeyecek; kişisel veya gizli ders notları demo girdisi olarak kullanılmayacaktır. İlgisiz gerekçelerden öğrencinin genel yeteneğine ilişkin sonuç çıkarılmayacaktır. Üç içerikle yapılan küçük değerlendirme, bütün derslerde doğruluk veya kalıcı öğrenme kazanımı kanıtı sayılmayacaktır. Model erişimi ve bağlantı sorunları prototipin tamamlanmasını etkileyebilir.

## 7. İş bölümü ve tamamlanacak işler

İrem teknik geliştirme, API bağlantısı ve birleştirmeyi; Mehmet Ali içerik, bağımsız kabul, rapor, İngilizce sunum ve teslim koordinasyonunu takip eder. Teslim için çalışan kodun eklenmesi, gerçek model erişimi, 20 senaryonun sonuçları, prompt karşılaştırması ve İngilizce demo kaydı tamamlanmalıdır. Bu rapor da ardından gerçek model ve sonuçlarla güncellenmelidir.

## Kaynaklar

1. [Birleşmiş Milletler, SDG 4 ve hedef 4.3](https://sdgs.un.org/goals/goal4)
2. [OpenStax, University Physics Volume 2, 7.2](https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference)
3. [OpenStax, Principles of Economics 3e, 2.1](https://openstax.org/books/principles-economics-3e/pages/2-1-how-individuals-make-choices-based-on-their-budget-constraint)
4. [Python resmî öğreticisi, range](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

Repo: https://github.com/Mehmetalimans/anlatim-koprusu
