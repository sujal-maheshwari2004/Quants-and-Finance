from math import exp

# The financial models below assume:
# x = initial amount of money
# r = interest rate (as a decimal, e.g., 0.05 for 5%)
# n = number of periods (e.g., years)

def future_discerete_value(x , r, n):
    return x * (1 + r) ** n

def present_discerete_value(x , r, n):
    return x * (1 + r) ** -n

def future_continious_value(x, r, n):
    return x * exp(r * n)

def present_continious_value(x, r, n):
    return x * exp(-r * n)


if __name__ == "__main__":
    # Example usage:
    initial_amount = 1000  # $1000
    interest_rate = 0.05   # 5%
    periods = 10           # 10 years

    fv_discrete = future_discerete_value(initial_amount, interest_rate, periods)
    pv_discrete = present_discerete_value(initial_amount, interest_rate, periods)

    fv_continuous = future_continious_value(initial_amount, interest_rate, periods)
    pv_continuous = present_continious_value(initial_amount, interest_rate, periods)

    print(f"Future Value (Discrete): ${fv_discrete:.2f}")
    print(f"Present Value (Discrete): ${pv_discrete:.2f}")
    print(f"Future Value (Continuous): ${fv_continuous:.2f}")
    print(f"Present Value (Continuous): ${pv_continuous:.2f}")