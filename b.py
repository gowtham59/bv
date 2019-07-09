bu1=input()
cnt2=0
for p3 in range(0,len(bu1)):
    if(bu1[p3].isdigit() or bu1[p3].isalpha() or bu1[p3]==' '):
        continue
    else:
        cnt2=cnt2+1
print(cnt2)
