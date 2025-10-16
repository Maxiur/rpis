import random as rand

class MonteCarlo():
    def __init__(self, samples, radius=1):
        self.samples = samples
        self.radius = radius

    def calculate_PI(self):
        success = 0
        for _ in range(self.samples):
            x = rand.uniform(0, 1)
            y = rand.uniform(0, 1)
            if x**2 + y**2 <= 1:
                success += 1

        return (success / self.samples) * 4

def main():
    samples = [10, 100, 1000, 100_000, 1_000_000]
    for i, sample in enumerate(samples, start=1):
        monte_carlo = MonteCarlo(sample)
        pi_estimate = monte_carlo.calculate_PI()
        print(f"Próba {i}:")
        print(f"    Liczba rzutów: {sample}")
        print(f"    Przybliżenie liczby \u03C0: {pi_estimate}\n")


if __name__ == "__main__":
    main()