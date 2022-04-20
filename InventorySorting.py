weights = [5240, 2130, 1200, 1000, 820, 600, 500, 400, 300, 200, 100, 40, 20, 10]

N = int(input('Enter your weight for a bag: '))
N = N * 1000
bag = []
count = 0

while sum(bag) < N:
    print("Iteration: ", count)
    print("=====================================")
    if weights[0] + sum(bag) <= N:
        bag += [weights.pop(0)]
        print("Weights: ", weights)
        print("Bag: ", bag, "sum = ", sum(bag))
        count += 1
    else:
        weights.pop(0)
        count += 1

print(bag)
