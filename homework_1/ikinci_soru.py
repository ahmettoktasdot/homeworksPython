def sayiAtama(sayi):
    sayi_uzunlugu = str(sayi)
    if len(sayi_uzunlugu) == 2:
        okunacak_sayi = sayi
        return(sayiOkuma(okunacak_sayi))
    else:
        print('Sayi 2 basamaklı ve pozitif olmalı')
        return sayi


def sayiOkuma(okunusu_sayi):
    birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
    onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
    birinci = okunusu_sayi % 10
    ikinci = okunusu_sayi // 10
    return onlar[ikinci] + " " + birler[birinci]


sayi = int(input("Sayı:"))
print(sayiAtama(sayi))

"""Logic bu şekilde olacaktır, input alma fonksiyon çağırma vs. farklı olabilir. Yazımlara dikkat edelim."""