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

print(f"you will {random_bar}  {random_person} and get a {random_career} career")
