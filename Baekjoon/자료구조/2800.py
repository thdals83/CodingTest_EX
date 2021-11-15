from itertools import combinations
str = input()

stack = []
match = []
final = []
for i in range(len(str)):
    if str[i] == '(':
        stack.append(i)
    elif str[i] == ')':
        num = stack.pop()
        match.append([i, num])


for i in range(1,len(match)+1):
    for com in list(combinations(match,i)):
        cut = []
        res = []
        for c in com:
            cut.append(c[0])
            cut.append(c[1])
        for j in range(len(str)):
            if j in cut:continue
            else: res.append(str[j])

        final.append(''.join(res))
final = list(set(final))

for i in sorted(final):
    print(i)
