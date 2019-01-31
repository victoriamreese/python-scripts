#which is in kata
#completed 1/31/19
#https://www.codewars.com/kata/which-are-in/train/python

def in_array(array1, array2):
    contained_strings=[] 
    for substring in array1:
       print(substring)
       for letternum in range(len(substring)+1):
           for string in array2:
               if substring == string[0+letternum:len(substring)+letternum]:
                   if substring not in contained_strings:
                       contained_strings.append(substring)
    contained_strings.sort()
    print(contained_strings) 

a1=['cod', 'code', 'wars', 'ewar', 'ar'] 
a2= ['lively', 'alive', 'harp', 'sharp', 'armstrong', 'codewars']
in_array(a1, a2)

