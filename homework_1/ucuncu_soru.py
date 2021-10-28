def harf_notu_hesaplama():
    vize1 = int(input("Vize1:"))
    while vize1 < 0 or vize1 > 100:
        print('1. Vize notunu 0-100 aralığında giriniz.')
        vize1 = int(input("Vize1:"))
    vize2 = int(input("Vize2:"))
    while vize2 < 0 or vize2 > 100:
        print('2. Vize notunu 0-100 aralığında giriniz.')
        vize2 = int(input("Vize2:"))
    final = int(input("Final:"))
    while final < 0 or final > 100:
        print('Final  notunu 0-100 aralığında giriniz.')
        final = int(input("Final: "))

    genel_not = vize1 * 3 / 10 + vize2 * 3 / 10 + final * 4 / 10

    if (genel_not >= 90):
        print("AA")
    elif (genel_not >= 85):
        print("BA")
    elif (genel_not >= 80):
        print("BB")
    elif (genel_not >= 75):
        print("CB")
    elif (genel_not >= 70):
        print("CC")
    elif (genel_not >= 65):
        print("DC")
    elif (genel_not >= 60):
        print("DD")
    elif (genel_not >= 55):
        print("FD")
    else:
        print("FF")


harf_notu_hesaplama()

"""Burda istenirse fonksiyon şeklinde tanımlama yapılıp çağırılabilir. Önemli olan sınav puanlarının doğru hesaplanması
    ve inputların 0-100 aralığında kontrol edilmesi.
"""

