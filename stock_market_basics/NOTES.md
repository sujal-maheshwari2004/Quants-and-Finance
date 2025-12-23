# 1. Time Value of Money (TVM)

## 1.1 Core Idea

> **Money today is worth more than the same amount in the future**
> because of:

* Opportunity cost
* Inflation
* Risk
* Liquidity preference

TVM answers:

> *“How do we compare cash flows occurring at different points in time?”*

---

## 1.2 Discrete Compounding

### Present Value (PV)

If you receive **FV** after **n** periods at interest rate **r**:

[
PV = \frac{FV}{(1+r)^n}
]

**Interpretation:**
How much money today is equivalent to a future payment.

---

### Future Value (FV)

[
FV = PV(1+r)^n
]

**Interpretation:**
How much today’s money grows into after **n** periods.

---

### Multiple Cash Flows (Discrete)

For cash flows ( C_t ) at time ( t ):

[
PV = \sum_{t=1}^{T} \frac{C_t}{(1+r)^t}
]

This is the backbone of:

* Bond pricing
* Equity valuation
* Capital budgeting

---

### Compounding Frequency

If compounding occurs **m times per year**:

[
FV = PV\left(1+\frac{r}{m}\right)^{mn}
]

As ( m \uparrow ), compounding becomes more frequent.

---

## 1.3 Continuous Compounding

### Why Continuous?

* Financial theory assumes **smooth time**
* Natural for stochastic calculus and asset pricing models

---

### Continuous Future Value

[
FV = PV \cdot e^{rt}
]

### Continuous Present Value

[
PV = FV \cdot e^{-rt}
]

Where:

* ( e ) = Euler’s number
* ( r ) = continuously compounded rate
* ( t ) = time

---

### Discrete vs Continuous (Key Insight)

As compounding frequency → ∞:

[
\lim_{m \to \infty} \left(1 + \frac{r}{m}\right)^{mt} = e^{rt}
]

This transition is fundamental in:

* Black–Scholes
* Interest rate models
* Option pricing

---

# 2. Stocks and Shares

## 2.1 What is a Stock?

A **stock** represents **ownership** in a company.

A **share** is a single unit of stock.

---

## 2.2 Rights of Shareholders

* Residual claim on profits
* Voting rights (common stock)
* Dividends (if declared)

---

## 2.3 Types of Stocks

### Common Stock

* Voting rights
* Variable dividends
* Higher risk, higher return

### Preferred Stock

* Fixed dividends
* Priority over common shareholders
* Usually no voting rights

---

## 2.4 Stock Valuation (Basic Models)

### Dividend Discount Model (DDM)

[
P_0 = \sum_{t=1}^{\infty} \frac{D_t}{(1+r)^t}
]

For constant growth ( g ):

[
P_0 = \frac{D_1}{r - g}, \quad r > g
]

---

### Risk–Return Tradeoff

* Stocks have **systematic risk**
* Expected return compensates for volatility

---

# 3. Commodities

## 3.1 Definition

**Commodities** are standardized raw materials traded in bulk.

Examples:

* Energy: Oil, Gas
* Metals: Gold, Copper
* Agriculture: Wheat, Coffee

---

## 3.2 Key Characteristics

* Homogeneous
* Fungible
* Priced globally

---

## 3.3 Why Trade Commodities?

* Inflation hedge
* Portfolio diversification
* Speculation
* Industrial demand

---

## 3.4 Spot vs Futures Prices

### Spot Price

Price for **immediate delivery**

### Futures Price

Agreed price today for **delivery in the future**

Cost-of-carry model (simplified):

[
F = S e^{(r + c - y)t}
]

Where:

* ( c ) = storage costs
* ( y ) = convenience yield

---

# 4. Currencies and the Forex Market

## 4.1 What is Forex?

**Foreign Exchange (FX)** is the market for trading currencies.

Largest financial market by volume.

---

## 4.2 Currency Pairs

Currencies are quoted as:

[
\text{Base Currency} / \text{Quote Currency}
]

Example:
EUR/USD = 1.10 → 1 EUR = 1.10 USD

---

## 4.3 Spot vs Forward FX

### Spot FX

Immediate exchange at current rate

### Forward FX

Rate agreed today for future exchange

---

## 4.4 Interest Rate Parity (IRP)

[
\frac{F}{S} = \frac{(1+r_d)}{(1+r_f)}
]

Ensures **no arbitrage** between FX and interest rates.

---

## 4.5 FX Risk

* Transaction risk
* Translation risk
* Economic risk

---

# 5. Short and Long Positions

## 5.1 Long Position

You **buy** an asset expecting price to rise.

Payoff:
[
\text{Profit} = P_{\text{sell}} - P_{\text{buy}}
]

**Max Loss:** Limited (price → 0)
**Max Gain:** Unlimited

---

## 5.2 Short Position

You **sell first**, buy later.

Steps:

1. Borrow asset
2. Sell at current price
3. Buy back later
4. Return asset

Payoff:
[
\text{Profit} = P_{\text{sell}} - P_{\text{buy}}
]

**Max Gain:** Limited
**Max Loss:** Unlimited ⚠️

---

## 5.3 Why Short?

* Hedge risk
* Express negative view
* Arbitrage strategies

---

## 5.4 Long vs Short (Summary)

| Aspect      | Long    | Short                |
| ----------- | ------- | -------------------- |
| Market View | Bullish | Bearish              |
| Risk        | Limited | Unlimited            |
| Used For    | Growth  | Hedging, speculation |
