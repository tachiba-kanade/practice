"""attractiveness as a bell curve

Simulate people's “true” attractiveness
Simulate how attractive they think they are
Draw the bell curve graph

"""


import numpy as np
import matplotlib.pyplot as plt

#total number of fake poeple

N = 100000
# 1. TRUE ATTRACTIVENESS
# Most people are around 5, with spread 1.5, so thats jokinigly true so base out of 10 people look avg 5 so true is basescale
true = np.random.normal(5, 1.5,N)


# 2. SELF DELULU
# now people general attractivness is scalling higher lets take 6.5,  Some overestimate, some underestimate.

people = np.random.normal(0, 1.45,N)
# Self-rating formula:
# Base self-rating is 6.5.
# Actual attractiveness affects self-rating only weakly: 0.24 factor like a noise. just to be easy on them

# true = 9
# self = 6.3 + 0.24 * (9 - 5)
# self = 6.3 + 0.96
# self = 7.26 before noise


self = 6.5 + 0.24 * (true - 5) + people


# lets measure the relationship
# Do people with higher true attractiveness also rate themselves higher?
# The answer is around:
# r is roughly 0.24

r = np.corrcoef(true, self)[0, 1]
"""
true = [3.2, 4.9, 5.1, 7.8, 8.5]
self = [5.7, 6.1, 6.4, 7.0, 7.3]

Person 1: true = 3.2, self = 5.7
Person 2: true = 4.9, self = 6.1
Person 3: true = 5.1, self = 6.4
Person 4: true = 7.8, self = 7.0
Person 5: true = 8.5, self = 7.3 and so on

correlation(true, true) = 1.00
correlation(true, self) = 0.24
correlation(self, true) = 0.24
correlation(self, self) = 1.00
The diagonal values are always 1.00

+1  = perfect positive relationship
 0  = no linear relationship
-1  = perfect negative relationship

r = 0.24
that means there is a weak positive relationship.
"""

print(f"Correlation between true and self rating: {r:.2f}")
"""
self = [6.2, 4.8, 7.1, 5.0, 6.9] all which are greater than 5
[True, False, True, False, True]
[1, 0, 1, 0, 1] then find the mean and percentage
3/5 = 0.79

(self > 5).mean()
 after decimal 2 places as the percentage
"""
per = (self>5).mean()
print(f"{per*100:.0f}think they're above average") # if 0.234 = 23

# Correlation between true and self rating: 0.24
# 81% think they're above average


#lets plot it

#normal distribution formula  for mesuring the height of bellcurve: f(x) = 1 / (σ√(2π)) × e^(-0.5 × ((x - μ) / σ)^2)

x = np.linspace(1,10,500)

mean = 5
std = 1.5

# Normal distribution formula
pdf = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(
    -0.5 * ((x - mean) / std) ** 2
)

plt.figure(figsize=(10, 6))

# Draw the smooth bell curve
plt.plot(x, pdf, linewidth=2)

# -----------------------------
# 5. Add dots under the curve
# -----------------------------

# Use fewer points for display, otherwise 100k dots is too much
dot_x = np.random.normal(loc=5, scale=1.5, size=4000)
dot_x = np.clip(dot_x, 1, 10)

# For each dot, calculate how high the bell curve is at that x position
dot_pdf = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(
    -0.5 * ((dot_x - mean) / std) ** 2
)

# Put each dot somewhere between y=0 and the curve height
dot_y = np.random.uniform(0, dot_pdf)
plt.scatter(dot_x, dot_y, s=3, alpha=0.4)

# -----------------------------
# 6. Add "YOU?" marker
# -----------------------------

you_x = 3
you_y = 0.04

plt.scatter([you_x], [you_y], s=80)
plt.vlines(you_x, you_y, you_y + 0.07)
plt.text(you_x - 0.45, you_y + 0.075, "YOU?", fontsize=16, fontweight="bold")

# -----------------------------
# 7. Final styling
# -----------------------------

plt.title("Human attractiveness rated 1-10")
plt.xlabel("Attractiveness rating")
plt.ylabel("Density")
plt.xlim(1, 10)
plt.ylim(0, max(pdf) * 1.15)

plt.show()