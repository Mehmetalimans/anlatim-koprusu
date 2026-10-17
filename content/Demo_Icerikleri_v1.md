# Anlatım Köprüsü — Üç Ders İçerik Paketi

**Takipçi: Mehmet Ali | 17 Ekim 2026 | MA-01 | Taslak v1**

Bu dosya İrem’in uygulamaya aktaracağı özgün Türkçe demo metinlerini içerir. İrem’in kesin içerik şeması henüz paylaşılmadığı için Markdown biçimindedir. Her “Kaynak metin” bölümü öğrenciye gösterilecek girdidir; kontrol notları ve gerekçeler öğrenci kaynağına eklenmez. Metinlerdeki paragraflar için P1/P2 gibi kimlikleri uygulama üretecektir.

Bu içerikler canlı AI çıktısı veya tamamlanmış uygulama testi değildir. Kaynaklar kavram kontrolü için okunmuştur; son demo çıktıları Mehmet Ali ve İrem tarafından ayrıca incelenmelidir.

## 1. Fizik 2 — Potansiyel ile enerjiyi ayırmak

- `id`: `fizik2_potansiyel`
- `subject_label`: `Fizik 2 — Elektrik`
- `title`: `Aynı gerilim, farklı enerji değişimi`
- `selected_phrase`: `birim yük başına düşen elektriksel potansiyel enerjiyi`
- `sources`: [OpenStax, University Physics Volume 2, Bölüm 7.2](https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference)

### Kaynak metin

Elektrostatik bir düzende elektriksel potansiyel, seçilmiş bir referansa göre birim yük başına düşen elektriksel potansiyel enerjiyi ifade eder. Potansiyel V ile, potansiyel enerji U ile gösterilir. Volt ile joule farklı büyüklüklerin birimleridir; bir volt, bir coulomb başına bir joule anlamına gelir. Bu yüzden bir noktadaki potansiyeli söylemek, o noktadaki her yükün aynı enerjiye sahip olduğunu söylemek değildir.

Bir q yükü A noktasından B noktasına taşındığında potansiyel farkı ΔV = V_B − V_A olarak tanımlanır. Potansiyel enerji değişimi ise ΔU = q × ΔV bağıntısıyla hesaplanır. Örneğin +2 C yük, potansiyelin 3 V arttığı bir noktaya taşınırsa enerji değişimi +6 J olur. Aynı noktalar arasında −2 C yük taşınırsa değişim −6 J olur. Bu karşılaştırmada alanı oluşturan düzenin değişmediği ve taşınan yükün bu düzeni etkilemediği varsayılır. Hesapta hem yükün hem potansiyel farkının işaretini korumak gerekir.

### Beklenen anlam ve korunacak koşullar

- Potansiyel enerji değildir; enerji/yük oranıyla ilişkilidir.
- Potansiyel farkı son eksi ilk potansiyeldir; ΔU = q × ΔV.
- Referans seçimi ve sabit dış alan varsayımı kaybolmamalıdır.
- Pozitif ve negatif yük örneklerinde birim ve işaret korunmalıdır.

### Yeni duruma aktarım için insan kontrol örneği

Bu soru sabit bir test örneğidir; canlı model sorusunun aynısı olması gerekmez.

**Soru:** Sabit dış alanda +3 C yük, potansiyelin 2 V azaldığı bir noktaya taşınıyor. Potansiyel enerji değişimi nedir?

- A: +6 J
- B: −6 J
- C: −2 J
- D: −2/3 J

**Anahtar:** B. ΔV = −2 V, dolayısıyla ΔU = (+3 C) × (−2 V) = −6 J.

- `correct_rationale`: “Son potansiyel daha küçük olduğundan fark −2 V. Pozitif 3 C ile çarpınca −6 J buluyorum.”
- `incorrect_rationale`: “Gerilim iki azaldığı için yük ne olursa olsun enerji −2 J azalır.”
- Yanlış gerekçede geri bildirim hedefi: Yük çarpanının atlandığını belirtmek; volt ile joule ayrımını açıklamak.

## 2. ECON 100 — Fırsat maliyeti

- `id`: `econ100_firsat_maliyeti`
- `subject_label`: `Temel ekonomi — ECON 100`
- `title`: `Vazgeçilen seçeneklerden hangisi sayılır?`
- `selected_phrase`: `vazgeçilen en iyi alternatifin değeridir`
- `sources`: [OpenStax, Principles of Economics 3e, Bölüm 2.1](https://openstax.org/books/principles-economics-3e/pages/2-1-how-individuals-make-choices-based-on-their-budget-constraint)

### Kaynak metin

Zaman ve kaynaklar sınırlı olduğu için bir seçim yapmak, başka bir fırsattan vazgeçmeyi gerektirebilir. Bir tercihin fırsat maliyeti, vazgeçilen en iyi alternatifin değeridir. Buradaki en iyi alternatif, karar veren kişinin koşullarına ve tercihlerine göre belirlenir. Dolayısıyla aynı kararı veren iki kişinin fırsat maliyeti farklı olabilir. Bu değer yalnızca para ile ifade edilmek zorunda değildir.

Deniz'in aynı akşam ders çalışmak, konsere gitmek veya film izlemek için iki saati vardır. Bu etkinlikler aynı zaman aralığındadır ve yalnızca biri yapılabilir. Deniz ders çalışmayı seçer. Ders çalışmasaydı konseri tercih edeceğini, filmi ise konserden daha az istediğini söyler. Bu durumda seçimin fırsat maliyeti, konser deneyiminin Deniz için taşıdığı değerdir. Konser ile filmin değerleri toplanmaz; ikisi birlikte gerçekleştirilebilen bir seçenek değildir. Örnek, Deniz'in sıralamasının karar anında sabit olduğunu varsayar. Alternatiflerin sırası değişirse değerlendirme de yeniden yapılmalıdır.

### Beklenen anlam ve korunacak koşullar

- Yalnızca vazgeçilen en iyi uygulanabilir alternatif esas alınır; bütün alternatifler toplanmaz.
- Etkinlikler aynı zaman diliminde birbirini dışlar; tercih sırası açıkça verilmiştir.
- Değer zorunlu olarak parasal değildir; kişinin tercihine bağlıdır.

### Yeni duruma aktarım için insan kontrol örneği

**Soru:** Ece aynı saatte yalnız bir etkinlik yapabilir: atölyeye katılmak, yürümek veya film izlemek. Atölyeyi seçer. Atölye olmasaydı yürümeyi, yürüyüş de mümkün olmasaydı filmi seçerdi. Atölyenin fırsat maliyeti hangisidir?

- A: Yürüyüşün Ece için değeri
- B: Yürüyüş ve filmin değerlerinin toplamı
- C: Otomatik olarak sıfır; çünkü etkinlikler için ücret belirtilmemiştir
- D: Atölyenin Ece için değeri

**Anahtar:** A. Seçilmeyen uygulanabilir alternatiflerden en çok tercih edilen yürüyüştür.

- `correct_rationale`: “Atölye yerine yürüyüşü yapacaktı. Vazgeçtiği en iyi seçenek yürüyüş olduğu için onun değeri esas alınır.”
- `incorrect_rationale`: “İki etkinliği de yapamadığı için yürüyüşün ve filmin değerlerini toplamalıyız.”
- Yanlış gerekçede geri bildirim hedefi: Aynı anda gerçekleştirilemeyen alternatiflerin neden toplanmadığını açıklamak.

## 3. Temel Python — for ve range

- `id`: `python_for_range`
- `subject_label`: `Temel Python`
- `title`: `Döngü hangi sayıda durur?`
- `selected_phrase`: `bitiş değeri dahil değildir`
- `sources`: [Python resmî öğreticisi, range işlevi](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

### Kaynak metin

Python'da for döngüsü, bir dizinin veya başka bir yinelenebilir nesnenin elemanlarını sırayla işler. Belirli tam sayılar üzerinde dolaşmak için range kullanılabilir. İki argümanlı range(start, stop) ifadesinde başlangıç değeri dahildir, bitiş değeri dahil değildir. Adım ayrıca verilmediğinde bir kabul edilir. Böylece range(1, 4), sırasıyla 1, 2 ve 3 değerlerini sağlar; 4 için döngü gövdesi çalışmaz.

```python
for sayi in range(1, 4):
    print(sayi)
```

Bu kodda sayi değişkeni her yinelemede sıradaki değeri alır. Girintili print satırı döngü gövdesidir ve her değer için bir kez çalışır. Çıktı ayrı satırlarda 1, 2 ve 3 olur. Girinti, satırın hangi bloğa ait olduğunu belirlediğinden yalnızca görsel bir tercih değildir. range(4) yazılsaydı başlangıç sıfır kabul edilir ve değerler 0, 1, 2, 3 olurdu. Döngünün kaç kez çalışacağını bulurken başlangıcın dahil, bitişin hariç olduğunu birlikte düşünmek gerekir.

### Beklenen anlam ve korunacak koşullar

- Pozitif varsayılan adımla başlangıç dahil, bitiş hariçtir.
- Örnekte üç yineleme ve üç ayrı çıktı satırı vardır.
- Girintiler, değişken adı ve kod bloğu korunmalıdır.
- Bu metin negatif adımları öğretmez; yeni soruda açıklanmayan ters yönlü adım kullanılmamalıdır.

### Yeni duruma aktarım için insan kontrol örneği

**Soru:** Aşağıdaki kod ne yazdırır?

```python
for sayi in range(2, 5):
    print(sayi)
```

- A: Ayrı satırlarda 2, 3, 4, 5
- B: Ayrı satırlarda 0, 1, 2, 3, 4
- C: Ayrı satırlarda 2, 3, 4
- D: Yalnızca 5

**Anahtar:** C. Başlangıç 2 dahil, bitiş 5 hariçtir.

- `correct_rationale`: “İkiyle başlar; beşe gelmeden durur. Bu yüzden 2, 3 ve 4 yazdırır.”
- `incorrect_rationale`: “Başlangıçtan bitişe kadar bütün sayıları içerdiğinden 2, 3, 4, 5 yazdırır.”
- Yanlış gerekçede geri bildirim hedefi: Bitiş sınırının dışarıda kaldığını belirtmek; öğrencinin başlangıcı doğru aldığını da görmek.

## İrem’e devir

1. Üç “Kaynak metin” bölümünü uygulama girdisi olarak kullan; diğer alanları kontrol verisi olarak tut.
2. Kesin içerik şemanı paylaş. Alan adlarını bu taslağa eşleştirip son veri dosyalarını Mehmet Ali hazırlayacak.
3. Hazır soru ve gerekçeler, model üretimini kontrol etmek içindir. Bunları sessizce canlı AI çıktısının yerine koyma.
4. Modelin ürettiği soruda seçenek sırası değişebilir. Gerekçe örneklerini denerken harf yerine ilgili seçeneğin anlamına göre eşleştir.
5. Kaynak metinleri özgün Türkçe anlatımlardır; bağlantılar kavramsal dayanağı gösterir. Başarı/öğrenme etkisi henüz ölçülmemiştir.
