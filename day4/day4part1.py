f = open("day4/day4_input.txt", "r")

wordsearch = []

for line in f:
    wordsearch.append(line)

xmas_counter = 0

i = 0
while (i < len(wordsearch)):
    wordsearch[i] = wordsearch[i].strip()
    j = 0
    while (j < len(wordsearch[i])):
        if (wordsearch[i][j] == "X"):
            #Straight Up
            if ((i-3 >= 0) and (wordsearch[i-1][j] == "M") and (wordsearch[i-2][j] == "A") and (wordsearch[i-3][j] == "S")):
                xmas_counter += 1
            #Up/Right
            if ((i-3 >= 0) and (j+3 < len(wordsearch[i])) and (wordsearch[i-1][j+1] == "M") and (wordsearch[i-2][j+2] == "A") and (wordsearch[i-3][j+3] == "S")):
                xmas_counter += 1
            #Straight Right
            if ((j+3 < len(wordsearch[i])) and (wordsearch[i][j+1] == "M") and (wordsearch[i][j+2] == "A") and (wordsearch[i][j+3] == "S")):
                xmas_counter += 1
            #Down/Right
            if ((i+3 < len(wordsearch)) and (j+3 < len(wordsearch[i])) and (wordsearch[i+1][j+1] == "M") and (wordsearch[i+2][j+2] == "A") and (wordsearch[i+3][j+3] == "S")):
                xmas_counter += 1
            #Straight Down
            if ((i+3 < len(wordsearch)) and (wordsearch[i+1][j] == "M") and (wordsearch[i+2][j] == "A") and (wordsearch[i+3][j] == "S")):
                xmas_counter += 1
            #Down/Left
            if ((i+3 < len(wordsearch)) and (j-3 >= 0) and (wordsearch[i+1][j-1] == "M") and (wordsearch[i+2][j-2] == "A") and (wordsearch[i+3][j-3] == "S")):
                xmas_counter += 1
            #Straight Left
            if ((j-3 >= 0) and (wordsearch[i][j-1] == "M") and (wordsearch[i][j-2] == "A") and (wordsearch[i][j-3] == "S")):
                xmas_counter += 1
            #Up/Left
            if ((i-3 >= 0) and (j-3 >= 0) and (wordsearch[i-1][j-1] == "M") and (wordsearch[i-2][j-2] == "A") and (wordsearch[i-3][j-3] == "S")):
                xmas_counter += 1
        j += 1
    i += 1

print(xmas_counter)