

def pvtx(price):
    return price * 0.0975

def fdtx(price):
    return price * 0.05

def comtx(price):
    return fdtx(price) + pvtx(price)

def totalpv(price):
    return price + pvtx(price)

def totalcom(price):
    return price + comtx(price)

def payment(loanAmount, interet, years):
    years = float(years) * 12
    interestRate = float(interet) / 100 / 12

    # Formula to calculate monthly payments
    return loanAmount * (interestRate * (1 + interestRate) ** years) / ((1 + interestRate) ** years - 1)

