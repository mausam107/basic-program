small="abcdefghijklmnopqrstuvwxyz"
capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesarCipher(s, k):
    if k <26:
        a= small[0:k]
        b=small[k:26]
        c=b+a
        e= capital[0:k]
        f=capital[k:26]
        g=f+e
    else :
        k = k%26
        a= small[0:k]
        b=small[k:26]
        c=b+a
        e= capital[0:k]
        f=capital[k:26]
        g=f+e
    for i in range(0,len(s)):
        if s[i].islower() == True:
            d= small.find(s[i])
            print(c[d],end="")
        elif s[i].isupper() == True:
            d= capital.find(s[i])
            print(g[d],end="")
        else:
            print(s[i],end="")

caesarCipher("www.abc.xy", 87)
