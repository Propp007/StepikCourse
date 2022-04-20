line = input().replace(" ","").replace("+", " +").replace("-", " -").split()
calc = []
for n in line:
    calc.append(int(n))
print(sum(calc))