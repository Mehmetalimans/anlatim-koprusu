# Anlatım Köprüsü - Proje Raporu

**Grup 14 | 17 Ekim 2026 | Değerlendirilen uygulama sürümü: 06a6c25**

## 1. Problem, hedef kullanıcı ve SDG bağlantısı

Üniversite öğrencileri bir konunun genel çerçevesini bilseler bile akademik terimler ve yoğun ifadeler nedeniyle ders metninde takılabilir. Anlatım Köprüsü, öğrencinin anlamadığı ifadeyi kaynak bağlamında açıklayan ve kısa bir uygulamayla anlama kontrolü sağlayan üretken AI prototipidir. Hedef kitle 18 yaş üstü üniversite öğrencileri; arayüz ve öğrenme çıktıları Türkçedir. Kullanıcı ihtiyacı henüz saha araştırmasıyla ölçülmemiştir.

Proje, SDG 4 - Nitelikli Eğitim ile ilişkilidir. Özellikle hedef 4.3'teki nitelikli yükseköğretime eşit erişim amacıyla bağlantı kurar [1]. Amaç, öğrenme materyallerinin anlaşılmasına destek olmaktır. Eğitim eşitsizliğini azalttığımız veya öğrenme başarısını artırdığımız ölçülmüş bir sonuç değildir.

## 2. Çözüm ve çalışan prototip

Öğrenci **Kendi metnim** seçeneğiyle en fazla 6.000 karakterlik kaynak yazar veya hazır ders örneği seçer. Kaynakta geçen zor ifadeyi belirtip **Açıkla** düğmesine basar. Sistem sade açıklama, terim kartları, kaynak paragraf referansları, ayrı etiketli üretilmiş örnek ve yeni duruma ilişkin dört seçenekli soru sunar. Öğrenci şık ve kısa gerekçe gönderir; geri bildirimden sonra aynı soruyu yeniden deneyebilir.

Kaynak ve açıklama yan yana gösterilir. Kod blokları görüntülenir, çalıştırılmaz. Girdi veya çalışma modu değişince eski sonuçlar temizlenir. Yetersiz kaynak sonucunda cevap formu açılmaz. Fizik 2, ECON 100 ve temel Python için özgün, kaynakları belirtilmiş üç ders metni vardır [2-4]. Bunlar test örnekleridir; kullanıcı girişi bu metinlerle sınırlı değildir.

## 3. Model, mimari ve kurulum

Python + Streamlit arayüzü, Gemini REST istemcisi ve Pydantic veri modelleri kullanılır. Yerel teknik ortam Python 3.12.14 ve Streamlit 1.66.0'dır. İrem'in paylaştığı gerçek çağrı kayıtlarında model **gemini-3.5-flash-lite**, sıcaklık 0.4 ve yapılandırılmış JSON çıktı kullanılmıştır. Model adı ortam değişkeniyle değiştirilebilir.

İki AI görevi vardır: `generate_bridge` açıklama/soru üretir; `evaluate_attempt` öğrencinin gerekçesini değerlendirir. Şık sonucu, modelin ürettiği cevap anahtarıyla kodda karşılaştırılır; model bu sonucu değiştiremez. Bu nedenle anahtarın anlam doğruluğu ayrıca incelenir. Kurulum komutları README'dedir; uygulama `streamlit run app.py` ile tarayıcıda açılır. Canlı mod internet ve yerel `GEMINI_API_KEY` gerektirir. Anahtarsız `.env.example` paylaşılır; gerçek `.env` repoya eklenmez.

## 4. Önemli promptlar ve tasarım gerekçeleri

**Açıklama promptundan:** “Öğrencinin zorlandığı ifadeyi (selected_phrase), YALNIZCA verilen kaynak parçalarına (segments) dayanarak açıkla.” Kaynak kimlikleriyle ilişki kurulması, açıklamanın bağlam içinde denetlenmesini sağlar.

**Soru promptundan:** “Öğrenci kuralı bu yeni duruma UYGULAMALI” ve “Seçenekler yalnızca cevap olsun; gerekçe (...) yalnızca answer_explanation alanında yer alsın.” Amaç, tanımı kopyalamak yerine yeni örnekte kullanımı sınamak ve cevabı seçenek içinde açıklamamaktır.

**Geri bildirim promptundan:** “Gerekçe doğru ve yeterliyse boş liste ver; hata veya eksik uydurma.” Kaynak, soru ve gerekçe JSON veri olarak iletilir; içlerindeki talimatlar görev sayılmaz. Geri bildirime kaynak metin de eklenerek kaynağa aykırı yorumların azaltılması hedeflenir. Tam promptlar `core/prompts.py` içindedir. Kurallardan oluşan `zero_shot` ile ozmoz konusunda bir biçim örneği ekleyen `few_shot` karşılaştırılmıştır; örnek demo derslerinden farklıdır.

---

## 5. Testler ve gerçek gözlemler

Son kodda bağımsız olarak yeniden çalıştırılan **69 otomatik testin tamamı geçti**. Bu testler ağ çağrılarını engelleyip kontrollü yanıtlar kullanır; canlı model başarısı veya öğrenci başarısı ölçümü değildir. Girdi sınırları, Türkçe harf/boşluk eşleşmesi, kod blokları, geçersiz referanslar, şık karşılaştırması, oturum sıfırlama, hata yönetimi ve Streamlit akışı kontrol edilmiştir.

İrem'in bilgisayarında iki prompt revizyonu boyunca **16 gerçek üretim ve 50 gerçek geri bildirim** kaydedilmiştir; bağlantı denemesi ayrı tutulur. Son üretim karşılaştırması üç ders ve iki prompt sürümünde altı çıktı içerir. Her hücrede tek çalıştırma vardır. Kayıtlardaki incelemede iki sürüm arasında cevap anahtarı doğruluğu farkı gözlenmemiş; örnekli sürüm daha kısa sorular üretmiştir. Bu küçük örneklem genel üstünlük iddiası için yeterli değildir.

Son geri bildirim revizyonunun 25 kaydında şık sonucu 25/25 kod anahtarıyla eşleşmiştir. “Doğru şık + yanlış gerekçe” alt grubunda altı denemeden beşinde hata belirtilmiş; bir ekonomi gerekçesinde listedeki sıraya dayanan yanlış düşünce övülmüştür. Bu, gerekçeye duyarlı değerlendirmenin henüz her durumda güvenilir olmadığını gösterir. Paylaşılan 16 üretim ve 50 geri bildirim kaydı ayrıca yerelde sözleşme ve şık eşleşmesi açısından incelenmiştir; yeni canlı çağrı yapılmamıştır.

## 6. Karşılaşılan zorluklar ve iyileştirmeler

İlk promptta fizik soruları tanım cümlesini tanımaya dayanıyordu. Sonraki revizyonda yeni duruma uygulama, sayısal koşullar ve seçeneklerde gerekçe bulunmaması kuralları eklendi. Geri bildirimde kaynağa aykırı veya alanlar arasında çelişen yorumlar görülünce kaynak metin isteme dahil edildi. Arayüzde mod değişiminde eski geliştirme sonucunun kalması ve sorulardaki kod gösterimi gibi üç regresyon yeniden üretilip düzeltildi.

Bilinen sınırlar: Bir fizik cevap açıklamasında potansiyel enerji U ile enerji değişimi ifadesi karışmıştır. Negatif yük/işaret örneği canlı sorularda ayrıca sınanmamıştır. Kaynaktaki talimat denemesinde normal açıklama üretilse de istenen harf ile gerçek doğru harf aynı olduğundan seçenek üzerindeki etki ayırt edilememiştir. Son üretim revizyonuyla son geri bildirim revizyonu aynı yeni sorular üzerinde uçtan uca henüz kaydedilmemiştir. Manuel yeni metinle son canlı deneme bu nedenle önemlidir.

## 7. Etik değerlendirme ve etkiyi ölçme

AI yanlış bilgi, hatalı soru anahtarı veya gerekçeyi yanlış öven geri bildirim üretebilir. Pydantic biçim kontrolü anlam doğruluğunu garanti etmez. Kaynağın görünür tutulması, geçerli paragraf referansları, üretilmiş örneklerin ayrı etiketlenmesi ve demo çıktılarının insan tarafından incelenmesi bu riskleri azaltmayı amaçlar. Az sayıda talimat testi genel güvenlik garantisi değildir. Geliştirme verisi açıkça etiketlenir ve canlı AI çıktısı olarak sunulmaz.

Öğrenciye genel yeterlilik puanı verilmez. Demo girdilerinde kişisel veya gizli notlar kullanılmaz; anahtar yerel ortamda tutulur. Mevcut doğrulama üç ders örneğiyle sınırlıdır; başka alanlara otomatik genellenmez. Sonraki değerlendirme, öğrencilere kısa anlama sorularını açıklama öncesi/sonrası uygulayarak doğru gerekçe oranını ve kullanılabilirliği inceleyebilir. Henüz böyle bir öğrenci çalışması veya ölçülmüş öğrenme kazanımı yoktur.

## Kaynaklar

1. [BM, SDG 4 ve hedef 4.3](https://sdgs.un.org/goals/goal4)
2. [OpenStax, University Physics Volume 2, 7.2](https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference)
3. [OpenStax, Principles of Economics 3e, 2.1](https://openstax.org/books/principles-economics-3e/pages/2-1-how-individuals-make-choices-based-on-their-budget-constraint)
4. [Python resmî öğreticisi, range](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

Kod, promptlar ve kurulum: https://github.com/Mehmetalimans/anlatim-koprusu/tree/codex/acceptance . Canlı kayıtlar: `evaluation/live/`; inceleme: `evaluation/Canli_Sonuclar_20261017.md`.
