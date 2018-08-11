"""
Created on 22 de dez de 2016

@author: patterson
"""

import math


def bubble(nlist):
    nlist = list(nlist)
    size = len(nlist) - 1
    
    if size <= 1:
        return nlist
    
    swapped = True
    
    for i in range(size):
        if not swapped:
            break

        swapped = False

        for j in range(size - i):
            if nlist[j] > nlist[j + 1]:
                nlist[j + 1], nlist[j] = nlist[j], nlist[j + 1]
                swapped = True
                
    return nlist

    
def insertion(nlist):
    nlist = list(nlist)
    size = len(nlist) 
    
    if size <= 1:
        return nlist

    for i in range(size):
        key = nlist[i]
        j = i - 1

        while j >= 0 and key < nlist[j]:
            nlist[j + 1] = nlist[j]
            j -= 1
        nlist[j + 1] = key
        
    return nlist


def selection(nlist):
    nlist = list(nlist)
    size = len(nlist)
    
    if size < 1:
        return nlist
    
    for i in range(size - 1):
        lower = i
        for j in range(i + 1, size):
            if nlist[j] < nlist[lower]:
                lower = j

        nlist[i], nlist[lower] = nlist[lower], nlist[i]
        
    return nlist

    
def quick(nlist):
    nlist = list(nlist)
    size = len(nlist)
    
    if size <= 1:
        return nlist
    
    pivot = nlist[0]
    lr = [x for x in nlist if x < pivot]    # lower
    gt = [x for x in nlist[1:] if x >= pivot]   # greater
    
    return quick(lr) + [pivot] + quick(gt)


def merge(nlist):
    if len(nlist) < 2:
        return nlist
    
    result, mid = list(), len(nlist) // 2
    
    l = merge(nlist[:mid])  # left
    r = merge(nlist[mid:])  # right
    
    while (len(l) > 0) and (len(r) > 0):
        if l[0] > r[0]:
            result.append(r.pop(0))
        else: 
            result.append(l.pop(0))
            
    result.extend(l + r)
    
    return result


def shell(nlist):
    nlist = list(nlist)
    size = len(nlist)
    
    if size < 2:
        return nlist
  
    gap = size // 2
    
    while gap > 0:
        for i in range(gap, size):
            val = nlist[i]
            j = i
            
            while j >= gap and nlist[j - gap] > val:
                nlist[j] = nlist[j - gap]
                j -= gap
            nlist[j] = val
            
        gap //= 2
        
    return nlist


def heap(nlist):
    nlist = list(nlist)
    size = len(nlist)
    
    if size < 2:
        return nlist
    
    for start in range((size - 2) // 2, -1, -1):
        _max_heap(nlist, start, size - 1)
        
    for end in range(size - 1, 0, -1):  
        nlist[end], nlist[0] = nlist[0], nlist[end]
        _max_heap(nlist, 0, end - 1)
        
    return nlist


def _max_heap(nlist, root, end):
    while True:
        child = root * 2 + 1
        
        if child > end:
            break
        if child + 1 <= end and nlist[child] < nlist[child + 1]:
            child += 1
        if nlist[root] < nlist[child]:
            nlist[root], nlist[child] = nlist[child], nlist[root]
            root = child
        else:
            break


def counting(alist):
    nlist = list(alist)
    size = len(nlist)
    
    if size < 2:
        return nlist
    
    m = min(nlist) 
    k = max(nlist) - m

    counter = [0] * ( k + 1 )

    for i in nlist:
        counter[i - m] += 1
        
    ndx = 0;
    for i in range( len( counter ) ):
        while 0 < counter[i]:
            nlist[ndx] = i + m 
            ndx += 1
            counter[i] -= 1
            
    return nlist


def radix(aList):
    nlist = list(aList)
    size = len(nlist)
    
    if size < 2:
        return nlist
    
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1
 
    while not maxLength:
        maxLength = True
        buckets = [list() for i in range(RADIX)]
 
        for i in nlist:
            tmp = int(i / placement)
            buckets[int(tmp % RADIX)].append(i)
            if maxLength and tmp > 0:
                maxLength = False
 
        a = 0
        for b in range( RADIX ):
            buck = buckets[b]
            for i in buck:
                nlist[a] = i
                a += 1
 
        placement *= RADIX
        
    return nlist


def bucket(aList, bucketSize=5):
    nlist = list(aList)
    size = len(nlist)
    
    if size < 2:
        return nlist

    minValue = min(nlist)
    maxValue = max(nlist)

    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    
    for i in range(0, bucketCount):
        buckets.append([])

    for i in range(0, size):
        buckets[math.floor((nlist[i] - minValue) / bucketSize)].append(nlist[i])

    nlist = []
    for i in range(0, len(buckets)):
        buckets[i] = insertion(buckets[i])
        for j in range(0, len(buckets[i])):
            nlist.append(buckets[i][j])

    return nlist


def gnome(aList):
    nlist = list(aList)
    size = len(nlist)
    
    if size < 2:
        return nlist
    
    pivot = 0
    nlist_length = len(nlist) 
    while pivot < nlist_length - 1:
        if nlist[pivot] > nlist[pivot + 1]:
            nlist[pivot + 1], nlist[pivot] = nlist[pivot], nlist[pivot + 1]
            if pivot > 0:
                pivot -= 2
        pivot += 1
        
    return nlist


def comb(aList):
    nlist = list(aList)
    size = len(nlist)
    
    if size < 2:
        return nlist
    
    gap = size
    swaps = True
    
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25)) # Minimun gap is 1
        swaps = False
        
        for i in range(size - gap):
            j = i + gap
    
            if nlist[i] > nlist[j]:
                nlist[i], nlist[j] = nlist[j], nlist[i]
                swaps = True
 
    return nlist


def cocktail(aList):
    nlist = list(aList)
    size = len(nlist)
    
    if size < 2:
        return nlist
    
    swapped = True
    i = 0
    j = size - 1
    
    while i < j and swapped:
        for k in range(i, j):
            if nlist[k] > nlist[k + 1]:
                nlist[k], nlist[k + 1] = nlist[k + 1], nlist[k]
                swapped = True
        j -= 1
        
        if swapped:
            swapped = False
            for k in range(j, i, -1):
                if nlist[k] < nlist[k - 1]:
                    nlist[k], nlist[k - 1] = nlist[k - 1], nlist[k]
                    swapped = True
        
        i += 1
        
        if not swapped:
            return nlist
