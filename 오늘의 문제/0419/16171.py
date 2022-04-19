words = input()
ans = input()

check = ''

for word in words:
    if '0' <= word <= '9':
        continue
    else:
        check += word

if check.find(ans) != -1:
    print(1)
else:
    print(0)