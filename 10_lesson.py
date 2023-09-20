class Cars:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

class SuperCar(Cars):
    def __init__(self, model, color, year, sponsor):
        super().__init__(model, color, year)
        self.sponsor = sponsor



