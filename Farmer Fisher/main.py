from Livestock import *
def main():
    farm = FarmApp()
    animal1 = Alpaca(5,600) # age and weight
    animal2 = Camel(5,3) #age and humps #
    animal3 = Donkey(6, "Miniature") # age and breed
    
    farm.addLivestock(animal1)
    farm.addLivestock(animal2)
    farm.addLivestock(animal3)
    animals = farm.getLivestock()
    
    print("List of Animals Sold")
    print("=====================\n")
    for animal in animals:
        print(animal.getType(), '\t$', animal.getPrice())
    print("\nTotal sales \t$", farm.getTotalPrice())
    
    animal4 = Donkey(2,"American Mammoth Jack")
    animal5 = Donkey(7, "Burro")
    animal6 = Alpaca(2,250)
    
    farm.addLivestock(animal4)
    farm.addLivestock(animal5)
    farm.addLivestock(animal6)
    
    for animal in animals:
        print(animal.getType(), '\t$', animal.getPrice())
    print("\nTotal sales \t$", farm.getTotalPrice())
main()