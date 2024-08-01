import random
import re
from colored import Fore, Style

class Game_Control:
    def __init__(self) -> None:
        self.__colors = ["r", "g", "b", "y"] 
        self.__correct = [] 
        pass
    
    def __machine_answer(self):
        while len(self.__correct) < 4:
            one_color = random.choice(self.__colors)
            self.__correct.append(one_color)
        print(self.__correct)
        
    def __player_answer(self):
        combination = input("Add combination with no commas ',', or spaces between letters the  colors are 'r' for red, 'b' for blue, 'y' for yellow and 'g' for green: ")
        pattern = r'^[rbgy]{4}$'
        if not re.match(pattern, combination):
            print("please add a valid combination ex: brbr,bryg,bbbb,yyrb")
            return self.__player_answer()
        else:
            combination = list(combination)
            return combination 
        
    def __player_or_machine(self):
        option = input("if you would like to make the combination press 'y' if you want the computer to create the combination press 'f': ")
        if option.lower() == "f" or option.lower() == "y":
            if option.lower() == "y":
                return self.__player_answer()
            else:
                self.__machine_answer()
        else: 
            print("Please press  'y' or 'f': ")
            return self.__player_or_machine()
            
    def get_correct(self):
        return self.__correct                 
        
class Guesser:
    def __init__(self) -> None:
        self.__attempts = 0
        self.__guess = None
        pass
    
    def __attempt(self):
        self.__guess = list(input("please introduce your attempt: "))
        self.__attempts += 1
        return self.__guess
    
    def __analizing_answer(self, correct, composition):
        result = []
        if correct == []:
            pattern = composition
        else:
            pattern = correct    
        for g, c in zip(self.__guess, pattern):
            if g == c:
                result.append('exact')
            elif g in correct:
                result.append('close')
            else:
                result.append('wrong')
        print(result)
        return result
        pass
        
    def get_attempts(self):
        return self.__attempts  
    
class Board:
    def __init__(self) -> None:
        self.__perfect = f'{Fore.green}☻ {Style.reset}'
        self.__almost = f'{Fore.yellow}☻ {Style.reset}'
        self.__wrong = '☻ '
        self.deffault = [self.__wrong, self.__wrong, self.__wrong, self.__wrong]
        self.rows = [self.deffault[:] for _ in range(12)]  # Initialize 12 rows with the default pattern
        pass    
    
    def __creating(self, results, tries):  
        temp_array = []
        for i in results:
            if i == "exact":
                temp_array.append(self.__perfect)
            elif i == "close":
                temp_array.append(self.__almost)
            else:
                temp_array.append(self.__wrong)
                        
        self.rows[tries] = temp_array  # Update the corresponding row with the current results

        for row in self.rows:
            print(*row)

if __name__ == "__main__":
    game = Game_Control()
    player_combination = game._Game_Control__player_or_machine()
    correct_sequence = game.get_correct()

    guesser = Guesser()
    board = Board()
    
    max_attempts = 12
    while guesser.get_attempts() < max_attempts:
        guess = guesser._Guesser__attempt()
        results = guesser._Guesser__analizing_answer(correct_sequence, player_combination)
        board._Board__creating(results, guesser.get_attempts() - 1)  # Use `get_attempts() - 1` because lists are zero-indexed

        if results == ["exact"] * 4:
            print("Congratulations! You've guessed the correct combination.")
            break
    else:
        print("Sorry, you've reached the maximum number of attempts.")
