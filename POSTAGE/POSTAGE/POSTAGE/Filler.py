for _ in range(int(input())):
n = int(input())
res = [-1] * (n+1)
p = 0
s = SortedList(list(range(1,1+n)))
for i in range(1, n+1):
x = (p + i) % len(s)
res[s[x]] = i
p = x
s.remove(s[x])
print(*res[1:])