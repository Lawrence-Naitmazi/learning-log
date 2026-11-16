#The Collatz sequence
def collatz(number):
    if number % 2 == 0:
        result = number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
    print(result, end = ' ')
    return(result)

try:
    userNumber = int(input("Ener an integer: "))
    while userNumber != 1:
        userNumber = collatz(userNumber)
except ValueError:
    print("Error: You must enter a valid integer")