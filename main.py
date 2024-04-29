

class Hero():

    def __init__(self) -> None:
        self.name = ""
        self.exp = 0
        self.lvl = self.get_tag()

    def start(self):
        self.name= input("Qual o nome do seu Herói? ")
        self.exp = int(input("Quantos pontos de experiência o Herói tem? "))
        self.lvl = self.get_tag()

    def get_tag(self):
        if self.exp <= 1000:
            return "Ferro"
        elif 1001 <= self.exp <= 2000:
            return "Bronze"
        elif 2001 <= self.exp <= 5000:
            return "Prata"
        elif 5001 <= self.exp <= 7000:
            return "Ouro"
        elif 7001 <= self.exp <= 8000:
            return "Platina"
        elif 8001 <= self.exp <= 9000:
            return "Ascendente"
        elif 9001 <= self.exp <= 10000:
            return "Imortal"
        elif self.exp >= 10001:
            return "Radiante"
        else:
            return "Error"

    def execute(self):
        self.start()
        print(self)

    def __str__(self) -> str:
        return f"O Herói de nome {self.name} está no nível {self.lvl}"


if __name__ == "__main__":
    Hero().execute()
