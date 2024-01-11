import os


def main():
    os.system('cls')
    print("Welcome to the auction program")
    bids = {}



    def get_details():
        while True:
            name = input("What is your name? ")
            if name.isalpha():
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Invalid input, please enter a text value.")
                continue

        while True: 
            try:
                bid_price = int(input("What is your Price? £"))
                os.system('cls')
                break
            except ValueError:
                os.system('cls')
                print("Invalid Input, please enter a number.")
                continue
        
        bids[name] = bid_price



    while True: 
        get_details()
        answer1 = input("Are there any other users that would like to bid? y/n: ").lower()
        if answer1 in ["n", "no"]: 
            os.system('cls')
            break
        elif answer1 in ["y","yes"]:
            continue
        else: 
            print("Invalid input, please enter yes or no. y/n")



    print(f"The winner is {max(bids, key=bids.get)} with a bid of £{max(bids.values())}")

    while True:
        answer2 = input("Would you like to start a new auction? y/n: ")
        if answer2 in ["n", "no"]: 
            os.system('cls')
            exit()
        elif answer2 in ["y","yes"]:
            main()
        else: 
            print("Invalid input, please enter yes or no. y/n")
            continue

main()




