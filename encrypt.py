#!/usr/bin/python

from random import randint
##from eucs import *
##from fixed_points import half_interval_method
from quotes import *
import math
import euclid_numbers

public_key = public_key = 61488978258849141
public_key_factors = () ## you will have to compute these

#code_separator = euclid_number(33)

def choose_random_factor_index(num_public_key_factors):
    return randint(0, num_public_key_factors-1)

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

#def pascal_tri_row_sum(n):
#    ## your code
#    pass

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
        


