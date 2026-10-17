# Anlatım Köprüsü — Video ekran akışı

**Grup 14 | İngilizce demo | Yaklaşık beş dakika hedefi**

Bu dosya konuşma metnini tekrar etmez; kayıt sırasında hangi ekrana geçileceğini ve hangi uygulama adımının yapılacağını belirtir. Konuşmalar [İngilizce demo metninde](Demo_Konusmasi_EN_v2.md). Süreler hedeftir; gerçek kayıt süresi henüz ölçülmedi. Şimdi ekran sırası okunarak gözden geçirilebilir; sesli prova gerektirmez.

## Kayıt öncesi hazırlık

- Canlı model testleri tamamlanmış son commit'i kullanın; dal ve commit'i not edin. Mehmet Ali'nin mevcut kabul tabanı `codex/acceptance` / `7c506c1`; daha yeni doğrulanmış sürüm varsa onu kullanın.
- `streamlit run app.py` ile uygulamayı açın. Canlı gösterimde **Canlı (Gemini)** modu seçili olmalı. Anahtarın bulunması tek başına başarılı çağrı kanıtı değildir; kayıt öncesinde gerçek bir akışın çalıştığını kontrol edin.
- Son PDF ve sunumdaki model, test sayısı ve prompt bulgularını gerçek kayıtlarla eşitleyin. Taslakta bekleyen bir sonucu tamamlanmış diye anlatmayın.
- Uygulamayı ve altı slaytlık sunumu açın. Yazıların kayıtta okunabildiğini, sesin duyulduğunu kısa teknik denemeyle kontrol edin. Anahtarın bulunduğu `.env` ekranını kayda almayın.
- ECON 100 örneği tam akışın ana konusu. Fizik ve Python'a ayrılan kısa bölümün hangi kanıtı göstereceğine önceden karar verin: gerçek çıktılar ya da açıkça içerik örneği olarak tanıtılan kaynaklar.

## Ekran ve tıklama sırası

| Hedef süre | Konuşmacı | Ekran / işlem | Görünür kanıt |
| --- | --- | --- | --- |
| 0:00–0:40 | Mehmet Ali | Kapak; ardından zor akademik ifade örneği. | Proje adı, Grup 14 ve hedef problem. |
| 0:40–1:10 | İrem | Öğrenme döngüsü slaytı; uygulamaya geç. | Kaynak → açıklama → soru → gerekçe akışı. |
| 1:10–1:35 | İrem | Metin listesinden **Vazgeçilen seçeneklerden hangisi sayılır?** seç. Ön dolu ifadeyi kaynakta göster: `vazgeçilen en iyi alternatifin değeridir`. **Açıkla** düğmesine bir kez bas. | Gerçek kaynak, seçilen ifade ve canlı üretimin başlaması. |
| 1:35–2:05 | İrem | Kaynak ve sade açıklamayı yan yana göster. İlgili paragraf kimliğini ve **Ek örnek** etiketini göster. | Kaynakla bağ ve üretilmiş örneğin ayrımı. |
| 2:05–2:40 | İrem | Yeni soruyu oku. Bu soruya uygun yanlış seçeneği seç; yanlış gerekçeyi yaz ve **Cevabı gönder**. | Sorudaki gerçek yanılgıya dayalı öğrenci denemesi. |
| 2:40–3:25 | İrem | Gerçek geri bildirimi göster. **Tekrar dene** düğmesine bas; aynı soruya doğru seçenek ve düzeltilmiş gerekçe yazıp gönder. | Yanlış ve düzeltilmiş gerekçeye verilen geri bildirim. |
| 3:25–4:00 | Mehmet Ali | Üç ders slaytı; fizik ve Python'un doğrulanmış kısa örnekleri. Ders değişimi eski çalışma sonucunu temizler. | İşaret/birim ve kod/sınır gibi farklı içerik türleri. |
| 4:00–4:35 | İrem | Prompt ve test slaytı; gerçek kabul kaydını göster. | Çevrimdışı testlerle canlı gözlemlerin kapsamı ve varsa gerçek prompt karşılaştırması. |
| 4:35–5:00 | Mehmet Ali | SDG 4 ve repo bağlantısı; kapanış. | Amaç, ölçülmemiş öğrenme kazanımı ve teslim bağlantısı. |

## ECON 100 denemesini seçme kuralı

Kaynakta Deniz ders çalışmayı seçiyor; çalışmasaydı konseri tercih edeceğini söylüyor. Kaynağın fırsat maliyeti konser deneyiminin değeridir. **Üretilen soru yeni bir kişi ve farklı seçenekler kullanabilir.** Soru Deniz hakkında olmak zorunda değildir; her seferinde yeni sorunun kendi koşulları ve seçenekleri okunmalı.

Yanlış gerekçede bütün vazgeçilen alternatifleri toplama yanılgısı, yalnızca gerçek soru buna uygunsa kullanılacak. Kaynak metne veya eski sabit soruya ait cevabı yeni soruya kopyalamayın. Doğru cevap anahtarı yanlışsa kayda devam etmeden hatayı kabul kaydına yazın ve düzeltin.

Yanlış denemeden sonra **Doğru cevabı göster** açılır bölümünü, yeniden deneme adımı bitene kadar kapalı tutun. İkinci denemede **Açıkla** düğmesine yeniden basmayın: bu yeni soru üretebilir. Formu **Tekrar dene** ile sıfırlayın.

## Akış aksarsa

- **API hatası:** Hata mesajını ve yeniden denemeyi kontrol edin. Son kayıtta başarılı canlı akış gerekiyor; sabit geliştirme verisini canlı yanıt diye kullanmayın.
- **Yanlış veya birden fazla doğru seçenek:** Çıktıyı hata olarak kaydedin. Yeni soruyu da okuyarak kontrol edin; sorunu gizleyip aynı cevabı ezberden göndermeyin.
- **Gecikme / süre aşımı:** Önce slaytlardaki tekrarları ve diğer iki dersin gösterim süresini azaltın. Ana derste soru, gerekçe ve geri bildirim adımlarını koruyun. Canlı yanıt gecikmesi, içerik doğruluğundan ayrı bir gözlemdir.

## Son kayıt kontrolü

- [ ] Kaydedilen dal/commit ve gerçek model adı belli.
- [ ] Ses ve uygulamadaki yazılar anlaşılır; İngilizce anlatım mevcut.
- [ ] Ana derste kaynak, canlı açıklama, soru, gerekçe ve geri bildirim görülüyor.
- [ ] Geliştirme verisi canlı model sonucu gibi gösterilmiyor.
- [ ] Konuşma ve slaytlardaki sonuçlar gerçek kabul kaydıyla aynı.
- [ ] Gerçek video süresi ölçülmüş; yaklaşık beş dakikalık hedef kontrol edilmiş.
- [ ] Video ve diğer teslim dosyaları hedef kitlenin açabileceği izinlerle paylaşılmış.

Bu liste işaretlenmiş bir test kaydı değildir; maddeler gerçek işlem tamamlandığında işaretlenir. Teslimin güncel dosyaları [delivery/README.md](../delivery/README.md) içinde.
