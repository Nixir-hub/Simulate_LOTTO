import random

def LOTTO_game():
    """
    Its console LOTTO game
    Try your luck!
    :return: compare player cupon to lucky_cupon
    """
    print("Lotto Game")
    print("Choose 6 numbers between from 1 to 49 ")
    user_cupon = []
    lucky_cupon = []
    while len(user_cupon) < 6:
        lucky_numbers = []
        lucky_number = random.randint(1, 49)
        if lucky_number not in lucky_cupon:
            lucky_numbers.append(lucky_number)  #adds lucky number to list lucky_numbers
        elif lucky_number == 1:
            lucky_numbers.append(lucky_number + 1)
        else:
            lucky_numbers.append(lucky_number - 1)
        user_numbers = []
        user_choice = input(f"Write your number {len(user_cupon) + 1}:")
        try:
            if int(user_choice) == ValueError:    #if input is not int() raise ValueError
                break
            elif 1 > int(user_choice) or int(user_choice) > 49:
                print("Number must be in range 1 - 49!")
            elif int(user_choice) not in user_cupon:
                user_numbers.append(int(user_choice))
            else:
                print("You must pick 6 diffrent numbers!")
            user_cupon += user_numbers
            lucky_cupon += lucky_numbers
        except ValueError:
            print("Pick number!")
        print(f"Your cupon: {sorted(user_cupon)}")
    print(f"Win numbers: {sorted(lucky_cupon)}")
    return f'Your matching numbers: {set(sorted(user_cupon)) & set(sorted(lucky_cupon))}'  #compare usercupon with_lucky

print(LOTTO_game())
