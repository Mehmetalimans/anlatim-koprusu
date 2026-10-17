# İrem / Claude — GitHub Üzerinden Başlangıç

**Güncel iş dağılımı: v2.** Önceki PDF'deki “Mehmet Ali core, İrem UI” ayrımı artık geçerli değildir.

## Önce oku

1. [Proje ve iş bölümü v2](Proje_ve_Is_Bolumu_v2.md)
2. [Üç ders içerik paketi](../content/Demo_Icerikleri_v1.md)
3. [Kabul testleri planı](../evaluation/Kabul_Test_Plani.md)
4. Reponun güncel dosyaları ve son commit'i.

İlk repo sürümünde uygulama kodu yoktur. Bu mesajı okuduğunda kod eklenmiş olabilir; güncel durumu kontrol etmeden yeniden yazmaya başlama.

## Görevin

Ben İrem. Grup 14 olarak **Anlatım Köprüsü** projesini seçtik. Teknik geliştirmeyi benim Claude oturumum takip ediyor: `core/`, `ui/`, `app.py`, Pydantic modelleri, örnek veriler, model/API araştırması ve bağlantısı, promptlar, oturum yönetimi, teknik testler, bağımlılıklar ve teknik README.

Mehmet Ali içerikleri, bağımsız kabul testlerini ve teslim belgelerini takip ediyor. **Mehmet Ali'den `core/contracts.py` ve örnek çıktı bekleme; bunları hazırlama görevi bizde.** Fikir seçimini yeniden açma.

İlk teknik teslim:

- Pydantic sözleşmeleri ve servis imzaları.
- `ready` ve `insufficient_source` geliştirme verileri.
- En küçük Streamlit uygulama iskeleti.
- Model erişim denemesinin gerçek sonucu veya açık erişim engeli.
- Mehmet Ali'nin içerikleri için kesin şema ve alan eşleştirmesi.

Ardından bir dersle gerçek açıklama → dört seçenekli soru → öğrenci gerekçesine dayalı geri bildirim akışını tamamla. Diğer dersleri aynı akışta bağla.

## İçerik paketini nasıl kullanacaksın?

`Demo_Icerikleri_v1.md` içindeki her **Kaynak metin** bölümü öğrenci girdisidir. Kaynak bağlantıları ve ders etiketleri metadatalardır. Beklenen anlamlar, sabit kontrol soruları, cevap anahtarları ve doğru/yanlış gerekçeler test materyalidir; hepsini öğrenci kaynağına ekleme. Hazır soruları canlı AI çıktısı yerine kullanma.

Şema kesinleşince Mehmet Ali son içerik dosyalarını hazırlayacak. İhtiyaç duyduğun alan/türleri tek bir devir mesajında paylaş; bu sırada teknik iskeleti ilerlet.

## Ortak çalışma

- Repo erişimini ve erişebildiğin dosyaları açıkça belirt. Sadece bağlantı verildiği için erişimin olduğunu varsayma.
- `codex/app` dalında güncel `main` üzerinden çalış; aynı dosyaya eşzamanlı müdahaleyi koordine et.
- `content/` ve `evaluation/` Mehmet Ali'nin takibinde. Bu dosyalarda gereken değişikliği örnekle bildir. Mehmet Ali'nin içerik/veri şemasını etkileyen değişiklikleri paylaş.
- Başka bir AI'ın sohbetini otomatik bildiğini varsayma. Devirde dal/commit, dosyalar, gerçek kontroller ve kalan işleri yaz.
- Repo üzerinde dosya değiştirme/push erişimin yoksa uygulanabilir dosya veya yama üret; uygulanmış gibi raporlama.
- API anahtarını yerel yapılandır; sohbete, repoya veya loga yazma. Ücretli hizmet açma.
- İlk sürümde teknik kapsamındaki rutin işler için yeniden onay beklemeden ilerle. Üçüncü saatte temel akışa odaklan; dördüncü saatte yeni özellik eklemeyi bırak.

## Devir şablonu

```text
İş / başlangıç commit'i:
Tamamlananlar:
Değişen dosyalar:
Çalıştırma komutu:
Gerçek kontroller ve sonuçları:
Yapılamayan kontroller / erişim engelleri:
Mehmet Ali'den gerekenler:
Sonraki adım:
```

İlk cevapta dosya erişimini, mevcut çalışmayı ve hemen başlayacağın somut teknik işi bildir.
