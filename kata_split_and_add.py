#Split then add both sides of an array together
#completed 1/30/19
#https://www.codewars.com/kata/split-and-then-add-both-sides-of-an-array-together/train/python
import numpy as np

def split_and_add(numbers, n):
    while len(numbers)>1 and n>0:
        top = np.asarray(numbers[0:int(len(numbers)/2)])
        bottom = np.asarray(numbers[int(len(numbers)/2):int(len(numbers))])
        if len(top) == len(bottom):
            numbers = np.add(top,bottom)
        else:
            top = np.insert(top, 0, 0)
            numbers = np.add(top, bottom)
            n-=1 
    if type(numbers) == list:
        return numbers  
    else:
        return numbers.tolist()

split_and_add([1,2,3,4,6],1)


#better solution
def split_and_add(numbers, n):
    for _ in range(n):
        middle = len(numbers) // 2
        left = numbers[:middle]
        right = numbers[middle:]
        numbers = [a + b for a, b in zip((len(right) - len(left)) * [0] + left, right)]
        if len(numbers) == 1:
            return numbers
    return numbers
