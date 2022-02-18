# simple loop: for and range
print('->range(4):')
for i in range (4):
    print(i)
print('->range(1, 4):')
for i in range (1,4):
    print(i)
print('->range(1, 4, 2):')
for i in range (1, 4, 2):
    print(i)
    
# show strings
print('->showing text methods:')
print('{0}:{1}'.format('test', 1))
print('%s:%6.3f' % ('test', 1.2))

# if - elif statment
print('->if - elif statment:')
a = 1
b = 2
if a == 2:
    print('a == 2: yes')
elif b == 2:
    print('b == 2: yes')
    
#
arr = ['a' ,'b']
for i in arr:
    print(i)
    
arr.append('c');
print(arr)

arr.pop(len(arr) - 1);
print(arr)

arr.append('a');
arr.remove('a'); #removethe first 'a' element
print(arr)

arr_1 = ['a', 'b']
arr_2 = ['c', 'd']
arr_1.extend(arr_2)
print(arr_1)

arr_1 = ['a', 'b']
tuple = ('c', 'd')
arr_1.extend(tuple)
print(arr_1)


#https://bravelab.io/blog/does-zappa-make-it-super-easy/
#Zappa, Flask, Pandas