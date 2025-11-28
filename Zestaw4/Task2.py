import numpy as np
import matplotlib.pyplot as plt
import random
import math

class FGP:
    def __init__(self, samples):
        self.samples = samples

    def generateFromInverseFGP(self):
        uniform_dist = random.random()

        if uniform_dist <= 1.0 / 6.0:
            return math.sqrt(6 * uniform_dist) - 1
        elif uniform_dist <= 5.0 / 6.0:
            return 3 * uniform_dist - 1 / 2
        else:
            return 3 - math.sqrt(6(1 - uniform_dist))

    def generateFGP_forSamples(self):
        return [self.generateFromInverseFGP() for _ in range(self.samples)]


def density(x: float) -> float:
    if x <= -1:
        return 0.0
    elif x <= 0:
        return x / 3 + 1/3
    elif x <= 2:
        return 1 / 3
    elif x <= 3:
        return (-x) / 3 + 1
    else:
        return 0.0

def generatePlot(f: FGP, title: str):
    data = f.generateFGP_forSamples()

    x_theory = np.linspace(-1.5, 3.5, 500)
    y_theory = [density(x) for x in x_theory]


import numpy as np
import matplotlib.pyplot as plt
import random
import math


class FGP:
    def __init__(self, samples):
        self.samples = samples

    def generateFromInverseFGP(self):
        uniform_dist = random.random()

        if uniform_dist <= 1.0 / 6.0:
            return math.sqrt(6 * uniform_dist) - 1
        elif uniform_dist <= 5.0 / 6.0:
            return 3 * uniform_dist - 1 / 2
        else:
            return 3 - math.sqrt(6(1 - uniform_dist))

    def generateFGP_forSamples(self):
        return [self.generateFromInverseFGP() for _ in range(self.samples)]


def density(self, x: float) -> float:
    if x <= -1:
        return 0.0
    elif x <= 0:
        return x / 3 + 1 / 3
    elif x <= 2:
        return 1 / 3
    elif x <= 3:
        return (-x) / 3 + 1
    else:
        return 0.0


def generatePlot(f: FGP):
    print(f"Generowanie {f.samples:,} próbek...".replace(',', ' '))
    data = f.generateFGP_forSamples()

    # Definiowanie teoretycznej FGP dla płynnej linii
    x_theory = np.linspace(-1.5, 3.5, 500)
    y_theory = [density(x) for x in x_theory]

    # WYKRES
    plt.figure(figsize=(10, 6))

    # Wykres histogramu (Eksperymentalna FGP)
    # density=True zapewnia normalizację do pola 1, pozwalając na porównanie z FGP.
    plt.hist(
        data,
        bins=50,
        density=True,
        alpha=0.6,
        color='skyblue',
        label=f'Histogram próbek Monte Carlo (N={f.samples:,})'.replace(',', ' ')
    )

    # Wykres teoretycznej FGP
    plt.plot(
        x_theory,
        y_theory,
        color='red',
        linewidth=3,
        label='Teoretyczna Funkcja Gęstości $f(x)$'
    )

    # Ustawienia końcowe
    plt.title(f'Porównanie FGP eksperymentalnej z teoretyczną')
    plt.xlabel('Wartość zmiennej losowej $X$')
    plt.ylabel('Gęstość Prawdopodobieństwa')
    plt.grid(axis='y', alpha=0.5, linestyle='--')
    plt.legend(loc='upper right')
    plt.xlim(-1.5, 3.5)
    plt.ylim(0, 0.4)
    plt.show()

def main():
    samples1 = 10 ** 3
    samples2 = 10 ** 5

    f1 = FGP(samples1)
    generatePlot(f1)

    f2 = FGP(samples2)
    generatePlot(f2)

if __name__ == "__main__":
    main()