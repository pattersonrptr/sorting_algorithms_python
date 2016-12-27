'''
Created on 22 de dez de 2016

@author: patterson
'''
import random

from sort.sort import bubble, insertion, selection, quick, merge, shell, heap, \
    counting, radix, bucket


if __name__ == '__main__':
    vet = [i for i in random.sample(range(100), 10)]
    # vet = [171]
    print(vet)
    print( bucket(vet) )
    


