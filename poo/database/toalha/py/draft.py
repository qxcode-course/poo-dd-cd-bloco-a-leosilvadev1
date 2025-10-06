class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0  

    def dry (self, amount:int) -> None:
        self.wetness += amount
        if self.wetness >= self.getMAxetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def isDry (self) -> bool:
        return self.wetness == 0

    def WringOut(self) -> None:
        self.wetness == 0    

    def getMaxWetness(self):
        if self.size == "P":
            return 10

        elif self.size == "M":
            return 20

        elif self.size == "G":
            return 30
        return 0

    def __str__(self) -> str: 
        return f"cor:{self.color}, tam:{self.size}, hum:{self.wetness}"

def main():
    toalha = Towel ("", "")
    while True:
        line:str = input()
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "new":
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0] == "show":
            print(toalha)
        elif args [0] == "dry":
            amount: int = int(args[1])
            toalha.dry(amount)
        else:
                print("Fail:comando inválido")
main()