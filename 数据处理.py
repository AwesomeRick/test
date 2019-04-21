
f1 = open("C:/Users/AwesomeRick/Desktop/Study/机器学习/样本01.txt","r+")
f2 = open("C:/Users/AwesomeRick/Desktop/Study/机器学习/样本01.txt", "r+")
for s in f1.readlines():
    s = s.replace(" ", ",")
    if len(s)<=30 or "0,0" in s:
        pass
    else:
        f2.write(s)
f1.close()
f2.close()