class Gempa:
    lokasi = ''
    skala = ''
    
    #contractor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    #method
    def dampak(self):
        if self.skala <2 :
            ket ='Gempa tidak berasa'
        elif self.skala >=2 and self.skala <4 :
            ket = 'Bangunan Retak-retak'
        elif self.skala >=4 and self.skala <6 :
            ket = 'Bangunan Roboh'
        else :
            ket = 'Bangunan roboh dan berpotensi Tsunami'
            
    #object
        print('Lokasi Gempa', self.lokasi, '\nSkala Gempa', self.skala, '\nDampak Gempa', ket)
        print('_______'*5)
        