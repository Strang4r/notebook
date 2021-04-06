class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"full name: {self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


position = Position(name="Boris ",
                    surname="TheBrawler",
                    position="Sofa Navy Admiral",
                    income={"wage": 100000, "bonus": 15040})

print(position.get_full_name())
print(position.get_total_income())
