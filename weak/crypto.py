# WEAK Main Library
# Licensed under GPLv3+

"""
    Copyright (C) 2018 apple502j

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import secrets
import random
import string

def up(s,n):
    """Up Here!"""
    l=list(s)
    l[n]=l[n].upper()
    return ''.join(l)

def __sameUp(arr_ll_a,arr_ll_b):
    """The same code used to load/make"""
    # Lower Upper
    arr_lu=[]
    for C1 in range(len(arr_ll_a)):
        arr_lu.append({up(arr_ll_a[C1],1):up(arr_ll_b[C1],1)})
    # Upper Lower
    arr_ul=[]
    for C1 in range(len(arr_ll_a)):
        arr_ul.append({up(arr_ll_a[C1],0):up(arr_ll_b[C1],0)})
    # Upper Upper
    arr_uu=[]
    for C1 in range(len(arr_ll_a)):
        arr_uu.append({arr_ll_a[C1].upper():arr_ll_b[C1].upper()})
    return (arr_lu,arr_ul,arr_uu)

def __randConvertMap():
    """Make a map"""
    # Lower Lower
    arr_ll_a=[]
    arr_ll_b=[]
    for C1 in string.ascii_lowercase:
        for C2 in string.ascii_lowercase:
            arr_ll_a.append(C1+C2)
    arr_ll_c=list(arr_ll_a)
    for C1 in range(26**2):
        arr_ll_rnd=arr_ll_c[secrets.randbelow(len(arr_ll_c)-1) if (len(arr_ll_c)-1)!=0 else 0]
        arr_ll_b.append(arr_ll_rnd)
        arr_ll_c.remove(arr_ll_rnd)
    arr_ll=[]
    C1=0
    for C1 in range(26**2):
        arr_ll.append({arr_ll_a[C1]:arr_ll_b[C1]})
    random.shuffle(arr_ll)
    arr_lu,arr_ul,arr_uu=__sameUp(arr_ll_a,arr_ll_b)
    random.shuffle(arr_lu)
    random.shuffle(arr_ul)
    random.shuffle(arr_uu)
    return (arr_ll,arr_lu,arr_ul,arr_uu)

def sn(t,n):
    """Split by num"""
    ra=[]
    sv=''
    i=0
    for c in t:
        i+=1
        sv=sv+c
        if i%n==0:
            ra.append(sv)
            sv=''
    if sv!='':
        ra.append(sv)
    return ra

def __CMCrypt(t,cm):
    """ ConvertMap Crypt """
    ta=sn(t,2)
    l=cm[0]+cm[1]+cm[2]+cm[3]
    rb=[]
    ra=[]
    for i in l:
        rb.append(list(i.keys())[0])
        ra.append(list(i.values())[0])
    for i in range(len(ta)):
        if ta[i] in rb:
            ta[i] = ra[rb.index(ta[i])]
    return ''.join(ta)

def __Str2CM(t):
    """String to ConvertMap"""
    ta=sn(t,2)
    b=[ta[i] for i in range(len(ta)) if i%2==0] # B is Before
    a=[ta[i] for i in range(len(ta)) if i%2==1] # A is After
    ll=[]
    for i in range(len(a)):
        ll.append({b[i]:a[i]})
    lu,ul,uu=__sameUp(b,a)
    return (ll,lu,ul,uu)

def __CM2Str(cm):
    """ConvertMap to String"""
    ll=cm[0]
    b=[]
    a=[]
    rs=''
    for i in ll:
        b.append(list(i.keys())[0])
        a.append(list(i.values())[0])
    for i in range(2* (26**2)):
        if i%2==0:
            rs=rs+b[i//2]
        else:
            rs=rs+a[(i-1)//2]
    return rs

def __keyChange(strkey):
    """Change Key2Key"""
    ta=sn(strkey,2)
    a=[ta[i] for i in range(len(ta)) if i%2==0] # B is Before
    b=[ta[i] for i in range(len(ta)) if i%2==1] # A is After
    ll=[]
    for i in range(len(a)):
        ll.append({b[i]:a[i]})
    lu,ul,uu=__sameUp(b,a)
    return __CM2Str(tuple((ll,lu,ul,uu)))

# Real Module

def generateKeys():
    """Generate Keys."""
    public=__CM2Str(__randConvertMap())
    private=__keyChange(public)
    return public,private

def crypt(text,key):
    """Encrypt/Decrypt"""
    return __CMCrypt(text,__Str2CM(key))
