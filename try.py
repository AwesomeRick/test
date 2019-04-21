f2 = open("C:/Users/AwesomeRick/Desktop/Study/机器学习/样本01.txt", "r+")
f3 = open("C:/Users/AwesomeRick/Desktop/Study/机器学习/样本01.txt", "w")
Walking,Jogging,Downstairs,Upstairs,Standing,Sitting = 0,0,0,0,0,0
for s in f2.readlines():
    if "Walking" in s and Walking % 100 == 0:
        f3.write(s)
        Walking += 1
    elif "Jogging" in s and Jogging % 100 == 0:
        f3.write(s)
        Jogging += 1
    elif "Downstairs" in s and Downstairs % 100 == 0:
        f3.write(s)
        Downstairs += 1
    elif "Upstairs" in s and Upstairs % 100 == 0:
        f3.write(s)
        Upstairs += 1
    elif "Standing" in s and Standing % 100 == 0:
        f3.write(s)
        Standing += 1
    elif "Sitting" in s and Sitting % 100 == 0:
        f3.write(s)
        Sitting += 1


f3.close()
f2.close()