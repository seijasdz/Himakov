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
data = [a,c,a,g,c,c,a,g,c,g,c,g,g,g,a,t,t,t,t,c,a,a,t,t,a,t,t,g,t,t,c,c,g,c,c,c,a,a,t,c,g,g,g,a,a,a,a,g,a,c,t,g,t,g,c,t,t,a,t,a,a,a,g,a,c,g,g,c,t,g,c,g,g,c,g,g,g,g,c,t,a,g,g,a,g,c,t,c,g,t,t,t,t,t,c,t,c,c,c,c,g,c,c,g]

numpy.random.seed(0)
numpy.set_printoptions(suppress=True)

st_bak2 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='bk2')
st_bak1 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='bk1')
st_bak3 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='bk3')


d_bre1 = DiscreteDistribution({'g': 0.5, 'c': 0.5})
st_bre1 = State(d_bre1, name='bre1')
st_i_bre1 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_bre1')
st_d_bre1 = State(None, name='d_bre1')

d_bre2 = DiscreteDistribution({'g': 0.5, 'c': 0.5})
st_bre2 = State(d_bre2, name='bre2')
st_i_bre2 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_bre2')
st_d_bre2 = State(None, name='d_bre2')

d_bre3 = DiscreteDistribution({'g': 0.5, 'a': 0.5})
st_bre3 = State(d_bre3, name='bre3')
st_i_bre3 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_bre3')
st_d_bre3 = State(None, name='d_bre3')

d_bre4 = DiscreteDistribution({'c': 1})
st_bre4 = State(d_bre4, name='bre4')
st_i_bre4 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_bre4')
st_d_bre4 = State(None, name='d_bre4')

d_bre5 = DiscreteDistribution({'g': 1})
st_bre5 = State(d_bre5, name='bre5')
st_i_bre5 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_bre5')
st_d_bre5 = State(None, name='d_bre5')

d_bre6 = DiscreteDistribution({'c': 1})
st_bre6 = State(d_bre6, name='bre6')
st_i_bre6 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_bre6')
st_d_bre6 = State(None, name='d_bre6')

d_bre7 = DiscreteDistribution({'c': 1})
st_bre7 = State(d_bre7, name='bre7')
st_i_bre7 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_bre7')
st_d_bre7 = State(None, name='d_bre7')

d_tat1 = DiscreteDistribution({'t': 1})
st_tat1 = State(d_tat1, name='tat1')
st_i_tat1 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_tat1')
st_d_tat1 = State(None, name='d_tat1')

d_tat2 = DiscreteDistribution({'a': 1})
st_tat2 = State(d_tat2, name='tat2')
st_i_tat2 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_tat2')
st_d_tat2 = State(None, name='d_tat2')

d_tat3 = DiscreteDistribution({'t': 1})
st_tat3 = State(d_tat3, name='tat3')
st_i_tat3 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_tat3')
st_d_tat3 = State(None, name='d_tat3')

d_tat4 = DiscreteDistribution({'a': 1})
st_tat4 = State(d_tat4, name='tat4')
st_i_tat4 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_tat4')
st_d_tat4 = State(None, name='d_tat4')

d_tat5 = DiscreteDistribution({'a': 1})
st_tat5 = State(d_tat5, name='tat5')
st_i_tat5 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_tat5')
st_d_tat5 = State(None, name='d_tat5')

d_tat6 = DiscreteDistribution({'a': 1})
st_tat6 = State(d_tat6, name='tat6')
st_i_tat6 = State(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), name='i_tat6')
st_d_tat6 = State(None, name='d_tat6')




st_inr1, st_i_inr1, st_d_inr1 = with_variations(DiscreteDistribution({'c': 0.5, 't': 0.5}), 'inr1')
st_inr2, st_i_inr2, st_d_inr2 = with_variations(DiscreteDistribution({'c': 0.5, 't': 0.5}), 'inr2')
st_inr3, st_i_inr3, st_d_inr3 = with_variations(DiscreteDistribution({'a': 1}), 'inr3')
st_inr4, st_i_inr4, st_d_inr4 = with_variations(DiscreteDistribution({'c': 0.5, 't': 0.5}), 'inr4')
st_inr5, st_i_inr5, st_d_inr5 = with_variations(DiscreteDistribution({'a': 0.25, 'c': 0.25, 'g': 0.25, 't': 0.25}), 'inr5')
st_inr6, st_i_inr6, st_d_inr6 = with_variations(DiscreteDistribution({'c': 0.5, 't': 0.5}), 'inr6')
st_inr7, st_i_inr7, st_d_inr7 = with_variations(DiscreteDistribution({'c': 0.5, 't': 0.5}), 'inr7')

model = HiddenMarkovModel()
model.add_states([st_bak1,
                  st_bak2,
                  st_bak3,
                  st_bre1, st_d_bre1, st_i_bre1,
                  st_bre2, st_d_bre2, st_i_bre2,
                  st_bre3, st_d_bre3, st_i_bre3,
                  st_bre4, st_d_bre4, st_i_bre4,
                  st_bre5, st_d_bre5, st_i_bre5,
                  st_bre6, st_d_bre6, st_i_bre6,
                  st_bre7, st_d_bre7, st_i_bre7,
                  st_inr1, st_d_inr1, st_i_inr1,
                  st_inr2, st_d_inr2, st_i_inr2,
                  st_inr3, st_d_inr3,  # st_i_inr3,
                  st_inr4, st_d_inr4, st_i_inr4,
                  st_inr5, st_d_inr5, st_i_inr5,
                  st_inr6, st_d_inr6, st_i_inr6,
                  st_inr7, st_d_inr7, st_i_inr7,
                  ])

model.add_transition(model.start, st_bak1, 0.9)

model.add_transition(st_bak1, st_bak1, 0.8)
model.add_transition(st_bak1, st_bre1, 0.06)
model.add_transition(st_bak1, st_d_bre1, 0.01)
model.add_transition(st_bak1, st_tat1, 0.05)
model.add_transition(st_bak1, st_d_tat1, 0.01)
model.add_transition(st_bak1, st_inr1, 0.06)
model.add_transition(st_bak1, st_d_inr1, 0.01)

model.add_transition(st_bre1, st_i_bre1, 0.10)
model.add_transition(st_bre1, st_bre2, 0.80)
model.add_transition(st_bre1, st_d_bre2, 0.10)
model.add_transition(st_i_bre1, st_i_bre1, 0.10)
model.add_transition(st_i_bre1, st_bre2, 0.8)
model.add_transition(st_i_bre1, st_d_bre2, 0.10)
model.add_transition(st_d_bre1, st_i_bre1, 0.10)
model.add_transition(st_d_bre1, st_bre2, 0.8)
model.add_transition(st_d_bre1, st_d_bre2, 0.10)

model.add_transition(st_bre2, st_i_bre2, 0.10)
model.add_transition(st_bre2, st_bre3, 0.8)
model.add_transition(st_bre2, st_d_bre3, 0.10)
model.add_transition(st_i_bre2, st_i_bre2, 0.10)
model.add_transition(st_i_bre2, st_bre3, 0.8)
model.add_transition(st_i_bre2, st_d_bre3, 0.10)
model.add_transition(st_d_bre2, st_i_bre2, 0.10)
model.add_transition(st_d_bre2, st_bre3, 0.8)
model.add_transition(st_d_bre2, st_d_bre3, 0.10)

model.add_transition(st_bre3, st_i_bre3, 0.10)
model.add_transition(st_bre3, st_bre4, 0.8)
model.add_transition(st_bre3, st_d_bre4, 0.10)
model.add_transition(st_i_bre3, st_i_bre3, 0.10)
model.add_transition(st_i_bre3, st_bre4, 0.8)
model.add_transition(st_i_bre3, st_d_bre4, 0.10)
model.add_transition(st_d_bre3, st_i_bre3, 0.10)
model.add_transition(st_d_bre3, st_bre4, 0.8)
model.add_transition(st_d_bre3, st_d_bre4, 0.10)

model.add_transition(st_bre4, st_i_bre4, 0.10)
model.add_transition(st_bre4, st_bre5, 0.8)
model.add_transition(st_bre4, st_d_bre5, 0.10)
model.add_transition(st_i_bre4, st_i_bre4, 0.10)
model.add_transition(st_i_bre4, st_bre5, 0.8)
model.add_transition(st_i_bre4, st_d_bre5, 0.10)
model.add_transition(st_d_bre4, st_i_bre4, 0.10)
model.add_transition(st_d_bre4, st_bre5, 0.8)
model.add_transition(st_d_bre4, st_d_bre5, 0.10)

model.add_transition(st_bre5, st_i_bre5, 0.10)
model.add_transition(st_bre5, st_bre6, 0.8)
model.add_transition(st_bre5, st_d_bre6, 0.10)
model.add_transition(st_i_bre5, st_i_bre5, 0.10)
model.add_transition(st_i_bre5, st_bre6, 0.8)
model.add_transition(st_i_bre5, st_d_bre6, 0.10)
model.add_transition(st_d_bre5, st_i_bre5, 0.10)
model.add_transition(st_d_bre5, st_bre6, 0.8)
model.add_transition(st_d_bre5, st_d_bre6, 0.10)

model.add_transition(st_bre6, st_i_bre6, 0.10)
model.add_transition(st_bre6, st_bre7, 0.8)
model.add_transition(st_bre6, st_d_bre7, 0.10)
model.add_transition(st_i_bre6, st_i_bre6, 0.10)
model.add_transition(st_i_bre6, st_bre7, 0.8)
model.add_transition(st_i_bre6, st_d_bre7, 0.10)
model.add_transition(st_d_bre6, st_i_bre6, 0.10)
model.add_transition(st_d_bre6, st_bre7, 0.8)
model.add_transition(st_d_bre6, st_d_bre7, 0.10)

model.add_transition(st_bre7, st_i_bre7, 0.10)
model.add_transition(st_bre7, st_tat1, 0.8)
model.add_transition(st_bre7, st_d_tat1, 0.10)
model.add_transition(st_i_bre7, st_i_bre7, 0.10)
model.add_transition(st_i_bre7, st_tat1, 0.8)
model.add_transition(st_i_bre7, st_d_tat1, 0.10)
model.add_transition(st_d_bre7, st_i_bre7, 0.10)
model.add_transition(st_d_bre7, st_tat1, 0.8)
model.add_transition(st_d_bre7, st_d_tat1, 0.10)





ins_prob = 0.005
normal_prob = 0.99
del_prob = 0.005

tata_ins_prob = 0.1
tata_del_prob = 0.1
tata_normal_prob = 0.8

transition_maker(model,
                 [st_tat1, st_d_tat1, st_i_tat1],
                 [(st_i_tat1, tata_ins_prob), (st_tat2, tata_normal_prob), (st_d_tat2, tata_del_prob)])

transition_maker(model,
                 [st_tat2, st_d_tat2, st_i_tat2],
                 [(st_i_tat2, tata_ins_prob), (st_tat3, tata_normal_prob), (st_d_tat3, tata_del_prob)])

transition_maker(model,
                 [st_tat3, st_d_tat3, st_i_tat3],
                 [(st_i_tat3, tata_ins_prob), (st_tat4, tata_normal_prob), (st_d_tat4, tata_del_prob)])

transition_maker(model,
                 [st_tat4, st_d_tat4, st_i_tat4],
                 [(st_i_tat4, tata_ins_prob), (st_tat5, tata_normal_prob), (st_d_tat5, tata_del_prob)])

transition_maker(model,
                 [st_tat5, st_d_tat5, st_i_tat5],
                 [(st_i_tat5, tata_ins_prob), (st_tat6, tata_normal_prob), (st_d_tat6, tata_del_prob)])

transition_maker(model,
                 [st_tat6, st_d_tat6, st_i_tat6],
                 [(st_i_tat6, 0.01), (st_bak2, 0.99)])


transition_maker(model,
                 [st_bak2],
                 [(st_bak2, 0.5), (st_inr1, 0.29), (st_d_inr1, 0.2), (model.end, 0.01)])

transition_maker(model,
                 [st_inr1, st_d_inr1, st_i_inr1],
                 [(st_i_inr1, ins_prob), (st_inr2, normal_prob), (st_d_inr2, del_prob)])

transition_maker(model,
                 [st_inr2, st_d_inr2, st_i_inr2],
                 [(st_i_inr2, ins_prob), (st_inr3, normal_prob), (st_d_inr3, del_prob)])

transition_maker(model,
                 # [st_inr3, st_d_inr3, st_i_inr3],
                 [st_inr3, st_d_inr3],
                 [(st_i_inr3, ins_prob), (st_inr4, normal_prob), (st_d_inr4, del_prob)])

transition_maker(model,
                 [st_inr4, st_d_inr4, st_i_inr4],
                 [(st_i_inr4, ins_prob), (st_inr5, normal_prob), (st_d_inr5, del_prob)])

transition_maker(model,
                 [st_inr5, st_d_inr5, st_i_inr5],
                 [(st_i_inr5, ins_prob), (st_inr6, normal_prob), (st_d_inr6, del_prob)])

transition_maker(model,
                 [st_inr6, st_d_inr6, st_i_inr6],
                 [(st_i_inr6, ins_prob), (st_inr7, normal_prob), (st_d_inr7, del_prob)])

transition_maker(model,
                 [st_inr7, st_d_inr7, st_i_inr7],
                 [(st_i_inr7, 0.01), (st_bak3, 0.99)])

transition_maker(model,
                 [st_bak3],
                 [(st_bak3, 0.8), (model.end, 0.2)])





seq = numpy.array(data)
model.bake()


# seq = numpy.array(list('acgtacgacgtactgaggcgcc'))

logp, path = model.viterbi(seq)


print("sequence: {}".format(''.join(seq)))
names = []
for p in path:
    names.append(p[1].name)
print("hmm pred: {}".format(' '.join(map( str, names))))