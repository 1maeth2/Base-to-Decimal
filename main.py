ans = ""
base = ""
mode = ""
arr = []
mode = input("What do you want to convert? base/decimal: ")
while not base.isnumeric():
    base = input("What base are you using?: ")
while not ans.isnumeric():
    ans = input("What is your value?: ")

def decimal_to_base():
    n = int(ans)
    r = 0
    i = 0
    while n != 0:
        r = n%2
        arr.append(int(r))
        n = (n-r)/2
        i += 1
    print(f"Decimal to Base {base} is ")
    for j in reversed(arr):
     print(j, end= "")

def base_to_decimal():
    i = 0
    r = 0
    n = int(ans)
    s = 0
    while(n != 0):
        r = n%10
        arr.append(r)
        n = (n-r)/10
        i += 1
    for j in range(i):
        s += arr[j] * int(base) ** j
    print(f"Base {base} to decimal is {s}")

if mode == "base":
    base_to_decimal()
elif mode == "decimal":
    decimal_to_base()