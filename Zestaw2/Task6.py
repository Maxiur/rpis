import random

class CardSimulation:
    def __init__(self, tolerance=0.001):
        self.samples = 100_000
        self.tolerance = tolerance
        """a) Generator liczb pseudolosowych"""
        random.seed()

    def draw_three_cards(self):
        """b) Pojedyncze losowanie 3 kart i sprawdzenie trefli"""
        deck = list(range(52))
        hand = random.sample(deck, 3) # losowanie bez zwracania
        """Załóźmy że trefle są liczbami od 0 do 12"""
        return all(card >= 13 for card in hand) # True jeśli nie wylosowało żadnego trefla

    def simulate_fixed_samples(self):
        """c) Symulacja z określoną liczbą powtórzeń"""
        successes = 0
        for _ in range(self.samples):
            if self.draw_three_cards():
                successes += 1

        return successes / self.samples

    def simulate_until_tolerance(self):
        """c) Ile prób potrzebujemy dla dokładności 0.1%"""
        i = 0
        successes = 0
        while True:
            i += 1
            if self.draw_three_cards():
                successes += 1
            # Spradzamy poprawność co 1000 prób
            if i % 1000 == 0:
                prob_estimate = successes / i
                if abs(prob_estimate -  9139 / 22100) < self.tolerance:
                    break

        return i, prob_estimate

def main():
    card1 = CardSimulation(tolerance=0.001) # 0.1%
    card2 = CardSimulation(tolerance=0.003) # 0.3%
    card3 = CardSimulation(tolerance=0.05) # 0.5%
    simulations = [card1, card2, card3]

    for i, simulation in enumerate(simulations, start=1):
        num_trials, prob_estimate = simulation.simulate_until_tolerance()
        prob_fixed_samples = simulation.simulate_fixed_samples()
        print(f"Próba {i}:")
        print(f"   Prawdopodobieństwo z dużej próbki ({simulation.samples}): {prob_fixed_samples * 100:.2f}%")
        print(f"   Liczba prób dla tolerancji {simulation.tolerance * 100:.1f}%: {num_trials}")
        print(f"   Symulowane prawdopodobieństwo: {prob_estimate * 100:.2f}%")
        print(f"   Prawdopodobieństwo teoretyczne: {9139 / 22100 * 100:.2f}%\n")

if __name__ == "__main__":
    main()


