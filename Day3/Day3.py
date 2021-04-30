#!/usr/bin/python
# Day3.py

# Author: Adela Gherga <adelagherga@gmail.com>
# Copyright © 2021, Adela Gherga, all rights reserved.
# Created: 30 April 2021
#
# Description: Day 3 of Advent of Code 2020
#
# Commentary:
#
# To do list:
#
# Example:
#

# Test Data
# geology = [ "..##.......",
#            "#...#...#..",
#            ".#....#..#.",
#            "..#.#...#.#",
#            ".#...##..#.",
#            "..#.##.....",
#            ".#.#.#....#",
#            ".#........#",
#            "#.##...#...",
#            "#...##....#",
#            ".#..#...#.#"]

import numpy as np

# Part 1 - find the number of trees you would encounter following a slope of right 3 and down 1

with open('./Day3//Day-3-Data.txt') as f:
    geology_length = len(f.readline().strip())

geology = open('./Day3/Day-3-Data.txt','r');

trees = 0;
x = 0;
for line in geology:
    if line[x] == "#":
        trees += 1;
    x = (x + 3) % geology_length;

print(trees);

# Part 2 - find the product of the number of trees encountered on each of the listed slopes

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]];
trees = [ 0 for i in range(0,len(slopes))];

for i in range(0,len(slopes)):
    x = 0;
    y = 0;

    geology = open('./Day3/Day-3-Data.txt','r');
    for line in geology:
        if (y % slopes[i][1] == 0):
            if line[x] == "#":
                trees[i] += 1;
            x = (x + slopes[i][0]) % geology_length;
        y = y + 1;

print(np.prod(np.array(trees)));
