#!/usr/bin/python
# Day1.py

# Author: Adela Gherga <adelagherga@gmail.com>
# Copyright © 2021, Adela Gherga, all rights reserved.
# Created: 21 April 2021
#
# Description: Day 1 of Advent of Code 2020
#
# Commentary:
#
# To do list:
#
# Example:
#

# Test Data
#Expenses = [1721, 979, 366, 299, 675, 1456];

# Part 1 - find the two entries that sum to 2020 and then multiply those two numbers together

Expenses = [];
file = open('./Day1/Day-1-Data.txt',"r");
for line in file:
    Expenses.append(int(line))

for i in Expenses:
    if ((2020 - i) in Expenses):
        print(i*(2020-i))
        break;

# Part 2 - find the three entries that meet the same criteria and find the product

for i in Expenses:
    for j in Expenses[i+1:]:
        if ((2020 - i - j) in Expenses):
            print(i*j*(2020-i-j));
            break;
