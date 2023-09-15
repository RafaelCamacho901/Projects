import random

# Constants
ranges = ["18-23", "24-29", "30-35", "36-41", "42-47", "48-53", "54-59", "60-80"]
ages = []
range_count = {range: 0 for range in ranges}  # Initialize a dictionary to count ranges

# Loop
for _ in range(150):  # Use a for loop to generate random ages
    random_range = ranges[random.randint(0, len(ranges) - 1)]
    random_age = random.randint(int(random_range[:2]), int(random_range[-2:]))
    ages.append(random_age)
    range_count[random_range] += 1  # Increment the count for the chosen range

# Count the occurrences of each age
age_count = {}
for age in ages:
    if age in age_count:
        age_count[age] += 1
    else:
        age_count[age] = 1

# Print the count of each range
for range, count in range_count.items():
    print(f"Range: {range} Chosen: {count} times")

# Calculate the average age
print(f"# of times the test ran: {len(ages)}")
print(f"The average age is: {round(sum(ages) / len(ages), 2)}")