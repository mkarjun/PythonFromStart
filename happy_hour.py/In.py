
affirmative=["Yes","yes","y","Y"]
negative=["No","no","n","N"]

answer = input(print("Do you want to hear a joke?"))
if answer in affirmative:
    print("Why did the chicken cross the road?")
    print("To get to the other side!")
elif answer in negative:
    print("Fine.")
else:
    print("-\('-')/-")