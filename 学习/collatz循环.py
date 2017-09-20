#!/usr/bin/python

def collatz(number):
    if (number/2)*2==number:
        return number//2
    else:
        return number*3+1

r=int(raw_input())
print r
while not(r==1):
    r=collatz(r)
    print r
