# Anlatım Köprüsü — Jüri soruları için cevap kartları

**Grup 14 | 17 Ekim 2026 | Canlı değerlendirme öncesi taslak**

Bu kartlar sesli prova gerektirmeden sunum içeriğini hazırlamak içindir. İngilizce cevaplar kısa tutuldu. Gerçek model sonuçları gelince ilgili cevaplar güncellenmelidir; aşağıdaki teknik test sayısı canlı model başarı oranı değildir.

## 1. Hangi problemi çözüyorsunuz?

**Question:** What problem are you solving?

**Answer:** University students can get stuck on a difficult expression in a course text. We explain that expression in context, then ask a question to help them apply the idea.

Türkçe dayanak: Hedef kitle 18 yaş üstü üniversite öğrencileri. Bütün bir dersin yerine geçmek yerine belirli bir ifadede takılma anına odaklanıyoruz. Kullanıcı ihtiyacını henüz öğrenci araştırmasıyla ölçmedik.

## 2. Genel bir sohbet aracından farkınız ne?

**Question:** What does your application add to a general chat tool?

**Answer:** We provide a guided workflow: source, explanation, a new question and feedback on the student's reason. The source stays next to the explanation so the student can check the context.

Türkçe dayanak: Bu, tasarım tercihimizin açıklamasıdır. Diğer araçlardan daha başarılı olduğumuzu veya dünyada ilk olduğumuzu gösteren karşılaştırmamız yok.

## 3. Üretken AI projede ne yapıyor?

**Question:** What does generative AI do in your project?

**Answer:** The model creates the explanation, term cards, an extra example and a new question. A separate model task gives feedback on the student's written reason.

Türkçe dayanak: Kodda iki işlem `generate_bridge` ve `evaluate_attempt`. Geliştirme modu sabit örnek kullanıyor; bu cevap son sunumda gerçek model akışıyla desteklenmeli.

## 4. Doğru cevaba kim karar veriyor?

**Question:** How do you decide whether an answer is correct?

**Answer:** The model generates a question and an answer key. Our code compares the student's option with that key. We also review the demo keys because a model can produce a wrong key.

Türkçe dayanak: Kodun şık karşılaştırması deterministiktir; AI tarafından oluşturulan anahtarın anlam bakımından doğruluğu ayrıca incelenir. Gerekçe hatalıysa şık sonucu değiştirilmeden geri bildirim verilir.

## 5. Hatalı bilgi üretmesini nasıl ele alıyorsunuz?

**Question:** How do you handle incorrect model output?

**Answer:** We keep the source visible, check the output structure and validate source identifiers. We label generated examples separately. These checks do not guarantee factual accuracy, so we also review the demo content.

Türkçe dayanak: Pydantic ve mevcut paragraf kimliği kontrolü anlam doğruluğu garantisi değildir. Kaynak yetersizliği için ayrı sonuç ve ekran vardır; modelin bu durumu doğru saptaması canlı test kapsamındadır.

## 6. Ne kadar test ettiniz?

**Question:** What have you tested so far?

**Answer — mevcut doğrulanmış durum:** We passed sixty-eight automated tests using controlled responses with live network calls blocked. We also checked the local interface in a browser. Live model quality and prompt comparison are still pending.

Türkçe dayanak: [Kabul kaydı](../evaluation/Kabul_Sonuclari_20261017.md). 68 test, 68 öğrenci veya 68 gerçek model denemesi değildir. İrem sonuçları gönderdiğinde son cümle gerçek sayılar ve bulgularla değiştirilecek.

## 7. Promptları nasıl geliştirdiniz?

**Question:** How are you evaluating your prompts?

**Answer — mevcut durum:** We prepared a prompt without an example and a version with an example. We plan to compare them on the same three texts, checking meaning, references, questions and feedback. We have not completed that comparison yet.

Türkçe dayanak: Kodda `zero_shot` ve `few_shot` sürümleri var. Son sunumda gözlenmiş fark yoksa örnekli sürümün daha iyi olduğu söylenmemeli.

## 8. Neden üç farklı ders?

**Question:** Why did you choose three subjects?

**Answer:** We want to check the same workflow on different kinds of material. Physics tests signs and units, economics tests a conceptual distinction, and Python tests code layout and boundaries.

Türkçe dayanak: Üç içerik uygulamada yükleniyor. Bu durum tüm derslerde doğruluk kanıtı değildir. Kullanıcı kendi metnini de yapıştırabilir; doğrulama kapsamımız seçtiğimiz örneklerle sınırlı.

## 9. SDG 4'e katkınız nedir? Öğrenmeyi artırdınız mı?

**Question:** How does this support SDG Four, and have you measured learning gains?

**Answer:** Our aim is to make learning materials easier to understand and support access to learning. We have not measured learning gains. A next step would be a small student study with comprehension tasks.

Türkçe dayanak: Sosyal etki hedefiyle ölçülmüş sonuç birbirinden ayrılır. Bu öğrenci çalışması mevcut hackathon teslimi için yapılmış bir faaliyet veya yeni zorunlu iş değildir.

## 10. Nerede çalışıyor ve başkaları nasıl kullanır?

**Question:** How can someone run your prototype?

**Answer:** It runs in a browser through Streamlit. The repository includes installation instructions. Live mode needs internet access and a valid API key; the local address only works on the computer running the app.

Türkçe dayanak: Prototipin internette yayınlanmış ortak bir adresi henüz yok. Geliştirme modu anahtar olmadan ekran akışını gösterebilir; gerçek model üretimi yerine geçmez.

## Cevapları sonlandırmak için gerekenler

İrem'den model adı, başarılı canlı çıktı kayıtları, içerik/geri bildirim incelemesi ve prompt karşılaştırması gelince özellikle 3, 6 ve 7 numaralı cevapları güncelleyin. Sayılar ve başarı iddiaları [gerçek kabul kayıtlarıyla](../evaluation/Kabul_Sonuclari_20261017.md) aynı olmalı. Kaynak olarak proje raporundaki SDG ve ders bağlantıları kullanılabilir; bu kartlar yeni bir dış araştırma içermez.
