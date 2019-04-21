f2 = open("C:/Users/AwesomeRick/Desktop/Study/机器学习/样本01.txt", "r+")
f3 = open("C:/Users/AwesomeRick/Desktop/Study/机器学习/样本01.txt", "r+")
num = 0
for s in f2.readlines():
    if num <100:
        s = s.replace("\n",",   ")
        f3.write(s)
    if num == 100:
        continue