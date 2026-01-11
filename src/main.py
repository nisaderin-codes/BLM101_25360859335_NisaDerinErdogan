# Cok Fonksiyonlu Taban Donusturucu
# Binary, Hexadecimal ve Two's Complement desteklidir.


# Girilen onluk tabandaki (decimal) sayiyi ikilik tabana (binary) donusturur.
def onluk_binary_cevir(sayi):
    if sayi == 0:
        return "0"

    bitler = []

    # Kalan hesaplanir ve listeye eklenir.
    while sayi > 0:
        kalan = sayi % 2
        bitler.append(str(kalan))
        sayi = sayi // 2

    # Bitler onem sirasina gore siralanir. msb-->lsb
    bitler.reverse()
    return "".join(bitler)


# Girilen onluk tabandaki (decimal) sayiyi onaltD1lD1k tabana (hexadecimal) donusturur.
def onluk_hex_cevir(sayi):
    if sayi == 0:
        return "0"

    hex_harfler = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]

    basamaklar = []
    while sayi > 0:
        kalan = sayi % 16
        basamaklar.append(hex_harfler[kalan])
        sayi = sayi // 16

    basamaklar.reverse()
    return "".join(basamaklar)


# Binary sayiyi 8 bitlik duzenli gosterim olmasi icin basina 0 ekleyerek duzenler.
def binary_8bit_yap(binary_sayi):
    eksik_bit = 8 - (len(binary_sayi) % 8)
    if eksik_bit != 8:
        binary_sayi = "0" * eksik_bit + binary_sayi
    return binary_sayi


# Bellekteki gorunumu gosterme fonksiyonu.
def sekiz_bit_kutucuk_goster(binary_sayi):
    binary_sayi = binary_8bit_yap(binary_sayi)
    kutular = []
    for bit in binary_sayi:
        kutular.append("[" + bit + "]")
    return "".join(kutular)


# Negatif sayiyi Two's Complement ile binary'ye cevirir.
def negatif_binary_cevir(sayi):
    pozitif = abs(sayi)
    binary = onluk_binary_cevir(pozitif)
    binary = binary_8bit_yap(binary)

    ters = ""
    for bit in binary:
        if bit == "0":
            ters += "1"
        else:
            ters += "0"

    sonuc = ""
    elde = 1
    for bit in reversed(ters):
        if bit == "1" and elde == 1:
            sonuc = "0" + sonuc
            elde = 1
        elif bit == "0" and elde == 1:
            sonuc = "1" + sonuc
            elde = 0
        else:
            sonuc = bit + sonuc

    return sonuc


def menu_goster():
    print("\n--- Cok Fonksiyonlu Taban Donusturucu ---")
    print("1 - Binary cevir")
    print("2 - Hexadecimal cevir")
    print("3 - Cikis")


def ana_program():
    while True:
        # Kullanicidan menu secimi alinir.
        menu_goster()
        secim = input("Seciminizi giriniz: ")

        # Secime gore donusum yapilir.
        if secim == "3":
            print("Program kapatiliyor...")
            break

        if secim != "1" and secim != "2":
            print("Hatali secim yaptiniz.")
            continue

        # Hatali giris yapilirsa uyari verilir ve menu tekrar dondurulur.
        try:
            sayi = int(input("Onluk sayi giriniz: "))
        except:
            print("Gecersiz giris yaptiniz.")
            continue

        if secim == "1":
            if sayi >= 0:
                binary_sayi = onluk_binary_cevir(sayi)
                binary_sayi = binary_8bit_yap(binary_sayi)
            else:
                binary_sayi = negatif_binary_cevir(sayi)

            print("Binary Sonuc:", binary_sayi)
            print("Bellek Gorunumu:", sekiz_bit_kutucuk_goster(binary_sayi))

        elif secim == "2":
            if sayi < 0:
                print("Hexadecimal negatif sayilar icin desteklenmiyor.")
                continue

            hex_sayi = onluk_hex_cevir(sayi)
            binary_sayi = onluk_binary_cevir(sayi)
            binary_sayi = binary_8bit_yap(binary_sayi)

            print("Hexadecimal Sonuc:", hex_sayi)
            print("Binary Karsiligi:", binary_sayi)
            print("Bellek Gorunumu:", sekiz_bit_kutucuk_goster(binary_sayi))


ana_program()
