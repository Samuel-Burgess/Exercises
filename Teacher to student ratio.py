"""teacher to student ratio"""

import easygui
import math

calc = "Yes"


def class_size_check():
    school_name = easygui.enterbox("Enter the name of the school", "School name")
    max_children = easygui.integerbox("What is the maximum number of children allowed per class?: \nMust be a number"
                                      "between 10 and 30", "Maximum class size", "", 10, 30)
    total_children = easygui.integerbox(f"What is the total number of children at {school_name}:\n"
                                        f"Must be a number between 10 and 1400", "Total roll of school", "", 10, 1400)
    easygui.msgbox(f"{math.ceil(total_children / max_children)} teachers will be needed, as there will need to be"
                   f" {math.ceil(total_children / max_children)} classes in total.")
    teachers = easygui.integerbox(f"How many teachers are Available at {school_name}\n"
                                  f"Must be a number between 1 and 120", "Teachers Available", "", 1, 120)
    if teachers == math.ceil(total_children / max_children):
        easygui.msgbox("You have the perfect number of teachers!", "Right amount of staff")
    elif teachers < math.ceil(total_children / max_children):
        easygui.msgbox(
            f"You are understaffed, you need {math.ceil((total_children / max_children) - teachers)} more teachers",
            "Under-Staffed")
    else:
        easygui.msgbox(
            f"You are Overstaffed, you could do without {teachers - (math.ceil(total_children / max_children))} "
            f"Teachers", "Over-Staffed")


while calc == "Yes":
    class_size_check()
    calc = easygui.buttonbox("Do you want to make another calculation?", "Calculate again", choices=["Yes", "No"])
easygui.msgbox("Goodbye", "Thanks for using this calculator")
