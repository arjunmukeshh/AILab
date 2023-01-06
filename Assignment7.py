def And(a, b):
  
  return [a[i] and b[i] for i in range(len(a))]

def Or(a, b):
  return [a[i] or b[i] for i in range(len(a))]

def Not(a):
  l = []
  for x in a:
    if x:
      l.append(0)
    else: 
      l.append(1)
  return l

def implies(a, b):
  return Or(Not(a), b)

def iff(a, b):
  return And(implies(a, b), implies(b, a))

def is_tautology(p,q,a):
  #print("\n  p   q  expr")
  #print("---------------")
  
  return min(a) == 1

def are_equivalent(a, b):
  return a == b

a=[0, 0, 1, 1]
b=[0, 1, 0, 1]

print("\n(~p∧q⇒~(p∨q)) ")
p=a
q=b
l1=Not(p)
l2=And(l1, q)
l3=Or(p, q)
l4=Not(l3)
l5=implies(l2, l4)
print("p  q  ~p  ~p∧q  p∨q  ~(p∨q)  ~p∧q⇒~(p∨q)")
for i in range(len(p)):
    
    print(p[i]," ",q[i]," ",l1[i]," ",l2[i]," ",l3[i],"   ",l4[i],"    ",l5[i])
l6=is_tautology(p,q,l5)
print("Tautology :", l6)


print("\n(p⇒q) ∨ (q⇒p)")
p=a
q=b
l1=implies(p, q)
l2=implies(q, p)
l3=Or(l1,l2)
l=is_tautology(p,q,l3)
print("p   q  p⇒q  q⇒p  (p⇒q)∨(q⇒p)")
for i in range(len(p)):
    print(p[i]," ",q[i]," ",l1[i]," ",l2[i],"  ",l3[i])
print("Tautology :", l)

print("\n~a∨b, a->b")
l1=Not(a)
l2=Or(l1, b)
l3=implies(a, b)
print("a   b  ~a  ~a∨b   a->b")
for i in range(len(b)):
    print(a[i]," ",b[i]," ",l1[i]," ",l2[i],"   ",l3[i])
print("\nAre Equivalent :", are_equivalent(l2, l3))

print("\np∨~p, p∧~p")
p=[0,1]
l1=Not(p)
l2=Or(p, l1)
l3=And(p, l1)
print("p  ~p  ~p∨p   p∧~p")
for i in range(len(p)):
    print(p[i]," ",l1[i]," ",l2[i],"   ",l3[i])
print("\nAre Equivalent :", are_equivalent(l2,l3))