import numpy as np
import matplotlib.pyplot as plt

class FGP_Vn:
    def __init__(self, n: int, samples: int):
        self.samples = samples
        self.n = n

    def expectedFunction(self, y: int):
        return np.power(y, (1.0 - self.n) / self.n) / (2.0 * self.n)

    def generateSamples(self):
        # Generowanie n-samples długości boku X ~ U(0, 2)
        X = np.random.uniform(0.0, 2.0, self.samples)
        # X jest wektorem, więc

        Vn = X ** self.n

        return Vn


def simulate_and_plot(n_values: list[int], samples: int = 1_000_000):
    """
    Tworzy wykresy porównujące wynik analityczny i numeryczny dla podanych wymiarów.
    """

    # Tworzenie siatki wykresów (tyle kolumn, ile jest wymiarów n)
    fig, axes = plt.subplots(1, len(n_values), figsize=(4 * len(n_values), 6))

    if len(n_values) == 1:
        axes = [axes]

    fig.suptitle(
        f'FGP Objętości $V_n = X^n$ ($N={samples:,}$)'.replace(',', ' '),
        fontsize=14
    )

    for idx, n in enumerate(n_values):
        model = FGP_Vn(n, samples)
        ax = axes[idx]
        V_max = 2 ** n

        print(f"Generowanie {samples:,} próbek dla n={n} (Max V={V_max})...".replace(',', ' '))

        # 1. Numeryczna: Generowanie próbek i histogram
        Vn_samples = model.generateSamples()

        ax.hist(
            Vn_samples,
            bins=100,
            density=True,
            alpha=0.6,
            color='skyblue',
            label='Numeryczne (Histogram)'
        )

        # 2. Analityczna: Rysowanie teoretycznej FGP
        # Zaczynamy od 1e-6 by uniknąć problemów numerycznych przy V=0
        v_theory = np.linspace(1e-6, V_max, 500)
        f_v_theory = model.expectedFunction(v_theory)

        ax.plot(
            v_theory,
            f_v_theory,
            color='red',
            linewidth=2,
            label='Analityczne ($f_{V_n}(v)$)'
        )

        # Ustawienia wykresu
        ax.set_title(f'Wymiar $n = {n}$')
        ax.set_xlabel('Objętość $V_n$')

        if idx == 0:
            ax.set_ylabel('Gęstość Prawdopodobieństwa')

        ax.grid(axis='y', alpha=0.5, linestyle='--')
        ax.legend(loc='upper right')
        ax.set_xlim(0, V_max * 1.05)

        # Dynamiczne ustawienie limitów Y (gęstość jest bardzo wysoka blisko zera dla małych n)
        if n <= 3:
            ax.set_ylim(0, 1.0)
        elif n == 4:
            ax.set_ylim(0, 0.6)
        elif n == 5:
            ax.set_ylim(0, 0.4)
        elif n >= 20:
            # Dla n=20, V_max jest ogromne (ok. 1M), więc ograniczamy X do 1.0
            ax.set_xlim(0, 1.0)
            ax.set_ylim(0, 0.2)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()



def main():
    samples = 1_000_000
    simulate_and_plot([1, 2, 3, 4, 5], samples)

    simulate_and_plot([20], samples)


if __name__ == "__main__":
    main()