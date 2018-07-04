# coding: utf-8
from numpy.random import rand
from numpy import split
x = rand(10000,)
from functools import reduce
numList = split(x, 10)
from numpy import mean
reduce(lambda x, y: x + y, map(mean, numList)) / 10
np.mean(x)
mean(x)
