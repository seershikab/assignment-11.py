1.
Finding largest and smallest numbers in list
In [9]:
l=sorted(input('enter the list'),reverse=False)
print(l)
print(l[0],'is an smallest number and the largest number is ',l[-1])
enter the list6321734
['1', '2', '3', '3', '4', '6', '7']
1 is an smallest number and the largest number is  7

2.
Check a list is empty or not
In [10]:
l=input('enter the list elements')
if len(l)==0:
  print('the list is empty')
else:
  print('the list contains some elements ')
enter the list elements
the list is empty

3.
To clone or copy the list
In [17]:
a=list(input('enter the list elements'))
b=a    #b=a.copy()
print(b)
a.append('h')
print(b)
print(a)
enter the list elements829233992
['8', '2', '9', '2', '3', '3', '9', '9', '2']
['8', '2', '9', '2', '3', '3', '9', '9', '2', 'h']
['8', '2', '9', '2', '3', '3', '9', '9', '2', 'h']

4.
Removing even numbers from a list
In [21]:
l=list(input('enter the elements of the list'))
for i in l:
  if int(i)%2==0:
    l.remove(i)
  else:
    pass
print(l)
enter the elements of the list23415678
['3', '1', '5', '7']

5.
Copy the contents of a file to another file
In [ ]:
import shutil
path= 'C:\\Users\\siva krishna\\Documents\\example1.txt'
target = 'C:\\Users\\siva krishna\\Documents\\example2.txt'
shutil(path,target)
f=open('example2.txt')
a=f.read()
print(a)

6.
sum of all the items in a list
In [22]:
l=list(input('enter the list elements'))
sum=0
for i in l:
  sum+=int(i)
print(sum)
enter the list elements3726349
34