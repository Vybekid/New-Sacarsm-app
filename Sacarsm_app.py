import tkinter as tk
from tkinter import messagebox

class WhatSheSaysApp:
    def __init__(self, master):
        self.master = master
        master.title("What She Says vs. What She Really Means")
        master.geometry("600x450") # Set a default window size
        master.resizable(False, False) # Make window non-resizable

        # Styling
        self.bg_color = "#f0f0f0"
        self.button_color = "#4CAF50" # Green
        self.button_fg = "white"
        self.font_title = ("Helvetica", 16, "bold")
        self.font_label = ("Helvetica", 12)
        self.font_entry = ("Helvetica", 12)
        self.font_result = ("Helvetica", 14, "bold")
        self.master.config(bg=self.bg_color)

        # Load the interpretations dictionary
        self.interpretations = self.load_interpretations()

        # Create widgets
        self.create_widgets()

    def load_interpretations(self):
        # Your provided data converted into a dictionary for easy lookup
        # We'll store keys in lowercase for case-insensitive matching later
        data = {
            "He's just a friend.": "This is the guy you should be worried about.",
            "Do whatever you want.": "You better not.",
            "I'm not mad.": "Oh, I'm absolutely furious.",
            "I'm fine.": "I'm definitely not fine.",
            "It’s whatever.": "It's absolutely not whatever.",
            "I don’t care.": "I care deeply, and you should know why.",
            "No, really, go have fun.": "If you go, I will remember this forever.",
            "Do I look fat in this?": "Say no. Say it fast.",
            "You don’t have to get me anything.": "You better show up with something amazing.",
            "I’m not hungry.": "I’ll eat your food when it gets here.",
            "Nothing’s wrong.": "Everything is wrong.",
            "I’ll be ready in 5 minutes.": "Settle in, it's going to be a while.",
            "We need to talk.": "You’re in trouble.",
            "I don’t want to ruin the mood.": "I'm about to ruin the mood.",
            "You never listen to me.": "You forgot that one time 6 months ago.",
            "It’s not a big deal.": "It’s a HUGE deal.",
            "I guess.": "No, but I’m trying to be nice.",
            "Wow, okay.": "You’ve just crossed a line.",
            "Have fun.": "Don’t have too much fun.",
            "You decide.": "I’ll judge your decision.",
            "I’m over it.": "I’m not over it.",
            "I don’t need help.": "Help me without me asking.",
            "I’ll let you know.": "Don’t count on it.",
            "I love how honest you are.": "You should’ve lied.",
            "We’ll see.": "That’s a no.",
            "Maybe.": "Still no.",
            "It’s cute.": "It’s hideous, but I’m being polite.",
            "Do you remember what today is?": "You forgot something important.",
            "I’m not jealous.": "I'm burning with jealousy.",
            "I’ll think about it.": "I've already decided. No.",
            "It's fine, I'll do it myself.": "You better offer to help again.",
            "I don’t want to talk about it.": "Ask me again.",
            "Go ahead.": "If you do, you're dead.",
            "I’m just tired.": "I’m upset, but I’m not saying why.",
            "I don’t want a relationship.": "With *you*.",
            "I'm not like other girls.": "I'm just like other girls, but I need you to think I’m not.",
            "I’m not looking for anything serious.": "Until I find someone worth it.",
            "He’s like a brother to me.": "I hug him a little too long.",
            "Let’s just be friends.": "You’re not attractive to me.",
            "I’m over my ex.": "I still check his Instagram every night.",
            "You’re like a brother to me.": "There is absolutely no chance.",
            "You deserve better.": "I'm not into you.",
            "It’s not you, it’s me.": "It’s definitely you.",
            "We can still be friends.": "We’re never talking again.",
            "I just need some space.": "I want to ghost you gently.",
            "I’m focusing on myself right now.": "I'm not interested in you at all.",
            "I’m not ready for a relationship.": "Just not with you.",
            "Let’s take it slow.": "I’m unsure but keeping my options open.",
            "I’m not texting anyone else.": "Except for the 3 guys in my DMs.",
            "It’s not a date-date.": "It’s a date, but don’t get your hopes up.",
            "We’re just talking.": "I have no intention of committing.",
            "I’m low maintenance.": "Until I’m high maintenance.",
            "I’m chill.": "Until I’m not.",
            "I hate drama.": "But somehow I’m always in it.",
            "I’m not that into social media.": "I check every like and story view.",
            "I don't want anything for my birthday.": "You better have planned a surprise.",
            "You don’t have to text me all the time.": "Why aren’t you texting me all the time?",
            "I’m just emotional today.": "I'm mad, but you better figure out why.",
            "Let’s not ruin the night.": "Prepare for an emotional ambush later.",
            "I don’t usually do this.": "I do this more often than I admit.",
            "Be honest with me.": "But lie if it’ll hurt my feelings.",
            "We’re not exclusive, right?": "I’ll lose my mind if you are seeing someone else.",
            "I'm not that hungry.": "I'll eat your fries.",
            "I’m not wearing makeup.": "I spent 40 minutes perfecting this 'natural' look.",
            "I’m fine with whatever.": "There’s a right answer, and you better guess it.",
            "You didn’t have to do that!": "I’m so glad you did that!",
            "Do you love me?": "I'm insecure today. Reassure me.",
            "I don't want to fight.": "I’m about to fight.",
            "I’ve had worse.": "This is terrible.",
            "It's okay, I understand.": "I will hold this against you forever.",
            "Thanks for being honest.": "How dare you say that to me.",
            "I'm not upset.": "I'm raging inside.",
            "We don’t have to celebrate.": "I expect a celebration.",
            "You’re so sweet.": "I see you as a friend.",
            "You're different.": "You're less toxic, but still annoying.",
            "Let's keep things casual.": "Until I catch feelings and get mad when you don’t.",
            "You're overthinking.": "You're getting too close to the truth.",
            "That's interesting.": "That's stupid.",
            "I’m not one to gossip, but...": "Here comes the full story.",
            "I’m totally over it.": "I think about it every night.",
            "You’re like a best friend to me.": "Friend zone: Level 100.",
            "I love your honesty.": "Except when it's inconvenient.",
            "We should hang out sometime!": "Probably never.",
            "Let me call you back.": "I’m not calling back.",
            "I just want to be alone right now.": "Come comfort me without me asking.",
            "I didn't even notice!": "I noticed. I just didn’t say anything.",
            "It’s not a big deal.": "It’s the biggest deal of the day.",
            "I’ll get ready quick.": "See you in 45 minutes.",
            "That’s cute.": "I would never wear that.",
            "This is fun!": "This is boring.",
            "He’s just my type.": "He’s emotionally unavailable.",
            "I’m not mad, I’m just disappointed.": "I’m mad and disappointed.",
            "I don’t mean to be rude, but…": "I’m about to be incredibly rude.",
            "Oh, you remembered!": "I can’t believe you finally did something right.",
            "It’s okay if you forget.": "You better not forget.",
            "You don’t have to explain.": "Start explaining, now.",
            "It’s not worth it.": "It’s totally worth arguing about.",
            "Let’s just drop it.": "I’m bringing this up again later.",
            "No worries!": "I’m very worried and slightly offended.",
            "It's cute that you think that.": "You're wrong, but I won't argue... yet."
        }
        return {k.lower(): v for k, v in data.items()} # Convert keys to lowercase for matching

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.master, text="What She Says vs. What She Really Means",
                                    font=self.font_title, bg=self.bg_color, pady=15)
        self.title_label.pack()

        # Input Label
        self.input_label = tk.Label(self.master, text="Enter what she said:",
                                     font=self.font_label, bg=self.bg_color, pady=5)
        self.input_label.pack()

        # Input Entry
        self.input_entry = tk.Entry(self.master, width=60, font=self.font_entry, relief="groove")
        self.input_entry.pack(pady=5)
        self.input_entry.bind("<Return>", self.interpret_message_event) # Allow Enter key to trigger

        # Interpret Button
        self.interpret_button = tk.Button(self.master, text="Interpret Message",
                                          command=self.interpret_message,
                                          font=self.font_label, bg=self.button_color, fg=self.button_fg,
                                          activebackground="#45a049", activeforeground="white",
                                          relief="raised", bd=3, padx=10, pady=5)
        self.interpret_button.pack(pady=10)

        # Output Label
        self.output_label_header = tk.Label(self.master, text="What she *actually* means:",
                                             font=self.font_label, bg=self.bg_color, pady=5)
        self.output_label_header.pack()

        self.output_label = tk.Label(self.master, text="",
                                     font=self.font_result, bg=self.bg_color, fg="blue",
                                     wraplength=550, justify="center", padx=10, pady=10, relief="solid", bd=1)
        self.output_label.pack(pady=10, padx=20)

        # Clear Button
        self.clear_button = tk.Button(self.master, text="Clear",
                                       command=self.clear_fields,
                                       font=self.font_label, bg="#f44336", fg="white", # Red
                                       activebackground="#d32f2f", activeforeground="white",
                                       relief="raised", bd=3, padx=10, pady=5)
        self.clear_button.pack(pady=5)


    def interpret_message(self):
        user_input = self.input_entry.get().strip().lower() # Get, strip whitespace, convert to lowercase

        if not user_input:
            messagebox.showwarning("Input Error", "Please enter a phrase to interpret.")
            self.output_label.config(text="")
            return

        meaning = self.interpretations.get(user_input, "Sorry, that phrase isn't in my dictionary yet. Maybe she really means it!")
        self.output_label.config(text=meaning)

    def interpret_message_event(self, event):
        # This function is called when the Enter key is pressed
        self.interpret_message()

    def clear_fields(self):
        self.input_entry.delete(0, tk.END)
        self.output_label.config(text="")


# Main part of the script
if __name__ == "__main__":
    root = tk.Tk()
    app = WhatSheSaysApp(root)
    root.mainloop()