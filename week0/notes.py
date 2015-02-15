'''
################
intro

three types of work:
    quizzes:
        during or after videos
        not graded

    hw:
        collection of problems, some of which are not submitted

    lab:
        like hw
        oriented towards applications of linear algebra
'''
'''
################
comprehensions
    produces a set or a list or a dictionary
    gives you a bit of functional programming with lambdas
    mimics mathematical notation
    ** will be required for some quiz questions
'''
'''
################
the function (notes on paper)

    S = {-4, 4, -3, 3, -2, 2, -1, 1, 0}
    s = {x for x in S if x >= 0}
    s = {0, 1, 2, 3, 4}

complex numbers
    z = 3 + 4j
'''
'''
################
PYTHON SYNTAX STUFF

set() creates a set {} of unique values
2 in S
S | R                       # union of two sets,            {1,2} | {2,3} >>> {1,2,3}
>>> {x for x in S | R}
S & R                       # intersection of two sets      {1,2} & {2,3} >>> {2}
>>> {x for x in S & R}
s.add(val)
s.remove(val)
S.update(R)                 # adds R to S (union set to S)
S.intersection_update(R)    # intersection set to S
S.copy()                    # returns a new copy of the set

[[x, y] for x in X for y in Y]
    # double comprehension; cartesian product of all elements against each other
[y for [x,y] in [[1,2], [3,4]]]
    # [1,3]

set([1,1])                  # {1}
list({1,2})                 # [1,2]

gen = (i for i in [1,2,3)   # GENERATOR OBJ
    tuple(gen)              # (1,2,3)
    set(gen)                # {1,2,3}
    list(gen)               # [1,2,3]

iter = zip([1,2], [3,4])    # ITERATOR OBJ
    list(iter)              # [(1,3), (2,4)]

enum = enumerate(['a', 'b'] # ENUMERATOR OBJ        ## you can't enum an obj
    list(enum)              # [(0, 'a'), (1, 'b')]

obj.keys()
obj.values()
obj.items()                 # dict_items([(k, v), (k, v)])
    list(obj.items())       # [(k, v), (k, v)]

import module as mod

import week0.resources.moduleName
                            # requires that every directory named contains a file named __init__.py

from imp import reload      # allows you to reload(module) when you make changes



'''
