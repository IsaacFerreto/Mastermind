import random
import re
from colored import Fore, Style


class Game_Control:

    # possible option created
    def __init__(self) -> None:
        self.__colors=["r","g","b","y"] #possible colors
        self.__correct=[]#list with new order
        
    
    def __machine_answer(self):#method created, to create a new list
        while len(self.__correct)<4:#this is going to make the list to be 4
            self.__correct.append(random.choice(self.__colors))#add the color to the list
        print(self.__correct)
        
    def __player_answer(self):
        combination=input("Add combination with no commas ',', or spaces between letters the  colors are 'r' for red, 'b' for blue, 'y' for yellow and 'g' for green: " )
        pattern= r'^[rbgy]{4}$'
        if not re.match(pattern,combination):
            print("please add a valid combination ex: brbr,bryg,bbbb,yyrb")
            
            return self.__player_answer()
        else:
            combination=list(combination)
            return combination 
        
    def __player_or_machine(self):
        option=input("if you would like to make the combination press 'y' if you want the computer to create the combination press 'f': ")
        
        if option.lower()=="f"or option.lower()=="y":
            if option.lower()=="y":
                
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
        self.__attempts=0#quantity of attempts player has made 
        self.__guess = None
        
        pass
    
    
    def __attempt(self):
        self.__guess=list(input("please introduce your attempt: "))#player guess i want to sent this to board
        self.__attempts+=1#we have to add one to it every time
        return self.__guess
    
    def __analizing_answer(self,correct,composition):
        result = []
        if correct ==[]:
            pattern=composition
        else:
            pattern=correct    
        for g, c in zip(self.__guess, pattern):
            if g == c:
                result.append('exact')
            elif g in correct:
                result.append('close')
            else:
                result.append('wrong')
        print(result)  # You could use the `Board` class to display these results
        return result
        pass
        
        
    def get_attempts(self):
        return self.__attempts#to send this to board  
     
    
    
    
    
class Board:
    def __init__(self) -> None:
        self.__perfect=f'{Fore.green}☻ {Style.reset}'#smile for when they guess the exact spot
        self.__almost=f'{Fore.yellow}☻ {Style.reset}'#smile for when it is on the array but not in the exact position
        self.__wrong='☻ '#smile for where it isn't on the combination
        self.deffault=[self.__wrong, self.__wrong, self.__wrong, self.__wrong]#a default where everything is going to be gray until player tries
        self.rows = [self.deffault[:] for _ in range(12)]  # Initialize 12 rows with the default pattern
            
    
    def __creating(self,results,tries):  
        rows=[]#empty array to create a matrix with the guesses
        temp_array=[]
        for i in results:#this cycle use results to add them to a temporary arraay to push 
            print(i)
            if i =="exact":
                temp_array.append(self.__perfect)
                
            elif i=="close":
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
    
    while guesser.get_attempts() < 12:
        guess = guesser._Guesser__attempt()
        results = guesser._Guesser__analizing_answer(correct_sequence, player_combination)
        board._Board__creating(results, guesser.get_attempts() - 1)  # Use `get_attempts() - 1` because lists are zero-indexed

        if results == ["exact"] * 4:
            print("Congratulations! You've guessed the correct combination.")
            break
    else:
        print("Sorry, you've reached the maximum number of attempts.")
    
         
                
                        
                