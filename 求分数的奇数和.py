#求1到1/19之间的奇数和

a=0
for i in range(1,20,2):
    a=a+1/i
    
print("和是:",a)
