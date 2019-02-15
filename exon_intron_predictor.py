import numpy
from pomegranate import DiscreteDistribution
from pomegranate import HiddenMarkovModel
from pomegranate import State
from helpers import with_variations, transition_maker

a = 'a'
c = 'c'
g = 'g'
t = 't'
p = 'p'

# Replace this sequence to make predictions
data = [g,c,t,g,g,c,t,a,c,t,a,c,t,g,c,a,g,g,t,c,t,c,c,a,g,c,a,g,a,g,t,c,t,t,c,a,c,g,g,a,a,g,g,a,g,a,a,c,c,t,c,t,g,g,c,c,t,t,g,a,g,g,t,g,t,c,a,t,g,c,g,t,g,g,a,a,g,g,a,t,a,a,g,c,t,g,g,t,g,t,a,c,a,a,t,g,t,g,c,t,t,t,a,c,t,a,t,c,g,a,a,a,t,g,g,c,a,a,a,g,c,c,t,t,t,a,a,g,t,t,t,t,t,c,c,a,c,t,g,g,a,a,t,t,c,t,a,a,c,c,t,c,a,c,c,a,t,t,c,t,g,a,a,a,a,c,c,a,a,c,a,t,a,a,g,t,c,a,c,a,a,t,g,g,c,a,c,c,t,a,c,c,a,t,t,g,c,t,c,a,g,g,c,a,t,g,g,g,a,a,a,g,c,a,t,c,g,c,t,a,c,a,c,a,t,c,a,g,c,a,g,g,a,a,t,a,t,c,t,g,t,c,a,c,t,g,t,g,a,a,a,g,g,t,a,t,t,g,t,a,t,t,g,g,a,a,t,a,g,t,c,a,t,a,g,a,a,c,t,g,a,t,a,g,t,c,c,c,t,c,c,c,c,c,t,g,a,g,g,g,a,c,c,a,t,c,a,t,a,a,a,t,a,t,t,c,t,a,a,a,c,t,c,c,t,c,a,c,t,t,t,a,a,t,t,t,a,c,a,a,g,t,g,a,a,g,a,a,a,c,c,g,g,g,c,t,c,c,a,g,a,g,a,g,g,t,a,a,a,c,t,g,c,a,t,t,a,c,t,a,a,a,g,g,c,c,a,c,a,c,c,a,t,g,a,c,c,a,g,t,a,g,c,t,g,g,a,a,c,c,a,g,a,a,c,t,g,a,g,g,t,c,t,c,t,g,g,g,t,c,c,t,a,g,t,c,c,a,a,t,a,c,t,c,t,t,t,c,c,a,g,t,g,t,a,c,c,g,c,a,a,c,c,c,c,c,a,t,c,a,a,c,a,a,t,c,a,c,a,g,g,a,g,c,t,a,a,t,g,t,c,a,a,t,g,t,c,a,g,g,g,c,a,t,a,a,t,g,g,t,g,a,t,c,c,a,t,t,t,c,a,t,c,c,a,t,c,a,t,t,a,t,t,t,t,a,g,t,t,g,t,a,a,a,g,a,a,t,a,c,a,g,a,c,t,c,a,c,t,c,t,a,g,g,t,a,g,a,t,a,g,g,a,g,a,g,t,t,a,g,a,a,a,a,t,a,a,t,a,c,c,a,t,g,g,a,a,t,c,t,c,a,t,g,g,a,a,g,c,c,c,c,a,t,a,g,a,a,a,g,a,g,a,a,a,c,c,t,g,g,a,a,a,a,t,a,t,g,a,a,g,a,a,c,g,g,g,c,t,a,t,a,c,t,g,t,c,c,a,t,c,t,a,c,c,t,c,t,c,a,g,g,g,a,c,a,a,a,g,c,a,g,c,c,t,c,t,g,t,g,g,t,g,c,c,a,c,t,t,c,t,t,c,c,t,g,a,g,c,a,t,c,t,g,c,a,g,g,c,t,a,a,g,c,a,g,t,t,t,g,c,a,t,a,t,g,g,c,c,t,t,g,t,t,c,t,g,a,c,c,c,t,t,t,c,a,c,g,g,c,c,t,t,t,c,c,t,c,t,t,a,a,t,a,c,a,a,t,c,a,c,t,a,g,c,a,a,c,c,t,t,t,c,t,c,t,g,t,c,t,g,a,g,a,a,a,a,a,a,a,a,a,a,g,t,t,c,a,c,t,c,c,t,g,t,g,g,g,a,a,a,g,a,a,a,t,t,a,t,t,g,t,c,c,c,a,g,a,t,t,a,t,c,t,t,t,t,a,a,a,g,t,c,a,g,g,a,a,c,a,a,a,a,a,t,a,a,t,g,a,g,t,c,a,c,t,g,a,a,a,t,g,t,g,g,c,g,g,g,c,a,c,c,t,g,t,a,g,t,c,c,c,a,g,c,t,a,c,t,c,g,g,g,a,g,g,c,t,g,a,g,g,c,a,g,g,a,g,a,a,t,a,g,c,a,t,g,a,a,c,c,c,g,g,g,a,a,g,c,g,g,a,g,c,t,t,g,c,a,g,t,g,a,g,c,t,g,a,g,a,t,a,g,c,g,c,c,a,c,t,g,c,a,c,t,c,c,a,g,c,c,t,g,g,g,c,a,a,c,a,g,a,g,c,g,a,g,a,c,t,a,c,g,t,c,t,c,a,a,a,t,a,a,t,a,a,t,a,a,t,a,a,t,a,a,t,a,a,t,a,a,t,a,a,t,g,a,t,g,a,t,a,a,t,a,a,a,g,t,c,a,c,t,g,a,a,a,t,g,g,c,a,a,g,t,g,t,g,t,g,a,g,t,c,a,g,g,g,t,t,c,a,c,t,c,c,t,a,g,t,t,g,a,c,c,a,c,t,g,c,c,a,a,a,a,g,g,g,c,a,t,g,g,t,t,a,c,t,g,a,c,c,a,g,a,t,g,a,c,a,c,g,g,t,c,a,t,t,c,a,g,g,g,a,a,g,g,a,t,g,g,a,c,c,t,t,g,t,a,g,a,g,c,a,g,g,g,g,t,t,c,c,c,a,a,c,c,c,t,t,a,c,t,g,g,t,c,c,g,t,g,g,c,c,t,g,t,t,a,g,g,a,a,c,t,g,g,g,c,t,g,c,a,c,a,g,c,a,g,g,a,g,g,t,g,a,g,c,t,t,c,t,t,c,a,t,g,a,g,c,c,a,g,c,a,t,t,a,c,g,g,c,c,t,g,a,g,c,t,c,c,t,c,c,t,c,c,t,g,t,c,c,a,a,t,c,a,g,t,g,g,c,a,a,c,a,t,t,a,g,a,t,t,c,t,c,a,c,a,g,a,a,a,c,a,t,g,a,a,c,c,c,t,a,t,t,g,t,g,a,a,t,t,g,t,g,c,g,t,g,c,c,t,g,a,t,g,a,t,c,t,g,a,g,g,t,g,g,a,a,c,a,g,t,t,a,c,c,t,t,c,c,a,a,a,a,c,t,g,t,c,c,c,c,a,c,t,t,c,a,c,c,c,c,c,c,g,g,c,t,g,t,g,g,a,a,a,a,g,t,t,g,c,c,t,t,c,c,a,c,a,a,a,a,t,c,c,a,t,c,c,c,t,a,g,t,g,c,c,a,a,a,a,a,g,g,t,t,g,g,g,g,a,c,c,a,c,t,g,g,t,a,t,a,g,a,g,g,t,a,t,c,c,t,c,a,g,t,a,g,g,a,c,t,c,a,g,c,a,a,g,c,t,g,g,c,a,a,c,c,c,t,a,a,t,t,a,t,g,t,c,t,a,t,t,a,g,g,a,c,a,c,c,c,c,a,a,g,a,a,t,g,g,c,t,c,t,c,t,g,c,t,g,g,a,a,g,t,a,a,a,a,a,g,g,g,t,t,a,a,t,g,c,c,t,t,a,t,g,g,a,t,g,c,a,t,t,t,t,c,t,a,g,g,g,c,c,a,g,g,t,t,t,c,c,c,a,a,g,g,g,g,g,t,a,a,a,g,g,g,c,a,t,g,t,c,t,t,t,t,g,t,g,a,a,a,a,g,g,a,c,c,t,g,g,a,t,g,c,t,a,a,a,c,a,g,g,c,a,a,c,c,t,t,g,t,c,c,c,c,c,a,t,c,a,a,c,t,t,t,c,t,c,c,t,t,a,g,a,g,c,t,a,t,t,t,c,c,a,g,c,t,c,c,a,g,t,g,c,t,g,a,a,t,g,c,a,t,c,t,g,t,g,a,c,a,t,c,c,c,c,a,c,t,c,c,t,g,g,a,g,g,g,g,a,a,t,c,t,g,g,t,c,a,c,c,c,t,g,a,g,c,t,g,t,g,a,a,a,c,a,a,a,g,t,t,g,c,t,c,t,t,g,c,a,g,a,g,g,c,c,t,g,g,t,t,t,g,c,a,g,c,t,t,t,a,c,t,t,c,t,c,c,t,t,c,t,a,c,a,t,g,g,g,c,a,g,c,a,a,g,a,c,c,c,t,g,c,g,a,g,g,c,a,g,g,a,a,c,a,c,a,t,c,c,t,c,t,g,a,a,t,a,c,c,a,a,a,t,a,c,t,a,a,c,t,g,c,t,a,g,a,a,g,a,g,a,a,g,a,c,t,c,t,g,g,g,t,t,a,t,a,c,t,g,g,t,g,c,g,a,g,g,c,t,g,c,c,a,c,a,g,a,g,g,a,t,g,g,a,a,a,t,g,t,c,c,t,t,a,a,g,c,g,c,a,g,c,c,c,t,g,a,g,t,t,g,g,a,g,c,t,t,c,a,a,g,t,g,c,t,t,g]
numpy.random.seed(0)
numpy.set_printoptions(suppress=True)
random_distribution = DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25})

states = []

st_back = State(random_distribution, name='back')
#states.append(st_back)

st_start_triplet0 = State(DiscreteDistribution({'a': 1}), name='start_tri0')
#states.append(st_start_triplet0)

st_start_triplet1 = State(DiscreteDistribution({'t': 1}), name='start_tri1')
#states.append(st_start_triplet1)

st_start_triplet2 = State(DiscreteDistribution({'g': 1}), name='start_tri2')
#states.append(st_start_triplet2)

st_exon_triplet0 = State(random_distribution, name='exon_tri0')
states.append(st_exon_triplet0)

st_exon_triplet1 = State(random_distribution, name='exon_tri1')
states.append(st_exon_triplet1)

st_exon_triplet2 = State(random_distribution, name='exon_tri2')
states.append(st_exon_triplet2)


st_intron_g0 = State(DiscreteDistribution({'g': 1}), name='intron_g0')
states.append(st_intron_g0)

st_intron_t0 = State(DiscreteDistribution({'t': 1}), name='intron_t0')
states.append(st_intron_t0)

st_intron_a0 = State(DiscreteDistribution({'a': 0.6, 'g': 0.4}), name='ia0')
states.append(st_intron_a0)

st_intron_a20 = State(DiscreteDistribution({'a': 0.9, 't': 0.1}), name='ia20')
states.append(st_intron_a20)

st_intron_g20 = State(DiscreteDistribution({'g': 1}), name='ig20')
states.append(st_intron_g20)

st_intron_t20 = State(DiscreteDistribution({'t': 1}), name='it20')
states.append(st_intron_t20)

st_intron_0 = State(random_distribution, name='intron_0')
states.append(st_intron_0)

st_intron_0c = State(DiscreteDistribution({'c': 0.5, 't': 0.5}), name='intron0c')
states.append(st_intron_0c)

st_intron_0a = State(DiscreteDistribution({'a': 1}), name='intron0a')
states.append(st_intron_0a)

st_intron_0g = State(DiscreteDistribution({'g': 1}), name='intron0g')
states.append(st_intron_0g)


st_intron_g1 = State(DiscreteDistribution({'g': 1}), name='intron_g1')
states.append(st_intron_g1)

st_intron_t1 = State(DiscreteDistribution({'t': 1}), name='intron_t1')
states.append(st_intron_t1)


st_intron_a1 = State(DiscreteDistribution({'a': 0.6, 'g': 0.4}), name='ia1')
states.append(st_intron_a1)

st_intron_a21 = State(DiscreteDistribution({'a': 0.9, 't': 0.1}), name='ia21')
states.append(st_intron_a21)

st_intron_g21 = State(DiscreteDistribution({'g': 1}), name='ig21')
states.append(st_intron_g21)

st_intron_t21 = State(DiscreteDistribution({'t': 1}), name='it21')
states.append(st_intron_t21)



st_intron_1 = State(random_distribution, name='intron_1')
states.append(st_intron_1)

st_intron_1c = State(DiscreteDistribution({'c': 0.5, 't': 0.5}), name='intron1c')
states.append(st_intron_1c)

st_intron_1a = State(DiscreteDistribution({'a': 1}), name='intron1a')
states.append(st_intron_1a)

st_intron_1g = State(DiscreteDistribution({'g': 1}), name='intron1g')
states.append(st_intron_1g)

st_intron_g2 = State(DiscreteDistribution({'g': 1}), name='intron_g2')
states.append(st_intron_g2)

st_intron_t2 = State(DiscreteDistribution({'t': 1}), name='intron_t2')
states.append(st_intron_t2)


st_intron_a2 = State(DiscreteDistribution({'a': 0.6, 'g': 0.4}), name='ia2')
states.append(st_intron_a2)

st_intron_a22 = State(DiscreteDistribution({'a': 0.9, 't': 0.1}), name='ia22')
states.append(st_intron_a22)

st_intron_g22 = State(DiscreteDistribution({'g': 1}), name='ig22')
states.append(st_intron_g22)

st_intron_t22 = State(DiscreteDistribution({'t': 1}), name='it22')
states.append(st_intron_t22)



st_intron_2 = State(random_distribution, name='intron_2')
states.append(st_intron_2)

st_intron_2c = State(DiscreteDistribution({'c': 0.5, 't': 0.5}), name='intron2c')
states.append(st_intron_2c)

st_intron_2a = State(DiscreteDistribution({'a': 1}), name='intron2a')
states.append(st_intron_2a)

st_intron_2g = State(DiscreteDistribution({'g': 1}), name='intron2g')
states.append(st_intron_2g)

model = HiddenMarkovModel()
model.add_states(states)

#transition_maker(model,
#                 [st_back],
#                 [(st_back, 0.9), (st_start_triplet0, 0.1)])

#transition_maker(model,
#                 [st_start_triplet0],
#                 [(st_start_triplet1, 1)])

#transition_maker(model,
#                 [st_start_triplet1],
#                 [(st_start_triplet2, 1)])

#transition_maker(model,
#                 [st_start_triplet2],
#                 [(st_exon_triplet0, 1)])

transition_maker(model,
                 [model.start],
                 [(st_exon_triplet0, 1)])

transition_maker(model,
                 [st_exon_triplet0],
                 [(st_exon_triplet1, 0.9), (st_intron_g0, 0.1)])

transition_maker(model,
                 [st_exon_triplet1],
                 [(st_exon_triplet2, 0.9), (st_intron_g1, 0.1)])

transition_maker(model,
                 [st_exon_triplet2],
                 [(st_exon_triplet0, 0.8), (st_intron_g2, 0.1), (model.end, 0.1)])

transition_maker(model,
                 [st_intron_g0],
                 [(st_intron_t0, 1)])
transition_maker(model,
                 [st_intron_t0],
                 [(st_intron_a0, 1)])
transition_maker(model,
                 [st_intron_a0],
                 [(st_intron_a20, 1)])
transition_maker(model,
                 [st_intron_a20],
                 [(st_intron_g20, 1)])
transition_maker(model,
                 [st_intron_g20],
                 [(st_intron_t20, 1)])
transition_maker(model,
                 [st_intron_t20],
                 [(st_intron_0, 1)])
transition_maker(model,
                 [st_intron_0],
                 [(st_intron_0, 0.9), (st_intron_0c, 0.1)])
transition_maker(model,
                 [st_intron_0c],
                 [(st_intron_0a, 1)])
transition_maker(model,
                 [st_intron_0a],
                 [(st_intron_0g, 1)])
transition_maker(model,
                 [st_intron_0g],
                 [(st_exon_triplet1, 1)])

transition_maker(model,
                 [st_intron_g1],
                 [(st_intron_t1, 1)])
transition_maker(model,
                 [st_intron_t1],
                 [(st_intron_a1, 1)])

transition_maker(model,
                 [st_intron_a1],
                 [(st_intron_a21, 1)])
transition_maker(model,
                 [st_intron_a21],
                 [(st_intron_g21, 1)])
transition_maker(model,
                 [st_intron_g21],
                 [(st_intron_t21, 1)])
transition_maker(model,
                 [st_intron_t21],
                 [(st_intron_1, 1)])

transition_maker(model,
                 [st_intron_1],
                 [(st_intron_1, 0.9), (st_intron_1c, 0.1)])
transition_maker(model,
                 [st_intron_1c],
                 [(st_intron_1a, 1)])
transition_maker(model,
                 [st_intron_1a],
                 [(st_intron_1g, 1)])
transition_maker(model,
                 [st_intron_1g],
                 [(st_exon_triplet2, 1)])

transition_maker(model,
                 [st_intron_g2],
                 [(st_intron_t2, 1)])
transition_maker(model,
                 [st_intron_t2],
                 [(st_intron_a2, 1)])

transition_maker(model,
                 [st_intron_a2],
                 [(st_intron_a22, 1)])
transition_maker(model,
                 [st_intron_a22],
                 [(st_intron_g22, 1)])
transition_maker(model,
                 [st_intron_g22],
                 [(st_intron_t22, 1)])
transition_maker(model,
                 [st_intron_t22],
                 [(st_intron_2, 1)])

transition_maker(model,
                 [st_intron_2],
                 [(st_intron_2, 0.9), (st_intron_2c, 0.1)])
transition_maker(model,
                 [st_intron_2c],
                 [(st_intron_2a, 1)])
transition_maker(model,
                 [st_intron_2a],
                 [(st_intron_2g, 1)])
transition_maker(model,
                 [st_intron_2g],
                 [(st_exon_triplet0, 1)])

seq = numpy.array(data)
model.bake()


# seq = numpy.array(list('acgtacgacgtactgaggcgcc'))

logp, path = model.viterbi(seq)


print("sequence: {}".format(''.join(seq)))
names = []
c = 0
for p in path:
    if c > 0 and c - 1 < len(data):
        names.append((p[1].name,     data[c-1]))
    c = c + 1
print("hmm pred: {}".format(' '.join(map( str, names))))

