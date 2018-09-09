



class Budget(object):
    def __init__(self):
        self.price = 13000
        self.years = 5
        self.interet = 7


    def pvtx(self):
        return self.price * 0.0975

    def fdtx(self):
        return self.price * 0.05

    def comtx(self):
        return self.fdtx() + self.pvtx()

    def totalpv(self):
        return self.price + self.pvtx()

    def totalcom(self):
        return self.price + self.comtx()

    def payment(self):
        month = float(self.years) * 12
        interestRate = float(self.interet) / 100 / 12

        # Formula to calculate monthly payments
        return self.totalcom() * (interestRate * (1 + interestRate) ** month) / ((1 + interestRate) ** month - 1)


    def set_price(self):
        while True:
            try:
                self.price = int(input('What is the price of the item?'))
                break
            except:
                print("That's not a valid number")

    def set_interest(self):
        while True:
            try:
                self.interet = int(input('What is the interest for the loan?'))
                break
            except:
                print("That's not a valid number")

    def set_years(self):
        while True:
            try:
                self.years = int(input('How long is the amortissement (years)?'))
                break
            except:
                print("That's not a valid number")