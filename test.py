#!/bin/python
import encrypt

print("Testing pascal_tri_row...");
i = 0
print('pascal_tri_row(0 - 20)')
for i in xrange(20):
    print(encrypt.pascal_tri_row(i));
