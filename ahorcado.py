import random
import os

def run():
    
    FRAMES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    
    DB = [
        "PYTHON",
        "JAVASCRIPT",
        "PHP",
        "JAVA",
        "SQL",
        "PYTHON",
        "SWIFT",
        "KOTLIN"  
    ]
    
    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 0
    
    while True:
        os.system('cls')
        for character in spaces:
            print(character, end=" ")
        print(FRAMES[attemps])
        letter = input('Elije una letra:\r\n').upper()
        
        found = False
        
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
                
        if not found:
            attemps += 1
            
        if "_" not in spaces:
            os.system('cls')
            print('Felicidades!! Has ganado!!!')
            break
            input()
            
        if attemps == 6:
            os.system('cls')
            print('Oh no!! Has perdido !!!')
            break
            input()
            
if __name__ == '__main__':
    run()