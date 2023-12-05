"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    i = 2
    while len(list) < number_of_primes:
        prime = True
        for j in range(2, 1+(i//2)):
            if i % j == 0:
                prime = False
                break
        if prime:
            list.append(i)
        i+= 1
    return list

