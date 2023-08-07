#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random

# Hedef fonksiyonumuz (minimumunu bulmaya çalışacağımız fonksiyon)
def hedef_fonksiyon(x):
    return x ** 2 - 4 * x + 4

# Yapay arı sınıfı
class YapayAri: #Her arının pozisyon ve değer özelliği var.
    def __init__(self, pozisyon): #constructor method...
#Yeni bir YapayAri nesnesi oluşturulduğunda bu metot otomatik olarak çalışır.
#pozisyon adlı bir girdi alır ve bu pozisyonu arının pozisyonu olarak atar.

        self.pozisyon = pozisyon #sınıfın pozisyon özelliğini, metoda geçirilen pozisyon değeriyle eşitler.
        self.deger = hedef_fonksiyon(self.pozisyon) #sınıfın deger özelliğini, arının bulunduğu pozisyondaki hedef fonksiyon değeriyle eşitler. Bu, yapay arının başlangıçta bulunduğu pozisyondaki hedef fonksiyon değerini hesaplar.#sınıfın deger özelliğini, arının bulunduğu pozisyondaki hedef fonksiyon değeriyle eşitler. Bu, yapay arının başlangıçta bulunduğu pozisyondaki hedef fonksiyon değerini hesaplar.

# Yapay arı koloni algoritması
def yapay_ari_koloni_algoritmasi(max_iterasyon, koloni_boyutu, azaltma_katsayisi, alfa, beta):
    # Başlangıçta arı kolonisi oluşturulur ve her arıya rastgele bir başlangıç pozisyonu atanır
    arilar = [YapayAri(random.uniform(-10, 10)) for _ in range(koloni_boyutu)]
 #Bu kod bloğu, her bir arının bulunduğu pozisyondaki hedef fonksiyon değerini hesaplamak için kullanılıyor. 
#Hedef fonksiyon değeri, arının bulunduğu konumdaki çözümün ne kadar iyi olduğunu temsil eder.
#Bu değer, optimizasyon problemine göre belirlenen bir kriterdir ve genellikle minimuma ulaşılması istenen bir değeri temsil eder.
    for iterasyon in range(max_iterasyon):#. Bu döngü, iterasyon adlı bir değişkeni range(max_iterasyon) ifadesi tarafından belirtilen değerler üzerinde sırayla dolaşarak çalışır.
        for arı in arilar:
            # Yeni pozisyon hesaplanır
            yeni_pozisyon = arı.pozisyon + random.uniform(-1, 1) * azaltma_katsayisi
#Burada, bir arının yeni pozisyonunu hesaplamak için mevcut pozisyonuna bir rastgele değer ekleyerek yeni bir konum oluşturuyoruz.
#random.uniform(-1, 1) ifadesi, -1 ile 1 arasında rastgele bir sayı üretir. Bu işlem, arının hareket ettiği yönü belirlemek için kullanılır. azaltma_katsayisi ise arının hareket ettiği mesafeyi kontrol eder. Bu katsayı, her iterasyonda hareket mesafesinin azaltılmasını sağlayarak algoritmanın daha iyi sonuçlara ulaşmasına yardımcı olur.
    
            yeni_pozisyon = max(min(yeni_pozisyon, 10), -10)  # #Bu kod, yeni pozisyonu -10 ile 10 arasında sınırlandırır.
    #Eğer yeni_pozisyon, -10'dan küçükse, -10 olarak ayarlanır. Eğer yeni_pozisyon, 10'dan büyükse, 10 olarak ayarlanır. Bu işlem, arıların hareketlerinin belirlenmiş sınırlar içinde kalmasını sağlar.


            # Yeni pozisyondaki hedef fonksiyon değeri hesaplanır
            yeni_deger = hedef_fonksiyon(yeni_pozisyon)

            # Alfa ve beta faktörleri kullanılarak yeni değer daha iyiyse pozisyon güncellenir
            if yeni_deger < arı.deger:
                arı.pozisyon = yeni_pozisyon
                arı.deger = yeni_deger

        # Kolonideki en iyi pozisyon ve değeri bulunur
        en_iyi_ari = min(arilar, key=lambda ari: ari.deger) #Bu satır, arıların bulunduğu kolonideki en iyi çözümü temsil eden arıyı belirlemek için kullanılır. 
#min() fonksiyonu, belirli bir sıralama kriterine göre koleksiyon içindeki minimum değeri bulmamıza izin verir. key parametresi ise minimum değeri belirlemek için kullanılan sıralama kriterini belirler.

#lambda ari: ari.deger ifadesi, her bir arı nesnesini alır ve ari.deger özelliğini kullanarak arıların hedef fonksiyon değerine göre sıralanmasını sağlar. Yani, min() fonksiyonu, arıları hedef fonksiyon değerine göre küçükten büyüğe doğru sıralayarak en küçük hedef fonksiyon değerine sahip arıyı bulur.


        # Koloninin pozisyonlarını azaltarak yeni iterasyona geçilir
        azaltma_katsayisi *= alfa
        #Bu satırda yapılan işlem, azaltma_katsayisi adlı bir değişkenin değerini güncellemektir. 
#Yapay Arı Koloni Algoritması'nda, hareket mesafesi olan azaltma_katsayisi her iterasyonda azaltılarak arıların daha hassas bir arama yapması sağlanır

        print(f"{iterasyon}. iterasyon: En iyi değer = {en_iyi_ari.deger}, En iyi pozisyon = {en_iyi_ari.pozisyon}")
    #Bu satır, her iterasyonda kolonideki en iyi arının değerini (en_iyi_ari.deger) ve pozisyonunu (en_iyi_ari.pozisyon) ekrana yazdırır. Bu sayede, algoritmanın her adımında en iyi çözüme yaklaştığını ve en iyi pozisyonun değerini takip edebilirsiniz.

    return en_iyi_ari.pozisyon, en_iyi_ari.deger #Algoritma tamamlandığında, en iyi çözümün pozisyonunu (en_iyi_ari.pozisyon) ve değerini (en_iyi_ari.deger) döndürür. Bu değerler, algoritmanın en iyi sonucunu temsil eder.

if __name__ == "__main__":
    max_iterasyon = 10
    koloni_boyutu = 10  #kolonideki arı sayısı
    azaltma_katsayisi = 0.95 #arıların hareket mesafesini azaltma oranı
    alfa = 1.0
    beta = 1.0

    en_iyi_pozisyon, en_iyi_deger = yapay_ari_koloni_algoritmasi(max_iterasyon, koloni_boyutu, azaltma_katsayisi, alfa, beta)

    print(f"En iyi pozisyon = {en_iyi_pozisyon}, En iyi değer = {en_iyi_deger}")


# In[ ]:




