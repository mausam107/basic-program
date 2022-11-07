# x=[[1]]*2
# print(x)
# x[0].append(2)
# print(x)

# var1=True
# var2=False
# var3=False
# if var1 or var2 and var3 :
#     print("True")
# else:
#     print("False")

# a={}
# b={1}
# print(type(a)) #dic
# print(type(b)) #set
# print( type(a) == type(b))

n = int(input())
my_list=[]
m=input()
k=m.split(" ")
res = [eval(i) for i in k]
for i in range(0,n):
    my_list.append(res[i])
plus=0
minus=0
zero=0
for i in range(0,n):
    if my_list[i]>0:
        plus+=1
    if my_list[i]<0:
        minus+=1
    if my_list[i]==0:
        zero+=1
print(round(plus/n,6))
print(round(minus/n,6))
print(round(zero/n,6))
        
    
            
        
