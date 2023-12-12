# num ceck +ve,-ve,zero 

num_chk=lambda num:"+ve" if num>0 else "-ve" if num<0 else "zero"
print(num_chk(5))

#max largest number

max_two=lambda n1,n2:n1 if n1>n2 else n2
print(max_two(10,100))

# cube

cube=lambda n:n**3
print(cube(3))

#odd even

odd_even=lambda n:"even" if n%2==0 else "odd"
print(odd_even(7))