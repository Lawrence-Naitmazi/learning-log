import random

NUM_EXPERIMENTS = 10_000
NUM_FLIPS = 100
STREAK_LENGTH = 6


def has_streak(flips, length):
    """Return True if `flips` contains `length` equal values in a row."""
    run = 0
    previous = None
    for flip in flips:
        run = run + 1 if flip == previous else 1
        if run == length:
            return True
        previous = flip
    return False


def run_experiment():
    flips = random.choices("HT", k=NUM_FLIPS)
    return has_streak(flips, STREAK_LENGTH)


def main():
    streaks = sum(run_experiment() for _ in range(NUM_EXPERIMENTS))
    print(f"Chance of streak: {streaks / NUM_EXPERIMENTS:.2%}")


if __name__ == "__main__":
    main()
