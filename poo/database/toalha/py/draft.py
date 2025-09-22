class Towel:
    def __init__(self, color: str, size: str):

        self.color = color
        self.size = size
        self.wetness = 0  

    def dry (self, amount:int) -> None:
        self.wetness =+ amount
        if self.wetness >= self.getMAxetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def isDry (self) -> bool:
        return self.wetness == 0

    def WringOut(self) -> None:
        self.wetness == 0

    def __str__(self) -> str: 

        return f"cor:{self.color}, tam:{self.size}, hum:{self.wetness}"

doguito = Towel ("Encardida","G")
doguito.size = "M"
print(doguito) 
doguito,dry(3)
print(doguito)
doguito.dry(15)
doguito.dry(10)
print(doguito)
print(doguito.isDry())



