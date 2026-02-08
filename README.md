## Bu proje, Twitter (X) üzerindeki belirli bir tartışma başlığı altındaki yanıtları çekerek, otomobil marka ve modellerine dair kullanıcı deneyimlerini ve tercihlerini analiz eder. Projenin temel amacı, ham sosyal medya verisinden anlamlı araç tavsiyeleri ve popülerlik sıralamaları üretmektir.
# Özellikler
* Dinamik Veri Kazıma: Playwright kullanarak Twitter'ın dinamik yapısından (infinite scroll) binlerce yanıtı otomatik olarak toplar.

* Gelişmiş Veri Ön İşleme: Metinleri NLP teknikleriyle (Tokenization, Stopwords temizliği) analiz edilebilir hale getirir.
* Duygu ve İçerik Analizi: Yanıtlar içinden sadece otomobil modellerine odaklanır, olumlu geri bildirimleri filtreler ve modelleri popülerliğine göre sıralar.

# Kullanılan Teknolojiler ve Kütüphaneler
* Veri Kazıma: Playwright

* Veri Analizi & Manipülasyon: Pandas, NumPy

* Doğal Dil İşleme (NLP): NLTK (Tokenization, Stopwords)

* Görselleştirme: Matplotlib, Seaborn

# Proje Adımları
1. Veri Toplama (scrape.py)
Belirlenen hedef tweet altındaki yanıtlar, kullanıcı adı ve metin içeriği ile birlikte playwright kullanılarak çekilir ve tweet_replies.csv olarak kaydedilir.

2. Veri Temizleme (data-cleaning.ipynb)
Gereksiz sütunların (tarih vb.) kaldırılması.

Tweet sahibinin kendi yanıtlarının veri setinden elenmesi.

Metinlerin tamamen küçük harfe çevrilmesi, noktalama işaretlerinin ve Türkçe etkisiz kelimelerin (stopwords) temizlenmesi.

3. Analiz ve Sıralama (analysing.ipynb)
Temizlenmiş metinler içinden belirli araç markalarının (Egea, Clio, Corolla vb.) tespiti.

Yanıtların "pozitif" veya "negatif" olarak sınıflandırılması.

Olumlu yorum alan araç modellerinin frekans analizi yapılarak en çok önerilen modellerin listelenmesi.

# Örnek Çıktı
Çalışma sonucunda, kullanıcıların bütçe ve performans odaklı en çok önerdiği modeller (örneğin: Fiat Egea, Renault Clio) görselleştirilerek sunulmaktadır.

Not: Bu proje kişisel bir içgörü çalışması olup, veri setinin kalitesine göre sonuçlar değişkenlik gösterebilir.
