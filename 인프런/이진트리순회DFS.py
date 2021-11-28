import sys
sys.stdin=open("input.txt", "r")

def DFS(v):
	if v>7:
		return
	else:
		print(v, end=" ")
		# print(v, end=' ')(전위순회) 1 2 4 5 3 6 7
		DFS(v*2)
		# print(v, end=' ')(중위순회) 4 2 5 1 6 3 7
		DFS(v*2+1) 
		# print(v, end=' ')(후위순위) 4 5 2 6 7 3 1

if __name__=="__main__":
	DFS(1)