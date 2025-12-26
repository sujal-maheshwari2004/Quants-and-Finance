class zeroCouponBond:
    def __init__(self, principal, maturity, interest_rate):
        self.principal = principal              # principal amount
        self.maturity = maturity                # maturity period in years
        self.interest_rate = interest_rate      # annual interest rate as a decimal

    def present_value(self, x, n):
        return x/(1 + self.interest_rate)**n
    
    def calculate_price(self):
        return self.present_value(self.principal, self.maturity)
    
if __name__ == "__main__":
    # Example usage
    bond = zeroCouponBond(principal=1000, maturity=5, interest_rate=0.05)
    price = bond.calculate_price()
    print(f"The price of the zero-coupon bond is: ${price:.2f}")