"""Tech free goal"""

import easygui
tech_days = ""
tech_list = []

tech_days = easygui.enterbox("Please enter each of the days you used technology with a space between each day.", "days tech was used")
tech_list = tech_days.split()
print(tech_days)
if len(tech_list) >= 4:
    easygui.msgbox(f"Too bad, you had {len(tech_list)} days with technology, that is {len(tech_list)-3} days more than your goal!", "too bad")
else:
    easygui.msgbox(f"Congratulations! you had 3 tech free days! you met your goal with {len(tech_list)} Tech free days.", "Congratulations")
