n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
i = j = 0
c = []
while i < n and j < m:
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
if j < m:
    c += b[j:]
if i<n:
    c += a[i:]
