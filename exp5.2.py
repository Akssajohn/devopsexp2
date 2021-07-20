from array import*
arr1=array('d',[3.9,2.7,6.5,8.3])
print('element of the first array are:')
for element in arr1:
    print(element)
    print("")
arr2=array(arr1.typecode, (a*3 for a in arr1))
print('Elements of Array 2 are: ')
for i in arr2 :
     print(i)
