#Q1
'''
z = input("coordinates in the 0-th second: ")
z = list(map(int, z.split()))
o = input("coordinates in the 1-th second: ")
o = list(map(int, o.split()))

speed = [o[i]-z[i] for i in range(2)]

s = int(input("shoots at ? second: "))

output = [z[i] + (speed[i] * s) for i in range(2)]
print("Output:")
for x in output:
    print(x, end = " ")
'''
#Q2
'''
num = input("Please enter the values: ")
num = list(map(int, num.split()))
check = num[1]**2 - (4*num[0]*num[2])
print("Output: ")
if check == 0:
    ans = -num[1] / (2 * num[0])
    print("%.2f"%ans, "(The roots are real and equal)")
    pass
elif check > 0:
    ans = [(-num[1] + check ** (1 / 2)) / (2 * num[0]), (-num[1] - check ** (1 / 2)) / (2 * num[0])]
    print("%.2f %.2f"%(ans[0], ans[1]), "(The roots are real and unequal)")
else:
    print("(The roots are imaginary)")
'''
#Q3
'''
num = input("Please enter three numbers: ")
num = list(map(int, num.split()))
print("Output: ")
if num[2]-num[1] == num[1]-num[0]:
    num.append(2 * num[2] - num[1])
    for n in num:
        print("%d"%n, end=" ")
    print("(An arithmetic sequence)")
elif num[2]/num[1] == num[1]/num[0]:
    num.append(num[2] * (num[2]/num[1]))
    for n in num:
        print("%d"%n, end=" ")
    print("(An geometric sequence)")
else:
    print("(Unknown)")
'''
#Q4
'''
num = input("Please enter the numbers:")
num = list(map(int, num.split()))
minute = [abs(num[3]-num[1]), 60-abs(num[3]-num[1])]
hour = [abs(num[2]-num[0]), 24-abs(num[2]-num[0])]
print(min(hour)+min(minute))
'''
#Q5
'''
code = input("Please enter the last code of ID and Day code: ")
code = list(map(int, code.split()))
print("Output:")
if code[1]==0:
    print("No restriction!")
elif (code[0]%2) == 0:
    print("The last code of the ID is even.")
    if (code[1]%2) == 0:
        print("You can go out to buy masks.")
    else:
        print("You can't go out to buy masks.")
elif (code[0]%2) != 0:
    print("The last code of the ID is odd.")
    if (code[1]%2) != 0:
        print("You can go out to buy masks.")
    else:
        print("You can't go out to buy masks.")
'''
#Q6
'''
num = input("Please enter your height(m) and weight(kg):")
num = list(map(float, num.split()))
bmi = num[1] / (num[0]**2)
print("Output:")
if bmi<18.5:
    normal = num[0]**2 * 18.5 - num[1]
    print("BMI: %.5f\n(Add %d kilograms, let your BMI index be normal!)"%(bmi, normal))
elif bmi>24:
    normal = num[1] - num[0] ** 2 * 24
    print("BMI: %.5f\n(Add %d kilograms, let your BMI index be normal!)" % (bmi, normal))
else:
    print("BMI: %.5f\n(Normal!)"%bmi)
'''
#Q7
'''
print("Input:")
p1 = input()
p1 = list(map(int, p1.split()))
p2 = input()
p2 = list(map(int, p2.split()))
p3 = input()
p3 = list(map(int, p3.split()))
p1_p2 = [p2[i]-p1[i] for i in range(2)]
p2_p3 = [p3[i]-p2[i] for i in range(2)]
print("Output:")
if p1_p2==p2_p3:
    print("Yes")
else:
    print("No")
'''
#Q8
'''
n = int(input("number of items: "))
items = []
for i in range(n):
    item = input()
    item = list(map(int, item.split()))
    items.append(item)
x = int(input("x: "))
print("Output: ")
ans = 0
for i in range(n):
    ans += (items[i][0]*(x**items[i][1]))
print(ans)
'''
#09
'''
num = input("Please enter the numbers: ")
num = list(map(int, num.split()))
lcm = max([num[1],num[3]])
while lcm%num[1] != 0 or lcm%num[3] != 0:
    lcm += 1
num[0] *= lcm/num[1]
num[2] *= lcm/num[3]
ans = [int(num[0]+num[2]), lcm]
gcd = min(ans)
while ans[0]%gcd != 0 or ans[1]%gcd != 0:
    gcd -= 1
ans = [int(x/gcd) for x in ans]
if ans[0]==ans[1]:
    print("1")
else:
    print("%d %d"%(ans[0], ans[1]))
'''
#10
num = input("Please enter the numbers: ")
num = list(map(int, num.split()))
n = 1
while num[0]**n <= num[1]:
    n+=1
print(n-1)