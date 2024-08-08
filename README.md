# GümüşAI  
Bu proje, açık kaynak büyük dil modellerinin Türkçe dilinde daha iyi performans göstermesini amaçlar.  Mevcut dil modelleri, Türkçe dil bilgisi, sözcük dağarcığı ve anlamsal bütünlük konularında yetersizlikler göstermektedir. Bu eksiklikler, Türkçe konuşan kullanıcılar için tatmin edici olmayan sonuçlar doğurmakta ve dil modellerinin etkili kullanımını sınırlamaktadır. Bu projede, bu sorunların çözülmesi ve dil modellerinin performansının iyileştirilmesi hedeflenmektedir.

## Başlarken 

Bu proje ile çalışmaya başlamak için aşağıdaki adımları takip edebilirsiniz:

### 1. Python'un Kurulumu

1. [Python'un resmi web sitesine](https://www.python.org/downloads/) gidin.
2. En son sürümü indirin ve işletim sisteminize uygun olanı seçin (Windows, macOS, veya Linux).
3. İndirilen yükleyici dosyasını çalıştırın.
4. Kurulum sihirbazında, "Add Python to PATH" seçeneğini işaretlediğinizden emin olun.
5. "Install Now" seçeneğine tıklayarak kurulumu tamamlayın.

Python kurulumunu doğrulamak için terminal veya komut istemcisinde aşağıdaki komutu çalıştırabilirsiniz:

bash'de
python --version yazıp versiyonu kontrol edin.

#### Visual Studio Code'un Kurulumu
Visual Studio Code'un resmi web sitesine gidin.
İndirme sayfasında işletim sisteminize uygun olan yükleyiciyi seçin ve indirin.
İndirilen yükleyici dosyasını çalıştırın ve kurulum adımlarını takip edin.
Visual Studio Code kurulumunu doğrulamak için uygulamayı açıp, Code komutunu çalıştırabilirsiniz.

##### Gerekli Python Kütüphanelerinin Yüklenmesi
Proje gereksinimlerini yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:

pip install -r requirements.txt

Bu adımlar, kullanıcıların projenizle çalışmaya başlamaları için gerekli olan temel yazılımları kurmalarına yardımcı olacaktır.

###### Gereksinimler

-Python 3.11.5
-Vs Code

###### GumusAI ile Entegrasyon

Bu proje, [GumusAI projesi](https://github.com/GumusAI/GumusAi/tree/main) ile entegre edebilirsiniz.
Bunun icin asagidaki adimlari izleyin

-Öncelikle, GumusAI projesini kendi bilgisayarınıza klonlayın.
git clone https://github.com/GumusAI/GumusAi.git (Bu komut, GumusAI projesinin tam bir kopyasını yerel makinenize indirecektir.)

-Klonlama tamamlandıktan sonra, GumusAI projesinin bulunduğu dizine geçin: (cd GumusAi)

-GumusAI projesi için gerekli bağımlılıkları kurmak için requirements.txt dosyasını kullanın. Eğer bu dosya mevcutsa, şu komutu çalıştırarak gerekli bağımlılıkları kurabilirsiniz:
pip install -r requirements.txt (Eğer kendi projenizde bağımlılıkları zaten kuruluysa, bu adımı atlayabilirsiniz.)

-GumusAI'den ihtiyacınız olan modülleri veya kod parçacıklarını projenize dahil edin. Örneğin, belirli bir Python dosyasını kullanmak istiyorsanız, onu kendi projenize kopyalayabilir veya doğrudan GumusAI'deki dosyaları referans alabilirsiniz. GumusAI klasöründen bir modülü import etme
from GumusAi.some_module import SomeClass

-GumusAI ile entegrasyonu tamamladıktan sonra, projenizi test edin. Kodunuzun sorunsuz çalıştığından ve entegrasyonun başarılı olduğundan emin olun.
python your_project_script.py

-Son olarak, GumusAI ile entegrasyonunuzu kaydetmek için git komutlarını kullanarak değişiklikleri version control sistemine ekleyin.
git add .
git commit -m "GumusAI entegrasyonu tamamlandı"
git push origin main
### Model Yapısı
```
 Layer (type)                Output Shape              Param #   
=================================================================
 embedding (Embedding)       (None, 199, 256)          77879296  
                                                                 
 lstm (LSTM)                 (None, 64)                82176     
                                                                 
 dropout (Dropout)           (None, 64)                0         
                                                                 
 dense (Dense)               (None, 304216)            19774040  
                                                                 
=================================================================
Total params: 97735512 (372.83 MB)
Trainable params: 97735512 (372.83 MB)
Non-trainable params: 0 (0.00 Byte)
_______________________________________
```

### Model Skorları
```
Test Sonuçları:
Accuracy: 1.0000
Precision: 1.0000
Recall: 1.0000
F1 Score: 1.0000
```


###### Geliştirici

- **Emin Gürses** - *Ana Geliştirici* - [Github Profil](https://github.com/orgs/GumusAI/people/bendexe)
- **Huriye TOPRAK** - *Katkıda bulunanlar* - [Github Profil](https://github.com/orgs/GumusAI/people/Hrytprk)
Sorularıınızı buradan da iletebilirsiniz 


