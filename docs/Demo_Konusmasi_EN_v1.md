# Anlatım Köprüsü - English Demo Script

Güncel konuşma metni: [Demo konuşması v2](Demo_Konusmasi_EN_v2.md). Bu dosya önceki taslak olarak saklanmıştır.

**Group 14 | Rehearsal draft v1 | Target: about five minutes**

Bu belge prova içindir. Canlı akış henüz çalıştırılmadı ve süre ölçülmedi. Söylenecek cümleler, çalışan sürümde gerçekten görülen davranışla eşleştirilecek. İngilizce metinler okunacak konuşmadır; Türkçe notlar kayıt ekibine yöneliktir. Yanlış bir davranış görülürse başarı cümlesi okunmaz; hata kaydedilir ve giderilir.

## 0:00-0:40 - Problem and users / Mehmet Ali

**Ekran:** İngilizce sunumun kapak slaytı, ardından akademik ifade örneği.

> Hello, we are Group Fourteen. Our project is Anlatım Köprüsü, which means a bridge to understanding. We focus on university students who find an academic phrase difficult to understand. A shorter sentence can help, but the student also needs to check its meaning in context. Our idea combines an explanation linked to the source with a short application question and feedback on the student's own reason. The interface and learning materials are in Turkish.

## 0:40-1:10 - The learning flow / İrem

**Ekran:** Öğrenme döngüsü slaytı, sonra uygulamaya geçiş. Bu bölüm yalnızca uygulama gerçekten çalışınca şimdiki zamanla okunur.

> The student chooses a source text and copies a difficult phrase. The model produces an explanation, term definitions and a separate example. The student then answers a multiple-choice question and explains the answer. We use Python and Streamlit for the application. The live model connection requires internet access. We will now show the complete flow using an economics example.

## 1:10-3:25 - Live economics demo / İrem

**Kayıt öncesi:** Geliştirme verisi modu kapalı olmalı. API erişimi ve kota önceden denenmeli. Örnek seçilse bile “Açıkla” düğmesi gerçek çağrı yapmalı. Canlı soru önceden yazılmış test sorusuyla değiştirilmemeli.

**1:10-1:35:** ECON 100 örneğini seç, kaynakta geçen “vazgeçilen en iyi alternatifin değeridir” ifadesini göster ve “Açıkla”ya bas.

> This text explains opportunity cost. Deniz chooses studying. If he did not study, he would prefer the concert to the film. I select the phrase about the best alternative he gives up and ask for an explanation.

**1:35-2:05:** Yanıt gelince gerçek açıklamayı ve ilgili kaynak paragrafını göster. Kaynakta olmayan ek örneğin etiketini aç. Ekrandaki anlam bu açıklamayla tutarlıysa konuş:

> Here we can compare the explanation with the source. The important point is the best alternative Deniz would choose. We should not add the values of every activity he cannot do. The additional example has a separate label, so the student can distinguish it from the original text.

**2:05-2:40:** Yeni soruyu ekranda oku. Yanlış seçeneği gerçek soru anahtarını kontrol ederek belirle. Gerekçeyi yeni sorudaki kişi ve seçeneklere uyarlayarak yaz. Modelin ürettiği soru bu kavramı sınamıyorsa önce soru kalitesi sorununu düzelt; zorla bu senaryoya uydurma.

> Now I will try the question with a common mistake. I will treat all the rejected alternatives as if we should add them together. The feedback should explain the problem in my reason, as well as show the result of my selected answer.

**2:40-3:25:** Gerçek geri bildirimi göster; yanlış düşünceyi gerçekten ele alıp almadığını kısaca açıkla. Doğru seçenek ve düzeltilmiş gerekçeyle yeniden dene.

> I will now explain the choice using the best available alternative. This lets us check whether the feedback responds to the student's reasoning. The app checks the selected option against the generated answer key. Our team also reviews the demo questions because a model can produce an incorrect key.

Gecikme uzarsa açıklama beklerken aynı cümleleri tekrar etme. İlk yanıttan sonra prova akışını kısalt; zorunlu canlı kullanım bölümünü koru. Uzun kesinti yaşanırsa bunu gizleyerek hazır veriyi canlı yanıt diye gösterme.

## 3:25-4:00 - Other subjects / Mehmet Ali

**Ekran:** Üç ders slaytı ve çalışan fizik/Python örneklerinden kısa görüntüler. İki alanda akış gerçekten denenmediyse “aynı akış çalışıyor” iddiası yerine kapsamın henüz doğrulanmadığını açıkla.

> We prepared two more subject examples. Physics focuses on the difference between electric potential and potential energy. Python focuses on for loops and the stopping boundary of range. We check the units and charge signs in physics, and the indentation and output values in Python. These examples help us examine whether the explanation preserves the original meaning.

## 4:00-4:35 - Prompt design and evidence / İrem

**Ekran:** Prompt yaklaşımı slaytı ve gerçek test kaydı. Şimdiki taslakta karşılaştırma tamamlanmadığı için aşağıdaki hazırlık cümlesi doğrudur:

> We separate explanation generation from feedback on the student's reason. Our evaluation plan compares a zero-shot prompt with a prompt that includes an example, using the same input texts. We examine meaning, source references, question quality and the relevance of feedback. The comparison is still pending in this draft.

**Son kayıt için:** Karşılaştırma yapıldıktan sonra son cümleyi yalnızca gerçek bulguyla değiştir. Örnek doldurma cümlesi veya uydurma başarı yüzdesi kullanma. Kesin model adını gerçek teknik kayıttan söyle. Ekrana gösterilecek kanıtlar, gerçek çıktı ve sürüm bilgisi içermeli.

## 4:35-5:00 - SDG 4 and limits / Mehmet Ali

**Ekran:** Sosyal etki ve sınırlar slaytı, repo bağlantısı.

> We connect this project to Sustainable Development Goal Four through access to understandable learning support. We have not measured learning gains. The model may still produce mistakes, so source visibility and human review remain important. Our repository documents the project and its test plan. Thank you.

## Kayıt öncesi kısa kontrol

- Mikrofon, ekran yazıları ve Türkçe karakterler okunuyor mu?
- API anahtarı, hesap bilgileri ve özel sekmeler görüntüden çıkarıldı mı?
- En az bir dersin açıklama, soru ve gerekçe geri bildirimi akışı gerçek çağrıyla tamamlandı mı?
- Konuşma, gösterilen sürümün yaptığı şeyi anlatıyor mu?
- Gerçek testler ve prompt karşılaştırması rapora/slaytlara işlendi mi?
- Video İngilizce mi ve prova süresi yaklaşık beş dakika mı?

Kaynak dayanağı: repo içindeki içerik paketi ve güncel proje planı. SDG 4: https://sdgs.un.org/goals/goal4
