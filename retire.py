# This is a programming for calculating retirement age
# Created by Marshall
retirementAge = 65
print('What is your current age?')
current_age = int(input())

#Calculate years till retirement
yearsTillRetirement = retirementAge - current_age
yearsLeftPlural = f"You have {yearsTillRetirement} years left before retirement."
yearsLeftSingle = f"You have {yearsTillRetirement} year left before retirement."
if yearsTillRetirement > 1 and yearsTillRetirement < 65: 
    print(yearsLeftPlural)
elif yearsTillRetirement == 0:
    print("Congrats! You're at retirement age now.")
elif current_age > 65:
   yearsAbsolute = yearsTillRetirement.__abs__()
   print(f"You should've retired {yearsAbsolute} years ago.")
else:
    print(yearsLeftSingle)

#Calculate Net Worth
if yearsTillRetirement <= 65:
    print('We bellieve your net-worth should be $1 Mill by retirement age. What is your current net-worth?')
    net_worth = float(input())
    requiredNetWorth = 1000000 - net_worth
    if net_worth >= 1000000:
        print("Nice, you have more than enough to retire on time!")
    elif net_worth < 1000000 and yearsTillRetirement > 0:
        print(f"Thanks! It looks like you don't have enough to retire just yet! You'll need {requiredNetWorth} more in the next {yearsTillRetirement} year(s) in order to retire.")
    else:
        print(f"You don't have enough to retire. You needed to have had at least {requiredNetWorth} by 65.")

#Recap the information provided
    if yearsTillRetirement >= 0:
        print("All right let's recap! \nYou are {} year(s) old, you are {} year(s) away from retirement, and your net-worth is ${}.".format(current_age, yearsTillRetirement, net_worth))
    else:
        print("All right let's recap! \nYou are {} year(s) old, you should've retired {} year(s) ago, and your net-worth is ${}.".format(current_age, yearsTillRetirement.__abs__(), net_worth))

 
 