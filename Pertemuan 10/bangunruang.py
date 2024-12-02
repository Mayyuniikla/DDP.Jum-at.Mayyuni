import math 

def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'Luas balok adalah {hitung}')
    
def l_kubus(sisi):
    hitung = 6 * math.pow(sisi, 2)
    print(f'Luas kubus adalah {hitung}')
    
def l_tabung(jari_jari, tinggi):
    hitung = 2 * 3.14 * jari_jari * (jari_jari + tinggi)
    print(f'Luas permukaan tabung adalah {hitung}')
    
def l_prisma_segitiga(alas, t_alas, t1, t2, t3):
    luas_alas = alas * t_alas / 2
    jml_luas_tegak = alas * t1 / 2 + alas * t2 / 2 + alas * t3 / 2
    luas = luas_alas + jml_luas_tegak
    print(f'Luas permukaan prisma segitiga adalah {luas}')
    

def l_limas_segitiga(alas, tinggi_segitiga, tinggi_limas, sisi1, sisi2, sisi3):
    luas_alas = 0.5 * alas * tinggi_segitiga
    keliling_alas = sisi1 + sisi2 + sisi3
    luas_sisi_tegak = 0.5 * keliling_alas * tinggi_limas
    luas_permukaan = luas_alas + luas_sisi_tegak
    print(f'Luas permukaan limas segitiga adalah {luas_permukaan}')