def blink(stones):
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            left_half = ((str(stones[i]))[:int(len(str(stones[i])) / 2)])
            right_half = ((str(stones[i]))[int(len(str(stones[i])) / 2):])
            stones[i] = int(left_half)
            stones.insert(i+1, int(right_half))
            i += 1
        else:
            stones[i] = stones[i] * 2024
        i += 1

f = open("day11/day11_input.txt", "r")

stones = f.read()
stones = stones.split()

for i in range(len(stones)):
    stones[i] = int(stones[i])

i = 0
while i < 25:
    blink(stones)
    i += 1

print(len(stones))