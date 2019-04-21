f2 = open("C:/Users/AwesomeRick/Desktop/Study/机器学习/样本01.txt", "r+")
f1 = open("C:/Users/AwesomeRick/Desktop/Study/机器学习/样本01.txt", "r+")
for s in f1.readlines():
    num1, num2 = 0, 0
    for i in s:
        if i == ",":
            num1 += 1
        num2 += 1
        if num1 == 3:
            break
    f2.write(s[num2:])
f1.close()
f2.close()