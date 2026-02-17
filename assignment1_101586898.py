"""
Author: Navjot Kaur Mathoda
Stu id : 101586898
Assignment: #1 COMP2152
"""

# Variables with data types
gym_member = "Alex Alliton"      # str
preferred_weight_kg = 20.5       # float
highest_reps = 25                # int
membership_active = True         # bool

# Dictionary storing workout minutes (dict with tuple values)
workout_stats = {
    "Alex": (30, 45, 20),
    "Gigi": (25, 35, 40),
    "Eric": (50, 30, 25)
}

# Calculate total minutes for each friend and add to dictionary
for friend, minutes in workout_stats.copy().items():
    total_minutes = sum(minutes)
    workout_stats[friend + "_Total"] = total_minutes

# Create 2D list (nested list) from workout minutes
workout_list = [list(workout_stats[friend]) for friend in ["Alex", "Gigi", "Eric"]]

# Slice and print yoga and running minutes
yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running minutes:", yoga_running)

# Slice and print weightlifting for last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting (last two friends):", weightlifting_last_two)

# Check if any friend has total >= 120 minutes
for friend in ["Alex", "Gigi", "Eric"]:
    if workout_stats[friend + "_Total"] >= 120:
        print(f"Great job staying active, {friend}!")

# Ask user for friend's name
friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats:
    print("Workout minutes (yoga, running, weightlifting):", workout_stats[friend_name])
    print("Total minutes:", workout_stats.get(friend_name + "_Total"))
else:
    print(f"Friend {friend_name} not found in the records.")

# Find highest and lowest total workout minutes
totals = {friend: workout_stats[friend + "_Total"] for friend in ["Alex", "Gigi", "Eric"]}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("Friend with highest total minutes:", highest_friend)
print("Friend with lowest total minutes:", lowest_friend)
