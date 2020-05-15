#For int (immutable)
print("For int (immutable): ")
a = 10
print("a is "+str(a)+" and it's ID is "+str(id(a)))
b = 10
print("b is "+str(b)+" and it's ID is "+str(id(b)))
a = a + 5
print("a is "+str(a)+" and it's ID is "+str(id(a)))
print("b is "+str(b)+" and it's ID is "+str(id(b)))

print("\n")

#For tuple (immutable)
print("For tuple (immutable): ")
t1 = (10, 20, 30)
print("t1 is "+str(t1)+" and it's ID is "+str(id(t1)))
t2 = (10, 20, 30)
print("t2 is "+str(t2)+" and it's ID is "+str(id(t2)))
t1 = t1 + (40, 50)
print("t1 is "+str(t1)+" and it's ID is "+str(id(t1)))
print("t2 is "+str(t2)+" and it's ID is "+str(id(t2)))

print("\n")

#For list (mutable)
print("For list (mutable): ")
l1 = [10, 20, 30]
print("l1 is "+str(l1)+" and it's ID is "+str(id(l1)))
l2 = [10, 20, 30]
print("l2 is "+str(l2)+" and it's ID is "+str(id(l2)))
x = l1.append(40)
print("l1 is "+str(l1)+" and it's ID is "+str(id(l1)))
print("l2 is "+str(l2)+" and it's ID is "+str(id(l2)))






