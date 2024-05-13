# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

expenses = [2200, 2350, 2600, 2130, 2190]

# Extra expense in Feb

extra_expense = expenses[1] - expenses[0]

print(f"Extra expenses in Feb {extra_expense}")

total_expense = sum(expenses[:3])

print(f"Total Expenses {total_expense}")

is_expense_2000 = any(x == 2000 for x in expenses)

print(f"If Any expenses 2000 {is_expense_2000}")

expenses.insert(5, 1980)

print(f"June expenses added to the list {expenses[5]}")

expenses[3] = expenses[3] - 200

print(f"Updated April expenses {expenses[3]}")


# 2

heros = ["spider man", "thor", "hulk", "iron man", "captain america"]

print(f"Heros {heros}")
print(f"Length of the list {len(heros)}")

heros.append("black panther")
heros.pop()
heros.insert(heros.index("hulk") + 1, "black panther")

print(f"Updated list {heros}")

heros[1:3] = ["doctor strange"]

print(f"Updated list after removal {heros}")
heros.sort()
print(f"{heros}")

x = 100

a = [x for x in range(100) if x % 2]
print(a)
