with open('dataset_3363_4.txt') as input, open('marks.txt','w') as output:
    strings = [s.rstrip() for s in input.readlines()]
    evaluation = [s.split(';')[1:] for s in strings]
    for x in evaluation:
        suma = (sum(map(int, x))/len(x))
        output.write(suma.__str__() + "\n")
    average_math = sum(int(x[0]) for x in evaluation)/len(evaluation)
    average_fizyka = sum(int(x[1]) for x in evaluation)/len(evaluation)
    average_jez_ros = sum(int(x[2]) for x in evaluation)/len(evaluation)
    output.write(average_math.__str__() + " ")
    output.write(average_fizyka.__str__() + " ")
    output.write(average_jez_ros.__str__() + " ")