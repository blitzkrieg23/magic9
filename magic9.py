import random

name = "John"

question = "Will I win the lottery?"

answer = ""

print(name + " asks:" + question)
random_number = random.randint(1,9)
print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
  print("Magic 9-Ball's answer: "+answer)
elif random_number == 2:
  answer =" It is decidedly so"
  print("Magic 9-Ball's answer: "+answer)
elif random_number == 3:
  answer = "Without a doubt"
  print("Magic 9-Ball's answer: "+answer)
elif random_number == 4:
  answer = "Reply hazy, try again"
  print("Magic 9-Ball's answer: "+answer)
elif random_number == 5:
  answer = "Ask again later"
  print("Magic 9-Ball's answer: "+answer)
elif random_number == 6:
  answer = "Better not tell you now"
  print("Magic 9-Ball's answer: "+answer)
elif random_number == 7:
  answer = "My sources say no"
  print("Magic 9-Ball's answer: "+answer)
elif random_number == 8:
  answer = "Outlook not so good"
  print("Magic 9-Ball's answer: "+answer)
elif random_number == 9:
  answer = "Very doubtful"
  print("Magic 9-Ball's answer: "+answer)
else:
  print("Error")