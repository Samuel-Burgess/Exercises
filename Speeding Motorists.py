# Police patrol care software indev ver0.1
total_fines = 0
speeders = []
speeds = []
warrants = ["ZACHARY CONROY", "JAMES WILSON", "HELGA NORMAN"]
speeders_name = ""


def daily_speeders():
    global warrants
    global speeders
    global total_fines
    global speeds
    global speeders_name
    while speeders_name != "X":
        print("##########")
        speeders_name = input("What is the speeders name?: ")
        if speeders_name.upper() in warrants:
            print(f"{speeders_name.upper()}, - WARRANT TO ARREST")
        if speeders_name not in "X":
            speeders.append(speeders_name)
            speed = int(input("How much over the speed limit were they traveling?: "))
            speeds.append(speed)
            if speed < 10:
                fine = 30
            elif speed < 15:
                fine = 80
            elif speed < 20:
                fine = 120
            elif speed < 25:
                fine = 170
            elif speed < 30:
                fine = 230
            elif speed < 35:
                fine = 300
            elif speed < 40:
                fine = 400
            elif speed < 45:
                fine = 510
            else:
                fine = 630
            print(f"{speeders_name} to be fined ${fine}")
            total_fines = total_fines + fine
            print("##########")
        else:
            print("Day over")
            print("##########")
            break


daily_speeders()
print(f"Total fines {len(speeds)}")
for i in range(len(speeders)):
    print(f"{i + 1}) Name: {speeders[i]} Amount over Limit: {speeds[i]}")
print(f"Total amount of fines: ${total_fines}")
