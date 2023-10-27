a=[4,2,5,7,12,9,6]

n = len(a)
swap_flag = False

while swap_flag == False:
    swaps=0
    for i in range(1,n):
        if a[i-1] < a[i]:
            a[i-1], a[i] = a[i], a[i-1]
            swaps+=1
    if swaps=0

print(a)

