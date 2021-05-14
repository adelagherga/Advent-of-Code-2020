#!/usr/bin/python
# Day4.py

# Author: Adela Gherga <adelagherga@gmail.com>
# Copyright © 2021, Adela Gherga, all rights reserved.
# Created: 10 May 2021
#
# Description: Day 4 of Advent of Code 2020
#
# Commentary:
#
# To do list:
#
# Example:
#

# Test Data
# passports =
# ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
#  "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
#  "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
#  "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"]

from itertools import chain

# Part 1 - find the number of valid passports

def get_passports(file):
    passports = open(file,'r');

    groups = [[]]
    for line in passports:
        if line != "\n":
            path = line.split('\n')[0]
            groups[-1].append(path)
        else:
            groups[-1] = " ".join(groups[-1])
            groups.append([])

    groups[-1] = " ".join(groups[-1])
    return groups;

passports = get_passports('./Day4/Day-4-Data.txt')
valid_passports = []
for line in passports:
    data = line.split(" ")
    if len(data) == 8:
        valid_passports.append(sorted(data))
    elif len(data) == 7:
        if "cid" not in line:
            valid_passports.append(sorted(data))

print(len(valid_passports));

# Part 2 - find the number of passports where all required fields are both present and valid

def test(inf,i):
    if i == 1:
        return (int(inf) in range(1920,2003))
    if i == 2:
        return (inf in ["amb","blu","brn","gry","grn","hzl","oth"])
    if i == 3:
        return (int(inf) in range(2020,2031))
    if i == 4:
        return ((len(inf) == 7) and (ord(inf[0]) == 35) and
                all([ord(j) in chain(range(48,58),range(97,103)) for j in inf[1:]]))
    if i == 5:
        test1 = inf.split("cm")
        test2 = inf.split("in")
        return ((len(test1) == 2 and int(test1[0]) in range(150,194)) or
                (len(test2) == 2 and int(test2[0]) in range(59,77)))
    if i == 6:
        return (int(inf) in range(2010,2021))
    if i == 7:
        return (all([ord(j) in range(48,58) for j in inf]) and (len(inf) == 9))

def data_validation(data):
    data = [inf.split(":")[1] for inf in data]
    valid = test(data[0],1)

    i = 2
    while valid and i <= 7:

        if len(data) == 8:
            valid = test(data[i],i)
        else:
            valid = test(data[i-1],i)
        i += 1
    return valid

valid = 0
for line in valid_passports:
    if data_validation(line):
        valid += 1

print(valid);
