'''
- 문자열 S = 0과 1로 이루어짐
- 모든 숫자를 전부 같게 만들어야 함

- 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것
행동의 최소 횟수
'''

s = input()
cnt0 = 0
cnt1 = 0

before = s[0]
if before == "0":
    cnt0 += 1
else: cnt1 += 1

for i in range(1, len(s)):
    if before == s[i]:
        continue
    else:
        if s[i] == "0": cnt0 += 1
        else: cnt1 += 1
        before = s[i]

if cnt0 == cnt1: print(cnt0)
else:
    print(min(cnt0,cnt1))