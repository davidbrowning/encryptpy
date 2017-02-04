#!/usr/bin/python

from random import randint
##from eucs import *
##from fixed_points import half_interval_method
from quotes import *
import math
import euclid_numbers

# found on stackoverflow by stefan edited by will ness 
# I tried to use the algorithm I had written for euclid_numbers.py, 
# but it got stuck in a loop somehow


def prime_factors(n):
    i = 2
    factors = []
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

public_key = public_key = 61488978258849141
factor_list = []
factor_list = prime_factors(public_key)
factor_list_set = set(factor_list)
public_key_factors =  factor_list_set ## you will have to compute these 
# use euclid_numbers.prime_factor(n, factor_list)

code_separator = euclid_numbers.euclid_number(33)

def choose_random_factor_index(num_public_key_factors):
    return randint(0, num_public_key_factors-1)


def half_interval_method(f, a, b):
    a_val = f(a)
    b_val = f(b)
    if a_val < 0 and b_val > 0:
        return search_for_midpoint(f, a, b)
    elif b_val < 0 and a_val > 0:
        return search_for_midpoint(f, b, a)
    else:
        raise Exception('Values are not of oppositive sign')


def is_even(num):
    if(num % 2 == 0):
        return True;
    else:
        return False;


def pascal_tri_row(n):
    k = 0;
    li = []
    while (k < n):
#        print '%d is less than %d' %(k, n) 
        li.append((math.factorial(n))/(math.factorial(k)*(math.factorial(n - k))))
        k += 1;

    if(is_even(n)):
        li.append((math.factorial(n))/(math.factorial(k)*(math.factorial(n - k))))
        k = k-1;
    else:
        while (k >= n):
            li.append((math.factorial(n))/(math.factorial(k)*(math.factorial(n - k))))
            k += -1;

    return li
    pass

def pascal_tri_row_sum(n):
    answer = 2
    if(euclid_numbers.is_prime(n)):
        k = pascal_tri_row(n)
        for item in k:
            if(item != 1):
                answer += (item/n)
    else:
        answer = -1
    return answer



#def encrypt_char(c):
#    ## your code
#    pass

#def encrypt_text(txt):
#    enc = ''
#    for c in txt: enc += encrypt_char(c)
#    return enc
    
#def decrypt_text(txt):
#    ## your code
#    pass
        


