import random
import time
import webbrowser

def roll_dice():
    return random.randint(1, 6)


def player_round():

    player_round_score = 0

    player_choice = input("Roll dice (r) or end your round (e): (r/e) ")
    time.sleep(1.1)

    while player_choice == "r" :
        dice_number = roll_dice()
        if dice_number == 1 :
            print("You rolled one.")
            player_round_score = 0
            print("Round Score: ",player_round_score)
            break
        else :
            print("You rolled",dice_number)
            player_round_score += dice_number
            print("Round Score: ",player_round_score)
            player_choice = input("Roll dice (r) or end your round (e): (r/e) ")
            time.sleep(1.1)
            if player_choice == "e" :
                break


    return player_round_score



def computer_round():
    computer_round_score = 0

    while True :
        if computer_round_score == 0 :
            dice_number = roll_dice()
            if dice_number == 1 :
                print("Computer rolled one.")
                time.sleep(1.1)
                computer_round_score = 0
                print("Computer round score: ",computer_round_score)
                break
            else :
                print("Computer rolled: ", dice_number)
                time.sleep(1.1)
                computer_round_score += dice_number

        if computer_round_score > 0 and computer_round_score <= 10 :
            probability = random.random()
            if probability >= 0.1 :
                dice_number = roll_dice()
                if dice_number == 1 :
                    print("Computer rolled one.")
                    time.sleep(1.1)
                    computer_round_score = 0
                    print("Computer round score: ",computer_round_score)
                    break
                else :
                    print("Computer rolled: ", dice_number)
                    time.sleep(1.1)
                    computer_round_score += dice_number
            else :
                print("Computer round score: ",computer_round_score)
                break

        if computer_round_score > 10 and computer_round_score <= 15 :
            probability = random.random()
            if probability >= 0.3 :
                dice_number = roll_dice()
                if dice_number == 1 :
                    print("Computer rolled one.")
                    time.sleep(1.1)
                    computer_round_score = 0
                    print("Computer round score: ",computer_round_score)
                    break
                else :
                    print("Computer rolled: ", dice_number)
                    time.sleep(1.1)
                    computer_round_score += dice_number
            else :
                print("Computer round score: ",computer_round_score)
                break

        if computer_round_score > 15 and computer_round_score <= 20 :
            probability = random.random()
            if probability >= 0.5 :
                dice_number = roll_dice()
                if dice_number == 1 :
                    print("Computer rolled one.")
                    time.sleep(1.1)
                    computer_round_score = 0
                    print("Computer round score: ",computer_round_score)
                    break
                else :
                    print("Computer rolled: ", dice_number)
                    time.sleep(1.1)
                    computer_round_score += dice_number
            else :
                print("Computer round score: ",computer_round_score)
                break

        if computer_round_score > 20 and computer_round_score <= 25 :
            probability = random.random()
            if probability >= 0.7 :
                dice_number = roll_dice()
                if dice_number == 1 :
                    print("Computer rolled one.")
                    time.sleep(1.1)
                    computer_round_score = 0
                    print("Computer round score: ",computer_round_score)
                    break
                else :
                    print("Computer rolled: ", dice_number)
                    time.sleep(1.1)
                    computer_round_score += dice_number
            else :
                print("Computer round score: ",computer_round_score)
                break
            
        if computer_round_score > 25 :
            probability = random.random()
            if probability >= 0.9 :
                dice_number = roll_dice()
                if dice_number == 1 :
                    print("Computer rolled one.")
                    time.sleep(1.1)
                    computer_round_score = 0
                    print("Computer round score: ",computer_round_score)
                    break
                else :
                    print("Computer rolled: ", dice_number)
                    time.sleep(1.1)
                    computer_round_score += dice_number
            else :
                print("Computer round score: ",computer_round_score)
                break

    return computer_round_score            






def game() :
    player_total_score = 0
    computer_total_score = 0
    winning_score = 100
    while player_total_score < winning_score and computer_total_score < winning_score :

        print("Player Turn.")
        time.sleep(1.1)
        player_total_score += player_round()
        print("Player Total Score: ",player_total_score)
        time.sleep(1.1)
        print("Computer Total Score: ", computer_total_score)

        time.sleep(1.1)

        if player_total_score >= winning_score :
            print("Player won.")
            break

        print("Computer Turn")
        time.sleep(1.1)

        computer_total_score += computer_round()
        print("Computer Total Score: ", computer_total_score)
        time.sleep(1.1)
        print("Player Total Score: ",player_total_score)

        time.sleep(1.1)

        if computer_total_score >= winning_score :
            print("Computer won.")
            break



while True :

    info = input("Welcome to the PIG dice game. If you don't know how to play, please press '1'. If you know press '2': ")

    if info == "1" :
        webbrowser.open("https://en.wikipedia.org/wiki/Pig_(dice_game)")
        info = input("If you learned. Press 2 to play: ")

    elif info == "2" :
        game()
        break

    else :
        print("Invalid choice.")


