def bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi):
    bolunen_sayi_listesi = []
    for i in range(min_sayi, max_sayi):
        if i % bolunecek_sayi == 0:
            bolunen_sayi_listesi.append(i)
    print(bolunen_sayi_listesi)
    toplam_sayi = len(bolunen_sayi_listesi)
    return toplam_sayi


print(bolunenSayiBulma(1, 100, 5))
"""Bu aşamada değerler dışardan alınabilir, inputlar kullanılabilir. Fonksiyon yazımına ve logic kontrol edilmeli"""