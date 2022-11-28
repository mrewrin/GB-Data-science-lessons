class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


worker_1 = Position("Arthas", "Menethil", "Lich-King", 1000000000, 50000000)
print(worker_1.get_full_name())
print(worker_1.position)
print(worker_1.get_total_income())
print("\n")

worker_2 = Position("Jaina", "Proudmoore", "Daughter of the Sea", 900000000, 45000000)
print(worker_2.get_full_name())
print(worker_2.position)
print(worker_2.get_total_income())
print("\n")

worker_3= Position("Sylvanas", "Windrunner", "Banshee Queen", 660000000, 66000000)
print(worker_3.get_full_name())
print(worker_3.position)
print(worker_3.get_total_income())
print("\n")

worker_4= Position("Thrall", "Son of Durotan", "Chieftain of the Frostwolf Clan", 450000000, 50000000)
print(worker_4.get_full_name())
print(worker_4.position)
print(worker_4.get_total_income())
print("\n")

worker_5= Position("Malfurion", "Stormrage", "Shan'do", 780000000, 25000000)
print(worker_5.get_full_name())
print(worker_5.position)
print(worker_5.get_total_income())
