



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

    def promp_int(self, msg):
        while True:
            try:
                self.price = int(input(msg))
                break
            except:
                print("That's not a valid number")


    def set_price(self):
        msg = 'What is the price of the item?'
        self.promp_int(msg)


    def set_interest(self):
        msg = 'What is the interest for the loan?'
        self.promp_int(msg)


    def set_years(self):
        msg = 'How long is the amortissement (years)?'
        self.promp_int(msg)
