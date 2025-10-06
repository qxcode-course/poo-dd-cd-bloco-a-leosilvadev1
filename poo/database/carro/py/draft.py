class Car:
    def __init__(self):
        self.pas:int = 0
        self.gas:int = 0
        self.km:int = 0
        
    def __str__(self) -> str:
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"

    def Enter(self):
        if self.pas < 2:
            self.pas += 1
        else:
            print("fail: limite de pessoas atingido")

    def Leave(self):
        if self.pas > 0:
            self.pas -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def Gas(self, increment:int) -> None:
        maxGas = 100
        self.gas += increment
        if self.gas > maxGas:
            self.gas = maxGas

    def Drive(self, increment:int)->None:
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if self.gas >= increment:
            self.km += increment
            self.gas -= increment
        else:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0

def main():
    car:Car=Car()
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

        if cmd == "show":
            print(car)

        elif cmd == "end":
            break

        elif cmd == "enter":
            car.Enter()

        elif cmd == "leave":
            car.Leave()

        elif cmd == "fuel":
            increment:int=int(parts[1])
            car.Gas(increment)

        elif cmd == "drive":
            increment:int=int(parts[1])
            car.Drive(increment)
main()