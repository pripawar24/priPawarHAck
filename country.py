from itertools import accumulate
# c=int(input())
# s=int(input())
# month=int(input())
# l=list(map(int,input().split(",")))[:c]
c=12
s=3
month=7
l=[4,5,7,9,3,2,5,1,3,2,4,1]
chunked_list = list()
chunk_size = 3
for i in range(0, len(l), chunk_size):
    chunked_list.append(l[i:i+chunk_size])
print(chunked_list)

new_m=len(l)-month
l_m=[]
for j in range(1,len(l)):
    if j==new_m:
        for k in range(s):
            l_m.append(l[j-k])
print()
             