#Q9
print('Q9: Number Swaping/ Manipulating bits\n')
a=input('Enter value of a: ')
b=input('Enter value of b: ')
print(a,b,sep='\t')
a=int(a)
b=int(b)
a=a^b
b=a^b
a=a^b
print(a,b,sep='\t')
