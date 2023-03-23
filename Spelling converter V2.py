"""Spelling converter, version 2"""

import easygui

word = ""
word = easygui.enterbox("PLease enter a word to ruin the spelling:", "enter the word to convert")
if "our" in word:
    bad_word = word.replace("our", "or")
    easygui.msgbox(f"the word with bad spelling is {bad_word}")
elif "ise" in word:
    bad_word = word.replace("ise", "ize")
    easygui.msgbox(f"the word with bad spelling is {bad_word}")
elif "yse" in word:
    bad_word = word.replace("yse", "yze")
    easygui.msgbox(f"the word with bad spelling is {bad_word}")
else:
    easygui.msgbox("No change in spelling")
