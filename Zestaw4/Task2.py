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
            return math.sqrt(6 * uniform_dist) - 1.0
        elif uniform_dist <= 5.0 / 6.0:
            return 3 * uniform_dist - 0.5
        else:
            return 3 - math.sqrt(6 * (1 - uniform_dist))

    def generateFGP_forSamples(self):
        return [self.generateFromInverseFGP() for _ in range(self.samples)]


def density(x: float) -> float:
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


def generatePlot(f: FGP, ax: plt.Axes):
    print(f"Generowanie {f.samples:,} próbek...".replace(',', ' '))
    data = f.generateFGP_forSamples()

    # Definiowanie teoretycznej FGP dla płynnej linii
    x_theory = np.linspace(-1.5, 3.5, 500)
    y_theory = [density(x) for x in x_theory]

    # Rysowanie histogramu na przekazanej osi 'ax'
    ax.hist(
        data,
        bins=50,
        density=True,
        alpha=0.6,
        color='skyblue',
        label='Histogram próbek Monte Carlo'
    )

    # Rysowanie teoretycznej FGP na przekazanej osi 'ax'
    ax.plot(
        x_theory,
        y_theory,
        color='red',
        linewidth=3,
        label='Teoretyczna FGP $f(x)$'
    )

    # Ustawienia końcowe
    ax.set_xlabel('Wartość zmiennej losowej $X$')
    ax.set_ylabel('Gęstość Prawdopodobieństwa')
    ax.grid(axis='y', alpha=0.5, linestyle='--')
    ax.legend(loc='upper right')
    ax.set_xlim(-1.5, 3.5)
    ax.set_ylim(0, 0.5)


def main():
    samples1 = 10 ** 3
    samples2 = 10 ** 5

    f1 = FGP(samples1)
    f2 = FGP(samples2)

    # Utworzenie jednej figury z dwoma podwykresami (1 wiersz, 2 kolumny)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Ustawienie głównego tytułu
    fig.suptitle('Porównanie FGP eksperymentalnej z teoretyczną', fontsize=16)

    # 1. Wykres po lewej stronie (N = 10^3)
    generatePlot(f=f1, ax=axes[0])
    axes[0].set_title(f'Mała próba: N = {samples1:,} próbek'.replace(',', ' '))

    # 2. Wykres po prawej stronie (N = 10^5)
    generatePlot(f=f2, ax=axes[1])
    axes[1].set_title(f'Duża próba: N = {samples2:,} próbek'.replace(',', ' '))
    axes[1].set_ylabel('') # Usuwamy powtarzającą się etykietę Y

    # Dostosowanie odstępów i wyświetlenie
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    main()
