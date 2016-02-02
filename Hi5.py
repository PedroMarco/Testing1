__author__ = 'acpb859'

###use eval, remember to use eval, or it will be a simple string

integer = eval(input('enter an integer '))


if integer != (integer%5):
    print('HiFive')
else:
    print('HiEven')