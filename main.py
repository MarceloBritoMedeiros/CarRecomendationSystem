import string

questions = [("Com quantas pessoas você costuma andar no carro?", 0, 1),
             ("Você (ou algum passageiro) precisaria de algum tipo de adaptação física no automóvel?", 0, 1),
             ("Carro manual ou automático?", 0, 1),
             ("Dentre as características abaixo, marque as 3 que você mais valoriza em um carro:", 0, 3),
             ("Para quais atividades você utiliza um carro?", 0, 1),
             ("Qual categoria de trabalho você se encaixaria?", 1, 1),
             ("Para quais lugares você viajou de carro recentemente?", 2, 1),
             ("Você costuma trocar de carro com frequência?", 0, 1)
             ]
answers = [{"Duas ou mais": [("Espaço", 2), ("Conforto", 2)], "Sozinho": [("Espaço", -2), ("Conforto", -2)]},
           {"Sim": [], "Não": []},
           {"Manual": [("Torque", 1)], "Automático": [("Conforto", 1)]},
           ["Espaço", "Conforto", "Economia", "Potência", "Torque"],
           {"Trabalho": 1, "Viagens": 2},
           {"Transporte de mercadorias": [("Espaço", 2), ("Trabalho", 1)],
            "Carregamento de materiais de obra ou semelhantes": [("Torque", 2), ("Trabalho", 1)],
            "Aplicativo ou taxi": [("Conforto", 2), ("Espaço", 2)], "Representante comercial": [("Economia", 2)]},
           {"Longe": [("Potência", 2)], "Perto": [("Economia", 2)]}
           ]

data = {"Economia": 0, "Conforto": 0, "Espaço": 0, "Potência": 0, "Torque": 0, "Trabalho":0}
direction = 0
categories = {"Pickup": ["Potência", "Espaço", "Torque"], "SUV Confort": ["Espaço", "Conforto", "Torque"],
              "SUV Sport": ["Espaço", "Conforto", "Potência"], "Sedan": ["Espaço", "Conforto", "Economia"]}


class Program:
    direction = 0
    def __init__(self, data):
        self.data = data
    def loop_questions(self):
        for i, (q, a) in enumerate(zip(questions, answers)):
            print(self.data)
            if self.verify_direction(q):
                self.display_questions(i, q)
                self.verify_types_of_question(a, q)
        print(self.calculate_result())

    def verify_direction(self, q):
        return self.direction == q[1]

    def display_questions(self, i, q):
        print(f"{i + 1}) {q[0]}")

    def display_answers(self, a):
        for c, j in zip(list(string.ascii_lowercase), a):
            print(f"    {c} - {j}")
        y = input()
        return y

    def verify_types_of_question(self, a, q):
        if q[2] == 1:
            y = self.display_answers(a)
            if type(a[y]) == int:
                self.direction = a[y]
            else:
                for i in a[y]:
                    self.data[i[0]] = self.data[i[0]] + i[1]
                    self.direction = 0
        else:
            for i in range(q[2], 0, -1):
                for c, j in zip(list(string.ascii_lowercase), a):
                    print(f"    {c} - {j}")
                y = input()
                self.data[y] = self.data[y] + i

    def calculate_result(self):
        data_sorted = sorted(self.data.items(), key=lambda x: x[1], reverse=True)
        data_sorted = [x[0] for x in data_sorted]
        result = ""
        for i in categories.items():
            if sorted(data_sorted[:3]) == sorted(i[1][:3]):
                result = i[0]
        return result

if __name__ == '__main__':
    p = Program(data)
    p.loop_questions()