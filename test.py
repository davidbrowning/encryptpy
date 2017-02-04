#!/bin/python

import encrypt
import euclid_numbers
print("Testing pascal_tri_row...");
i = 0
print('pascal_tri_row(0 - 20)')
for i in xrange(20):
    print(encrypt.pascal_tri_row(i));

#n = encrypt.pascal_tri_row(8);
#encrypt.pascal_tri_row_sum(n);
#print encrypt.pascal_tri_row(euclid_numbers.euclid_number(2));
#r = euclid_numbers.euclid_number(4);
#print r
#q = encrypt.pascal_tri_row(r);
#print q
#print encrypt.pascal_tri_row_sum(q);
# I've tested the above 8 lines, and it passed but it took longer than 
#  I care to test again

print(encrypt.pascal_tri_row_sum(3))
print(encrypt.pascal_tri_row_sum(5))
print(encrypt.pascal_tri_row_sum(7))

print(encrypt.encrypt_char('a'))
print(encrypt.encrypt_char('b'))
print(encrypt.encrypt_char('c'))
print(encrypt.encrypt_char('d'))

print(encrypt.encrypt_text('abd'));
my_string = encrypt.encrypt_text('abd')
print(encrypt.decrypt_text(my_string))
