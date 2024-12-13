class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def makan(self):
        print(f"{self.nama} sedang makan {self.makanan}")
        
    def hidup(self):
        print(f"{self.nama} sedang hidup")
        
    def berkembang_biak(self):
        print(f"{self.nama} sedang berkembang biak")
        
    def info_animal(self):
        print("Nama \t\t\t :", self.nama,
              "\nMakanan \t\t : ", self.makanan,
              "\nHidup \t\t\t : ", self.hidup,
              "\nBerkembang Biak \t : ", self.berkembang_biak)
        
binatang = Animal("Kucing", "Ikan", "Darat", "Beranak")
binatang.info_animal()
print("==================================================")