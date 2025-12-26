import math

class CouponBond:
    def __init__(self, principal, rate, maturity, interest_rate):
        self.principal = principal              # principal amount
        self.rate = rate                        # annual coupon rate as a decimal
        self.maturity = maturity                # maturity period in years
        self.interest_rate = interest_rate      # annual interest raten of the market as a decimal

    def present_value(self, x, n):
        return x / (1 + self.interest_rate) ** n
    
    def continuous_present_value(self, x, n):
        return x * math.exp(-self.interest_rate * n)
    
    def calculate_price(self):
        price = 0
        # Present value of coupon payments
        for t in range(1, self.maturity + 1):
            #price += self.continuous_present_value(self.principal * self.rate, t)
            price += self.present_value(self.principal * self.rate, t)
        
        # Present value of principal repayment
        #price += self.continuous_present_value(self.principal, self.maturity)
        price += self.present_value(self.principal, self.maturity)
        
        return price
    

if __name__ == "__main__":
    # Example usage
    bond = CouponBond(principal=1000, rate=0.10, maturity=3, interest_rate=0.04)
    price = bond.calculate_price()
    print(f"The price of the coupon bond is: ${price:.2f}")