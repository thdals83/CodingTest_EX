N = int(input())

con5 = -1
con3 = 0 

for i in range (int(N/5), -1, -1):
    if (N - 5 * i) % 3 == 0:
        con5 = i
        con3 = int((N - 5*i)/3) 
        break

print(con5+con3)