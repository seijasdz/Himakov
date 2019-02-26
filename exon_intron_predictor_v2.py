from pomegranate import DiscreteDistribution
from helpers import ModelWraper
import numpy
a = 'a'
c = 'c'
g = 'g'
t = 't'
p = 'p'

# Replace this sequence to make predictions
data = [g,g,a,g,c,c,a,c,c,a,g,c,a,g,a,a,c,c,t,c,t,t,c,a,a,t,a,t,c,t,t,g,c,a,t,g,t,t,a,c,a,g,a,t,t,t,c,a,c,t,g,c,t,c,c,c,a,c,c,a,g,c,t,t,g,g,a,g,a,c,a,a,c,a,t,g,t,g,g,t,t,c,t,t,g,a,c,a,a,c,t,c,t,g,c,t,c,c,t,t,t,g,g,g,g,t,a,a,g,t,t,g,g,a,c,t,c,a,g,a,g,g,g,g,a,c,a,g,t,t,a,g,a,a,g,g,g,t,a,c,a,g,g,c,t,g,t,g,g,c,t,g,t,t,g,t,g,a,g,t,c,a,a,g,a,g,t,t,t,t,g,t,c,t,t,c,c,t,g,t,g,g,t,a,a,c,t,c,t,g,g,g,t,a,g,a,a,c,t,c,a,t,g,a,g,t,a,t,g,a,a,g,c,a,a,c,t,t,g,t,a,t,c,t,g,t,g,c,t,t,c,c,a,t,g,g,t,t,t,a,t,t,a,g,a,g,c,t,t,a,t,t,t,t,a,t,g,a,a,a,a,g,g,a,t,g,g,g,a,a,g,g,g,c,a,a,c,c,c,t,g,a,g,g,t,a,g,c,a,t,t,a,a,g,c,c,t,g,g,a,c,g,c,a,c,c,g,c,a,g,t,g,a,a,g,t,t,t,c,c,t,t,g,a,t,a,a,c,c,a,c,c,t,g,t,a,g,c,t,t,g,t,t,c,a,g,t,t,c,t,g,t,t,a,g,t,a,c,t,g,g,a,t,t,t,t,g,a,g,a,a,a,g,a,g,a,a,a,t,a,g,a,a,a,c,t,c,a,a,g,a,g,a,t,c,t,g,a,g,t,t,g,a,t,c,c,c,t,c,a,g,a,g,t,c,t,a,c,a,t,t,a,a,t,t,c,t,g,t,c,t,c,c,c,c,a,a,t,t,c,t,c,t,c,t,t,c,c,t,c,a,t,t,a,t,t,t,t,c,c,t,t,g,g,a,c,c,a,a,c,t,g,a,t,a,t,c,t,t,t,a,t,t,c,t,c,t,g,a,t,c,t,c,t,t,g,c,a,g,t,t,c,c,a,g,t,t,g,a,t,g,g,g,c,a,a,g,t,g,g,g,t,g,a,g,t,g,a,t,c,t,c,t,a,a,c,t,c,a,g,c,t,t,c,t,c,c,t,t,c,t,a,t,g,c,c,a,c,t,t,t,c,c,t,a,c,t,t,c,c,a,a,a,g,g,a,t,g,g,g,t,c,c,t,a,t,t,a,a,c,c,t,g,c,a,g,a,a,g,a,g,c,a,t,a,t,a,g,g,g,a,a,a,g,c,a,g,a,g,a,a,a,g,a,a,g,a,a,a,g,a,t,t,t,a,t,a,a,a,t,t,a,t,g,t,a,a,a,a,t,c,t,c,c,c,a,t,a,t,t,c,a,g,a,g,c,a,t,g,a,t,t,t,t,c,a,t,a,a,a,a,a,c,t,a,t,g,a,t,t,t,g,t,a,a,g,c,t,t,t,c,t,t,t,c,t,a,a,a,g,t,t,t,t,c,t,g,a,a,t,g,a,g,c,t,c,t,t,t,c,c,t,c,t,g,a,g,c,g,a,a,a,t,g,c,c,t,g,a,a,t,g,t,a,t,a,t,a,t,a,a,c,a,g,c,a,g,g,a,a,a,g,g,g,c,c,a,g,a,a,t,t,g,c,a,c,a,a,a,c,a,c,t,a,a,a,g,t,a,g,t,c,t,g,c,t,g,a,c,a,c,t,g,a,a,g,t,a,g,t,c,t,g,c,t,g,g,g,t,t,t,c,c,c,a,a,c,a,t,c,c,c,c,t,a,a,a,c,c,a,g,t,c,c,c,c,t,t,t,a,c,a,a,g,a,a,a,g,c,a,g,a,g,t,g,g,g,t,t,t,t,t,t,c,t,c,c,t,c,a,g,a,a,a,g,a,g,c,c,a,g,g,c,a,a,a,t,a,c,t,g,a,a,g,g,c,t,t,c,a,a,a,g,a,g,a,g,g,a,g,t,t,t,g,a,a,c,c,t,c,c,g,t,t,t,c,c,a,a,t,g,t,a,c,a,a,g,c,t,g,c,t,g,a,a,g,c,c,c,t,g,c,a,a,t,g,t,a,c,t,c,t,c,a,g,a,g,a,c,a,g,t,a,t,a,g,c,t,c,a,g,a,g,g,a,t,a,a,g,g,a,a,a,a,c,a,g,c,t,c,c,g,c,t,t,g,g,c,t,t,g,c,c,c,a,a,g,t,c,t,a,a,a,a,c,c,c,t,g,c,t,t,c,a,t,t,g,c,t,c,c,c,a,a,c,a,g,a,a,a,a,a,c,c,t,a,c,a,t,c,a,g,t,a,a,t,t,t,a,a,t,c,c,t,c,a,g,g,a,g,c,c,c,c,a,g,a,t,t,c,c,c,a,a,c,a,c,c,c,a,g,a,t,g,a,g,g,a,t,t,t,a,a,t,a,a,c,a,a,t,g,a,a,c,a,g,a,g,g,t,c,t,c,t,g,c,a,g,c,a,g,g,a,g,g,a,c,a,c,t,c,t,t,a,a,a,g,g,c,t,g,g,c,t,t,t,t,g,t,a,g,g,t,t,t,c,c,a,c,t,t,g,c,c,t,a,t,t,t,t,t,c,a,a,a,t,a,a,a,t,c,t,a,a,a,t,a,t,g,t,a,t,t,t,t,t,c,c,c,t,t,g,t,g,c,t,a,t,c,c,a,c,a,a,a,a,g,c,c,t,c,a,c,c,a,g,t,t,g,c,t,c,a,g,a,g,c,c,c,t,c,c,c,c,t,t,t,a,c,t,c,c,a,c,t,t,g,a,t,c,t,t,t,t,t,c,t,t,t,t,t,c,t,t,c,t,t,g,t,a,a,t,c,t,c,c,a,a,g,t,a,g,a,c,a,c,c,a,c,a,a,a,g,g,c,a,g,t,g,a,t,c,a,c,t,t,t,g,c,a,g,c,c,t,c,c,a,t,g,g,g,t,c,a,g,c,g,t,g,t,t,c,c,a,a,g,a,g,g,a,a,a,c,c,g,t,a,a,c,c,t,t,g,c,a,c,t,g,t,g,a,g,g,t,g,c,t,c,c,a,t,c,t,g,c,c,t,g,g,g,a,g,c,a,g,c,t,c,t,a,c,a,c,a,g,t,g,g,t,t,t,c,t,c,a,a,t,g,g,c,a,c,a,g,c,c,a,c,t,c,a,g,a,c,c,t,c,g,a,c,c,c,c,c,a,g,c,t,a,c,a,g,a,a,t,c,a,c,c,t,c,t,g,c,c,a,g,t,g,t,c,a,a,t,g,a,c,a,g,t,g,g,t,g,a,a,t,a,c,a,g,g,t,g,c,c,a,g,a,g,a,g,g,t,c,t,c,t,c,a,g,g,g,c,g,a,a,g,t,g,a,c,c,c,c,a,t,a,c,a,g,c,t,g,g,a,a,a,t,c,c,a,c,a,g,a,g,g,t,a,a,t,t,a,t,g,a,c,t,t,g,g,a,c,c,a,g,g,a,g,g,g,c,c,g,g,a,a,a,c,c,a,c,a,a,g,g,t,c,t,t,c,c,t,c,t,g,c,g,t,t,c,t,c,t,c,c,t,t,t,c,t,g,g,a,t,g,c,c,a,g,a,t,g,t,g,t,g,t,g,t,g,t,c,g,a,t,t,t,a,t,c,t,g,g,g,t,g,c,a,g,g,t,c,t,c,a,g,c,a,c,t,a,t,g,t,a,c,c,t,a,c,c,a,g,g,t,g,a,a,a,c,t,a,a,a,t,c,a,g,t,a,t,a,c,t,c,a,a,a,a,c,a,t,c,a,c,a,g,c,a,g,g,g,t,c,c,t,t,a,a,a,c,t,g,t,g,t,a,c,c,a,a,c,a,g,t,a,c,c,t,c,a,g,c,t,a,g,g,c,c,a,g,c,t,c,t,a,a,g,t,a,g,g,a,t,g,t,c,t,a,g,a,g,t,a,a,g,a,c,t,t,a,g,g,c,c,c,t,a,a,g,a,t,t,g,t,a,t,c,a,t,t,a,t,t,c,c,a,a,a,t,g,t,a,t,g,c,c,t,g,t,a,c,a,t,a,g,t,a,a,a,t,a,a,t,a,a,t,a,a,t,t,c,a,a,a,c,a,a,a,t,g,a,g,c,a,a,t,a,a,t,g,a,a,c,a,a,t,g,a,a,a,t,a,t,c,t,t,c,c,t,c,c,c,a,c,c,c,a,a,a,a,c,c,t,a,g,a,t,c,t,g,c,a,g,t,c,a,c,c,t,t,c,c,a,c,a,g,a,a,a,c,a,a,a,a,c,t,g,c,t,a,a,t,a,t,a,t,a,t,a,t,a,c,a,t,a,t,t,a,t,g,c,a,t,a,t,a,t,a,t,g,t,a,t,a,t,a,t,t,a,g,c,a,t,t,a,t,t,a,t,a,t,a,t,a,a,a,c,t,a,t,a,t,a,t,a,t,a,t,a,t,a,t,
a,t,a,t,a,c,a,c,a,c,a,t,a,t,a,t,a,t,a,g,t,t,t,t,a,a,a,g,c,t,g,t,g,g,g,t,g,g,t,a,g,a,a,c,a,c,t,t,t,c,t,a,a,g,t,a,t,t,g,t,c,c,t,a,t,a,t,c,t,t,a,c,t,t,t,t,a,t,c,a,c,t,t,a,a,a,a,t,a,c,c,t,t,a,a,a,g,t,t,c,t,g,t,t,t,a,t,a,t,t,a,a,t,a,g,a,a,a,t,c,c,a,c,t,t,t,a,a,a,a,t,g,t,c,t,g,c,t,g,c,a,c,a,g,c,t,g,t,a,c,c,a,g,a,a,t,t,a,a,t,t,t,a,a,c,c,a,t,t,c,t,g,c,c,t,a,t,t,a,g,c,a,a,a,t,t,t,a,t,a,a,g,a,t,g,t,t,t,c,c,a,c,t,c,t,t,t,t,g,a,t,t,t,t,a,c,a,a,g,c,a,t,t,g,c,t,g,c,a,a,t,a,a,t,t,a,t,c,t,t,t,a,t,a,c,a,t,a,c,a,t,t,c,c,g,g,g,g,g,c,a,c,a,t,t,t,c,a,t,a,g,g,g,t,a,t,c,t,g,t,a,a,g,a,t,a,a,t,a,t,t,c,t,g,g,a,c,a,t,g,g,a,a,t,t,a,t,t,g,t,c,a,t,a,t,t,t,t,a,a,t,a,a,a,t,g,g,a,a,g,c,a,g,a,a,a,a,g,c,c,c,a,c,c,a,c,c,c,a,c,t,t,a,a,a,c,c,t,g,t,a,a,g,g,a,g,t,t,t,c,t,a,t,t,c,a,t,c,a,a,g,a,g,a,t,g,g,a,g,a,c,t,g,c,a,a,t,a,t,t,c,t,t,c,a,g,g,g,a,a,a,a,a,t,g,c,t,t,c,a,t,t,c,a,a,t,a,t,g,c,a,a,g,a,c,a,a,a,a,t,a,a,c,c,a,a,a,t,g,t,a,t,t,a,t,t,t,a,g,t,t,a,t,t,c,a,g,a,a,g,t,g,a,t,g,a,g,t,t,t,a,a,a,c,t,t,c,g,t,t,a,a,a,a,a,t,g,a,t,a,a,t,g,c,a,a,a,a,g,t,c,a,a,t,c,c,a,c,a,c,t,g,g,a,g,g,c,a,a,a,a,t,t,g,c,c,t,t,t,a,t,g,c,a,g,a,c,a,t,g,g,t,t,g,c,t,g,t,t,a,g,a,g,g,a,a,a,t,g,t,g,t,t,t,t,a,g,c,c,a,a,g,g,a,a,a,t,g,t,t,g,a,g,a,a,t,g,t,c,t,g,a,g,g,g,a,a,g,g,c,t,t,g,a,t,g,t,t,c,c,t,c,a,t,g,t,g,t,c,c,c,t,t,a,g,g,t,c,t,c,t,g,t,a,a,a,t,a,a,g,t,t,c,t,t,a,g,g,a,t,g,g,a,g,a,g,g,t,t,a,g,g,g,a,a,g,c,t,g,a,c,a,g,a,g,c,t,g,t,t,t,c,g,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,a,g,a,c,a,g,a,g,t,c,t,c,a,c,t,c,c,g,t,t,g,c,c,c,a,g,g,c,t,g,g,a,a,t,g,c,a,g,t,g,g,t,g,t,g,a,t,c,t,t,g,g,c,t,c,a,c,t,g,c,a,a,c,c,t,c,t,g,a,c,a,g,a,g,c,t,g,t,t,t,c,a,a,c,a,a,g,a,t,a,c,t,t,t,g,g,g,t,a,a,t,t,c,a,a,g,c,a,g,a,a,g,t,g,t,t,t,c,a,t,g,g,t,t,c,a,a,g,t,g,a,c,a,a,c,a,a,a,a,g,g,a,c,t,a,g,g,g,c,t,g,g,g,a,a,g,a,g,t,c,c,a,t,t,t,t,c,t,t,t,a,c,c,t,c,t,a,c,a,c,a,g,a,c,t,c,t,a,g,g,a,c,a,c,t,c,a,g,c,a,t,c,a,g,t,g,a,c,t,t,a,c,t,g,a,g,a,a,t,c,a,t,a,t,c,t,t,t,t,t,t,a,t,a,t,t,a,c,a,t,t,t,t,a,a,t,g,t,g,a,a,t,t,t,t,c,a,t,t,g,a,a,a,t,a,t,a,a,c,t,t,a,t,g,t,a,c,a,a,c,a,a,g,c,c,a,t,a,a,a,t,g,t,a,t,g,c,c,a,c,a,g,t,a,a,a,t,t,t,t,t,t,c,a,a,a,g,t,a,a,a,c,a,g,c,a,t,c,c,a,g,a,t,c,t,a,t,t,t,t,a,g,a,c,a,t,t,t,c,c,a,g,c,a,c,c,t,c,a,g,a,a,a,c,t,c,c,t,t,c,t,t,g,c,c,c,a,t,t,t,c,t,a,g,t,c,c,a,c,c,c,c,t,g,a,c,a,c,t,g,a,c,t,t,c,c,a,g,c,a,c,c,a,t,a,g,g,t,t,t,t,t,t,g,c,c,t,a,t,t,t,t,t,g,a,a,c,t,t,c,a,t,a,t,a,a,a,g,g,g,c,t,a,c,g,g,t,a,t,g,g,g,a,c,a,g,g,a,t,g,t,a,c,t,c,t,t,t,t,g,t,g,t,c,t,g,g,t,t,t,a,t,t,t,t,t,c,t,c,a,a,c,a,t,t,a,t,g,a,t,t,g,t,g,a,a,c,t,g,t,a,t,a,c,a,t,g,t,t,g,t,a,a,a,t,t,g,a,a,g,t,t,c,a,t,t,t,g,t,t,c,t,t,a,t,t,a,c,t,g,t,a,t,a,t,t,t,c,a,t,a,t,t,t,t,c,c,c,a,t,t,c,t,g,c,t,g,a,g,g,g,g,c,t,c,g,g,g,t,t,g,c,t,t,c,t,g,g,t,t,t,t,g,a,c,c,a,c,t,t,a,c,a,a,a,t,a,g,t,a,a,t,g,c,t,g,t,g,g,a,t,a,t,t,t,t,t,g,t,t,t,a,c,a,t,g,t,t,t,c,a,a,a,t,a,t,t,t,t,c,t,a,c,c,a,t,t,a,c,t,a,a,t,g,t,t,t,g,a,c,a,g,t,a,t,c,t,g,a,t,g,g,a,g,g,t,a,t,g,t,t,a,c,a,a,t,t,t,c,c,c,a,c,t,c,t,t,t,t,g,g,a,t,a,t,a,c,a,a,a,t,g,c,a,a,a,t,t,a,a,g,c,a,t,t,t,c,c,c,t,a,a,t,g,a,c,t,a,t,g,a,t,a,t,t,g,a,c,c,a,t,t,t,t,t,c,a,c,g,t,t,t,a,t,t,a,c,c,t,a,t,t,t,g,g,g,t,a,t,c,c,t,t,t,t,t,t,g,t,a,a,g,g,t,c,t,t,t,t,t,g,a,t,a,a,t,t,t,t,t,c,t,a,t,t,g,t,c,t,g,t,c,t,t,t,t,t,c,t,t,a,c,t,g,a,c,t,t,a,c,a,g,g,a,g,t,t,a,t,t,t,a,t,a,t,a,t,t,c,t,g,g,a,t,a,t,a,a,g,t,c,c,t,t,t,t,t,c,a,a,g,t,g,t,c,t,t,a,a,a,t,a,t,c,t,t,c,t,c,c,c,a,c,t,c,t,g,t,g,g,c,t,t,t,t,c,t,t,t,t,c,a,c,t,a,t,a,a,t,a,t,t,a,a,a,g,t,t,t,t,g,t,t,t,g,t,t,t,t,c,a,a,t,g,a,a,c,a,a,g,a,c,t,t,g,t,t,a,a,t,t,t,t,a,c,t,a,c,a,g,t,a,c,a,a,t,a,c,a,c,c,a,a,c,a,t,t,t,t,t,g,g,t,t,g,g,t,g,c,c,g,t,c,t,a,t,g,c,c,c,t,a,t,t,t,t,a,a,a,a,t,g,t,t,t,t,g,c,c,a,c,a,g,t,c,a,g,c,c,a,t,g,g,g,g,a,a,t,t,c,a,a,t,t,g,c,a,g,c,t,c,a,c,t,g,a,c,t,c,t,t,a,g,t,c,a,t,t,t,c,a,a,t,t,t,a,a,t,c,a,g,t,a,t,a,t,g,c,t,a,a,g,a,c,c,a,a,g,a,a,a,a,t,g,c,a,g,c,t,g,g,t,t,g,g,t,g,g,a,c,c,c,g,a,g,c,c,c,t,a,a,t,c,a,t,a,t,g,g,c,t,g,a,c,a,c,c,a,a,a,g,t,c,a,t,g,a,a,g,g,t,a,g,g,g,g,a,a,t,g,a,t,t,g,t,t,g,a,g,t,a,g,g,a,a,a,t,t,a,g,t,a,a,t,g,t,c,t,g,c,t,a,a,a,a,g,c,t,g,c,a,t,c,t,c,g,t,g,a,g,t,t,t,t,g,a,t,a,t,a,t,a,a,t,a,c,t,a,c,c,a,t,t,a,c,c,a,t,t,t,a,a,g,t,t,t,a,a,a,a,a,c,t,c,a,t,a,a,a,t,t,t,c,c,a,t,t,a,
t,a,c,a,t,t,a,t,t,t,t,a,t,t,c,a,t,g,a,a,t,t,a,c,t,t,a,g,a,t,g,t,t,t,t,t,t,g,g,a,g,g,g,t,a,g,t,t,t,t,t,t,g,c,t,a,t,t,g,a,t,t,t,c,t,a,a,t,a,t,t,a,t,a,g,c,a,c,t,t,t,g,g,t,t,a,g,a,a,t,t,t,g,t,g,t,t,a,a,a,c,a,t,g,g,t,a,t,c,a,g,t,t,c,a,t,t,a,g,t,a,t,t,t,g,t,t,g,a,a,a,a,t,t,g,c,t,t,t,g,t,g,g,c,c,t,a,g,t,t,c,a,c,a,c,t,t,a,a,t,t,t,t,t,c,t,a,a,t,a,t,t,g,c,a,t,g,t,g,t,g,t,t,t,g,a,a,a,a,g,c,a,t,a,t,g,a,a,t,t,t,t,c,t,t,t,c,t,a,a,a,g,t,a,g,a,g,c,a,t,c,c,a,c,a,a,a,a,t,c,a,a,g,c,c,t,a,t,t,a,a,t,t,g,t,g,t,c,a,t,t,c,a,a,a,t,a,t,t,t,t,c,t,a,c,c,a,t,t,a,c,t,a,g,t,g,t,t,t,g,a,c,a,g,t,t,t,c,t,g,a,t,g,g,a,g,a,t,g,t,g,a,c,a,g,c,a,c,t,t,c,c,c,a,c,t,c,t,t,t,t,g,g,a,t,a,t,a,t,a,a,a,g,c,a,a,a,g,a,t,g,g,c,a,g,t,g,t,t,t,g,g,g,c,a,g,t,g,c,a,g,t,c,t,t,t,c,a,g,c,a,t,c,t,g,c,t,g,g,c,t,g,t,g,g,g,t,g,g,g,a,a,t,a,a,g,g,g,a,g,g,g,a,a,g,a,g,a,a,t,t,a,a,t,t,c,t,a,t,t,t,g,g,a,a,g,c,a,t,t,a,t,a,t,c,a,g,t,a,t,c,c,a,t,g,a,c,t,g,t,a,a,a,a,t,t,c,a,t,g,c,t,a,t,g,t,a,t,a,g,c,a,t,a,g,a,a,a,c,a,c,c,t,g,c,c,t,t,c,c,a,t,t,c,t,t,a,g,a,t,a,a,g,t,t,c,t,g,g,a,g,g,g,g,g,a,a,a,a,g,g,c,a,c,t,a,t,t,g,t,c,t,c,t,t,t,t,c,c,g,c,c,t,t,a,g,t,c,t,c,c,t,a,a,g,a,a,c,c,c,c,a,t,t,t,t,t,a,c,t,t,a,g,c,c,a,a,a,c,c,a,a,c,t,g,c,c,t,c,t,g,g,a,g,a,a,a,a,g,a,a,a,a,g,t,a,g,t,t,g,a,a,g,c,a,t,t,t,t,t,g,g,t,t,a,t,g,t,g,t,a,g,a,g,g,t,g,t,a,t,g,t,c,g,a,a,a,g,g,a,a,a,a,g,c,c,c,a,t,t,g,a,c,t,t,g,g,a,g,c,t,t,g,t,t,t,t,g,c,t,a,g,t,g,a,t,a,t,c,a,t,t,g,a,t,c,t,t,a,c,a,t,a,t,g,t,g,a,g,t,a,t,t,c,a,t,a,t,c,a,a,t,g,t,a,g,t,a,g,g,a,t,g,t,t,t,a,t,a,t,c,t,g,g,a,t,g,t,t,t,g,c,c,c,t,t,c,t,g,t,g,t,g,t,t,t,g,t,c,t,t,a,g,g,a,t,g,c,g,t,g,g,t,c,c,t,a,t,t,a,a,c,a,a,a,t,t,t,g,t,c,a,a,g,a,g,t,t,g,g,a,g,t,g,t,a,t,t,t,g,t,t,t,t,c,t,a,t,t,g,c,t,g,t,g,t,a,a,c,a,a,a,t,t,t,a,g,c,a,a,c,a,a,c,a,t,a,c,a,t,t,t,a,a,g,a,t,c,t,t,c,c,a,g,t,t,t,c,c,a,t,g,g,g,t,c,a,g,g,a,c,t,c,c,c,a,t,c,a,c,a,g,c,t,t,a,g,c,t,g,a,g,t,g,c,t,c,t,g,c,t,g,a,g,a,g,t,c,t,t,c,c,a,a,g,g,c,t,g,c,a,g,t,t,a,g,g,g,t,g,t,t,g,a,c,t,t,t,g,c,t,g,t,g,t,t,t,c,t,t,t,t,t,g,c,a,g,c,t,c,t,t,c,c,a,g,g,c,t,c,a,c,a,a,g,g,t,c,a,c,t,g,g,c,a,g,a,a,t,t,c,a,g,t,t,c,t,t,t,g,t,g,g,t,t,g,t,a,g,g,a,c,t,g,a,g,g,t,t,c,c,t,g,c,t,t,t,c,t,t,g,c,t,g,c,c,c,a,t,c,a,g,t,g,g,g,g,g,g,c,c,a,c,t,c,t,c,a,g,c,t,c,c,t,a,g,a,g,g,c,c,c,t,t,g,c,c,t,t,g,t,g,g,c,a,c,t,c,t,t,g,t,a,g,g,c,c,c,t,c,t,c,c,t,g,g,c,a,t,g,g,c,a,g,c,t,t,a,c,c,t,c,t,t,c,a,a,g,t,t,c,a,g,g,a,g,g,a,g,a,c,t,t,t,c,c,a,t,c,c,a,g,a,c,t,g,c,t,a,a,g,a,t,a,g,a,g,t,c,t,t,a,c,a,t,a,a,t,g,t,a,g,c,a,a,t,c,c,c,a,a,g,a,g,t,g,a,c,a,t,t,t,c,a,t,c,a,c,c,c,t,t,g,t,c,a,t,a,t,t,c,t,g,t,t,g,g,c,t,a,g,a,a,g,c,a,a,g,t,c,a,t,a,g,g,t,t,c,c,a,c,c,c,a,c,a,c,t,c,a,a,g,g,g,g,a,t,t,a,t,g,c,a,a,g,g,g,a,g,t,g,a,g,t,c,a,t,t,g,g,g,a,t,c,a,t,t,t,t,a,g,a,a,t,t,c,t,g,c,c,t,a,c,c,a,t,g,c,t,g,t,a,t,g,a,a,c,t,g,t,t,t,t,t,g,t,t,t,c,a,a,c,c,a,a,c,t,t,c,t,g,a,g,a,t,c,t,g,g,a,a,a,g,g,g,a,a,g,a,t,a,a,g,a,a,a,g,g,g,c,t,g,t,g,t,a,c,g,c,a,g,t,t,g,c,c,a,g,t,a,a,a,g,a,t,t,g,c,t,t,t,t,c,t,t,t,c,c,a,c,c,a,a,a,g,c,t,a,a,a,g,a,t,a,t,t,t,g,a,g,g,a,a,c,t,g,g,a,t,a,t,a,g,g,c,c,t,g,a,g,a,t,t,t,g,g,c,a,g,a,g,c,t,c,t,g,a,g,g,c,t,g,g,a,t,g,t,t,g,c,a,a,g,g,a,g,a,a,a,a,a,a,t,a,g,g,a,a,g,c,c,c,a,c,a,g,g,g,c,c,a,a,g,c,t,t,g,g,g,c,c,t,c,c,t,t,g,t,a,c,c,t,c,c,t,c,c,a,c,t,g,t,a,t,a,c,a,t,a,c,a,t,t,t,t,g,g,g,t,t,c,a,t,a,t,t,t,t,t,c,a,g,g,c,t,g,g,c,t,a,c,t,a,c,t,g,c,a,g,g,t,c,t,c,c,a,g,c,a,g,a,g,t,c,t,t,c,a,c,g,g,a,a,g,g,a,g,a,a,c,c,t,c,t,g,g,c,c,t,t,g,a,g,g,t,g,t,c,a,t,g,c,g,t,g,g,a,a,g,g,a,t,a,a,g,c,t,g,g,t,g,t,a,c,a,a,t,g,t,g,c,t,t,t,a,c,t,a,t,c,g,a,a,a,t,g,g,c,a,a,a,g,c,c,t,t,t,a,a,g,t,t,t,t,t,c,c,a,c,t,g,g,a,a,t,t,c,t,a,a,c,c,t,c,a,c,c,a,t,t,c,t,g,a,a,a,a,c,c,a,a,c,a,t,a,a,g,t,c,a,c,a,a,t,g,g,c,a,c,c,t,a,c,c,a,t,t,g,c,t,c,a,g,g,c,a,t,g,g,g,a,a,a,g,c,a,t,c,g,c,t,a,c,a,c,a,t,c,a,g,c,a,g,g,a,a,t,a,t,c,t,g,t,c,a,c,t,g,t,g,a,a,a,g]
model = ModelWraper()

# EXON
# Exon triplets states

st_exon_triplet0 = model.add_state(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='tri0')
st_exon_triplet1 = model.add_state(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='tri1')
st_exon_triplet2 = model.add_state(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='tri2')

st_exon_inter0 = model.add_state(DiscreteDistribution({'g': 1}), name='int0')
st_exon_inter1 = model.add_state(DiscreteDistribution({'g': 1}), name='int1')
st_exon_inter2 = model.add_state(DiscreteDistribution({'g': 1}), name='int2')

st_exon_last

# INTRON

# Intronic Distributions
d_intron_in0 = DiscreteDistribution({'g': 1})
d_intron_in1 = DiscreteDistribution({'t': 1})
d_intron_in2 = DiscreteDistribution({'a': 0.48258706467661694, 'c': 0.014925373134328358, 'g': 0.4975124378109453, 't': 0.004975124378109453})
d_intron_in3 = DiscreteDistribution({'a': 0.6567164179104478, 'c': 0.13930348258706468, 'g': 0.12437810945273632, 't': 0.07960199004975124})
d_intron_in4 = DiscreteDistribution({'a': 0.06467661691542288, 'c': 0.04975124378109453, 'g': 0.8059701492537313, 't': 0.07960199004975124})
d_intron_in5 = DiscreteDistribution({'a': 0.12437810945273632, 'c': 0.2537313432835821, 'g': 0.3034825870646766, 't': 0.31840796019900497})
d_intron_n = DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25})
d_intron_cl0 = DiscreteDistribution({'a': 0.029850746268656716, 'c': 0.42786069651741293, 'g': 0.10945273631840796, 't': 0.43283582089552236})
d_intron_cl1 = DiscreteDistribution({'a': 0.03980099502487562, 'c': 0.47761194029850745, 'g': 0.14427860696517414, 't': 0.3383084577114428})
d_intron_cl2 = DiscreteDistribution({'a': 0.11940298507462686, 'c': 0.4626865671641791, 'g': 0.07462686567164178, 't': 0.34328358208955223})
d_intron_cl3 = DiscreteDistribution({'a': 0.05472636815920398, 'c': 0.5174129353233831, 'g': 0.06965174129353234, 't': 0.3582089552238806})
d_intron_cl4 = DiscreteDistribution({'a': 0.06467661691542288, 'c': 0.4577114427860697, 'g': 0.04975124378109453, 't': 0.42786069651741293})
d_intron_cl5 = DiscreteDistribution({'a': 0.2835820895522388, 'c': 0.31343283582089554, 'g': 0.22388059701492538, 't': 0.1791044776119403})
d_intron_cl6 = DiscreteDistribution({'a': 0.024875621890547265, 'c': 0.8407960199004975, 't': 0.13432835820895522})
d_intron_cl7 = DiscreteDistribution({'a': 1})
d_intron_cl8 = DiscreteDistribution({'g': 1})

#Intron states type0

st_intron_0_in0 = model.add_state(d_intron_in0, name='i0_in0')
st_intron_0_in1 = model.add_state(d_intron_in1, name='i0_in1')
st_intron_0_in2 = model.add_state(d_intron_in2, name='i0_in2')
st_intron_0_in3 = model.add_state(d_intron_in3, name='i0_in3')
st_intron_0_in4 = model.add_state(d_intron_in4, name='i0_in4')
st_intron_0_in5 = model.add_state(d_intron_in5, name='i0_in5')
st_intron_0_n = model.add_state(d_intron_n, name='i0_n')
st_intron_0_cl0 = model.add_state(d_intron_cl0, name='i0_cl0')
st_intron_0_cl1 = model.add_state(d_intron_cl1, name='i0_cl1')
st_intron_0_cl2 = model.add_state(d_intron_cl2, name='i0_cl2')
st_intron_0_cl3 = model.add_state(d_intron_cl3, name='i0_cl3')
st_intron_0_cl4 = model.add_state(d_intron_cl4, name='i0_cl4')
st_intron_0_cl5 = model.add_state(d_intron_cl5, name='i0_cl5')
st_intron_0_cl6 = model.add_state(d_intron_cl6, name='i0_cl6')
st_intron_0_cl7 = model.add_state(d_intron_cl7, name='i0_cl7')
st_intron_0_cl8 = model.add_state(d_intron_cl8, name='i0_cl8')

#Intron states type1

st_intron_1_in0 = model.add_state(d_intron_in0, name='i1_in0')
st_intron_1_in1 = model.add_state(d_intron_in1, name='i1_in1')
st_intron_1_in2 = model.add_state(d_intron_in2, name='i1_in2')
st_intron_1_in3 = model.add_state(d_intron_in3, name='i1_in3')
st_intron_1_in4 = model.add_state(d_intron_in4, name='i1_in4')
st_intron_1_in5 = model.add_state(d_intron_in5, name='i1_in5')
st_intron_1_n = model.add_state(d_intron_n, name='i1_n')
st_intron_1_cl0 = model.add_state(d_intron_cl0, name='i1_cl0')
st_intron_1_cl1 = model.add_state(d_intron_cl1, name='i1_cl1')
st_intron_1_cl2 = model.add_state(d_intron_cl2, name='i1_cl2')
st_intron_1_cl3 = model.add_state(d_intron_cl3, name='i1_cl3')
st_intron_1_cl4 = model.add_state(d_intron_cl4, name='i1_cl4')
st_intron_1_cl5 = model.add_state(d_intron_cl5, name='i1_cl5')
st_intron_1_cl6 = model.add_state(d_intron_cl6, name='i1_cl6')
st_intron_1_cl7 = model.add_state(d_intron_cl7, name='i1_cl7')
st_intron_1_cl8 = model.add_state(d_intron_cl8, name='i1_cl8')

#Intron states type2

st_intron_2_in0 = model.add_state(d_intron_in0, name='i2_in0')
st_intron_2_in1 = model.add_state(d_intron_in1, name='i2_in1')
st_intron_2_in2 = model.add_state(d_intron_in2, name='i2_in2')
st_intron_2_in3 = model.add_state(d_intron_in3, name='i2_in3')
st_intron_2_in4 = model.add_state(d_intron_in4, name='i2_in4')
st_intron_2_in5 = model.add_state(d_intron_in5, name='i2_in5')
st_intron_2_n = model.add_state(d_intron_n, name='i2_n')
st_intron_2_cl0 = model.add_state(d_intron_cl0, name='i2_cl0')
st_intron_2_cl1 = model.add_state(d_intron_cl1, name='i2_cl1')
st_intron_2_cl2 = model.add_state(d_intron_cl2, name='i2_cl2')
st_intron_2_cl3 = model.add_state(d_intron_cl3, name='i2_cl3')
st_intron_2_cl4 = model.add_state(d_intron_cl4, name='i2_cl4')
st_intron_2_cl5 = model.add_state(d_intron_cl5, name='i2_cl5')
st_intron_2_cl6 = model.add_state(d_intron_cl6, name='i2_cl6')
st_intron_2_cl7 = model.add_state(d_intron_cl7, name='i2_cl7')
st_intron_2_cl8 = model.add_state(d_intron_cl8, name='i2_cl8')

add_trans = model.add_transition

add_trans([model.model.start], [(st_exon_triplet0, 1)])

add_trans([st_exon_triplet0],
          [(st_exon_triplet1, 0.9), (st_intron_0_in0, 0.1)])
add_trans([st_exon_triplet1],
          [(st_exon_triplet2, 0.9), (st_intron_1_in0, 0.1)])
add_trans([st_exon_triplet2],
          [(st_exon_triplet0, 0.8), (st_intron_2_in0, 0.1), (model.model.end, 0.1)])

add_trans([st_exon_inter0], [(st_exon_triplet1, 1)])
add_trans([st_exon_inter1], [(st_exon_triplet2, 1)])
add_trans([st_exon_inter2], [(st_exon_triplet0, 1)])


add_trans([st_intron_0_in0], [(st_intron_0_in1, 1)])
add_trans([st_intron_0_in1], [(st_intron_0_in2, 1)])
add_trans([st_intron_0_in2], [(st_intron_0_in3, 1)])
add_trans([st_intron_0_in3], [(st_intron_0_in4, 1)])
add_trans([st_intron_0_in4], [(st_intron_0_in5, 1)])
add_trans([st_intron_0_in5], [(st_intron_0_n, 1)])
add_trans([st_intron_0_n], [(st_intron_0_n, 0.9), (st_intron_0_cl0, 0.1)])
add_trans([st_intron_0_cl0], [(st_intron_0_cl1, 1)])
add_trans([st_intron_0_cl1], [(st_intron_0_cl2, 1)])
add_trans([st_intron_0_cl2], [(st_intron_0_cl3, 1)])
add_trans([st_intron_0_cl3], [(st_intron_0_cl4, 1)])
add_trans([st_intron_0_cl4], [(st_intron_0_cl5, 1)])
add_trans([st_intron_0_cl5], [(st_intron_0_cl6, 1)])
add_trans([st_intron_0_cl6], [(st_intron_0_cl7, 1)])
add_trans([st_intron_0_cl7], [(st_intron_0_cl8, 1)])
add_trans([st_intron_0_cl8], [(st_exon_inter1, 1)])


add_trans([st_intron_1_in0], [(st_intron_1_in1, 1)])
add_trans([st_intron_1_in1], [(st_intron_1_in2, 1)])
add_trans([st_intron_1_in2], [(st_intron_1_in3, 1)])
add_trans([st_intron_1_in3], [(st_intron_1_in4, 1)])
add_trans([st_intron_1_in4], [(st_intron_1_in5, 1)])
add_trans([st_intron_1_in5], [(st_intron_1_n, 1)])
add_trans([st_intron_1_n], [(st_intron_1_n, 0.9), (st_intron_1_cl0, 0.1)])
add_trans([st_intron_1_cl0], [(st_intron_1_cl1, 1)])
add_trans([st_intron_1_cl1], [(st_intron_1_cl2, 1)])
add_trans([st_intron_1_cl2], [(st_intron_1_cl3, 1)])
add_trans([st_intron_1_cl3], [(st_intron_1_cl4, 1)])
add_trans([st_intron_1_cl4], [(st_intron_1_cl5, 1)])
add_trans([st_intron_1_cl5], [(st_intron_1_cl6, 1)])
add_trans([st_intron_1_cl6], [(st_intron_1_cl7, 1)])
add_trans([st_intron_1_cl7], [(st_intron_1_cl8, 1)])
add_trans([st_intron_1_cl8], [(st_exon_inter2, 1)])


add_trans([st_intron_2_in0], [(st_intron_2_in1, 1)])
add_trans([st_intron_2_in1], [(st_intron_2_in2, 1)])
add_trans([st_intron_2_in2], [(st_intron_2_in3, 1)])
add_trans([st_intron_2_in3], [(st_intron_2_in4, 1)])
add_trans([st_intron_2_in4], [(st_intron_2_in5, 1)])
add_trans([st_intron_2_in5], [(st_intron_2_n, 1)])
add_trans([st_intron_2_n], [(st_intron_2_n, 0.9), (st_intron_2_cl0, 0.1)])
add_trans([st_intron_2_cl0], [(st_intron_2_cl1, 1)])
add_trans([st_intron_2_cl1], [(st_intron_2_cl2, 1)])
add_trans([st_intron_2_cl2], [(st_intron_2_cl3, 1)])
add_trans([st_intron_2_cl3], [(st_intron_2_cl4, 1)])
add_trans([st_intron_2_cl4], [(st_intron_2_cl5, 1)])
add_trans([st_intron_2_cl5], [(st_intron_2_cl6, 1)])
add_trans([st_intron_2_cl6], [(st_intron_2_cl7, 1)])
add_trans([st_intron_2_cl7], [(st_intron_2_cl8, 1)])
add_trans([st_intron_2_cl8], [(st_exon_inter0, 1)])

model.bake()

seq = numpy.array(data)
logp, path = model.viterbi(seq)

print("sequence: {}".format(''.join(seq)))
names = []
c = 0
in_exon = True
exons = 1
introns = 0

for p in path:
    if c > 0 and c - 1 < len(data):
        if '_' not in p[1].name and not in_exon:
            in_exon = True
            exons = exons + 1
        if '_' in p[1].name and in_exon:
            in_exon = False
            introns = introns + 1
        names.append((p[1].name,     data[c-1]))
    c = c + 1
print("hmm pred: {}".format(' '.join(map( str, names))))

print('exons', exons)
print('introns', introns)