'''
buatlah program meghitung luas bangun datar meggunakan fungsi.
-segitiga
-persegi panjang
'''


def luas_s(alas, tinggi):
    luas = 1/2 * alas * tinggi
    print("luas segitiga adalah", luas)

luas_s(6, 7)

def luas_pp(panjang, lebar):
    luas = panjang * lebar
    print("luas persegi panjang", luas)

luas_pp(8, 9)