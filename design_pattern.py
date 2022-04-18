# Classe Base 
class Imovel:
    def Rooms(self):
        print("Room division")

    def Wall(self):
        print("Each wall has one object")

#Classe Filhas 

class House:
    def locks(self):
        print("All the doors have Locks")

    def keys(self):
        print("All Locks have one Keys 🔑")

    def Sink(Self):
        print("All House have one kitchen Sink")

    def Douche(self):
        print("All House have one Douche 🚿")

class Appartement:
    def Windows(self):
        print("All Appartment have Windows 🪟")

    def TV(self):
        print("All Appartment have TV 📺")

    def Socket(self):
        print("All Appartement there are severeal eletrical sockets 🔌")

if __name__ == "__ main __":
    print("---------- 🏠 HOUSE 🏠 ----------")
    my_house = House()
    my_house.locks()
    my_house.keys()
    my_house.Sink()
    my_house.Douche()
    print("---------- 🏢 Appartement 🏢 ----------")
    my_Appartement = Appartement()
    my_Appartement.Windows()
    my_Appartement.TV()
    my_Appartement.Socket()