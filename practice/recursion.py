
val=0
def count(n):
    global val
    if n<1:
        return 
    val+=n
    return count(n-1)
count(5)
print(val)