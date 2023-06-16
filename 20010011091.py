# 20010011091/HASAN/CEYHAN

from datetime import datetime

urun_bilgileri = {}
urun_turleri = set()
sepet = []


def urun_bilgilerini_al():
      with open('20010011091_urun_listesi.txt') as file:
        for line in file:
            (urun_adi, urun_turu, fiyat, stok_miktari, birim) = line.split('/')

            urun_bilgileri[urun_adi] = {                
                'tur' : urun_turu,
                'fiyat' : fiyat,
                'miktar' : stok_miktari,
                'birim' : birim
            }          
            urun_turleri.add(urun_turu)

def tum_urun_listele():
    for urun in urun_bilgileri:
        print('Ürün: ' + urun) 
        print('\t Türü: ' + urun_bilgileri[urun]['tur'])
        print('\t Fiyat: ' + urun_bilgileri[urun]['fiyat'])
        print('\t Miktar: ' + urun_bilgileri[urun]['miktar'])
        print('\t Birim: ' + urun_bilgileri[urun]['birim'])

def ture_gore_listele():
    print('\n')
    for tur in urun_turleri:
        print('-> ' + tur)
        
    secim = input('\nListelemek istediğiniz türü yazınız : ')
    say = 0

    for urun in urun_bilgileri:
        if urun_bilgileri[urun]['tur'] == secim:
            print('Ürün: ' + urun)
            print('\t Türü: ' + urun_bilgileri[urun]['tur'])
            print('\t Fiyat: ' + urun_bilgileri[urun]['fiyat'])
            print('\t Miktar: ' + urun_bilgileri[urun]['miktar'])
            print('\t Birim: ' + urun_bilgileri[urun]['birim'])
            say += 1
    
    if say == 0:
        print('\nYazdığınız türde bir ürün bulunamadı. Lütfen listede olan bir tür seçiniz.\n')

def urun_adiyla_listele():
    urun_adi = input('\nÜrün adını yazınız : ')
    # ürün urun_bilgileri sözlüğünde var mı kontrolü yapılıyor.
    if urun_var_mi(urun_adi, urun_bilgileri):
        return
    else:
        print('\nAranan ürün bulunamadı.\n')

def urun_var_mi(urun_adi,liste):
    if type(liste) == dict:    
        for urun in liste:
            if urun == urun_adi:
                print('\nÜrün: ' + urun_adi) 
                print('\t Türü: ' + liste[urun_adi]['tur'])
                print('\t Fiyat: ' + liste[urun_adi]['fiyat'])
                print('\t Miktar: ' + liste[urun_adi]['miktar'])
                print('\t Birim: ' + liste[urun_adi]['birim']) 
                return True
        return False
    elif type(liste) == list: 
        for i in liste:
            if i[0] == urun_adi:
                print('\nÜrün: ' + i[0]) 
                print('\t Fiyat: ' + i[1])
                print('\t Miktar: ' + str(i[2])+ ' ' + i[3])
                print('\t Tutari: ' + str(i[4]) + ' TL')
                return True
        return False

def sepete_urun_ekle():
    
    while True:
        urun_adi = input('\nSepete eklenecek ürün adını yazınız : ')

        # ana menüye çıkış
        if urun_adi == '0':
            return

        # sepette aynı ürün var mı kontrolü
        for i in sepet:
            if i[0] == urun_adi:
                print('\nEklemek istediğiniz ürün sepetinizde mevcut. Menüden sepetteki ürünü güncellemeyi seçebilirsiniz.')
                return        

        # ürün urun_bilgileri ssözlüğünde var mı kontrolü
        if urun_var_mi(urun_adi, urun_bilgileri):
            break
        else:
            print('\nAranan ürün bulunamadı. Tekrar arama yapabilir veya ana menü için 0 yazabilirsiniz.\n')

    stok_miktari = float(urun_bilgileri[urun_adi]['miktar'])

    while True:
        miktar = float(input('\nSatın almak istediğiniz miktarı giriniz : '))

        if miktar <= stok_miktari:
            hesaplanan_tutar = miktar * float(urun_bilgileri[urun_adi]['fiyat'])
            sepet.append([urun_adi, urun_bilgileri[urun_adi]['fiyat'], miktar, urun_bilgileri[urun_adi]['birim'],hesaplanan_tutar ]) 
            urun_bilgileri[urun_adi]['miktar'] = str(stok_miktari - miktar)
            print('\n{} ürünü sepete eklendi.\n'.format(urun_adi))
            sepeti_goster()
            break
        else:
            print('\nStok miktarı : {} , en fazla stok miktarı kadar giriş yapılabilir.\n'.format(stok_miktari))

def sepetteki_urunu_guncelle():
    urun_adi = input('\nSepetteki güncellemek istediğiniz ürün adını yazınız : ')
    # ürün sepet listesinde var mı kontrolü
    if not urun_var_mi(urun_adi, sepet):
       print('\nAranan ürün sepette bulunamadı.\n')
       return
    while True:
        guncellenecek_miktar = int(input('\nGüncellemek istediğiniz miktar bilgisini giriniz : '))

        stok_miktari = float(urun_bilgileri[urun_adi]['miktar'])

        sepetteki_miktar = 0

        for i in sepet:
            if i[0] == urun_adi:
                sepetteki_miktar = float(i[2])
                fiyat = float(i[1])
                stok_miktari = stok_miktari + sepetteki_miktar
                if (guncellenecek_miktar <= stok_miktari):
                    i[2] = guncellenecek_miktar
                    hesaplanan_tutar = guncellenecek_miktar * fiyat
                    i[4] = hesaplanan_tutar
                    print('\nSepetteki {} ürünü miktarı {} olarak güncellenmiştir.\n'.format(i[0],guncellenecek_miktar))
                    urun_bilgileri[urun_adi]['miktar'] = str(stok_miktari-guncellenecek_miktar)
                    return
                break
        print("\nGüncellenmek istenen miktar, stok miktarinden ({}) büyük olamaz.\n".format(stok_miktari))
    
def sepetteki_urunu_sil():
    urun_adi = input('\nSepetteki silmek istediğiniz ürün adını yazınız : ')
    # ürün sepet listesinde var mı kontrolü
    if not urun_var_mi(urun_adi, sepet):
       print('\nAranan ürün sepette bulunamadı.\n')
       return

    for i in range(len(sepet)):
        if urun_adi in sepet[i]:
            sepetteki_miktar = float(sepet[i][2])
            stok_miktari = float(urun_bilgileri[urun_adi]['miktar'])
            urun_bilgileri[urun_adi]['miktar'] = str(stok_miktari + sepetteki_miktar)            
            del sepet[i]
            print("Ürün silindi.")
            break

def sepeti_goster():
    print('\nSepet bilginiz : \n')

    toplam_tutar = 0

    def topla(sayi):
        nonlocal toplam_tutar
        toplam_tutar += sayi

    for i in sepet:
        print(i[0], str(i[1]) + ' TL', str(i[2]) + ' ' + i[3].strip('\n'), 'Tutarı :' + str(i[4]) + ' TL', sep=', ')        
        topla(float(i[4]))

    if (toplam_tutar == 0):
        print('Sepetiniz boş.\n')
        return 0
    print("\n\tToplam sepet tutarı = {} TL".format(toplam_tutar))
    return toplam_tutar

def alisverisi_tamamla():
    toplam_tutar = sepeti_goster()

    if (toplam_tutar == 0):
        return

    tamamla = input('\n Sepetinizin toplam tutarı {} TL\'dir. Alışverişinizi tamamlamak istiyor musunuz? (E / H) : '.format(toplam_tutar))

    if (tamamla == 'E' or tamamla == 'e'):
        global sepet
        ad_soyad = input('\nAdınız ve soyadınızı giriniz :')
        adres = input('\nAdresinizi giriniz : ')
        urunler ='\n'
        for i in sepet:
            urunler = urunler + '\t ' + i[0] + ' ' + str(i[1]) + ' TL ' + str(i[2]) + ' ' + i[3].strip('\n') + ' ' + ' Tutarı :' + str(i[4]) + ' TL\n'        
            toplam_tutar += float(i[4]) 
        dosya = open('20010011091_siparisler.txt','a', encoding="utf-8")
        dosya.write('\nSipariş: ' + ad_soyad + '/' + adres + '/' + str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")) + '-->' + '\n' + urunler + '\n') # Tarih bilgisi gün/ay/yıl
               
        dosya.write('\tToplam sepet tutarı = {} TL\'dir\n'.format(toplam_tutar))
        dosya.close() 
        sepet = []  
        print('\nAlışverişiniz tamamlandı. Siparişleriniz 1 saat içersinde adresinize yollanacaktır.')
    elif (tamamla == 'H' or tamamla == 'h'):
        print('\nAlışverişe devam ediliyor...\n')
    else:
        print('\nHatalı seçim. Alışverişe devam ediliyor...\n')

def urun_bilgisikaydet():
    file = open("20010011091_urun_listesi.txt","w")
    for urun in urun_bilgileri: 
        guncel_urun = urun + "/" + str(urun_bilgileri[urun]["tur"]) + "/" + str(urun_bilgileri[urun]["fiyat"]) + "/" + str(urun_bilgileri[urun]["miktar"]) + "/" + str(urun_bilgileri[urun]["birim"])
        file.write(guncel_urun) 
    
def programdan_cik():
    global sepet
    if (len(sepet) != 0):
        cevap = input('\nSepetinizde ürünler bulunmaktadır. Çıkış yapmanız durumunda sepetinizdeki ürünler silinecektir. Yinede çıkmak istiyor musunuz? (E/ H) : ')
        if (cevap == 'E' or cevap == 'e'):
            
            for i in range(len(sepet)):
                urun_adi = sepet[i][0]
                sepetteki_miktar = float(sepet[i][2])
                stok_miktari = float(urun_bilgileri[urun_adi]['miktar'])
                urun_bilgileri[urun_adi]['miktar'] = str(stok_miktari + sepetteki_miktar)            
            sepet = []
            print('\nSepet boşaltıdı. İyi günler dileriz.\n')
            urun_bilgisikaydet()
            exit()  
        elif (cevap == 'H' or cevap == 'h'):
            print('\nAlışverişe devam ediliyor...\n')
        else:
            print('\nHatalı seçim. Alışverişe devam ediliyor...\n')
    else:
        print('\nİyi günler dileriz.\n')
        exit()
        
def main():
    urun_bilgilerini_al()
    while True:
        print('\n1. Ürünleri listele\n2. Sepete ürün ekle\n3. Sepetteki ürünü güncelle\n4. Sepetteki ürünü sil\n' \
            + '5. Sepetimi göster\n6. Alışverişi tamamla\n7. Çıkış')
        secim = input('\nYapmak istediğiniz işlemi seçiniz : ')

        if secim == '1':
            while True:
                print('\n1. Tüm ürünleri listele\n2. Türüne göre listele\n3. Ürün adıyla arama\n4. Ana menüye dön')
                secim_listele = input('\nYapmak istediğiniz işlemi seçiniz : ')

                if secim_listele == '1':
                    tum_urun_listele()
                elif secim_listele == '2':
                    ture_gore_listele()
                elif secim_listele == '3':
                    urun_adiyla_listele()   
                elif secim_listele == '4':
                    break
                else:
                    print ('\nHatalı giriş. Liste numarasını kullanarak bir seçim yapınız.\n')
        elif secim == '2':
            sepete_urun_ekle()
        elif secim == '3':
            sepetteki_urunu_guncelle()
        elif secim == '4':
            sepetteki_urunu_sil()
        elif secim == '5':
            sepeti_goster()
        elif secim == '6':
            alisverisi_tamamla()
        elif secim == '7':            
            programdan_cik()
        else:
            print ('\nHatalı giriş. Liste numarasını kullanarak bir seçim yapınız.\n')
main()
