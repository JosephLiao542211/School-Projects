def hanoi1(n,s,b,e):
    if n==1:
        print('move disk 1','from',s,'to',e)
    else:
        hanoi1(n - 1, s, e, b)
        print('move disk', n, 'from', s, 'to', e)
        hanoi1(n - 1, b, s, e)


def hanoi2(n,s,b,e):

    hanoi1(n-1,s,e,b)
    hanoi1(n,s,b,e)
    print('move disk',n,'from',s,'to',e)
    hanoi1(n - 1, b, s, e)
    return

def hanoi3(n,s,b,e):
    hanoi2(n-1,s,e,b)
    hanoi1(n,s,b,e)
    print('move disk', n, 'from', s, 'to', e)
    hanoi2(n-1,b,s,e)

def hanoi4(n,s,b,e):
    hanoi3(n-1,s,e,b)
    hanoi1(n,s,b,e)
    print('move disk', n, 'from', s, 'to', e)
    hanoi3(n-1,b,s,e)
hanoi1(3,'A','B','C')