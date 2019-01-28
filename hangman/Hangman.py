"""
The Internship Program Developer Exam 2019
Hangman game
Developer:Thanakorn Amnajsatit
"""

import random
import re

from Category_1 import category as cat1
from Category_2 import category as cat2
from Category_3 import category as cat3
from Category_4 import category as cat4
from Category_5 import category as cat5

def main():
    #Categories รวมcategoryทั้งหมดไว้
    all_categories = [cat1,cat2,cat3,cat4,cat5]

    #Attributes
    choosed_category = select_Category(all_categories)
    guess_count = 10
    score = 0
    wrong_guessed = []
    shown_text = []

    #Check win or lose and main loop
    while(guess_count > 0 and len(choosed_category['Words']) > 0):
        #Random index of word to play
        indexOfword = random.randint(0, len(choosed_category['Words'])-1)

        #showHint
        showHint(choosed_category, indexOfword)

        #Convert real words to be hidden
        shown_text = hideWords(choosed_category, indexOfword)

        #Show text to play
        showProgress(shown_text, score, guess_count, wrong_guessed)

        #Show progress of guessing and guess the word
        while(True):
            #Get input
            answer = input("Guess:")
            if isEnglish(answer) == True and len(answer) == 1:
                #Check the answer & do case-insensitive
                if answer.lower() in choosed_category['Words'][indexOfword].lower(): #When you guess correct
                    if answer.lower() not in shown_text and answer.upper() not in shown_text: #เช็คว่าพิมตัวที่ถูกนี้ซ้ำไหม
                        for index in range(0, len(choosed_category['Words'][indexOfword])): #ไล่ใส่ตัวที่ถูกในส่วนแสดงผลให้หมด
                            if choosed_category['Words'][indexOfword][index].lower() == answer.lower():
                                 shown_text[index] = choosed_category['Words'][indexOfword][index]
                        score += 15
                        showProgress(shown_text, score, guess_count, wrong_guessed)
                    else:
                        print("You already answer this character.")
                else:
                    if answer.lower() not in wrong_guessed: #When you guess wrong
                        guess_count -= 1
                        wrong_guessed.append(answer.lower())
                        showProgress(shown_text, score, guess_count, wrong_guessed)
                    else:
                        print("You already try this character.")
            elif isEnglish(answer) == True and len(answer) > 1: #เช็คว่าถ้าพิมเกิน1ตัวอักษร
                print("Please type only one character.")
            else:
                print("That's not English character.")

            #เช็คว่าแพ้หรือชนะ
            result = resultChecker(choosed_category, shown_text, indexOfword, guess_count, score)

            #If you win or lose stop the loop
            if result == 'Win':
                #Bonus check
                bonus = bonusChecker(guess_count, score)
                score += bonus
                break
            elif result == 'Lose':
                break
    else:
        print("Your final score is "+str(score))

def hideWords(choosed_category, indexOfword):
    shown_text = []
    for character in choosed_category['Words'][indexOfword]:
        if character.isalpha():
            shown_text.append('-')
        else:
            shown_text.append(character)
    return shown_text

def showHint(choosed_category, indexOfword):
    print("")
    print("Hint: \""+choosed_category['Hint'][indexOfword]+"\"")
    print("")

def resultChecker(choosed_category, shown_text, indexOfword, guess_count,score):
    if '-' not in shown_text: #To go to the next word for guessing
        if len(choosed_category['Words']) > 0:
            print("")
            print("You win!!! Next word.")
            choosed_category['Words'].pop(indexOfword)
            choosed_category['Hint'].pop(indexOfword)
            shown_text.clear()
        else:
            print("You win this category!!!")
        return 'Win'
    elif guess_count < 1: #When you lose get out of loop
        print("You lose.")
        return 'Lose'

def bonusChecker(guess_count, score):
    if guess_count > 0:
        print("Bonus score per remaining guess is 1 x "+str(guess_count))
        return guess_count*1
    else:
        print("No bonus score per remaining guess")
        return 0
        

def showProgress(shown_text, score, guess_count, wrong_guessed):
    for character in shown_text:
        print(character, end="")
    print(" score "+str(score)+", remaining wrong guess "+str(guess_count), end="")
    if len(wrong_guessed) > 0:
        print(", wrong guessed: ", end="")
        for character in wrong_guessed:
            print(character, end=" ")
    print("")
    
def isEnglish(letters):
    if re.search('[a-zA-Z]', letters) == None:
        return False
    else:
        return True
    

def select_Category(categories):
    #เช็คว่ามีตั้งแต่ 1 category ขึ้นไป
    if len(categories) == 0:
        print("There's no categories.")
    else:
        #แสดงหมวดหมู่ทั้งหมดที่สามารถเลือกได้
        print("Select Category:")
        for category in categories:
            print(str(categories.index(category)+1)+"."+category['Name'])
        print("\n")
        print("Please choose numbers between 1-"+str(len(categories))+":")
    
    #ตรวจเช็คค่าที่รับเข้ามาให้ตรงเงื่อนไขในการรับInput
    while(True):
        try:
            choice = int(input("Choose: "))
            if choice in range(1,len(categories)+1):
                return categories[choice-1]
            else:
                print("Not a number between 1 - "+str(len(categories)))
                print("Try again...")
        except:
            print("Oops! That's not a number.")
            print("Try again...")

main()
