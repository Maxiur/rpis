import numpy as np
import matplotlib.pyplot as plt

class FGP_Vn:
    def __init__(self, n: int, samples: int):
        self.samples = samples
        self.n = n

    # def expectedFunction(self, y: int):
    #     return np.power(y, (1.0 - self.n) / self.n) / (2.0 * self.n)

    def expectedFunction(self, v: np.ndarray):
        V_max = 2 ** self.n
        n_float = float(self.n)
        f_v = np.zeros_like(v, dtype=float)

        valid_range = (v > 0) & (v < V_max)
        exponent = (1.0 / n_float) - 1.0
        constant = 1.0 / (2.0 * n_float)

        # Obliczenie gęstości, zwracanie 0 dla v poza (0, 2^n)
        f_v[valid_range] = constant * np.power(v[valid_range], exponent)

        return f_v

    def generateSamples(self):
        # Generowanie n-samples długości boku X ~ U(0, 2)
        X = np.random.uniform(0.0, 2.0, self.samples)
        # X jest wektorem, więc

        Vn = X ** self.n

        return Vn


def simulate_and_plot(n_values: list[int], N_samples: int):

    fig, axes = plt.subplots(1, len(n_values), figsize=(4 * len(n_values), 6))
    if len(n_values) == 1:
        axes = [axes]

    fig.suptitle(f'FGP Objętości $V_n = X^n$ ($N={N_samples:,}$)'.replace(',', ' '), fontsize=14)

    for idx, n in enumerate(n_values):
        model = FGP_Vn(n, N_samples)
        ax = axes[idx]
        V_max = 2**n

        # 1. Numeryczna
        Vn_samples = model.generateSamples()
        ax.hist(Vn_samples, bins=100, density=True, alpha=0.6, color='skyblue', label='Numeryczne')

        # # 2. Analityczna
        # v_theory = np.linspace(1e-6, V_max, 500)
        # f_v_theory = model.expectedFunction(v_theory)
        # ax.plot(v_theory, f_v_theory, color='red', linewidth=2, label='Analityczne')

        # Ustawienia wykresu
        ax.set_title(f'Wymiar $n = {n}$')
        ax.set_xlabel('Objętość $V_n$')
        if idx == 0:
            ax.set_ylabel('Gęstość Prawdopodobieństwa')

        ax.legend(loc='upper right')

        # Ustawienie X i Y (Korekta dla n=20)
        if n <= 3:
            ax.set_ylim(0, 1.0)
        else:
            ax.set_ylim(0, 0.6)
            ax.set_xlim(0, V_max * 1.05)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


def main():
    samples = 10_000_000
    simulate_and_plot([1, 2, 3, 4, 5, 20], samples)

    # simulate_and_plot([20], samples)


if __name__ == "__main__":
    main()