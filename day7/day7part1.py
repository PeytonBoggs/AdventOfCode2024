def determine_possible(test_value, equation, evaluation, i):
    if (test_value == evaluation and i == len(equation)):
        return True
    
    if (i >= len(equation)):
        return False
    
    return (determine_possible(test_value, equation, int(evaluation) + int(equation[i]), i + 1) or determine_possible(test_value, equation, int(evaluation) * int(equation[i]), i + 1))

f = open("day7/day7_input.txt", "r")

total_calibration_result = 0

for equation in f:
    equation = equation.split()

    equation[0] = equation[0][:-1]
    test_value = int(equation[0])

    evaluation = equation[1]

    if (determine_possible(test_value, equation, evaluation, 2)):
        total_calibration_result += test_value
    
print(total_calibration_result)
