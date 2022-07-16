import random

bars = ["Pass",
        "Fail"]

people = ["Btech",
          "Degree"]

career = ["good",
          "bad"]          

random_bar = random.choice(bars)
random_person = random.choice(people)
random_career = random.choice(career)

print(f"You will {random_bar}  {random_person} \n and get a {random_career} career")
