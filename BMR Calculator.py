g=input("enter male or female")
h=int(input("enter the height in cm : "))
a=int(input("enter the age in years : "))
w=int(input("enter the weight in kg : "))
male =88.362+(13.397*w)+(4.799*h)-(5.677*a)
female =447.593+(9.247*w)+(3.098*h)-(4.330*a)
if g=="male":
  if male<=1599:
    print ("you are lesser than the normal")
    print("Tips to increase 1.Eat protien at every meal 2.Drink more cold water 3.Do a high intensity workout 4.Lift heavy things 5.Get a good sleep")
  elif 1600>male<1800:
    print ("you are normal")
  else:
    print ("you are in obesity kindly go to checkup")
    print ("1.Healthy eating plan and regular physical activity 2.Weight management programs 4.consume less processed and sugary foods 4. Eat plenty of dietary fiber")
else:
  if female<=1399:
    print ("you are lesser than the normal")
    print("Tips to increase 1.Eat protien at every meal 2.Drink more cold water 3.Do a high intensity workout 4.Lift heavy things 5.Get a good sleep")
  elif 1400< female<1699:
    print ("you are normal")
  else:
    print ("you are in obesity kindly go to checkup")
    print ("1.Healthy eating plan and regular physical activity 2.Weight management programs 4.consume less processed and sugary foods 4. Eat plenty of dietary fiber")
