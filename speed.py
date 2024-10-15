from time import *
import random as r



def mistakes(partest,usertest):
      error=0
      for i in range(len(partest)):
            try:
                  if partest[i]!=usertest[i]:
                        error=error+1
            except:
                  error=error+1
      return error


def speed_time(time_s,time_e,user_input):
      time_delay=time_e-time_s
      time_R=round(time_delay,2)
      speed=len(user_input)/time_R
      return round


test=["my self vivek arya","from uttam nagr east"]
 
test1=r.choice(test)
print("***typing speed***")
print(test1)
print()
print()
time_1=time()
testinput=input("ENTER :")
time_2=time()

print('speed:',speed_time(time_1,time_2,testinput),"w/s ")
print("error:",mistakes(test1,testinput))