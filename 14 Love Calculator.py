# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name=name1 + name2
lower_name=name.lower() #all aplphabet in small
#TRUE
t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")
true= t+r+u+e

#LOVE
l=lower_name.count("l")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")
love=l+o+v+e

#combine TRUE LOVE
score=str(true)+ str(love) #    in str
love_score=int(score) #converted into int

if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
