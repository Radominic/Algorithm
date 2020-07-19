# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:25:55 2020

@author: Gangmin
"""
'''
def cut_rod(n): 
    p = [0,1,5,8,9,10,15,15,17,18,21]
    r = [0]
    if n == 0: 
        return r[0] 
    if n >= 1: 
        max_val = float('-inf')
        for j in range(1, n+1): 
            for i in range(0, j):
                max_val = max(max_val, p[j-i] + r[i]) 
            r.append(max_val) 
    return r[n]
print(cut_rod(10)) # 22
'''
p = [0,1,5,8,9,10,15,15,17,18,21]
s=[] 
r= []
def memoized_cut_rod(p,n):

    for i in range(n+1):
        r.append(-1)
        s.append(-1)
    return memoized_cut_rod_aux(p,n,r)

def memoized_cut_rod_aux(p,n,r):
    if r[n]>=0:
        return r[n]
    if n == 0:
        q=0
    else:
        q = -1
        for i in range(1,n+1):
            temp = q
            q = max(q,p[i]+memoized_cut_rod_aux(p,n-i,r))
            if temp != q:
                s[n] = i
    r[n]=q
    return q

def print_cut_rod(n):
    while n>0:
        print(s[n])
        n=n-s[n]