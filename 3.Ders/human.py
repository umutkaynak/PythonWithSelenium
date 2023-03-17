class Human:
    # name ="Halit"
    #constructor
    #intilaze
    def __init__(self,name):
        self.name=name
        print("bir human instance'i üretildi")
    def __str__(self):
        return f"STR fonk dönen değer: {self.name}"

    def talk(self,sentence):
        print(f"{self.name} : {sentence}")
        #self koyulmazsa şekilde hata alır.
    #TypeError: Human.walk() takes 0 positional arguments but 1 was given
    def walk(self):
        print("Human is walking..")
