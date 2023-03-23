# a program to keep track of the day for a taxi driver

drivers_name = ""
daily_income = 0
total_time = 0
num_trips = 0

drivers_name = input("What is the driver's name?: ")

# loop to start new trips
while True:
    start_trip = input("Start a trip? (yes or no): ")
    if start_trip.lower() == "yes":
        time = int(input("How long did the trip take in minutes?: "))
        cost = time * 2 + 10  # calculate the cost of the trip
        print("The cost of this trip is $", cost)
        daily_income += cost  # add the cost of the trip to the daily income
        total_time += time  # add the time of the trip to the total time
        num_trips += 1  # increment the number of trips
    elif start_trip.lower() == "no":
        break  # exit the loop when the user is done with trips
    else:
        print("Please enter 'yes' or 'no'.")  # handle invalid input

# print the driver's name, total time, average time, total income, and average cost
print("Driver's name:", drivers_name)
print("Total time of all trips:", total_time, "minutes")
if num_trips > 0:
    print("Average time of all trips:", total_time / num_trips, "minutes")
print("Total income for the day: $", daily_income)
if num_trips > 0:
    print("Average cost of all trips: $", daily_income / num_trips)
