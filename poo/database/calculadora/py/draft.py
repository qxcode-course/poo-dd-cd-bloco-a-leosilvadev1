class Calculadora:
    def __init__(self,batteryMax: int):
        self.batteryMax: int = batteryMax
        self.battery: int = 0
        self.display: float = 0.0

    def __str__(self) -> str:
        return (f"display = {self.display:.2f}, battery = {self.battery}")

    def Charge(self, increment:int) -> None:
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def Sum(self, num1:float, num2:float) -> None:
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return
        else:
            self.display = num1 + num2
            self.battery -= 1

    def Div(self, num1:float, num2:float) -> None:
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return
        if num2 == 0:
            print("fail: divisao por zero")
            self.battery -= 1
            return
        else:
            self.display = num1 / num2
            self.battery -= 1

def main():
    animal = None
    while True:
        try:
            line =input().strip()
        except EOFError:
            break

        if not line:
            continue

        print(f"${line}")

        parts = line.split()
        cmd = parts[0]
    
        if cmd == "end":
            break

        if cmd == "init":
            batteryMax:int = int(parts[1])
            calculator = Calculadora(batteryMax)

        if cmd == "charge":
            increment:int = int(parts[1])
            calculator.Charge(increment)

        if cmd == "show":
            print(calculator)

        if cmd == "sum":
            num1:float = float(parts[1])
            num2:float = float(parts[2])
            calculator.Sum(num1, num2)

        if cmd == "div":
            num1:float= float(parts[1])
            num2:float=float(parts[2])
            calculator.Div(num1,num2)
main()
