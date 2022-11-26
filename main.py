import tkinter as tk
from random import choices
import time

root = tk.Tk()


class App:

    correct_words = 0

    def __init__(self, master):
        
        self.master = master
        master.title ("Typing Test")
        master.geometry ("1000x1000")
        master.configure (bg = "#A4A6D6")

        self.sentences = ["Good morning! I would like something to eat, please!",
                        "This coffee is delicious! How do you make it?",
                        "How are you doing? Hope you have a wonderfull day!",
                        "Happiness can be found in the depths of chocolate pudding.",
                        "He loved eating his bananas in hot dog buns.",
                        "The door slammed on the watermelon.",
                        "I caught my squirrel rustling through my gym bag."
                        "The external scars tell only part of the story.",
                        "The fish listened intently to what the frogs had to say.",
                        "He was sitting in a trash can with high street class.",
                        "I'll have you know I've written over fifty novels",
                        "Flash photography is best used in full sunlight."
                        "He was disappointed when he found the beach to be so sandy and the sun so sunny.",
                        "He had unknowingly taken up sleepwalking as a nighttime hobby.",
                        "Homesickness became contagious in the young campers' cabin.",
                        "The efficiency with which he paired the socks in the drawer was quite admirable.",
                        "You'll see the rainbow bridge after it rains cats and dogs.",
                        "I'd always thought lightning was something only I could see.",
                        "It was always dangerous to drive with him since he insisted the safety cones were a slalom course.",
                        "Not all people who wander are lost."
                        "After fighting off the alligator, Brian still had to face the anaconda."
                        "There was no ice cream in the freezer, nor did they have money to go to the store."
                        "Today I bought a raincoat and wore it on a sunny day."
                        "I'm confused: when people ask me what's up, and I point, they groan."
                        "The llama couldn't resist trying the lemonade.",
                        "Facing his greatest fear, he ate his first marshmallow.",
                        "Bill ran from the giraffe toward the dolphin.",
                        "Harrold felt confident that nobody would ever suspect his spy pigeon.",
                        "His mind was blown that there was nothing in space except space itself.",
                        "I may struggle with geography, but I'm sure I'm somewhere around here.",
                        "The toy brought back fond memories of being lost in the rain forest.",
                        "Malls are great places to shop; I can find everything I need under one roof.",
                        "The swirled lollipop had issues with the pop rock candy.",
                        "Before he moved to the inner city, he had always believed that security complexes were psychological.",
                        "She was sad to hear that fireflies are facing extinction due to artificial light, habitat loss, and pesticides.",
                        "She couldn't decide of the glass was half empty or half full so she drank it."

]

        self.main_label = tk.Label (master, width = 50, text = "1. Click the start button.\n\n2. After typing the sentence, press enter on your keyboard.",
        font = "Arial 14 bold", bg = "#A4A6D6")
        self.start_button = tk.Button (master, width = 30, height = 2, text = "Start", command = self.start, bg = "#7f68a8", highlightthickness = 0)
        self.display_label = tk.Label (master, bg = "#A4A6D6")
        self.display_time = tk.Label (master, bg = "#A4A6D6")
        self.sentence_input = tk.Entry (master, borderwidth = 0, width = 50)

        self.results = tk.Label (master, bg = "#A4A6D6", font = "Arial 12 bold")

        self.main_label.pack(pady = 20)
        self.start_button.pack(pady = 10)
        self.display_time.pack(pady = 20)
        self.display_label.pack(pady = 5)

        self.master.bind('<Return>', self.analysis)

    def start(self):
        #resets correct words if user decides to redo the test
        self.correct_words = 0
        self.start_button.configure (text = "Try again")

        self.sentence_input.delete (0, tk.END)
        self.sentence = choices(self.sentences)
        self.sentence = "".join(self.sentence).replace("{", "").replace("}", "")
        self.display_label.configure (text = self.sentence, font = "Arial 12 bold")
            
        self.sentence_input.pack()
        time.sleep(1)
        
        self.start_time = time.time()

    def analysis(self, event):

        self.elapsed_time = round(time.time() - self.start_time) - 1
        # Since the user will have to use more time to click on the text box, 1 second will be removed from the elapsed time.

        self.user_sentence = self.sentence_input.get().split()
        self.displayed_sentence = self.sentence.split()

        if len(self.user_sentence) == len(self.displayed_sentence):

            for word in self.displayed_sentence:             

                if word == self.user_sentence[self.displayed_sentence.index(word)]:

                    self.correct_words += 1

                else:

                    continue

        elif len(self.user_sentence) != len(self.displayed_sentence):

            if len(self.user_sentence) < len(self.displayed_sentence):

                self.delete_margin = (len(self.displayed_sentence) - len(self.user_sentence))

                self.modified_displayed_sentence = self.displayed_sentence[:-(self.delete_margin)]
                print (self.modified_displayed_sentence)

            elif len(self.user_sentence) > len(self.displayed_sentence):
                
                self.delete_margin = (len(self.user_sentence) - len(self.displayed_sentence))
                self.user_sentence = self.user_sentence[:-(self.delete_margin)]
                self.modified_displayed_sentence = self.displayed_sentence
                print (self.user_sentence)

            for word in self.modified_displayed_sentence:

                if word == self.user_sentence[self.modified_displayed_sentence.index(word)]:

                    self.correct_words += 1

                else:

                    continue

        self.accuracy = round(self.correct_words/(len(self.displayed_sentence) - (self.displayed_sentence.count(" "))) * 100)
        self.wpm = round(len(self.user_sentence) - (self.user_sentence.count(" "))/5)/(self.elapsed_time/60)

        self.results.configure (text = str(self.wpm) + " WPM, with " + str(self.accuracy) + "% accuracy.")
        self.results.pack(pady = 10)


if __name__ == "__main__":
    
    App (root)
    root.mainloop()
