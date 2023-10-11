#CHATBOT WITH RULE-BASED

#Importing the required libraries

import re
import random


#Chatbot class
class rule_chatbot:

  def __init__(self, language1, language2, language3):
    self.languages = [language1, language2, language3]
    self.vocabulary = {
        'hello': {
            'translations': {
                'English': 'hello',
                language1: 'hola',
                language2: 'bonjour',
                language3: 'hallo'
            },
            'part_of_speech': 'greeting'
        },
        'goodbye': {
            'translations': {
                'English': 'goodbye',
                language1: 'adiós',
                language2: 'au revoir',
                language3: 'verabschiedung'
            },
            'part_of_speech': 'farewell'
        },
        'thank you': {
            'translations': {
                'English': 'thank you',
                language1: 'gracias',
                language2: 'merci',
                language3: 'danke'
            },
            'part_of_speech': 'expression of gratitude'
        },
    }
    self.selected_language = None

  def start_learning(self):
    while True:
      self.learn_word()
      continue_learning = input(
          "Do you want to continue learning? (yes/no): ").lower()
      if continue_learning != 'yes':
        print("Thank you for learning with us. Have a good day!\n")
        break

  def learn_word(self):
    word = random.choice(list(self.vocabulary.keys()))
    translations = self.vocabulary[word]['translations']
    part_of_speech = self.vocabulary[word]['part_of_speech']

    print(
        f"Your word to learn: {word.capitalize()} (Part of speech: {part_of_speech})"
    )
    print(f"Translations:")
    print(
        f"{self.selected_language.capitalize()}: {translations[self.selected_language]}\n"
    )

    user_translation = input(
        f"Enter the translation in {self.selected_language.capitalize()}: "
    ).lower()

    if user_translation == translations[self.selected_language]:
      print("Correct! Nice work!")
    else:
      print(
          f"Incorrect! The correct translation is: {translations[self.selected_language].capitalize()}"
      )

  def greet(self):
    self.name = input("What is your name?\n")
    print(f"Hi {self.name}, I am Rule_base_chatbot. We warmly welcome you here.\n")

  def make_exit(self, reply):
    for command in self.exit_commands:
      if reply == command:
        print("Okay, have a good day! See you soon!")
        return True

  def choose_language(self):
    self.greet()
    print("Available languages:")
    for index, lang in enumerate(self.languages, start=1):
      print(f"{index}. {lang}")

    while True:
      choice = input(
          "Choose the language by entering the corresponding number: ")
      if choice.isdigit() and 1 <= int(choice) <= len(self.languages):
        self.selected_language = self.languages[int(choice) - 1]
        print(f"Let's start learning {self.selected_language}!\n")
        break
      else:
        print("Choice is invalid. Please enter a valid number.")


# Create an instance of the rule_chatbot
language_bot = rule_chatbot(language1='Spanish',
                            language2='French',
                            language3='German')

# Choose the language
language_bot.choose_language()

# Start learning the choosen language
language_bot.start_learning()
