import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for themed widgets, specifically Notebook


class WhatSheSaysApp:
    def __init__(self, master):
        self.master = master
        master.title("VYBEKID's Female Decoder")  # Your custom title
        master.geometry("750x650")  # Adjust window size for more content
        master.resizable(False, False)  # Make window non-resizable

        # Styling
        self.bg_color = "#f0f0f0"
        self.button_color_interpret = "#4CAF50"  # Green
        self.button_color_clear = "#f44336"  # Red
        self.button_fg = "white"
        self.font_title = ("Helvetica", 20, "bold")  # Slightly larger title font
        self.font_label = ("Helvetica", 13)
        self.font_entry = ("Helvetica", 13)
        self.font_result_header = ("Helvetica", 14, "bold", "underline")
        self.font_result_item = ("Helvetica", 12)
        self.master.config(bg=self.bg_color)

        # Load all interpretations
        self.phrase_interpretations, self.action_interpretations = self.load_interpretations()
        self.phrase_interpretations_raw, self.action_interpretations_raw = self.load_interpretations_raw()

        # Create Notebook (tabs)
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # Create Frames for each tab
        self.phrase_frame = ttk.Frame(self.notebook, style="TFrame")
        self.action_frame = ttk.Frame(self.notebook, style="TFrame")

        self.phrase_frame.pack(fill="both", expand=True)
        self.action_frame.pack(fill="both", expand=True)

        self.notebook.add(self.phrase_frame, text="Phrases")
        self.notebook.add(self.action_frame, text="Actions")

        # Configure Notebook style (optional, but makes tabs look better)
        style = ttk.Style()
        style.theme_use("clam")  # 'clam', 'alt', 'default', 'classic'
        style.configure("TNotebook", background=self.bg_color)
        style.configure("TNotebook.Tab", background=self.bg_color, foreground="black", font=("Helvetica", 11, "bold"))
        style.map("TNotebook.Tab", background=[("selected", "lightblue")], foreground=[("selected", "black")])
        style.configure("TFrame", background=self.bg_color)

        # Create widgets for each tab
        self.create_phrase_tab_widgets(self.phrase_frame)
        self.create_action_tab_widgets(self.action_frame)

    def load_interpretations(self):
        # Master list for spoken phrases (all previous + new "Quote / Phrase" set)
        phrase_data = {
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
            "Whatever you say.": "You're wrong and I’m judging you.",
            "You don’t care.": "You’re not reacting the way I expected.",
            "Come over to my place.": "I’m lonely and want attention... now.",
            "It’s urgent.": "I’ve decided this is now your emergency too.",
            # "Do whatever you want.": "Do it and suffer the fallout.", # Duplicate (original #2)
            "Why don’t you ever listen?": "You didn’t guess what I *didn’t* say out loud.",
            "I just needed you to care.": "You should’ve read my mind.",
            "I’m not the problem here.": "You’re 100% the villain in this story.",
            "You never take my side.": "You dared to have an opinion that wasn’t mine.",
            "Let me think about it.": "The answer is no, but I want to sound polite.",
            "I didn’t mean it like that.": "You took it exactly how I meant it, but now I regret saying it.",
            "So you really don’t care?": "Show me more affection, immediately.",
            "This is why I don’t talk to you.": "You’re not reacting the way I rehearsed in my head.",
            "I’m not going to tell you again.": "I’ll tell you again — louder and more frustrated.",
            "So I’m crazy now?": "You’re about to see crazy if you keep talking.",
            "Explain it to me then.": "I dare you to try.",
            "I just think it’s funny how…": "This will not be funny. It’s a trap.",
            "Don’t make me beg.": "I already am, but now I'm resentful.",
            # "Whatever helps you sleep at night.": "You're a delusional liar and I know it.", # Duplicate (original #141)
            "I’m tired.": "I’m emotionally drained from everything you didn’t notice.",
            # "Can we talk?": "You're in trouble.", # Duplicate (original #13)
            "It’s not about the money.": "It’s *definitely* about the money.",
            "So who is she?": "You looked at your phone weird and now I'm investigating.",
            "You really forgot?": "This matters. You should’ve remembered.",
            "Don't act like you don’t know.": "You definitely know. Or you better guess fast.",
            "You should’ve known.": "Even if I didn’t say it, you should’ve magically known.",
            "I’m fine, I promise.": "I'm lying.",
            "This isn't about you.": "This is 100% about you.",
            "I'm busy.": "I’m ignoring you to prove a point.",
            "I don’t want to be a burden.": "You better offer to help immediately.",
            # "We need to talk.": "Brace yourself for emotional chaos.", # Duplicate (original #13)
            "No one else would put up with this.": "You're lucky I love you, barely.",
            "Oh, you're free now?": "Where were you when I needed you 2 hours ago?",
            "Don't you think it's weird that...": "I’ve already decided it’s weird and I want you to agree.",
            "It's always about you.": "Why aren’t you making it about me this time?",
            # "I’m not mad, just surprised.": "I’m fuming.", # Duplicate (original #168)
            "I thought you were different.": "You're disappointing me in a brand-new way.",
            "You said you’d change.": "You’ve disappointed me. Again.",
            # "I'm not jealous.": "I’m jealous.", # Duplicate (original #29)
            "I just needed space.": "I wanted space until you chased me.",
            "I’m not ready to talk about it.": "I want you to *force* me to talk about it.",
            "You don’t even know me.": "You should’ve known that would upset me.",
            "This is exhausting.": "You're exhausting me emotionally.",
            "I’m not doing this again.": "We are absolutely doing this again.",
            "You don’t have to prove anything.": "Actually, you do.",
            "Don’t call me.": "Call me anyway, I’ll ignore it, but I’ll notice.",
            # "It’s whatever.": "It’s very much *not* whatever.", # Duplicate (original #5)
            "I just didn’t expect that from you.": "I expected you to be better.",
            # "I’m over it.": "Still bothered, possibly for life.", # Duplicate (original #21)
            "Wow, you really went there.": "I can't believe you actually said that.",
            "I hope you have fun.": "You better not have fun without me.",
            "I’m not needy.": "Please pay attention to me immediately.",
            "So that's what we're doing now?": "You're acting shady and I’m catching on.",
            "You don’t have to say anything.": "You better say exactly the right thing now.",
            "Oh really?": "That was a stupid thing to say, try again.",
            "Just forget it, seriously.": "I will never forget this.",
            "I’m just venting.": "I need emotional backup, not logic.",
            "It was just a joke.": "It wasn’t, but now I’m backtracking.",
            # "I’m not like other girls.": "I am, but I’m branding myself.", # Duplicate (original #36)
            # "You’re so dramatic.": "You finally matched my energy.", # Duplicate (original #172, was overdramatic)
            "It’s complicated.": "You won’t like the truth.",
            # "I’m totally chill.": "I’m actively suppressing rage.", # Duplicate (original #53)
            "Don’t lie to me.": "I already know the truth. Test me.",
            "You’ll regret that.": "Threat detected.",
            "I don’t care what she said.": "I care deeply and I’m judging her and you.",
            # "We’ll see.": "No.", # Duplicate (original #25)
            "That’s not important right now.": "It’s very important, but I want control of the timing.",
            "I don't do drama.": "I *thrive* on drama but pretend to hate it.",
            "I’m not one of those girls.": "I’m exactly that girl but with better marketing.",
            "Why are you being weird?": "Why aren’t you behaving how I want you to?",
            "You know what? Never mind.": "You better figure it out without me saying it.",
            "We’ll talk later.": "You're not off the hook, just on hold.",
            # "No, really, go have fun.": "Don’t you dare enjoy yourself too much.", # Duplicate (original #7)
            "I’ve moved on.": "I absolutely haven’t.",
            # "You're overthinking it.": "You're close to the truth and I’m nervous.", # Duplicate (original #77)
            "I don’t mean to make it a big deal.": "This is a *huge* deal.",
            # "It’s not you, it’s me.": "It’s you.", # Duplicate (original #43)
            "I don’t know what I want.": "I want you to prove you can figure me out.",
            "You're not getting it.": "You're absolutely not getting it and I’m losing patience.",
            "I just needed reassurance.": "You failed the test.",
            "You made me do this.": "I’m blaming you for my emotional choices.",
            "You made me feel crazy.": "You didn’t validate my feelings.",
            "You always turn it around.": "Stop deflecting and apologize already.",
            "You still don’t get it, do you?": "This is why I cried last week.",
            # "I don’t want to argue.": "I absolutely do, and I will win.", # Duplicate (original #68)
            "I just don’t feel heard.": "You’re not agreeing with me.",
            "That’s not even the point.": "You're winning this argument but I’m shifting topics.",
            # "I’m done explaining.": "You're not worth the effort anymore, for now.", # Duplicate (original #192)
            # "I’m just being honest.": "I’m being critical and hiding behind ‘honesty’.", # Duplicate (original #166)
            "You don’t even care how I feel.": "You missed every cue I dropped.",
            "I need time.": "I need drama, space, and then a surprise romantic gesture.",
            "Why would I be mad about that?": "I’m furious. You fool.",
            "I’m not playing games.": "You are now officially playing my game.",
            "No, go out. I’ll be fine.": "You’ll owe me an apology and possibly flowers.",
            "I just want honesty.": "But only if I like what I hear.",
            # "You never listen!": "You didn’t agree fast enough.", # Duplicate (original #15)
            # "Let’s just drop it.": "Let’s pause and return to this in dramatic fashion later.", # Duplicate (original #98)
            "You always say that.": "You’ve said this twice and I memorized it.",
            "This isn’t about you.": "This is totally about you.",
            "Just trust me.": "I may or may not have caused chaos.",
            "I can't believe you.": "Oh, I believe you. I just *don’t like* you right now.",

            # New Phrases (from the last two tables merged into the "Phrases" category)
            "I have a question...": "Prepare for an interrogation disguised as curiosity",
            "Can I ask you something?": "I already know the answer — just seeing if you'll lie",
            "Be honest with me...": "Lie, and I’ll know. Tell the truth, and I’ll still be mad",
            "Just wondering...": "I’ve been obsessively overthinking this for days",
            "So who’s [insert girl's name]?": "I already checked her Instagram and your likes from 2019",
            "Do you think she's pretty?": "There is no right answer. Abort mission",
            "If I wasn’t around, would you still...": "Testing your loyalty in hypothetical emotional warfare",
            "Do you miss your ex?": "Please say no. Or lie convincingly",
            "Would you still love me if I was a worm?": "Trick question. This is a test of imagination *and* love",
            "What would you do if I died?": "I want to hear you’d cry and never move on",
            "Who’s that texting you?": "I saw the name, now explain it before I launch an investigation",
            "Can we talk later?": "You’re not sleeping tonight",
            "What do you mean by that?": "You’ve already said something offensive",
            "How come you didn’t notice...?": "I needed you to be psychic — you failed",
            "Why do you like me?": "Compliment me, in detail. Right now.",
            "Do you even love me?": "I’m feeling emotionally dramatic — please reassure me",
            "Where do you see this going?": "Commit now, or start panicking",
            "How many girls have you talked to before me?": "I will judge every answer",
            "What would you do if I cheated on you?": "Hypothetical. Maybe. Or not",
            "Would you fight for me?": "I expect a poetic and heroic answer",
            "If I gained 50 pounds, would you still...?": "Say yes. No hesitation.",
            "You wouldn't lie to me, right?": "I suspect you're already lying",
            "Would you pick me or your mom?": "There’s no safe answer — choose wisely",
            "Are you hiding something?": "I already found it, just waiting to see if you confess",
            "What did you mean by liking her picture?": "You’ve entered the Instagram danger zone",
            "So you’ve been really quiet lately...": "I’ve noticed. And I’m not happy about it",
            "What’s your type, exactly?": "Describe me or suffer",
            "What if I told you I was talking to someone?": "I want to see how jealous you get",
            "Why didn’t you tell me about that?": "You withheld information = betrayal",
            "Are you bored of me?": "Say no like your life depends on it",
            "I don't understand you.": "I *do* understand… I just don’t like what I’m hearing.",
            # "Do what you want.": "I *dare* you to make the wrong move.", # Duplicate
            # "I'm not mad.": "I’m boiling inside. Proceed with extreme caution.", # Duplicate
            # "Whatever.": "Conversation over. You lost.", # Duplicate
            # "It’s your life.": "You’re making a dumb decision and I disapprove.", # Duplicate
            # "I’m fine.": "I’m anything *but* fine. Figure it out.", # Duplicate
            # "You don’t get it.": "You didn’t read my mind like I expected.", # Duplicate
            # "Forget it.": "This is not over. Just postponed.", # Duplicate
            # "I’m just tired.": "I’m emotionally drained by *you.*", # Duplicate
            # "If you say so.": "I don’t believe you, but okay.", # Duplicate
            "It’s not that deep.": "It’s *very* deep. And I’m still overthinking it.",
            # "I guess...": "I’m disappointed but trying to suppress it.", # Duplicate
            # "You always do this.": "I’ve been mentally noting this for weeks.", # Duplicate
            # "Wow.": "Shock. Disappointment. A storm is brewing.", # Duplicate
            "Okay then.": "That’s your final answer? Interesting.",
            # "Sure.": "Absolutely not, but I’ll let you walk into the trap.", # Duplicate
            # "Go ahead.": "I will remember this betrayal forever.", # Duplicate
            # "I don't care.": "I care. I care so much it hurts.", # Duplicate
            # "It’s not you, it’s me.": "It’s you. 100%. But I’m trying to be nice.", # Duplicate
            "I said what I said.": "I meant it. Deal with it.",
            # "I'm over it.": "I am *not* over it.", # Duplicate
            "You just don’t listen.": "You heard me but didn’t *feel* me.",
            "I don't need anyone.": "I need someone — preferably *you* — to care more.",
            "Why can’t you just talk to me?": "You’re being emotionally unavailable and I’m tired of chasing clarity.",
            "This is why I don't open up.": "You missed your chance to show empathy.",
            "Maybe we're just too different.": "I'm testing whether you'll fight for this or give up.",
            "It’s whatever, honestly.": "It’s definitely *not* whatever. I'm just done arguing.",
            # "You never change.": "My patience is wearing thin.", # Duplicate
            # "I just want honesty.": "I know you’re hiding something — time to confess.", # Duplicate
            "You wouldn’t understand.": "Try harder to understand — or at least pretend to."
        }
        # Convert keys to lowercase for matching, handling potential duplicates by keeping the last one
        phrase_interpretations = {k.lower(): v for k, v in phrase_data.items()}

        # Separate list for actions
        action_data = {
            "Sends you a photo after days of no talking": "Reminder: “I still exist, and I still look good — notice me.”",
            "Likes your old post after ghosting": "She’s breadcrumbing attention — *you’re not out of her mind yet*",
            "Leaves your message on “Seen” and posts a selfie": "Message received: “I’m ignoring you… but here’s what you’re missing”",
            "Comments on your friend’s post, not yours": "Passive-aggressive proximity play",
            "Randomly unblocks you, but doesn’t text": "“I’ve forgiven you… but I want you to sweat first.”",
            "Sends you a random song link": "Hidden message inside the lyrics — read it like a breakup prophecy",
            "Removes her profile picture": "Something's wrong. She’s either heartbroken or preparing a comeback",
            "Posts a “throwback” from a date you were on": "“Remember this? Yeah, I do too.”",
            "Joins your game lobby/Discord call uninvited": "“I’m still in your digital space — pay attention.”",
            "Posts a pic with another guy in her story": "Jealousy delivery: express shipping",
            "Opens your message but doesn’t respond": "“I *could* talk… but you haven’t earned that right today.”",
            "Views your story instantly, but doesn't reply": "Monitoring your emotional activity from a distance",
            "Sends a “casual” mirror selfie": "Craving validation — “Tell me I look fire.”",
            "Randomly compliments you": "Setting emotional bait — or softening you up",
            "Tags you in a meme after weeks of silence": "She’s ready to reopen the conversation but not directly",
            "Wears your hoodie in a selfie": "Marking territory again — “This is mine, and I miss you”",
            "Sends a pet photo": "“Look how soft and loving I am… say something cute back”",
            "Follows your sibling but not you": "Tactical emotional pressure",
            "Updates her bio with an inside joke": "“I’m thinking about you, but you better catch the hint.”",
            "Posts a screenshot of your chat": "It was cute — or dramatic. Either way, she wants people to *see*",
            "Deletes all posts except one of you two": "“This still meant something… don’t forget that.”",
            "Joins your Spotify session": "Music = emotion spy mode",
            "Sends an old pic of you two randomly": "She’s reminiscing — or trying to make you do the same",
            "Likes your new girl’s photo": "She saw it. She *wants* you to know she saw it",
            "Suddenly adds you to her close friends list": "You’ve re-entered the emotional VIP zone",
            "Sends a pic and says “felt cute”": "Translation: “Hype me up or I’m blocking you”",
            "Uses your nickname in a story or caption": "You’ve been tagged emotionally — it’s personal now",
            "Reacts to your story with 🔥 or ❤️‍🔥": "“I’m watching, I’m still into you — now do something about it”",
            "Purposely lets your friend “accidentally” see her IG": "She's making moves… indirectly",
            "Sends a pic with “miss this day” caption": "The day = you. The message = respond."
        }
        action_interpretations = {k.lower(): v for k, v in action_data.items()}

        return phrase_interpretations, action_interpretations

    def load_interpretations_raw(self):
        # This method is for getting original casing for display, without lowercasing keys for matching purposes.
        # Ensure it mirrors the structure of load_interpretations but with original casing.
        phrase_data_raw = {
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
            "Whatever you say.": "You're wrong and I’m judging you.",
            "You don’t care.": "You’re not reacting the way I expected.",
            "Come over to my place.": "I’m lonely and want attention... now.",
            "It’s urgent.": "I’ve decided this is now your emergency too.",
            "Why don’t you ever listen?": "You didn’t guess what I *didn’t* say out loud.",
            "I just needed you to care.": "You should’ve read my mind.",
            "I’m not the problem here.": "You’re 100% the villain in this story.",
            "You never take my side.": "You dared to have an opinion that wasn’t mine.",
            "Let me think about it.": "The answer is no, but I want to sound polite.",
            "I didn’t mean it like that.": "You took it exactly how I meant it, but now I regret saying it.",
            "So you really don’t care?": "Show me more affection, immediately.",
            "This is why I don’t talk to you.": "You’re not reacting the way I rehearsed in my head.",
            "I’m not going to tell you again.": "I’ll tell you again — louder and more frustrated.",
            "So I’m crazy now?": "You’re about to see crazy if you keep talking.",
            "Explain it to me then.": "I dare you to try.",
            "I just think it’s funny how…": "This will not be funny. It’s a trap.",
            "Don’t make me beg.": "I already am, but now I'm resentful.",
            "I’m tired.": "I’m emotionally drained from everything you didn’t notice.",
            "Can we talk?": "You're in trouble.",
            "It’s not about the money.": "It’s *definitely* about the money.",
            "So who is she?": "You looked at your phone weird and now I'm investigating.",
            "You really forgot?": "This matters. You should’ve remembered.",
            "Don't act like you don’t know.": "You definitely know. Or you better guess fast.",
            "You should’ve known.": "Even if I didn’t say it, you should’ve magically known.",
            "I’m fine, I promise.": "I'm lying.",
            "This isn't about you.": "This is 100% about you.",
            "I'm busy.": "I’m ignoring you to prove a point.",
            "I don’t want to be a burden.": "You better offer to help immediately.",
            "We need to talk.": "Brace yourself for emotional chaos.",
            "No one else would put up with this.": "You're lucky I love you, barely.",
            "Oh, you're free now?": "Where were you when I needed you 2 hours ago?",
            "Don't you think it's weird that...": "I’ve already decided it’s weird and I want you to agree.",
            "It's always about you.": "Why aren’t you making it about me this time?",
            "I’m not mad, just surprised.": "I’m fuming.",
            "I thought you were different.": "You're disappointing me in a brand-new way.",
            "You said you’d change.": "You’ve disappointed me. Again.",
            "I'm not jealous.": "I’m jealous.",
            "I just needed space.": "I wanted space until you chased me.",
            "I’m not ready to talk about it.": "I want you to *force* me to talk about it.",
            "You don’t even know me.": "You should’ve known that would upset me.",
            "This is exhausting.": "You're exhausting me emotionally.",
            "I’m not doing this again.": "We are absolutely doing this again.",
            "You don’t have to prove anything.": "Actually, you do.",
            "Don’t call me.": "Call me anyway, I’ll ignore it, but I’ll notice.",
            "It’s whatever.": "It’s very much *not* whatever.",
            "I just didn’t expect that from you.": "I expected you to be better.",
            "I’m over it.": "Still bothered, possibly for life.",
            "Wow, you really went there.": "I can't believe you actually said that.",
            "I hope you have fun.": "You better not have fun without me.",
            "I’m not needy.": "Please pay attention to me immediately.",
            "So that's what we're doing now?": "You're acting shady and I’m catching on.",
            "You don’t have to say anything.": "You better say exactly the right thing now.",
            "Oh really?": "That was a stupid thing to say, try again.",
            "Just forget it, seriously.": "I will never forget this.",
            "I’m just venting.": "I need emotional backup, not logic.",
            "It was just a joke.": "It wasn’t, but now I’m backtracking.",
            "I’m not like other girls.": "I am, but I’m branding myself.",
            "You’re so dramatic.": "You finally matched my energy.",
            "It’s complicated.": "You won’t like the truth.",
            "I’m totally chill.": "I’m actively suppressing rage.",
            "Don’t lie to me.": "I already know the truth. Test me.",
            "You’ll regret that.": "Threat detected.",
            "I don’t care what she said.": "I care deeply and I’m judging her and you.",
            "We’ll see.": "No.",
            "That’s not important right now.": "It’s very important, but I want control of the timing.",
            "I don't do drama.": "I *thrive* on drama but pretend to hate it.",
            "I’m not one of those girls.": "I’m exactly that girl but with better marketing.",
            "Why are you being weird?": "Why aren’t you behaving how I want you to?",
            "You know what? Never mind.": "You better figure it out without me saying it.",
            "We’ll talk later.": "You're not off the hook, just on hold.",
            "No, really, go have fun.": "Don’t you dare enjoy yourself too much.",
            "I’ve moved on.": "I absolutely haven’t.",
            "You're overthinking it.": "You're close to the truth and I’m nervous.",
            "I don’t mean to make it a big deal.": "This is a *huge* deal.",
            "It’s not you, it’s me.": "It’s you.",
            "I don’t know what I want.": "I want you to prove you can figure me out.",
            "You're not getting it.": "You're absolutely not getting it and I’m losing patience.",
            "I just needed reassurance.": "You failed the test.",
            "You made me do this.": "I’m blaming you for my emotional choices.",
            "You made me feel crazy.": "You didn’t validate my feelings.",
            "You always turn it around.": "Stop deflecting and apologize already.",
            "You still don’t get it, do you?": "This is why I cried last week.",
            "I don’t want to argue.": "I absolutely do, and I will win.",
            "I just don’t feel heard.": "You’re not agreeing with me.",
            "That’s not even the point.": "You're winning this argument but I’m shifting topics.",
            "I’m done explaining.": "You're not worth the effort anymore, for now.",
            "I’m just being honest.": "I’m being critical and hiding behind ‘honesty’.",
            "You don’t even care how I feel.": "You missed every cue I dropped.",
            "I need time.": "I need drama, space, and then a surprise romantic gesture.",
            "Why would I be mad about that?": "I’m furious. You fool.",
            "I’m not playing games.": "You are now officially playing my game.",
            "No, go out. I’ll be fine.": "You’ll owe me an apology and possibly flowers.",
            "I just want honesty.": "But only if I like what I hear.",
            "You never listen!": "You didn’t agree fast enough.",
            "Let’s just drop it.": "Let’s pause and return to this in dramatic fashion later.",
            "You always say that.": "You’ve said this twice and I memorized it.",
            "This isn’t about you.": "This is totally about you.",
            "Just trust me.": "I may or may not have caused chaos.",
            "I can't believe you.": "Oh, I believe you. I just *don’t like* you right now.",

            # New Phrases for the phrase tab
            "I have a question...": "Prepare for an interrogation disguised as curiosity",
            "Can I ask you something?": "I already know the answer — just seeing if you'll lie",
            "Be honest with me...": "Lie, and I’ll know. Tell the truth, and I’ll still be mad",
            "Just wondering...": "I’ve been obsessively overthinking this for days",
            "So who’s [insert girl's name]?": "I already checked her Instagram and your likes from 2019",
            "Do you think she's pretty?": "There is no right answer. Abort mission",
            "If I wasn’t around, would you still...": "Testing your loyalty in hypothetical emotional warfare",
            "Do you miss your ex?": "Please say no. Or lie convincingly",
            "Would you still love me if I was a worm?": "Trick question. This is a test of imagination *and* love",
            "What would you do if I died?": "I want to hear you’d cry and never move on",
            "Who’s that texting you?": "I saw the name, now explain it before I launch an investigation",
            "Can we talk later?": "You’re not sleeping tonight",
            "What do you mean by that?": "You’ve already said something offensive",
            "How come you didn’t notice...?": "I needed you to be psychic — you failed",
            "Why do you like me?": "Compliment me, in detail. Right now.",
            "Do you even love me?": "I’m feeling emotionally dramatic — please reassure me",
            "Where do you see this going?": "Commit now, or start panicking",
            "How many girls have you talked to before me?": "I will judge every answer",
            "What would you do if I cheated on you?": "Hypothetical. Maybe. Or not",
            "Would you fight for me?": "I expect a poetic and heroic answer",
            "If I gained 50 pounds, would you still...?": "Say yes. No hesitation.",
            "You wouldn't lie to me, right?": "I suspect you're already lying",
            "Would you pick me or your mom?": "There’s no safe answer — choose wisely",
            "Are you hiding something?": "I already found it, just waiting to see if you confess",
            "What did you mean by liking her picture?": "You’ve entered the Instagram danger zone",
            "So you’ve been really quiet lately...": "I’ve noticed. And I’m not happy about it",
            "What’s your type, exactly?": "Describe me or suffer",
            "What if I told you I was talking to someone?": "I want to see how jealous you get",
            "Why didn’t you tell me about that?": "You withheld information = betrayal",
            "Are you bored of me?": "Say no like your life depends on it",
            "I don't understand you.": "I *do* understand… I just don’t like what I’m hearing.",
            "It’s not that deep.": "It’s *very* deep. And I’m still overthinking it.",
            "Okay then.": "That’s your final answer? Interesting.",
            "I said what I said.": "I meant it. Deal with it.",
            "You just don’t listen.": "You heard me but didn’t *feel* me.",
            "I don't need anyone.": "I need someone — preferably *you* — to care more.",
            "Why can’t you just talk to me?": "You’re being emotionally unavailable and I’m tired of chasing clarity.",
            "This is why I don't open up.": "You missed your chance to show empathy.",
            "Maybe we're just too different.": "I'm testing whether you'll fight for this or give up.",
            "It’s whatever, honestly.": "It’s definitely *not* whatever. I'm just done arguing.",
            "You wouldn’t understand.": "Try harder to understand — or at least pretend to."
        }

        action_data_raw = {
            "Sends you a photo after days of no talking": "Reminder: “I still exist, and I still look good — notice me.”",
            "Likes your old post after ghosting": "She’s breadcrumbing attention — *you’re not out of her mind yet*",
            "Leaves your message on “Seen” and posts a selfie": "Message received: “I’m ignoring you… but here’s what you’re missing”",
            "Comments on your friend’s post, not yours": "Passive-aggressive proximity play",
            "Randomly unblocks you, but doesn’t text": "“I’ve forgiven you… but I want you to sweat first.”",
            "Sends you a random song link": "Hidden message inside the lyrics — read it like a breakup prophecy",
            "Removes her profile picture": "Something's wrong. She’s either heartbroken or preparing a comeback",
            "Posts a “throwback” from a date you were on": "“Remember this? Yeah, I do too.”",
            "Joins your game lobby/Discord call uninvited": "“I’m still in your digital space — pay attention.”",
            "Posts a pic with another guy in her story": "Jealousy delivery: express shipping",
            "Opens your message but doesn’t respond": "“I *could* talk… but you haven’t earned that right today.”",
            "Views your story instantly, but doesn't reply": "Monitoring your emotional activity from a distance",
            "Sends a “casual” mirror selfie": "Craving validation — “Tell me I look fire.”",
            "Randomly compliments you": "Setting emotional bait — or softening you up",
            "Tags you in a meme after weeks of silence": "She’s ready to reopen the conversation but not directly",
            "Wears your hoodie in a selfie": "Marking territory again — “This is mine, and I miss you”",
            "Sends a pet photo": "“Look how soft and loving I am… say something cute back”",
            "Follows your sibling but not you": "Tactical emotional pressure",
            "Updates her bio with an inside joke": "“I’m thinking about you, but you better catch the hint.”",
            "Posts a screenshot of your chat": "It was cute — or dramatic. Either way, she wants people to *see*",
            "Deletes all posts except one of you two": "“This still meant something… don’t forget that.”",
            "Joins your Spotify session": "Music = emotion spy mode",
            "Sends an old pic of you two randomly": "She’s reminiscing — or trying to make you do the same",
            "Likes your new girl’s photo": "She saw it. She *wants* you to know she saw it",
            "Suddenly adds you to her close friends list": "You’ve re-entered the emotional VIP zone",
            "Sends a pic and says “felt cute”": "Translation: “Hype me up or I’m blocking you”",
            "Uses your nickname in a story or caption": "You’ve been tagged emotionally — it’s personal now",
            "Reacts to your story with 🔥 or ❤️‍🔥": "“I’m watching, I’m still into you — now do something about it”",
            "Purposely lets your friend “accidentally” see her IG": "She's making moves… indirectly",
            "Sends a pic with “miss this day” caption": "The day = you. The message = respond."
        }

        # Convert keys to lowercase for internal matching (main self.interpretations)
        phrase_interpretations = {k.lower(): v for k, v in phrase_data_raw.items()}
        action_interpretations = {k.lower(): v for k, v in action_data_raw.items()}

        return phrase_interpretations, action_interpretations

    def create_phrase_tab_widgets(self, frame):
        # Input Label
        input_label = tk.Label(frame, text="Enter what she said:",
                               font=self.font_label, bg=self.bg_color, pady=5)
        input_label.pack()

        # Input Entry
        self.phrase_input_entry = tk.Entry(frame, width=70, font=self.font_entry, relief="groove")
        self.phrase_input_entry.pack(pady=5)
        self.phrase_input_entry.bind("<Return>", lambda event: self._interpret_message(
            self.phrase_input_entry, self.phrase_output_text, self.phrase_output_header_label,
            self.phrase_interpretations, self.phrase_interpretations_raw
        ))

        # Interpret Button
        interpret_button = tk.Button(frame, text="Interpret Phrase",
                                     command=lambda: self._interpret_message(
                                         self.phrase_input_entry, self.phrase_output_text,
                                         self.phrase_output_header_label,
                                         self.phrase_interpretations, self.phrase_interpretations_raw
                                     ),
                                     font=self.font_label, bg=self.button_color_interpret, fg=self.button_fg,
                                     activebackground="#45a049", activeforeground="white",
                                     relief="raised", bd=3, padx=10, pady=5)
        interpret_button.pack(pady=10)

        # Output Header Label
        self.phrase_output_header_label = tk.Label(frame, text="",
                                                   font=self.font_result_header, bg=self.bg_color, fg="black", pady=5)
        self.phrase_output_header_label.pack()

        # Output Text Widget
        self.phrase_output_text = tk.Text(frame, wrap="word", height=8, width=75,
                                          font=self.font_result_item, bg="white", fg="blue",
                                          relief="solid", bd=1, padx=10, pady=10)
        self.phrase_output_text.pack(pady=10, padx=20)
        self.phrase_output_text.config(state="disabled")

        # Clear Button
        clear_button = tk.Button(frame, text="Clear",
                                 command=lambda: self._clear_fields(
                                     self.phrase_input_entry, self.phrase_output_text, self.phrase_output_header_label
                                 ),
                                 font=self.font_label, bg=self.button_color_clear, fg="white",
                                 activebackground="#d32f2f", activeforeground="white",
                                 relief="raised", bd=3, padx=10, pady=5)
        clear_button.pack(pady=5)

    def create_action_tab_widgets(self, frame):
        # Input Label
        input_label = tk.Label(frame, text="Describe her action:",
                               font=self.font_label, bg=self.bg_color, pady=5)
        input_label.pack()

        # Input Entry
        self.action_input_entry = tk.Entry(frame, width=70, font=self.font_entry, relief="groove")
        self.action_input_entry.pack(pady=5)
        self.action_input_entry.bind("<Return>", lambda event: self._interpret_message(
            self.action_input_entry, self.action_output_text, self.action_output_header_label,
            self.action_interpretations, self.action_interpretations_raw
        ))

        # Interpret Button
        interpret_button = tk.Button(frame, text="Interpret Action",
                                     command=lambda: self._interpret_message(
                                         self.action_input_entry, self.action_output_text,
                                         self.action_output_header_label,
                                         self.action_interpretations, self.action_interpretations_raw
                                     ),
                                     font=self.font_label, bg=self.button_color_interpret, fg=self.button_fg,
                                     activebackground="#45a049", activeforeground="white",
                                     relief="raised", bd=3, padx=10, pady=5)
        interpret_button.pack(pady=10)

        # Output Header Label
        self.action_output_header_label = tk.Label(frame, text="",
                                                   font=self.font_result_header, bg=self.bg_color, fg="black", pady=5)
        self.action_output_header_label.pack()

        # Output Text Widget
        self.action_output_text = tk.Text(frame, wrap="word", height=8, width=75,
                                          font=self.font_result_item, bg="white", fg="blue",
                                          relief="solid", bd=1, padx=10, pady=10)
        self.action_output_text.pack(pady=10, padx=20)
        self.action_output_text.config(state="disabled")

        # Clear Button
        clear_button = tk.Button(frame, text="Clear",
                                 command=lambda: self._clear_fields(
                                     self.action_input_entry, self.action_output_text, self.action_output_header_label
                                 ),
                                 font=self.font_label, bg=self.button_color_clear, fg="white",
                                 activebackground="#d32f2f", activeforeground="white",
                                 relief="raised", bd=3, padx=10, pady=5)
        clear_button.pack(pady=5)

    def _interpret_message(self, input_entry_widget, output_text_widget, output_header_label_widget,
                           interpretation_dict, interpretation_dict_raw):
        user_input_raw = input_entry_widget.get().strip()
        user_input_cleaned = user_input_raw.lower()

        if not user_input_cleaned:
            messagebox.showwarning("Input Error", "Please enter text in the input field.")
            self._clear_fields(input_entry_widget, output_text_widget, output_header_label_widget)
            return

        output_text_widget.config(state="normal")
        output_text_widget.delete(1.0, tk.END)

        exact_meaning = interpretation_dict.get(user_input_cleaned, None)
        if exact_meaning:
            output_header_label_widget.config(text="What it *actually* means:")
            output_text_widget.insert(tk.END, exact_meaning + "\n")
        else:
            possible_meanings = []

            search_terms = [user_input_cleaned]
            if len(user_input_cleaned.split()) > 1:
                search_terms.extend(word for word in user_input_cleaned.split() if len(word) > 2)
            search_terms = list(set(search_terms))

            for phrase_lower, meaning in interpretation_dict.items():
                for term in search_terms:
                    if term in phrase_lower:
                        original_phrase_match = next(
                            (k for k in interpretation_dict_raw.keys() if k.lower() == phrase_lower), phrase_lower)
                        possible_meanings.append((original_phrase_match, meaning))
                        break

            if possible_meanings:
                output_header_label_widget.config(text="Possible interpretations:")
                unique_meanings_tuples = list(set(possible_meanings))
                sorted_unique_meanings = sorted(unique_meanings_tuples, key=lambda x: len(x[0]))

                for i, (original_phrase, meaning) in enumerate(sorted_unique_meanings):
                    output_text_widget.insert(tk.END, f"{i + 1}. '{original_phrase}'\n  -> {meaning}\n\n")
            else:
                output_header_label_widget.config(text="")
                output_text_widget.insert(tk.END,
                                          "Sorry, that isn't in my dictionary, and no close matches were found. Maybe it's literal!\n")

        output_text_widget.config(state="disabled")

    def _clear_fields(self, input_entry_widget, output_text_widget, output_header_label_widget):
        input_entry_widget.delete(0, tk.END)
        output_text_widget.config(state="normal")
        output_text_widget.delete(1.0, tk.END)
        output_text_widget.config(state="disabled")
        output_header_label_widget.config(text="")


# Main part of the script
if __name__ == "__main__":
    root = tk.Tk()
    app = WhatSheSaysApp(root)
    root.mainloop()