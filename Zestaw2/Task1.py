import random as rand

# Na płaszczyźnie naniesiono siatkę kwadratową o boku 'a'.
# Na płaszczyznę rzucono losowo monetę o promieniu r < a/2.
# Znaleźć prawdopodobieśtwo tego, że moneta nie upadnie na ani jeden bok kwadratu.

class Probability:
    def __init__(self, a, r):
        self.a = a
        self.r = r
        self.samples = 1_000_000

    def get_numeric_probability(self) -> float:
        a, r = self.a, self.r
        coin_not_touch_side = 0
        for _ in range(self.samples):
            x = rand.uniform(1e-9, a) # (0,a]
            y = rand.uniform(1e-9, a)
            if r < x < a - r and r < y < a - r:
                coin_not_touch_side += 1

        return coin_not_touch_side / self.samples

    def get_expected_probability(self):
        return 1 - 4*(self.r/self.a) + 4*(self.r**2 / self.a**2)


def main():
    # r < a/2
    # 2r < a
    prob1 = Probability(10, 2)
    prob2 = Probability(10, 4)
    prob3 = Probability(40, 10)
    prob4 = Probability(50, 20)
    prob5 = Probability(100, 50)

    for i, p in enumerate([prob1, prob2, prob3, prob4, prob5], start=1):
        print(f"Przypadek {i}:")
        print(f"   Symulacja: {p.get_numeric_probability() * 100:.2f}%")
        print(f"   Wzór:      {p.get_expected_probability() * 100:.2f}%\n")

if __name__ == "__main__":
    main()


