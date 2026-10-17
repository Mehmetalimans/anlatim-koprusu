# Anlatım Köprüsü - English demo script

**Group 14 | Rehearsal draft v2 | Target: about five minutes**

Bu sürüm konuşma dilini sadeleştirir ve v1 konuşma taslağının yerine geçer. Konuşmacı süreleri hedef aralıklardır; sesli prova henüz yapılmadı. İngilizce bloklar okunacak metindir. Türkçe notlar ekranda yapılacak işi açıklar. Uygulama davranışını anlatan cümleler, son kayıtta yalnızca ekranda gerçekten gösterilen davranışla örtüşüyorsa kullanılır.

## A. 0:00-0:40 - Problem / Mehmet Ali

Ekran: Kapak ve akademik ifade örneği.

> Hello, we are Group Fourteen. Our project is Anlatım Köprüsü. It helps university students understand difficult parts of their course texts. A student may know the topic but still struggle with the words. We show the original text and explain the difficult part. Then we ask a short question and give feedback on the student's reason. The app and learning materials are in Turkish.

## B. 0:40-1:10 - How it works / İrem

Ekran: Öğrenme döngüsü, ardından uygulama. Yerel arayüz doğrulandı; canlı model gösterimi ayrıca doğrulanacak.

> We use Python and Streamlit. The student chooses a text and copies a difficult phrase. The model gives an explanation and a separate example. It also creates a question. The student chooses an answer and writes a short reason. The app needs internet access for the model. We will show the full process with an economics example.

## C. 1:10-1:35 - Choose the phrase / İrem

ECON 100 kaynağını seç. Kaynaktaki `vazgeçilen en iyi alternatifin değeridir` ifadesini kopyala. “Açıkla” düğmesine bas. Geliştirme verisi modu kapalı olmalı.

> Deniz chooses to study. His other choices are a concert and a film. He prefers the concert to the film. I select the phrase about the best alternative he gives up. Then I ask the model to explain it.

## D. 1:35-2:05 - Read the explanation / İrem

Gerçek yanıt gelince kaynak referansını ve ayrı etiketli ek örneği göster. Açıklama doğruysa aşağıdaki konuşmayı kullan. Yanıt yanlışsa prova notuna hatayı yazıp düzeltmeden başarı cümlesi okuma.

> The explanation stays next to the source. We can check what it means. Deniz would choose the concert if he did not study. So the concert is the best alternative he gives up. We should not add the concert and the film together. The extra example has a separate label.

## E. 2:05-2:40 - Try a wrong reason / İrem

Yeni soruyu oku ve gerçek seçenekleri kontrol et. Yanlış seçeneği ve gerekçeyi yeni sorudaki kişi/etkinliklere göre belirle. Aşağıdaki yanılgı yalnızca modelin sorusu gerçekten bu ayrımı sınıyorsa kullanılmalı. Sabit soru ve cevap anahtarı canlı modelin yerine konmayacak.

> I will try a common mistake. I will choose an answer that adds all the other options together. My reason says that every option we give up should count. The feedback should explain what is wrong with this reason.

## F. 2:40-3:25 - Try again / İrem

Gerçek geri bildirimi göster. Doğru seçenek ve düzeltilmiş gerekçeyle yeniden gönder. Anahtarı üretimden önce seyirciye açma. Metin veya seçenek sonucu hatalıysa bunu test hatası olarak kaydet.

> I will try again using the best alternative. We check the chosen option in code. The model comments on the written reason. A correct option can still have a wrong reason, so we check both. We also review the demo answer keys because AI can make mistakes.

## G. 3:25-4:00 - Other subjects / Mehmet Ali

Ekran: Üç ders slaytı. Çalışan fizik ve Python örneklerini kısaca göster. Bu iki alanda canlı akış henüz denenmediyse başarı iddiası ekleme.

> We also prepared examples for Physics Two and basic Python. Physics covers electric potential and potential energy. We check the units and the signs. Python covers for loops and range. We check the code layout and output values. The same learning process is designed for all three subjects.

## H. 4:00-4:35 - Prompts and checks / İrem

Ekran: Prompt yaklaşımı ve gerçek değerlendirme kaydı. Şimdilik aşağıdaki paragraf hazırlık durumunu doğru anlatır. Son kayıtta karşılaştırma tamamlandıysa son cümleyi gerçek bulgu ve kullanılan model adıyla değiştir. Sonuç uydurma.

> We use separate prompts for explanations and feedback. Sixty-eight automated tests passed with controlled responses and no live model calls. We still need to compare the two prompts using the same texts. We will check the meaning, the questions and the feedback. Learning gains have not been measured.

## I. 4:35-5:00 - Social impact and limits / Mehmet Ali

Ekran: SDG 4 ve repo bağlantısı.

> Our goal is to make course texts easier to understand. This connects our project to Sustainable Development Goal Four. We have not measured learning gains. AI can make mistakes, so we show the original text and review the demo results. Thank you.

## Kayıt ve süre kuralları

- Gerçek konuşma süresi ölçülmeden bu akış “beş dakika sürdü” diye raporlanmaz.
- C ve D arasında model yanıtını beklemek için ayrılan zaman sınırlıdır. Gerçek gecikme provada ölçülür; gerekirse anlatım kısaltılır.
- Süre aşılırsa önce tekrar eden açıklamalar azaltılır. Soru, gerekçe ve geri bildirim akışı korunur.
- API çalışmazsa hazır veri canlı yanıt diye gösterilmez. Prova durdurulur veya hata açıkça belirtilir.
- Teknik davranış ve gerçek testler doğrulanmadan şimdiki zamanla anlatılan tasarım, tamamlanmış özellik gibi sunulmaz.
- Son kayıtta taslak sunumun “Pending” bölümleri ve karşılaştırma cümlesi gerçek sonuçlarla güncellenir.
