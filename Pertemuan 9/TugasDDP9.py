#soal nomor 1
def celcius_ke_fahrenheit(celcius):
    hasil_konversi = (celcius*9/5) + 32
    return hasil_konversi

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

print("=====================")

#soal nomor 2
def is_genap(x):
    return x % 2 == 0
  
print(is_genap(4))
print(is_genap(7))  

print("=====================")

#soal nomor 3
def nilai_lulus(nilai):
    if nilai >= 80:
        return 'lulus'
    else :
        return 'gagal'
print(nilai_lulus(80))
print(nilai_lulus(60))

print("=====================")

#soal nomor 4
def bilangan_ganjil(batas):
    return list(range(1,batas,2))

print(bilangan_ganjil(20)) 

#Soal Tantangan
#outputnya syamil bisa pulang kalo gagal ga pulang
def ddp(ketentuan):
    if ketentuan == "bisa" :
        print("syamil pulang")
    elif ketentuan == "gagal" :
        print("syamil ga pulang")
    else :
        print("inputan tidak valid")
        
ddp("bisa")
        
           

  


