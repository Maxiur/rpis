import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import gamma

def generate_normal_dist():
    u1 = np.random.uniform(0.0, 1.0)
    u2 = np.random.uniform(0.0, 1.0)

    return np.sqrt(np.log((1.0 / u1) ** 2)) * np.sin(2 * np.pi * u2)

def generate_chi(n: int):
    sum = 0.0
    for _ in range(n):
        sum += generate_normal_dist() ** 2
    return sum

def generate_plot(a: int, samples: int, bins: int):
    data = np.array([generate_chi(a) for _ in range(samples)])
    plt.hist(
        data, bins, facecolor="#feb24c", alpha=0.7, density=True, label="Numeryczne"
    )

    x = np.linspace(0, data.max(), 1000)
    y = ((x / 2) ** (a / 2 - 1) * np.exp(-x / 2)) / (2 * gamma(a / 2))
    plt.plot(x, y, label="Analityczne")
    plt.grid(True)
    plt.title("Rozkład Chi-wadrat n=" + str(a))
    plt.xlabel("x")
    plt.ylabel("Prawdopodobieństwo")
    plt.xlim(-0.1)
    plt.legend()
    plt.show()
    plt.savefig("histogram" + ".png")

if __name__ == "__main__":
    generate_plot(3, 500_000, 100)