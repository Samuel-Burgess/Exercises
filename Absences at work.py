# Define variables and data structures
employee_names = []
absence_days = []
total_days = 0
max_absentee = 0
max_absentee_name = ""
not_absent = []
above_average = []


# Define functions
def input_employee_data():
    while True:
        data = input().strip()
        if data == "$":
            break
        parts = data.split()
        employee_names.append(" ".join(parts[:-1]))
        absence_days.append(int(parts[-1]))


def calculate_total_days():
    global total_days
    total_days = sum(absence_days)


def calculate_average():
    return total_days / len(employee_names)


def find_max_absentee():
    global max_absentee
    global max_absentee_name
    for i in range(len(employee_names)):
        if absence_days[i] > max_absentee:
            max_absentee = absence_days[i]
            max_absentee_name = employee_names[i]


def find_not_absent():
    for i in range(len(employee_names)):
        if absence_days[i] == 0:
            not_absent.append(employee_names[i])


def find_above_average():
    average = calculate_average()
    for i in range(len(employee_names)):
        if absence_days[i] > average:
            above_average.append(employee_names[i])


# Get input data
input_employee_data()

# Calculate data
calculate_total_days()
find_max_absentee()
find_not_absent()
find_above_average()

# Print results
print(f"Average number of days staff were absent: {calculate_average():.2f}\n")
print(f"Person with most days absent: {max_absentee_name} with {max_absentee} days\n")
print("List of people not absent at all:")
for name in sorted(not_absent):
    print(name)
print()
print("List of people absent above average:")
for name in sorted(above_average):
    print(f"{name} {absence_days[employee_names.index(name)]}")

