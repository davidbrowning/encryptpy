#!/usr/bin/python3

from random import randint
from eucs_py3 import *
from fixed_points_py3 import half_interval_method as him
from quotes import *

public_key = 614889782588491410
public_key_factors = () ## you will have to compute these
code_separator = euclid_number(33)

def choose_random_factor_index(num_public_key_factors):
    return randint(0, num_public_key_factors-1)

def pascal_tri_row(n):
    ## your code
    pass

def pascal_tri_row_sum(n):
    ## your code
    pass

def encrypt_char(c):
    ## your code
    pass

def encrypt_text(txt):
    enc = ''
    for c in txt: enc += encrypt_char(c)
    return enc
    
def decrypt_text(txt):
    ## your code
    pass
        


