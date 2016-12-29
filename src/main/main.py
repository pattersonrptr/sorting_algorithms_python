'''
Created on 22 de dez de 2016

@author: patterson
'''

from pyqtgraph.python2_3 import xrange
import random
import time

from sort.sort import bubble, insertion, selection, quick, merge, shell, heap, \
    counting, radix, bucket, gnome, comb, cocktail
    
    
def test_all_algoithms():
    for i in range(len(sort_methods) ):
        test_algoithm(i)
        
        print('Press [Enter] to continue!')
        input()
        
def test_algoithm(op):
    print('\nSorting by ', algorithms[op], ' method...')
    print('\nOrdered array: ')
            
    ini = time.time()
    print(sort_methods[op](vet))
    fim = time.time()
    print('\n\nTotal time spent: ', fim-ini)


if __name__ == '__main__':
    
    algorithms = [ 'Bubble', 'Insertion', 'Selection', 'Quick', 'Merge',
                   'Shell', 'Heap', 'Counting', 'Radix', 'Bucket', 'Gnome', 'Comb', 'Cocktail', 'Todos' ]
    
    sort_methods = [bubble, insertion, selection, quick, merge, shell, heap, counting, radix, bucket, gnome, comb, cocktail]
    
    
    while True:
        print('\n\n\tSorting Algorithms\n\n')
    
        a_length = int(input('Size of the array to be sorted: '))
        min = int(input('Smallest possible number: '))
        max = int(input('Greater possible number: '))
        
        vet = [random.randint(min, max) for r in xrange(a_length)]
        
        print('\nOrdered array: ')
        print(vet)
        
        print('\nChoose a Sort Algorithm.: ')
        for i, x in enumerate(algorithms):
            print(i, ' - ', x)
        op = input()
        
        if op == '13':
            test_all_algoithms()
        elif int(op) > 13 or int(op) < 0:
            print('Invalid option.')
        else:
            test_algoithm(int(op))
        
            
            
        
        
        
        
        
        
        
        