a=int(input())
for i in range (1,a+1):
    if (i%10==1 or i==1) and i!=11:
        print("На лугу", i,"корова")
    elif (i%10==2 or i%10==3 or i%10==4) and (i!=12 and i!=13 and i!=14):
        print ("На лугу", i,"коровы")
    else:
        print("На лугу", i,"коров")  