def noufi_cards():
    c1,c2,c3=input().split()
    d={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'D':8,'G':9,'K':10,}
    c=(d[c1] + d[c2] + d[c3])%10
    if c==0:print("Karaa")
    elif c==9:print("Noufi")
    else:print(c)

    # LyGolv:
    p=print
    d={'D':8,'G':9,'K':10,}
    a=sum(int(x)if x in"1234567"else d[x]for x in input().split())%10 # 1 2 3
    if a==0:p("Karaa")
    elif a==9:p("Noufi")
    else:p(a)
