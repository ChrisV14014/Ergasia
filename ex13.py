n= int(input("Είσαγε αριθμό ψηφίων"))
s= int(input("Είσαγε άθροισμα ψηφίων"))
maxn=(10**n)-1
minn=10**(n-1)
nums=[]
while (minn<=maxn) :
     nums.append(minn)
     minn+=1
def sum(num):
    global tmp
    tmp += num%10
    num //= 10
    if num<10:
        tmp+=num
        return tmp
    else:
        return sum(num)
final=[]
for i in nums:
    tmp=0
    sumn=sum(i)
    if sumn==s :
        final.append(i)
print (final)