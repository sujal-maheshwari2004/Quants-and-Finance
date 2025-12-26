## 1. What are Bonds?

A **bond** is a **debt instrument**.

* **Issuer**: Government / corporation
* **Investor**: Lender
* **Promise**:

  * Periodic interest payments (coupons)
  * Repayment of principal at maturity

### Key Components

* **Face (Par) Value (F)** – amount repaid at maturity
* **Coupon Rate (c)** – interest paid on face value
* **Maturity (T)** – time until repayment
* **Bond Price (P)** – current market value

> Economically, a bond is a **series of fixed future cash flows**.

---

## 2. Yields and Yield to Maturity (YTM)

### Yield (General Idea)

**Yield** measures the **return** earned on a bond.

Common yield measures:

* Coupon yield
* Current yield
* **Yield to Maturity (YTM)** (most important)

---

### Yield to Maturity (YTM)

**YTM** is the **single discount rate** that equates the present value of all future cash flows to the current bond price.

[
P = \sum_{t=1}^{T} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^T}
]

Where:

* (y) = yield to maturity

---

### Interpretation

YTM is the bond’s **internal rate of return (IRR)** assuming:

* Bond is held to maturity
* Coupons are reinvested at YTM
* No default

These assumptions are idealized but standard.

---

## 3. Interest Rates and Bonds

### Fundamental Relationship

[
\boxed{\text{Interest Rates ↑  ⇒ Bond Prices ↓}}
]

[
\boxed{\text{Interest Rates ↓  ⇒ Bond Prices ↑}}
]

---

### Why This Happens

Bond prices are present values of fixed cash flows:

[
P = \sum_{t} \frac{C_t}{(1+r)^t}
]

Higher discount rate → lower present value.

---

### Sensitivity Depends On

* Time to maturity
* Size of coupons
* Timing of cash flows

This motivates **duration**.

---

## 4. Macaulay Duration

### Definition

**Macaulay Duration** is the **weighted average time** of a bond’s cash flows.

[
D = \sum_{t=1}^{T} t \cdot \frac{PV(C_t)}{P}
]

---

### Interpretation

* Measures **interest-rate sensitivity**
* Expressed in **years**
* Think of it as the bond’s **center of mass in time**

---

### Key Properties

* **Zero-coupon bond**:
  [
  D = T
  ]

* **Coupon bond**:
  [
  D < T
  ]

---

### Price Sensitivity Approximation

[
\frac{\Delta P}{P} \approx -D \cdot \Delta y
]

---

## 5. Risks with Bonds

### 5.1 Interest Rate Risk

* Bond prices fall when rates rise
* Higher duration → higher risk

---

### 5.2 Credit (Default) Risk

* Issuer may fail to meet obligations
* Reflected in credit spreads

---

### 5.3 Reinvestment Risk

* Coupons reinvested at lower future rates
* Zero-coupon bonds avoid this risk

---

### 5.4 Inflation Risk

* Fixed payments lose real value

---

### 5.5 Liquidity Risk

* Difficulty selling without price impact

---

## 6. Stocks and Bonds

| Aspect          | Stocks    | Bonds  |
| --------------- | --------- | ------ |
| Nature          | Ownership | Debt   |
| Cash Flows      | Uncertain | Fixed  |
| Risk            | Higher    | Lower  |
| Claim Priority  | Residual  | Senior |
| Expected Return | Higher    | Lower  |

---

### Portfolio Role

* **Stocks** → growth and upside
* **Bonds** → stability and income

Bonds reduce volatility and improve risk control in diversified portfolios.
