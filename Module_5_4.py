class Building:

    def __init__(self, total):
        self.total = total

    def __str__(self):
        return f'Экземпляр класса Building № {self.total}'


for i in range(1,41):
    building = Building(total=i)
    print(building)


