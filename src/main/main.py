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
        
        print('[Enter] para continuar!')
        input()
        
def test_algoithm(op):
    print('\nOrdenando pelo método ', algorithms[op], '...')
    print('\nVetor ordenado: ')
            
    ini = time.time()
    print(sort_methods[op](vet))
    fim = time.time()
    print('\n\nTempo total gasto: ', fim-ini)


if __name__ == '__main__':
    
    algorithms = [ 'Bubble', 'Insertion', 'Selection', 'Quick', 'Merge',
                   'Shell', 'Heap', 'Counting', 'Radix', 'Bucket', 'Gnome', 'Comb', 'Cocktail', 'Todos' ]
    
    sort_methods = [bubble, insertion, selection, quick, merge, shell, heap, counting, radix, bucket, gnome, cocktail, cocktail]
    
    
    while True:
        print('\n\n\tSorting Algorithms\n\n')
    
        a_length = int(input('Tamanho do array a ser ordenado: '))
        min = int(input('Menor número possível: '))
        max = int(input('Maior número possível: '))
        
        vet = [random.randint(min, max) for r in xrange(a_length)]
        
        print('\nVetor gerado: ')
        print(vet)
        
        print('\nEscolha um algoritmo de Ordenação: ')
        for i, x in enumerate(algorithms):
            print(i, ' - ', x)
        op = input()
        
        if op == '0':
            sort_alg = bubble
        elif op == '1':
            sort_alg = insertion
        elif op == '2':
            sort_alg = selection
        elif op == '3':
            sort_alg = quick
        elif op == '4':
            sort_alg = merge
        elif op == '5':
            sort_alg = shell
        elif op == '6':
            sort_alg = heap
        elif op == '7':
            sort_alg = counting
        elif op == '8':
            sort_alg = radix
        elif op == '9':
            sort_alg = bucket
        elif op == '10':
            sort_alg = gnome
        elif op == '11':
            sort_alg = comb
        elif op == '12':
            sort_alg = cocktail
        elif op == '13':
            test_all_algoithms()
            continue
        else:
            print('\nOpção inválida.')
            
        test_algoithm(int(op))
            
            
        
        
        
        
        
        
        
        