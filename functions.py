#adding two numbers

def sum(x,y) :
    z = x + y
    return z 

print(sum(2,3))

#subtracting two numbers

def subtract(m,n) :
    p = m - n
    return p
print(subtract(7,3))

#dividing two numbers

def divide(a,b) :
    c = a / b
    return c
print(divide(25,5))


#multiplying two numbers

def multiply(j,k) :
    l =j * k
    return l
print(multiply(28,4))


#using linear equations
def solve_equation(a,b,c) :
    dis = (b**2 - 4 * a *c)**(1/2)
    if dis > 0 :
        root1 = (-b + dis/2)/(2*a)
        root2 = (-b-dis)/2/(2*a)
        return root1, root2
    else :
        roots = "imaginary"

ans = solve_equation(1,2,-8)
print(ans)


    