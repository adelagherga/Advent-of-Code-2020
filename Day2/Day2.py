#!/usr/bin/python
# Day2.py

# Author: Adela Gherga <adelagherga@gmail.com>
# Copyright © 2021, Adela Gherga, all rights reserved.
# Created: 23 April 2021
#
# Description: Day 2 of Advent of Code 2020
#
# Commentary:
#
# To do list:
#
# Example:
#

# Test Data
# policies = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

# Part 1 - find the number of passwords that are valid according to their policies

valid = 0;
policies = open('./Day2/Day-2-Data.txt',"r");
for line in policies:
    line_split = line.split(" ");

    min_no = int(line_split[0].split("-")[0]);
    max_no = int(line_split[0].split("-")[1]);

    x = ord(line_split[1].split(":")[0]);
    passwords = [ord(i) for i in line_split[2]];

    count = 0;
    for i in passwords:
        if x == i:
            count += 1;

    if (count in range(min_no, max_no+1)):
        valid += 1;

print(valid);

# Part 2 - find the number of passwords that are valid according to the new interpretation of the policies

valid = 0;
policies = open('./Day2/Day-2-Data.txt',"r");
for line in policies:
    line_split = line.split(" ");

    test_1 = int(line_split[0].split("-")[0]) - 1;
    test_2 = int(line_split[0].split("-")[1]) - 1;

    x = ord(line_split[1].split(":")[0]);
    passwords = [ord(i) for i in line_split[2]];

    count = 0;
    if (x == passwords[test_1]):
        count += 1;
    if (x == passwords[test_2]):
        count += 1

    if (count == 1):
        valid += 1;

print(valid);
