def hesapmakinesi():
    print("╔═════════════════════════════╗")
    print("║     HESAP MAKİNESİ          ║")
    print("║                             ║")
    print("║         1-Toplama           ║")
    print("║         2-Çıkarma           ║")
    print("║         3-Çarpma            ║")
    print("║         4-Bölme             ║")
    print("║         5-Üs Alma           ║")
    print("║         6-Kare Alanı        ║")
    print("║         7-Karenin çeversi   ║")
    print("║                             ║")
    print("║           Seçimini yap      ║")
    print("╚═════════════════════════════╝")
    secim = input()
    print("Seçiminiz:", secim)
    if secim == '1':
        print("Toplamayı seçtiniz")
        sayi1 = int(input("1.sayı:"))
        sayi2 = int(input("2.sayı:"))
        print("Toplam:", sayi1 + sayi2)
    if secim == '2':
        print("Çıkarmayı seçtiniz")
        sayi1 = int(input("1.sayı:"))
        sayi2 = int(input("2.sayı:"))
        print("Fark:", sayi1 - sayi2)
    if secim == '3':
        print("Çarpma seçtiniz")
        sayi1 = int(input("1.sayı:"))
        sayi2 = int(input("2.sayı:"))
        print("Çarpım:", sayi1 * sayi2)
    if secim == '4':
        print("Bölme seçtiniz")
        sayi1 = int(input("1.sayı:"))
        sayi2 = int(input("2.sayı:"))
        print("Bölüm:", sayi1 / sayi2)
    if secim == '5':
        print("Üs alma seçtiniz")
        sayi1 = int(input("1.sayı:"))
        sayi2 = int(input("2.sayı:"))
        print("Sonuc:", sayi1**sayi2)
    if secim == '6':
        print("Kare alanı seçtiniz")
        sayi = int(input("Sayı:"))
        print("Sonuc:", sayi**2)
    if secim == '7':
        print("Karenin çevresini seçtiniz")
        sayi = int(input("sayı:"))
        print("sonuc:", sayi * 4)