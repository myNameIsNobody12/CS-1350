class Livestock:
    def __init__(self, age):
        self.age = age
    #return age
    def getAge(self):
        return self.age
    #return type (alpaca, camel, or donkey)
    def getType(self):
        return self.type
    #price
    def getPrice(self):
        return 0
class Alpaca(Livestock):
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight
        self.type = 'Alpaca'
        if age <= 3:
            self.price = 10000
        else:
            if self.weight <= 300:
                self.price = 80000
            else:
                self.price = 100000
    def getPrice(self):
        return self.price
class Camel(Livestock):
    def __init__(self, age, hump):
        self.age = age
        self.hump = hump
        self.type = 'Camel'
        if age <= 3:
            self.price = 50000
        else:
            if self.hump == 2:
                self.price = 150000
            else:
                self.price = 200000
    def getPrice(self):
        return self.price
class Donkey(Livestock):
    def __init__(self, age, breed):
        self.age = age
        self.breed = breed
        self.type = 'Donkey'
        if age <= 3:
            self.price = 20000
        else:
            if self.breed == "Miniature":
                self.price = 100000
            elif self.breed == "Burro":
                self.price = 120000
            elif self.breed == "American Mammoth Jack":
                self.price = 180000
    def getPrice(self):
        return self.price
class FarmApp():
    def __init__(self):
        self.livestockList = []
    #return a list of sold animals
    def getLivestock(self):
        return self.livestockList
    def addLivestock(self,obj):
        self.livestockList.append(obj)
    def getTotalPrice(self):
        total = 0
        for i in self.livestockList:
            total = total + i.price
        return total