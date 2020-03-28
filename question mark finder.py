sample = "5??5???5"
b = 0
counter = 0
trueCheck = False
DigiCounter = 0
SecondDigit = 0
questionCheck = 0
firstCount = 0
testEnd = 0


length = len(sample)
for i in sample:
    if i.isdigit():
        DigiCounter += 1
        if DigiCounter == 2:
            SecondDigit = i
            testEnd = counter
        if DigiCounter == 1 and firstCount == 0:
            FirstDigit = i
            testStart = counter
            firstCount += 1
        summation = int(FirstDigit) + int(SecondDigit)
        if summation == 10:
            summation = 0
            while testStart <= testEnd:
                if sample[testStart] == "?" and int(questionCheck) < 3:
                    questionCheck += 1
                    print("question check: ", questionCheck)
                testStart += 1
                print("test sart: ", testStart)
                print("test end: ", testEnd)
                if questionCheck == 3:
                    final = True
            questionCheck = 0
            testStart = 0
            testEnd = 0
        if firstCount == 1 and DigiCounter == 2:
            testStart = counter
            FirstDigit = SecondDigit
        DigiCounter = 1
    counter += 1

if final is True:
    print(final)
else:
    final = False
    print(final)

