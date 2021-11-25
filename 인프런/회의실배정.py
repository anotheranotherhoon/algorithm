n=int(input())
meeting=[]
for i in range(n):
	s, e = map(int, input().split())
	meeting.append((s,e))
#정렬 기준을 x[1] << 끝나는 시간으로 만약 끝나는 시간이 같다면 두 번째 x[0]의 순서대로 정렬
meeting.sort(key=lambda x :(x[1], x[0]))
et=0
cnt=0
for s, e in meeting:
	if s >= et:
		et=e
		cnt+=1
print(cnt)