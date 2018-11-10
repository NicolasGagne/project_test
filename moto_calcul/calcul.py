'''
File to calculate the Budget associated with new motorcycle
'''

class Budget(object):
    def __init__(self):
        self.price = 13000
        self.years = 5
        self.interet = 7

    def pvtx(self):
        """Calcul of the provincial tax on sale price"""
        return self.price * 0.0975

    def fdtx(self):
        """Calcul of the Federal taxe on sale price"""
        return self.price * 0.05

    def comtx(self):
        """Calcul taxe for a Commercial transaction"""
        return self.fdtx() + self.pvtx()

    def totalpv(self):
        """Calcul Total price for a Private transaction"""
        return self.price + self.pvtx()

    def totalcom(self):
        """Calcul Total price for a Commercial Transaction"""
        return self.price + self.comtx()

    def payment(self):
        """Calculate payment for for a commercial transaction"""
        month = float(self.years) * 12
        interest_rate = float(self.interet) / 100 / 12

        # Formula to calculate monthly payments
        return self.totalcom() * (interest_rate * (1 + interest_rate) ** month) / ((1 + interest_rate) ** month - 1)

    def promp_int(self, msg):
        """ General def to ask for user for information
            DO NOT CALL DIRECLY
        """
        while True:
            try:
                x = int(input(msg))
                break
            except:
                print("That's not a valid number")
        return x

    def set_price(self):
        """Call to change the price of the item"""
        msg = 'What is the price of the item?'
        self.price = self.promp_int(msg)

    def set_interest(self):
        """Call to change the interest rate"""
        msg = 'What is the interest for the loan?'
        self.interet = self.promp_int(msg)

    def set_years(self):
        """Call to change the ammoritssmeent"""
        msg = 'How long is the amortissement (years)?'
        self.years = self.promp_int(msg)
