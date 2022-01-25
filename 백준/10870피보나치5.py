def fibonaci(num):
    if num <= 1:
        return num
    return fibonaci(num-1) + fibonaci(num-2)

num = int(input())
print(fibonaci(num))