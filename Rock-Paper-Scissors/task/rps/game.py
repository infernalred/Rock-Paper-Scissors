import random


class RockPaperScissors:
    def __init__(self):
        self.user_input = None
        self.comp_choose = None
        self.list = ("rock", "paper", "scissors")
        self.name = None
        self.score = 0
        self.table_wins = {}

    def run(self):
        self.name = input("Enter your name: ")
        print(f"Hello, {self.name}")
        new_list = input().split(",")
        if len(new_list) > 1:
            self.list = new_list
        print("Okay, let's start")
        while True:
            self.comp_choose = random.choice(self.list)
            self.user_input = input()
            if self.user_input == "!exit":
                break
            elif self.user_input == "!rating":
                print(self.print_rating())
            elif self.user_input not in self.list:
                print("Invalid input")
                continue
            else:
                print(self.find_win())

    def print_rating(self):
        return f"Your rating: {self.score}"

    def find_win(self):
        if self.comp_choose == self.user_input:
            self.score += 50
            return f"There is a draw ({self.comp_choose})"
        elif self.who_win():
            self.score += 100
            return f"Well done. Computer chose {self.comp_choose} and failed"

        return f"Sorry, but computer chose {self.comp_choose}"

    def load_table_win(self):
        file = open("rating.txt", "r")
        for line in file.readlines():
            name, rating = line.split()
            self.table_wins[name] = int(rating)
        if self.name in self.table_wins:
            self.score = self.table_wins[self.name]
        file.close()

    def write_table(self):
        file = open("rating.txt", "w")
        file.writelines(self.table_wins)

    def who_win(self):
        x = self.list.index(self.comp_choose)
        y = self.list.index(self.user_input)
        l = len(self.list) // 2
        return x < y and y - x <= l or y < x and x - y > l


rps = RockPaperScissors()
rps.run()
