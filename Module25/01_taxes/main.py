class Property:
    def __init__(self, worth, coeff=0):
        self.worth = worth
        self.coeff = coeff

    def tax(self):
        return self.worth * self.coeff


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth, 1 / 1000)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth, 1 / 200)


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth, 1 / 500)


cash = int(input('Сколько денег? '))
apartment = Apartment(int(input('Сколько стоит квартира? ')))
car = Car(int(input('Сколько стоит машина? ')))
c_house = CountryHouse(int(input('Сколько стоит дача? ')))

total_tax = apartment.tax() + car.tax() + c_house.tax()
if total_tax > cash:
    print('Не хватает', total_tax - cash)
else:
    print('Денег хватает')
