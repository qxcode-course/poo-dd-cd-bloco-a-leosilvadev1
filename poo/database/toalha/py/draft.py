class Towel:
    def __init__(self, color: str, size: str):

        self.color = color
        self.size = size
        self.wetness = 0        
    def __str__(self): 

        return f"cor:{self.color}, tam:{self.size}, hum:{self.wetness}"

towel = Towel("green","g")
towel1 = Towel("black","p")



