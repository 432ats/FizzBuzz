A = []
m = 0
k = 0
f = open('input.txt')

data1 = f.read()  
f.close()
lines1 = data1.split('\n')

for line in lines1:
    A.append(line.split(':'))
m = A[-2][0]
A.pop(-1)
A.pop(-1)

new_A = sorted(A)

for i in range(len(new_A)):
    if int(m)%int(new_A[i][0]) == 0:
        k = 1
        print(new_A[i][1], end='')
        
if k == 0:
    print(m)
