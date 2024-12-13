from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_sisik, jenis_sirip):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_sisik = warna_sisik
        self.jenis_sirip = jenis_sirip
        
    def info_ikan(self):
        super().info_animal(),
        print("Warna Sisik \t\t :", self.warna_sisik,
              "\nJenis Sirip \t\t :", self.jenis_sirip)
        
ikan_buntal = Ikan("Buntal", "Alga dan invertebrata kecil", "Terumbu karang dan perairan hangat", "Bertelur", "Bercak Coklat dan Putih", "Punggung dan Ekor")
ikan_buntal.info_ikan()
print("-----------------------------------------------")
ikan_batu = Ikan("Batu", "Ikan kecil dan krustasea", "Dekat Terumbu Karang Laut tropis dan subtropis", "Bertelur", " Warna coklat kehijauan dengan pola yang menyerupai batu", "Punggung dan Dada")
ikan_batu.info_ikan()
print("================================================")
    