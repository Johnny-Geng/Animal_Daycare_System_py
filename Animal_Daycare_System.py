# Johnny Geng, johnnyge@usc.edu
# This program is a simulation of an animal daycare system.


class Animal(object):
    def __init__(self, hunger, happiness, health, energy, age, name, species):
        self.hunger = hunger
        self.happiness = happiness
        self.health = health
        self.energy = energy
        self.age = age
        self.name = name
        self.species = species

    def play(self):
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
        self.hunger += 5
        if self.hunger > 100:
            self.hunger = 100

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0

    def giveMedicine(self):
        self.happiness -= 20
        if self.happiness < 0:
            self.happiness = 0
        self.health += 20
        if self.health > 100:
            self.health = 100

    def sleep(self):
        self.energy += 20
        if self.energy > 100:
            self.energy = 100
        self.age += 1

    def __str__(self):
        animalInfo = "Name: " + self.name + " the " + self.species + "\n" + \
              "Health: " + str(self.health) + "\n" + \
              "Happiness: " + str(self.happiness) + "\n" + \
              "Hunger: " + str(self.hunger) + "\n" + \
              "Energy: " + str(self.energy) + "\n" + \
              "Age: " + str(self.age)
        return animalInfo


def loadAnimals(nameFile):
    objectList = []
    fileIn = open(nameFile, "r")
    for line in fileIn:
        line = line.strip()
        dataList = line.split(",")
        animal = Animal(int(dataList[0]), int(dataList[1]), int(dataList[2]), int(dataList[3]),
                        int(dataList[4]), dataList[5], dataList[6])
        objectList.append(animal)
    fileIn.close()
    return objectList


def displayMenu():
    print("1) Play\n"
          "2) Feed\n"
          "3) Give Medicine\n"
          "4) Sleep\n"
          "5) Print an Animal's stats\n"
          "6) View All Animals\n"
          "7) Exit\n")


def selectAnimal(listOfAnimals):
    for order in range(0, len(listOfAnimals)):
        print(str(order + 1) + ")" + listOfAnimals[order].name + " the " + listOfAnimals[order].species)
    invalid = True
    while invalid:
        selection = input("\nPlease select an animal from the list (enter the 1-5): ")
        if selection.isdigit():
            if int(selection) in range(1, 6):
                invalid = False
            else:
                print("Invalid input, please try again!")
        else:
            print("Invalid input, please try again!")
    animalObject = listOfAnimals[(int(selection) - 1)]
    return animalObject


def main():
    print("Welcome to the Animal Daycare! Here is what we can do:\n")
    animalObjectList = loadAnimals("animals.csv")
    status = True
    while status:
        displayMenu()
        choice = input("Please make a selection: ")
        while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("*Invalid selection, please try again.\n")
            displayMenu()
            choice = input("Please make a selection: ")
        if choice == "6":
            for i in animalObjectList:
                print(i)
                print("********************************")
        elif choice == "7":
            status = False
        else:
            animalChoice = selectAnimal(animalObjectList)
            if choice == "1":
                animalChoice.play()
                print("You played with " + animalChoice.name + " the " + animalChoice.species + "!\n")
            elif choice == "2":
                animalChoice.feed()
                print("You fed " + animalChoice.name + " the " + animalChoice.species + "!\n")
            elif choice == "3":
                animalChoice.giveMedicine()
                print("You gave " + animalChoice.name + " the " + animalChoice.species + " some medicine!\n")
            elif choice == "4":
                animalChoice.sleep()
                print(animalChoice.name + " the " + animalChoice.species + " took a nap!\n")
            elif choice == "5":
                print(animalChoice)
                print("********************************")
    print("Goodbye!")


main()