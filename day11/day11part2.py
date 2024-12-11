import functools

@functools.cache
def calculateSum(i, stone, sum):
    if i >= 75:
        return 1

    if stone == 0:
        sum = calculateSum(i+1, 1, sum)
    elif len(str(stone)) % 2 == 0:
        temp = 0
        temp += calculateSum(i+1, int(((str(stone))[:int(len(str(stone)) / 2)])), sum)
        temp += calculateSum(i+1, int(((str(stone))[int(len(str(stone)) / 2):])), sum)
        sum = temp
    else:
        sum = calculateSum(i+1, stone * 2024, sum)

    return sum

f = open("day11/day11_input.txt", "r")

stones = f.read()
stones = stones.split()

for i in range(len(stones)):
    stones[i] = int(stones[i])

sum = 0
for stone in stones:
    sum += calculateSum(0, stone, sum)

print(sum)