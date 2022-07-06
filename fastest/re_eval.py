def re_eval(s="1+2*3"):
    import re
    a, *d = re.findall('\d+', s)
    o = re.findall('[^\d]', s)

    for i,j in zip(o, d):
        a = str(eval(a+i+j))

    print(a)


def re_eval_mod(s="+2*4+1*2-5"):
    import re
    a, *d = re.findall('\d+', s)  # unpack list
    o = re.findall('[^\d]', s)

    print(list(zip(o, d)))  # test regex

    for i, j in zip(o, d):  # create tuple
        a = str(eval(a + i + j))

    print(a)




