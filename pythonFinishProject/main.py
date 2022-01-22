"""1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi)
 oluşabileceği gibi, non-scalar verilerden de oluşabilir."""

def flat_gen(givenlist):
    if type(givenlist) is list:
        for i in givenlist:
            yield from flat_gen(i)
    else:
        yield givenlist

def flatten(givenlist):
    return list(flat_gen(givenlist))

givenlist = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list = flatten(givenlist)
print(flat_list)

"""----------------------------------------------------------------------------------------------------------------"""
"""2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün."""

numbers = ([[1, 2],[3, 4],[5, 6, 7]])

print([i[::-1] for i in numbers[::-1]])



