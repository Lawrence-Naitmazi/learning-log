import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 10,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    coinFlips = []
    for i in range(100):
        coinFlips.append(random.randint(0, 1))
    
    for i in range(len(coinFlips)):
        if coinFlips[i] == 0:
            coinFlips[i] = 'H'
        elif coinFlips[i] == 1:
            coinFlips[i] = 'T'

    # Code that checks if there is a streak of 6 heads or tails in a row
    headStreak = ['H', 'H', 'H', 'H', 'H', 'H']
    tailStreak = ['T', 'T', 'T', 'T', 'T', 'T']
    for i in range(len(coinFlips) - 5):
        if coinFlips[i:i+6] == headStreak or coinFlips[i:i+6] == tailStreak:
            number_of_streaks += 1
            break
print('Chance of streak: %s%%' % (number_of_streaks / 100))