class person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def berjalan(self):
        print(f"{self.name}sedang berjalan")
        
    def ngomong(self):
        if self.gender == "pria":
            print(f"{self.name} tidak bercerita karena dia {self.gender}")
        else: 
            print(f"{self.name} Senang bercerita karena dia {self.gender}")
            
class supir(person):
    def __init__(self, name, age, gender, sim):
        super().__init__(name, age, gender)
        self.sim = sim
        
    def berkendara(self):
        print(f"{self.name} Sedang berkendara dengan SIM {self.sim}")
        
budi = person('budi',20,'pria')
budi.ngomong()

agus = supir('agus',20,'wanita','A')
agus.ngomong()


        
