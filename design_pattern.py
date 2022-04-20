# Classe Base 
class Imovel:
    def Rooms(self):
        print("We rolled out the new carpet in the living room.")

    def Wall(self):
        print("The builders have walled the area around the lot.")

#Classe Filhas 

class House:
    def lock(self):
        print(" always lock the door when I leave the house.")

    def key(self):
        print("How Many Doors Have One Key 🔑")

    def Sink(Self):
        print("The ring fell off her finger and sank into the kitchen sink.")

    def Douche(self):
        print("How many Douche have One Appartament 🚿")

class Appartement:
    def Window(self):
        print("The display of prices in the window is correct. 🪟")

    def TV(self):
        print("How many features a tv has 📺")

    def Socket(self):
        print("How many there are severeal eletrical sockets One Flat 🔌")

if __name__ == "__main__":
    print("---------- 🏠 HOUSE 🏠 ----------")
    my_house = House()
    my_house.lock()
    my_house.key()
    my_house.Sink()
    my_house.Douche()
    print("---------- 🏢 Appartement 🏢 ----------")
    my_Appartement = Appartement()
    my_Appartement.Window()
    my_Appartement.TV()
    my_Appartement.Socket()
