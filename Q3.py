import json
result = 0
numberOfQuestion = 0
name = input("Enter yout name: ")
with open('q.json') as json_file:
    data = json.load(json_file)
    for question in data:
        print(question+": ")
        answer = input()
        if answer == data[question]:
            result = result + 1
        numberOfQuestion = numberOfQuestion + 1

outputFile = open("result.txt", "w")
outputFile.write(name+": " +str(result)+"/" + str(numberOfQuestion))
outputFile.close()
