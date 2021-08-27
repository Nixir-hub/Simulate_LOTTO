import random

print("Lotto Game")
print("Choose 6 numbers between from 1 to 49 ")



def LOTTO_game():
    user_cupon = []
    lucky_cupon = []
    while len(user_cupon) < 6:
        lucky_numbers = []
        lucky_number = random.randint(1, 49)
        lucky_numbers.append(lucky_number)
        user_numbers = []
        user_choice = input(f"Write your number {len(user_cupon) + 1}:" )
        try:
            if int(user_choice) == ValueError:
               break
            elif 1 > int(user_choice) or int(user_choice)> 49:
                print("Number must be in range 1 - 49!")
            elif int(user_choice) not in user_cupon:
                user_numbers.append(int(user_choice))
            else:
                print("You must pick 6 diffrent numbers!")
            user_cupon += user_numbers
            lucky_cupon += lucky_numbers
        except ValueError:
                print("Pick number!")
        print("Your cupon: ", sorted(user_cupon))
    return f"Win numbers: {lucky_cupon}"

print(LOTTO_game())