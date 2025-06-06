import tkinter as tk
from tkinter import messagebox


class WhatSheSaysApp:
    def __init__(self, master):
        self.master = master
        master.title("What She Says vs. What She Really Means")
        master.geometry("700x550")  # Adjust window size for more text
        master.resizable(False, False)  # Make window non-resizable

        # Styling
        self.bg_color = "#f0f0f0"
        self.button_color_interpret = "#4CAF50"  # Green
        self.button_color_clear = "#f44336"  # Red
        self.button_fg = "white"
        self.font_title = ("Helvetica", 18, "bold")
        self.font_label = ("Helvetica", 13)
        self.font_entry = ("Helvetica", 13)
        self.font_result_header = ("Helvetica", 14, "bold", "underline")
        self.font_result_item = ("Helvetica", 12)
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
            "It's cute that you think that.": "You're wrong, but I won't argue... yet.",
            # --- New Phrases Start Here ---
            "It’s fine.": "It’s absolutely not fine.",
            "Whatever.": "I'm annoyed but pretending not to be.",
            "Forget it.": "You better remember it.",
            "I'm okay.": "I'm emotionally spiraling.",
            "Don't worry about it.": "Worry about it immediately.",
            "It’s nothing.": "It’s everything.",
            "I'm used to it.": "I hate this but I’ve given up complaining.",
            "You didn’t have to do that.": "I'm glad you did, because if you hadn’t, I’d be mad.",
            "I’m good.": "I’m lying but I don’t want to explain why.",
            "Sure.": "I’m reluctantly agreeing, but I don’t like it.",
            "If you say so.": "You're wrong, but I'm too tired to argue.",
            "Mmhmm.": "I’m listening, but I don’t like what you’re saying.",
            "That’s fine with me.": "It’s not fine with me at all.",
            "Interesting.": "That was dumb but go on.",
            "K.": "I'm annoyed and this conversation is over.",
            "You're the best.": "You finally did the bare minimum.",
            "I don’t want to talk about it.": "Ask me more questions or suffer.",  # Duplicate, refined meaning or merge
            "I guess that makes sense.": "I totally disagree but don’t want to fight.",
            "You’re right.": "I’m giving up but I’m still mad.",
            "Cool.": "Not cool.",
            "Go ahead.": "You’ll regret that choice.",  # Duplicate, refined meaning or merge
            "No big deal.": "It's a colossal deal.",
            "I get it.": "I absolutely do not get it.",
            "Just forget it.": "Don't forget it. Ever.",
            "I’m done.": "Keep talking until I feel heard.",
            "It’s your choice.": "Make the wrong one and suffer.",
            "I’m not trying to be difficult.": "I’m about to be difficult.",
            "It’s your life.": "You're making terrible decisions.",
            "Fine, whatever.": "I’m giving up but resenting you forever.",
            "That’s not what I said.": "That's exactly what I said, but I changed my mind.",
            "You’re imagining things.": "You caught on and I’m gaslighting you now.",
            "I'm not in the mood.": "You messed up earlier, fix it.",
            "It's not worth talking about.": "It’s worth an entire therapy session.",
            "Why would I be mad?": "Obviously, I’m mad.",
            "Do what you want.": "And face the consequences.",  # Duplicate, refined meaning or merge
            "I’m not going to argue.": "I’m 100% right, and I’m furious you don’t see it.",
            "We’re fine.": "We’re absolutely not fine.",
            "Go have fun with your little friends.": "I’m jealous, insecure, and irritated.",
            "It’s cute that you think that.": "You are wildly wrong.",  # Duplicate, refined meaning or merge
            "Oh, I just find it funny that...": "Prepare to be emotionally disassembled.",
            "Whatever helps you sleep at night.": "You're lying to yourself and I know it.",
            "I said it’s fine.": "You're one breath away from danger.",
            "It's just weird, that's all.": "It's *super* not okay, but I’m pretending it is.",
            "Oh wow, okay then.": "Wow. You're officially on thin ice.",
            "Sure, I believe you.": "I don’t believe a single word.",
            "I’m not mad, just disappointed.": "I’m both mad *and* disappointed.",
            # Duplicate, refined meaning or merge
            "It’s not about that.": "It’s entirely about that.",
            "You’re unbelievable.": "I can’t believe how annoyed I am.",
            "You're so funny.": "You're so annoying.",
            "Are you serious right now?": "You have 5 seconds to fix this.",
            "Just do what you want.": "I dare you.",
            "I don’t even care anymore.": "I care so much I’m exhausted.",
            "Nothing.": "Everything. It’s everything.",
            "Don't start.": "You already started, now face the wrath.",
            "That’s not what happened.": "That’s what happened but I don’t like how it sounds.",
            "If you think that’s best.": "I think it's a terrible idea.",
            "That’s how you feel?": "Wrong feelings. Try again.",
            "Why are you being so defensive?": "You're not agreeing with me fast enough.",
            "It’s not about the gift.": "It’s *definitely* about the gift.",
            "You’re just being sensitive.": "You’re not being sensitive enough to me.",
            "Wow, thanks.": "Thanks for the bare minimum.",
            "You're lucky I love you.": "You’re *barely* surviving this conversation.",
            "I don't even know anymore.": "I know exactly what I mean. You just don’t get it.",
            "You never change.": "Still doing the same thing that annoys me.",
            "I’m not saying it again.": "I’ll say it again, louder, with tears.",
            "I’m just being honest.": "I’m being harsh and calling it honesty.",
            "Let’s not talk about this now.": "I’ll bring it up when it’s most inconvenient for you.",
            "I'm not mad, just surprised.": "I'm both mad and surprised.",
            "Oh, good for you.": "I’m not happy for you at all.",
            "You’re really going to do that?": "I dare you to try it.",
            "I’m not trying to be mean.": "I’m definitely about to be mean.",
            "You’re being overdramatic.": "You’re finally matching my energy.",
            "I don’t even care who you talk to.": "I stalk every girl you follow.",
            "You’re annoying.": "I love you, but also shut up.",
            "Wow, must be nice.": "I’m jealous and I hate you a little.",
            "I don’t need anything.": "I expect you to get it anyway.",
            "So that’s how it is?": "You're in trouble now.",
            "I thought I could trust you.": "You’ve made a minor mistake I will magnify emotionally.",
            "Don't worry about me.": "Worry about me more than anything.",
            "No rush.": "Why isn't it done already?",
            "That’s okay, I’ll wait.": "Tick... tock... you're already late.",
            "You’re being ridiculous.": "You're winning the argument and I hate that.",
            "It’s not like I care.": "I care more than anything.",
            "You’re so dumb.": "I actually think you're cute but don't push it.",
            "Is that what you think?": "You're about to rethink your entire life.",
            "Say that again?": "So I can kill you more dramatically.",
            "Okay, but I’m not wrong.": "I’m right, even when I’m not.",
            "Just because.": "I don’t want to tell you the reason because you’ll win.",
            "I said I’m over it!": "I will bring this up in 3 to 6 months.",
            "Don’t make me repeat myself.": "Repeat myself I will — louder and angrier.",
            "No, it’s totally fine!": "It’s catastrophically not fine.",
            "I'm just done explaining.": "You never understood me anyway.",
            "You always do this.": "I’m frustrated and generalizing now.",
            "Oh, it’s fine, I’ll just suffer.": "You’ve failed me and must now make up for it.",
            "I don’t need to explain myself.": "I'm 100% right, and too angry to argue.",
            "Just don't.": "You're already on thin ice.",
            "I hope you're happy.": "You're in deep, deep trouble.",
            "Oh, I’m not mad.": "I'm just plotting your emotional demise.",
            "Go ahead, be honest.": "Be careful what you say.",
            "Whatever you say.": "You're wrong and I’m judging you."
        }
        # Convert keys to lowercase for matching, handling potential duplicates by keeping the last one
        return {k.lower(): v for k, v in data.items()}

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
        self.input_entry = tk.Entry(self.master, width=70, font=self.font_entry, relief="groove")
        self.input_entry.pack(pady=5)
        self.input_entry.bind("<Return>", self.interpret_message_event)  # Allow Enter key to trigger

        # Interpret Button
        self.interpret_button = tk.Button(self.master, text="Interpret Message",
                                          command=self.interpret_message,
                                          font=self.font_label, bg=self.button_color_interpret, fg=self.button_fg,
                                          activebackground="#45a049", activeforeground="white",
                                          relief="raised", bd=3, padx=10, pady=5)
        self.interpret_button.pack(pady=10)

        # Output Header Label (for "What she *actually* means:")
        self.output_header_label = tk.Label(self.master, text="",
                                            font=self.font_result_header, bg=self.bg_color, fg="black", pady=5)
        self.output_header_label.pack()

        # Output Text Widget for multiple meanings (better for dynamic text)
        self.output_text = tk.Text(self.master, wrap="word", height=8, width=75,
                                   font=self.font_result_item, bg="white", fg="blue",
                                   relief="solid", bd=1, padx=10, pady=10)
        self.output_text.pack(pady=10, padx=20)
        self.output_text.config(state="disabled")  # Make it read-only

        # Clear Button
        self.clear_button = tk.Button(self.master, text="Clear",
                                      command=self.clear_fields,
                                      font=self.font_label, bg=self.button_color_clear, fg="white",
                                      activebackground="#d32f2f", activeforeground="white",
                                      relief="raised", bd=3, padx=10, pady=5)
        self.clear_button.pack(pady=5)

    def interpret_message(self):
        user_input_raw = self.input_entry.get().strip()
        user_input_cleaned = user_input_raw.lower()  # For dictionary lookup and substring search

        if not user_input_cleaned:
            messagebox.showwarning("Input Error", "Please enter a phrase to interpret.")
            self.output_text.config(state="normal")
            self.output_text.delete(1.0, tk.END)
            self.output_text.config(state="disabled")
            self.output_header_label.config(text="")
            return

        self.output_text.config(state="normal")  # Enable text widget for editing
        self.output_text.delete(1.0, tk.END)  # Clear previous results

        # --- Attempt exact match first ---
        exact_meaning = self.interpretations.get(user_input_cleaned, None)
        if exact_meaning:
            self.output_header_label.config(text="What she *actually* means:")
            self.output_text.insert(tk.END, exact_meaning + "\n")
        else:
            # --- If no exact match, search for partial matches ---
            possible_meanings = []

            # Simple keyword extraction: split the user input into words,
            # filtering out very short words or common stop words.
            # For simplicity, let's just use the full cleaned input as the search term first,
            # and then individual words if that doesn't yield anything specific.

            # Prioritize matching longer parts of the phrase first
            search_terms = [user_input_cleaned]
            if len(user_input_cleaned.split()) > 1:  # If multiple words, also try individual words
                search_terms.extend(word for word in user_input_cleaned.split() if len(word) > 2)
            search_terms = list(set(search_terms))  # Remove duplicates

            for phrase_lower, meaning in self.interpretations.items():
                # Check if the cleaned user input is a substring of the dictionary phrase
                # Or if any significant word from user input is in the dict phrase
                for term in search_terms:
                    if term in phrase_lower:
                        # Store the original phrase from the dictionary for better context
                        # Find the exact original phrase by iterating through the original data structure
                        original_phrase_match = next(
                            (k for k in self.load_interpretations_raw().keys() if k.lower() == phrase_lower),
                            phrase_lower)
                        possible_meanings.append(f"'{original_phrase_match}'\n  -> {meaning}\n")
                        break  # Only add once per dictionary entry

            if possible_meanings:
                self.output_header_label.config(text="Possible interpretations:")
                # Remove duplicates in case multiple search terms matched the same phrase
                unique_meanings = sorted(list(set(possible_meanings)), key=len)  # Sort for consistent display
                for i, entry in enumerate(unique_meanings):
                    self.output_text.insert(tk.END, f"{i + 1}. {entry}\n")
            else:
                self.output_header_label.config(text="")
                self.output_text.insert(tk.END,
                                        "Sorry, that phrase isn't in my dictionary yet, and no close matches were found. Maybe she really means it!\n")

        self.output_text.config(state="disabled")  # Make it read-only again

    def interpret_message_event(self, event):
        # This function is called when the Enter key is pressed
        self.interpret_message()

    def clear_fields(self):
        self.input_entry.delete(0, tk.END)
        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state="disabled")
        self.output_header_label.config(text="")  # Clear the header too

    def load_interpretations_raw(self):
        # This method is just to get the original casing for display,
        # without lowercasing keys for matching purposes.
        # It's a bit redundant but ensures we can show the exact original phrase.
        return {
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
            "It's cute that you think that.": "You're wrong, but I won't argue... yet.",
            # --- New Phrases Start Here ---
            "It’s fine.": "It’s absolutely not fine.",
            "Whatever.": "I'm annoyed but pretending not to be.",
            "Forget it.": "You better remember it.",
            "I'm okay.": "I'm emotionally spiraling.",
            "Don't worry about it.": "Worry about it immediately.",
            "It’s nothing.": "It’s everything.",
            "I'm used to it.": "I hate this but I’ve given up complaining.",
            "You didn’t have to do that.": "I'm glad you did, because if you hadn’t, I’d be mad.",
            "I’m good.": "I’m lying but I don’t want to explain why.",
            "Sure.": "I’m reluctantly agreeing, but I don’t like it.",
            "If you say so.": "You're wrong, but I'm too tired to argue.",
            "Mmhmm.": "I’m listening, but I don’t like what you’re saying.",
            "That’s fine with me.": "It’s not fine with me at all.",
            "Interesting.": "That was dumb but go on.",
            "K.": "I'm annoyed and this conversation is over.",
            "You're the best.": "You finally did the bare minimum.",
            "I don’t want to talk about it.": "Ask me more questions or suffer.",
            "I guess that makes sense.": "I totally disagree but don’t want to fight.",
            "You’re right.": "I’m giving up but I’m still mad.",
            "Cool.": "Not cool.",
            "Go ahead.": "You’ll regret that choice.",
            "No big deal.": "It's a colossal deal.",
            "I get it.": "I absolutely do not get it.",
            "Just forget it.": "Don't forget it. Ever.",
            "I’m done.": "Keep talking until I feel heard.",
            "It’s your choice.": "Make the wrong one and suffer.",
            "I’m not trying to be difficult.": "I’m about to be difficult.",
            "It’s your life.": "You're making terrible decisions.",
            "Fine, whatever.": "I’m giving up but resenting you forever.",
            "That’s not what I said.": "That's exactly what I said, but I changed my mind.",
            "You’re imagining things.": "You caught on and I’m gaslighting you now.",
            "I'm not in the mood.": "You messed up earlier, fix it.",
            "It's not worth talking about.": "It’s worth an entire therapy session.",
            "Why would I be mad?": "Obviously, I’m mad.",
            "Do what you want.": "And face the consequences.",
            "I’m not going to argue.": "I’m 100% right, and I’m furious you don’t see it.",
            "We’re fine.": "We’re absolutely not fine.",
            "Go have fun with your little friends.": "I’m jealous, insecure, and irritated.",
            "It’s cute that you think that.": "You are wildly wrong.",
            "Oh, I just find it funny that...": "Prepare to be emotionally disassembled.",
            "Whatever helps you sleep at night.": "You're lying to yourself and I know it.",
            "I said it’s fine.": "You're one breath away from danger.",
            "It's just weird, that's all.": "It's *super* not okay, but I’m pretending it is.",
            "Oh wow, okay then.": "Wow. You're officially on thin ice.",
            "Sure, I believe you.": "I don’t believe a single word.",
            "I’m not mad, just disappointed.": "I’m both mad *and* disappointed.",
            "It’s not about that.": "It’s entirely about that.",
            "You’re unbelievable.": "I can’t believe how annoyed I am.",
            "You're so funny.": "You're so annoying.",
            "Are you serious right now?": "You have 5 seconds to fix this.",
            "Just do what you want.": "I dare you.",
            "I don’t even care anymore.": "I care so much I’m exhausted.",
            "Nothing.": "Everything. It’s everything.",
            "Don't start.": "You already started, now face the wrath.",
            "That’s not what happened.": "That’s what happened but I don’t like how it sounds.",
            "If you think that’s best.": "I think it's a terrible idea.",
            "That’s how you feel?": "Wrong feelings. Try again.",
            "Why are you being so defensive?": "You're not agreeing with me fast enough.",
            "It’s not about the gift.": "It’s *definitely* about the gift.",
            "You’re just being sensitive.": "You’re not being sensitive enough to me.",
            "Wow, thanks.": "Thanks for the bare minimum.",
            "You're lucky I love you.": "You’re *barely* surviving this conversation.",
            "I don't even know anymore.": "I know exactly what I mean. You just don’t get it.",
            "You never change.": "Still doing the same thing that annoys me.",
            "I’m not saying it again.": "I’ll say it again, louder, with tears.",
            "I’m just being honest.": "I’m being harsh and calling it honesty.",
            "Let’s not talk about this now.": "I’ll bring it up when it’s most inconvenient for you.",
            "I'm not mad, just surprised.": "I'm both mad and surprised.",
            "Oh, good for you.": "I’m not happy for you at all.",
            "You’re really going to do that?": "I dare you to try it.",
            "I’m not trying to be mean.": "I’m definitely about to be mean.",
            "You’re being overdramatic.": "You’re finally matching my energy.",
            "I don’t even care who you talk to.": "I stalk every girl you follow.",
            "You’re annoying.": "I love you, but also shut up.",
            "Wow, must be nice.": "I’m jealous and I hate you a little.",
            "I don’t need anything.": "I expect you to get it anyway.",
            "So that’s how it is?": "You're in trouble now.",
            "I thought I could trust you.": "You’ve made a minor mistake I will magnify emotionally.",
            "Don't worry about me.": "Worry about me more than anything.",
            "No rush.": "Why isn't it done already?",
            "That’s okay, I’ll wait.": "Tick... tock... you're already late.",
            "You’re being ridiculous.": "You're winning the argument and I hate that.",
            "It’s not like I care.": "I care more than anything.",
            "You’re so dumb.": "I actually think you're cute but don't push it.",
            "Is that what you think?": "You're about to rethink your entire life.",
            "Say that again?": "So I can kill you more dramatically.",
            "Okay, but I’m not wrong.": "I’m right, even when I’m not.",
            "Just because.": "I don’t want to tell you the reason because you’ll win.",
            "I said I’m over it!": "I will bring this up in 3 to 6 months.",
            "Don’t make me repeat myself.": "Repeat myself I will — louder and angrier.",
            "No, it’s totally fine!": "It’s catastrophically not fine.",
            "I'm just done explaining.": "You never understood me anyway.",
            "You always do this.": "I’m frustrated and generalizing now.",
            "Oh, it’s fine, I’ll just suffer.": "You’ve failed me and must now make up for it.",
            "I don’t need to explain myself.": "I'm 100% right, and too angry to argue.",
            "Just don't.": "You're already on thin ice.",
            "I hope you're happy.": "You're in deep, deep trouble.",
            "Oh, I’m not mad.": "I'm just plotting your emotional demise.",
            "Go ahead, be honest.": "Be careful what you say.",
            "Whatever you say.": "You're wrong and I’m judging you."
        }


# Main part of the script
if __name__ == "__main__":
    root = tk.Tk()
    app = WhatSheSaysApp(root)
    root.mainloop()