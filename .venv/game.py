import random
import re
from colored import Fore, Style

class Game_Control:
    def __init__(self) -> None:
        self.__colors = ["r", "g", "b", "y"]  # possible colors
        self.__correct = []  # list with new order
    
    def __machine_answer(self):
        while len(self.__correct) < 4:
            self.__correct.append(random.choice(self.__colors))
        return self.__correct
    
    def __player_answer(self):
        combination = input(
            "Add combination with no commas ',', or spaces between letters. The colors are 'r' for red, 'b' for blue, 'y' for yellow, and 'g' for green: "
        )
        pattern = r'^[rbgy]{4}$'
        if not re.match(pattern, combination):
            print("Please add a valid combination ex: brbr, bryg, bbbb, yyrb")
            return self.__player_answer()
        else:
            combination = list(combination)
            self.__correct = combination
            return combination
    
    def __player_or_machine(self):
        option = input("If you would like to make the combination, press 'y'. If you want the computer to create the combination, press 'f': ")
        if option.lower() == "f":
            return self.__machine_answer()
        elif option.lower() == "y":
            return self.__player_answer()
        else:
            print("Please press 'y' or 'f'.")
            return self.__player_or_machine()
    
    def get_correct(self):
        return self.__correct

class Guesser:
    def __init__(self) -> None:
        self.__attempts = 0  # quantity of attempts player has made 
        self.__guess = None
    
    def __attempt(self):
        self.__guess = list(input("Please introduce your attempt: "))  # player guess
        self.__attempts += 1  # increase attempts
        return self.__guess
    
    def __analizing_answer(self, correct, player_combination):
        result = []
        for g, c in zip(self.__guess, correct):
            if g == c:
                result.append('exact')
            elif g in correct:
                result.append('close')
            else:
                result.append('wrong')
        return result
    
    def get_attempts(self):
        return self.__attempts

class Board:
    def __init__(self) -> None:
        self.__perfect = f'{Fore.green}☻ {Style.reset}'  # smile for when they guess the exact spot
        self.__almost = f'{Fore.yellow}☻ {Style.reset}'  # smile for when it is in the array but not in the exact position
        self.__wrong = '☻ '  # smile for where it isn't in the combination
        self.__r = f'{Fore.red}☻ {Style.reset}'
        self.__b = f'{Fore.blue}☻ {Style.reset}'
        self.__g = f'{Fore.green}☻ {Style.reset}'
        self.__y = f'{Fore.yellow}☻ {Style.reset}'
        self.default = [self.__wrong, self.__wrong, self.__wrong, self.__wrong]  # a default where everything is gray until player tries
        self.rows = [self.default[:] for _ in range(12)]  # Initialize 12 rows with the default pattern
    
    def __creating(self, results, tries, attmpcomb):
        attemptrow = []
        for i in attmpcomb:
            if i == "r":
                attemptrow.append(self.__r)
            elif i == "g":
                attemptrow.append(self.__g)
            elif i == "b":
                attemptrow.append(self.__b)
            else:
                attemptrow.append(self.__y)
        
        resultrow = []
        for i in results:
            if i == "exact":
                resultrow.append(self.__perfect)
            elif i == "close":
                resultrow.append(self.__almost)
            else:
                resultrow.append(self.__wrong)
        
        # Combine the attempt and result into a single row for display
        combined_row = attemptrow + [' | '] + resultrow
        self.rows[tries] = combined_row  # Update the board's row with the current attempt and result
    
    def display_board(self):
        print("*******************************************")
        for row in self.rows:
            print(' '.join(row))  # Join each row's elements with a space for display

if __name__ == "__main__":
    game = Game_Control()
    player_combination = game._Game_Control__player_or_machine()
    correct_sequence = game.get_correct()
    
    guesser = Guesser()
    board = Board()
    
    while guesser.get_attempts() < 12:
        guess = guesser._Guesser__attempt()
        results = guesser._Guesser__analizing_answer(correct_sequence, player_combination)
        board._Board__creating(results, guesser.get_attempts() - 1, guess)
        board.display_board()  # Display the board after each attempt
        
        if results == ["exact"] * 4:
            print("Congratulations! You've guessed the correct combination.")
            break
    else:
        print("Sorry, you've reached the maximum number of attempts.")
