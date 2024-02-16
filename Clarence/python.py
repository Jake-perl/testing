import pygame

print("Hello Clarence")

name = clarence
if name = clarence
  print("Welcome Clarence")
elif name = Jake
  print("Hello Jake")
else
  print("Hello.")
class Game:
    def __init__(self):
        self.code = "clarence"
        self.horse_position = 0
        self.fodder_position = 10
        self.obstacle_position = 5

    def start(self):
        entered_code = input("Enter the code to start the game: ")
        if entered_code.lower() != self.code:
            print("Wrong code. You can't play the game.")
            return
        print("Welcome to the Horse Jumping Game!")
        while True:
            self.play_turn()

    def play_turn(self):
        action = input("Enter 'jump' to jump, 'collect' to collect fodder, or 'quit' to quit the game: ")
        if action.lower() == "quit":
            print("You quit the game.")
            exit(0)
        elif action.lower() == "jump":
            if self.horse_position == self.obstacle_position:
                print("You successfully jumped over the obstacle!")
                self.obstacle_position += 5
            else:
                print("There was no obstacle to jump over.")
        elif action.lower() == "collect":
            if self.horse_position == self.fodder_position:
                print("You collected the fodder!")
                self.fodder_position += 10
            else:
                print("There was no fodder to collect.")
        else:
            print("Invalid action.")
        self.horse_position += 1

game = Game()
game.start()
