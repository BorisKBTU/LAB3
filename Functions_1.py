import math
from itertools import permutations
from random import random, randint


def recipe(grams):
    ounces = 28.3495231 * grams
    return ounces



def farenheit(temp):
    cels = (5 / 9) * (temp - 32)
    return cels



def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            print(f'Chickens number: {chickens}')
            print(f'Rabbits number: {rabbits}')




def filter_prime(li):
    def find_multipliers(a):
        mult = []
        for i in range(1, a + 1):
            if a % i == 0:
                mult.append(i)
        if len(mult) > 2:
            return False
        return True

    print(f'Prime numbers: {list(filter(lambda x: find_multipliers(x), li))}')



def permutation(string):
    print([''.join(i) for i in list(permutations(string))])




def reverse(string):
    return ' '.join(string.split()[::-1])




def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] == 3:
            return True
    return False




def spy_game(nums):
    nums_ = list(filter(lambda x: x == 0 or x == 7, nums))
    for i in range(2, len(nums_)):
        if nums_[i - 2] == nums_[i - 1] == 0 and nums_[i] == 7:
            return True
    return False




def sphere(r):
    return math.pi * (r ** 3) / 3



def unique(li):
    dic = {i: [] for i in li}
    return list(dic.keys())



def palindrome(string):
    return string == string[::-1]



def histogram(lis):
    return ['*' * i + '\n' for i in lis]

def game():
    num = randint(1, 20)
    print('Hello! What is your name?')
    name = input()
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    k = 1
    guess=False
    num_inp = int(input())
    if num_inp > num:
        print('Your guess is too high.')
        print('Take a guess.')
    elif num_inp < num:
        print('Your guess is too low.')
        print('Take a guess.')
    else:
        print(f'Good job, KBTU! You guessed my number in {k} guesses!')
        guess = True
    while True and guess==False:
        num_inp = int(input())
        if num_inp > num:
            print('Your guess is too high.')
            print('Take a guess.')
        elif num_inp < num:
            print('Your guess is too low.')
            print('Take a guess.')
        else:
            print(f'Good job, KBTU! You guessed my number in {k} guesses!')
            break
        k += 1
def check():
    print(recipe(20))
    print(farenheit(273))
    solve(25, 94)
    filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9])
    permutation('abs')
    print(reverse('We are ready'))
    print(has_33([1, 3, 3]))
    print(has_33([1, 3, 1, 3]))
    print(has_33([3, 1, 3]))
    print(spy_game([1, 2, 4, 0, 0, 7, 5]))
    print(spy_game([1, 0, 2, 4, 0, 5, 7]))
    print(spy_game([1, 7, 2, 0, 4, 5, 0]))
    print(sphere(2))
    print(unique([1, 2, 7, 8, 4, 5, 5, 5, 5, 6, 7]))
    print(palindrome('mada'))
    print(*histogram([4, 9, 7]), end='', sep='')
    game()
