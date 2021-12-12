a = int(input())

zero = [1,0,1]
one = [0,1,1]

def cal(num):
    length = len(zero)
    # 1,2,3 까지는 미리 구해놔서 구한 값을 바로 출력함. if 문에서 false
    if length <= num:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[num],one[num]))

for i in range(a):
    k = int(input())
    cal(k)
