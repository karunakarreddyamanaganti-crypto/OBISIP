name=input("enter your name:")
print("hello",name)
weight=float(input("enter your weight (kg)"))
height=float(input("enter your height (cm)"))
height=height/100
bmi=weight/(height*height) 
print ("your BMI is:",round(bmi,2))
if bmi<18.5:
 print("category:Under weight")
elif bmi<25:
 print("category:Normal weight")
elif bmi<30:
 print("category:Over weight")
else: print("category:Obese") 








            