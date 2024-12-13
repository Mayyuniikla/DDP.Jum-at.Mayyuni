from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, pertahanan, warna_sisik):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.pertahanan = pertahanan
        self.warna_sisik = warna_sisik
        
    def info_ular(self):
        super().info_animal(),
        print("Pertahanan \t\t :", self.pertahanan,
              "\nWarna Sisik \t\t :", self.warna_sisik,)
        
ular_cobra = Ular( "Cobra", "Daging", "Darat" , "Bertelur", "Menggigit, Melebarkan Tudung, dan Mendesis", "Hitam")
ular_cobra.info_ular()
print("-------------------------------------------------")
ular_anaconda_hijau = Ular("Anaconda Hijau", "Daging", "Sungai Amazon", "Ovovivipar", "Gigitan dan Lilitan", "Hijau dengan Bercak Hitam")
ular_anaconda_hijau.info_ular()
print("==================================================")