# Day 21 - Sprint Challenge
# Week 3 Finale
#
# Constraint:
# Do NOT use:
# sort(), sum(), max(), min()
#
# Challenge 1: Recursion
# Challenge 2: Stack


# ============================================================
# CHALLENGE 1 - RECURSION
# Find the largest number without using max()
# ============================================================

def find_largest(numbers, index=0):
    # Base case
    if index == len(numbers) - 1:
        return numbers[index]

    # Recursively find largest value in remaining elements
    largest_remaining = find_largest(numbers, index + 1)

    # Manually compare values
    if numbers[index] > largest_remaining:
        return numbers[index]
    else:
        return largest_remaining


# ============================================================
# CHALLENGE 2 - STACK
# Reverse a string using a stack
# ============================================================

def reverse_using_stack(text):
    stack = []

    # Push every character into the stack
    for character in text:
        stack.append(character)

    reversed_text = ""

    # Pop characters to reverse the string
    while len(stack) > 0:
        reversed_text += stack.pop()

    return reversed_text


# ============================================================
# MAIN PROGRAM
# ============================================================

print("======================================")
print("       WEEK 3 SPRINT CHALLENGE")
print("======================================")

# ------------------------------------------------------------
# Challenge 1
# ------------------------------------------------------------

print("\n--- Challenge 1: Recursive Largest Number ---")

numbers = list(
    map(
        int,
        input("Enter numbers separated by spaces: ").split()
    )
)

if len(numbers) == 0:
    print("Please enter at least one number.")
else:
    largest = find_largest(numbers)

    print("Numbers:", numbers)
    print("Largest number:", largest)


# ------------------------------------------------------------
# Challenge 2
# ------------------------------------------------------------

print("\n--- Challenge 2: Stack String Reversal ---")

text = input("Enter a string: ")

reversed_text = reverse_using_stack(text)

print("Original string:", text)
print("Reversed string:", reversed_text)


print("\n======================================")
print("Challenge Completed!")
print("No sort(), sum(), max(), or min() used.")
print("======================================")
