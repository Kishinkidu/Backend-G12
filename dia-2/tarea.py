n=(4)

if n % 2 != 0:
    print("weird")
else:
    if n >=2 and n<=5:
        print("not weird")
    elif n>=6 and n <=20:
        print("weird")
    elif n>=21:
        print("not weird")


a=(4)
b=(3)

print(int(a/b))
print(float(a/b))
print("------------")
n=(3)
for numero in range(1,n+1):
  print(numero,end="")
print("-------------")

n=(6)
i=()
for numero in range(0,n):
    print(numero*numero) 
    

print("-------------")
def print_full_name(first_name, last_name):
    print("Hello " + first_name + " " + last_name + "! You just delved into python.")
