# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[k] for k in keylist]

def list2dict(L, keylist): return {keylist[i]:L[i] for i in range(len(L))}

# def listrange2dict(L): return {n:x for x in L for n in range(len(L))}

def listrange2dict(L): return list2dict(L, range(len(L)))