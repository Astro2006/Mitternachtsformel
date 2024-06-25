#zahl ** potenz zahl
#import math as m und m.sqrt(potenz) = wurzel gezogen


import math as m



a1 = input("Geben sie A ein: ")
b1 = input("Geben sie B ein: ")
c1 = input("Geben sie C ein: ")

a = float(a1)
b = float(b1)
c = float(c1)

#b2 =(b)**2
b2 = 25
#print(b2)

# x1
w = m.sqrt(b2-4*a*c)
x1 = (-(b)+w)/2*a
# x2
x2 = (-(b)-w)/2*a

print(str(x1)+ " und " + str((x2)))
