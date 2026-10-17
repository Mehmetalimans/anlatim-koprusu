# Hazır içerik ve referans verilerini kullanma

Bu paket İrem'in koduna bağlı olmadan hazırlanmıştır. Veriler uygulama/model testinin sonucu değildir. Önceden yazılmış soruların tamamı geliştirme ve kontrol amacı taşır.

## Üç doğrudan kullanılabilir girdi

[demo_inputs.json](../content/demo_inputs.json) üç dersin kaynak metnini, seçilen ifadesini, ders etiketini ve kaynak bağlantısını içerir. Her öğenin `request` alanı ortak plandaki `BridgeRequest` alanlarına karşılık gelir:

```python
import json
from pathlib import Path

items = json.loads(Path("content/demo_inputs.json").read_text(encoding="utf-8"))["items"]
request_fields = items[0]["request"]
# Gerçek sözleşme geldiğinde BridgeRequest(**request_fields) ile kullanılabilir.
```

Bu örnek bir dosya okuma işlemidir; API çağrısı yapmaz. Kesin uygulama içerik şeması henüz İrem'den gelmediği için bütün JSON dosyasının uygulama yükleyicisine uyduğu varsayılmaz. UI üzerinden de `source_text` ve `selected_phrase` alanları kopyalanarak kullanılabilir.

## On iki şık/gerekçe denemesi

[feedback_reference_cases.json](feedback_reference_cases.json) üç sabit referans sorusu ve her biri için dört öğrenci denemesi içerir:

| Şık | Gerekçe | Beklenen ayrım |
| --- | --- | --- |
| Doğru | Kavramsal olarak doğru | Şık doğru; geri bildirim doğru düşünceyi tanır. |
| Yanlış | Kavramsal olarak yanlış | Şık yanlış; gerekçedeki somut hata açıklanır. |
| Doğru | Kavramsal olarak yanlış | Şık doğru kalır; gerekçedeki hata ayrıca açıklanır. |
| Yanlış | Kavramsal olarak doğru | Şık yanlış kalır; doğru düşünce ile seçim arasındaki uyuşmazlık belirtilir. |

`bridge_fixture`, ortak plandaki alan adlarıyla hazırlanmış geliştirme verisidir. Kesin Pydantic modelleriyle uyum, modeller geldiğinde ayrıca doğrulanır. `feedback_review_points` içerik değerlendirmesine yardımcı olur; AI geri bildiriminin belirli bir cümleyi birebir yazması şart değildir.

Önemli: A/B/C/D anahtarları yalnızca bu sabit sorular için geçerlidir. Canlı modelin yeni sorusuna aynı harfler taşınmaz. Python referansındaki P1/P3 kimlikleri, kod bloklarının tek parça tutulduğu ortak paragraf kuralını varsayar. Gerçek bölücüyle uyum ayrıca kontrol edilir.

## On iki girdi senaryosu

[input_reference_cases.json](input_reference_cases.json), boş girdi, kaynakta bulunmayan ifade, 6.000/6.001 karakter sınırı, boşluk farkı, Türkçe harf farkı, çoklu eşleşme, kod içi boş satır, kapanmamış kod bloğu, yetersiz bağlam ve talimat içeren kaynak için gerçek gönderilebilir girdiler içerir.

`expected_prevalidation=pass`, yalnızca giriş kontrolünün model adımına izin vermesi gerektiğini söyler. Modelin mutlaka `ready` döndürmesi anlamına gelmez. `execution_status=not_run` alanları uygulama denendikten sonra kanıtla birlikte güncellenir.

## Altı açıklama/soru üretimi denemesi için kayıt

[prompt_comparison_records.json](prompt_comparison_records.json), üç ders çarpı iki prompt yaklaşımı için altı boş kayıt içerir. Bu kayıtlar `generate_bridge` görevini karşılaştırır. Promptları İrem sağlayacak. Aynı kaynak ve ifadeyle gerçek çıktı alındığında model adı, prompt sürümü ve gözlemler kaydedilir. Gerekçe geri bildirimi ayrıca 12 denemelik referans paketiyle incelenir. Boş alanlar başarı puanı veya sonuç olarak doldurulmaz.

## Otomatik dosya kontrolü

Proje kökünde çalıştır:

```text
python evaluation/check_materials.py --report evaluation/materials_check_result.json
```

PDF sayfa kontrolü için `pypdf` gerekir. Bu bilgisayardaki Codex çalışma ortamında paket mevcuttur. Bu kontrol aracının gereksinimi, İrem'in uygulama bağımlılıklarını değiştirmez.

Araç; girdilerin sınırlarını, Markdown/JSON eşleşmesini, referans anahtarlarını, dört gerekçe kombinasyonunu, yerel belge bağlantılarını, PDF sayfa sayısını, PPTX yapısını ve konuşma kelime sayısını denetler. Model çağırmaz, öğrenci kodu çalıştırmaz, canlı uygulamanın doğruluğunu veya öğrenme etkisini ölçmez.
