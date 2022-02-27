booked = [["09:55", "hae"],["10:05", "jee"]]
unbooked = [["10:04", "hee"], ["14:07", "eom"]]
answer = []
time = 0
for i in range(len(booked)):
    hour = (booked[i][0])[-5:-3]
    minute = (booked[i][0])[-2:]
    time = int(hour+minute)
    booked[i][0] = time    


for i in range(len(unbooked)):
    hour = (unbooked[i][0])[-5:-3]
    minute = (unbooked[i][0])[-2:]
    time = int(hour+minute)
    unbooked[i][0] = time    

if booked[0][0] < unbooked[0][0]:
    #55분 시간때문에 조건문
    if (booked[0][0])[-2] >= 55:
        time = booked[0][0] + 50
        answer.append(booked[0][1])
    else:
        time = booked[0][0] + 10
        answer.append(booked[0][1])
else:
    if (unbooked[0][0])[-2] >= 55:
        time = booked[0][0] + 50
        answer.append(unbooked[0][1])
    else:
        time = unbooked[0][0] + 10
        answer.append(unbooked[0][1])
