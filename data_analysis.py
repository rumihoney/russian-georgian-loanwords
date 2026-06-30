# This file analyzes the data from the russianloans.py file and counts the number of words in each category, 
# as well as the total number of words and the percentage of each category.

from russianloans import data

# Count categories
category_counts = {}

for word, info in data.items():
    category = info["category"].strip().lower()

    if category == "":
        category = "unclassified"

    if category not in category_counts:
        category_counts[category] = 0

    category_counts[category] += 1

# Print results
print("Category counts:\n")

for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{category}: {count}")

# Total words
total = sum(category_counts.values())

print("\nTotal words:", total)

# Percentages
print("\nPercentages:\n")

for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
    percent = (count / total) * 100
    print(f"{category}: {percent:.2f}%")