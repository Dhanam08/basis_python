import random
print("Guessing the number GAME")
print("=============================")
game_on=None
guesses = None
secret= None
def diff_level_easy():
    global secret
    secret = int(random.randrange(0,100))
    while game_on:
        guess=int(input("Guess a number:"))
        if guess > secret:
            print("guess is too high")
        elif guess < secret:
            print("guess is too low")
        elif guess == secret:
            print("You Win!")
            play_again()

def diff_level_hard():
    global guesses
    global secret
    guesses=3
    secret = int(random.randrange(0,100))
    for i in range(guesses):
        guess=int(input("Guess a number:"))
        
        if i ==2:
            print("game over!, Try again")
            play_again()
        elif guess > secret:
            print("guess is too high")
        elif guess < secret:
            print("guess is too low")
        elif guess == secret:
            print("You Win!")
            play_again()
def start_game():
    global game_on
    game_on = True
    
    level = raw_input("welcome,type easy,hard or quit:")
    if level == "easy":
        diff_level_easy()
    elif level == "hard":
        diff_level_hard()
    elif level == "quit":
        game_on = False
        print("Thankyou for playing")
def play_again():
    global game_on
    game_on = True
    play =raw_input("play again?,(Y/N):")
    if play == "Y":
        start_game()
    else: 
        game_on=False
        print("Thankyou for playing")
start_game()



    
        