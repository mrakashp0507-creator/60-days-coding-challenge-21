# Day 21 - Sprint Challenge

## Week 3 Finale

This challenge combines recursion and stack concepts under one important constraint:

## Constraint

The following built-in helper functions were NOT used:

- sort()
- sum()
- max()
- min()

The goal was to manually implement the required logic.

---

# Challenge 1 - Recursive Largest Number

## Problem

Find the largest number in an array using recursion without using max().

## Approach

The recursive function checks one element at a time.

### Base Case

When the function reaches the final element, it returns that value.

### Recursive Case

The function finds the largest value in the remaining elements and compares it with the current element.

Example:

    [10, 25, 7, 40, 15]

Result:

    40

## Complexity

Time Complexity: O(n)

Space Complexity: O(n)

The extra space comes from recursive function calls.

---

# Challenge 2 - Stack String Reversal

## Problem

Reverse a string using a stack.

## Approach

1. Create an empty stack.
2. Push every character into the stack.
3. Pop characters one by one.
4. Build the reversed string.

Example:

    ROBOT

Stack output:

    TOBOR

## Complexity

Time Complexity: O(n)

Space Complexity: O(n)

---

# Built-in Functions Avoided

The following functions were intentionally not used:

    sort()
    sum()
    max()
    min()

All required logic was implemented manually.

---

# Concepts Practiced

- Recursion
- Base cases
- Recursive calls
- Stack
- LIFO
- Manual comparison
- Array processing
- String processing
- Complexity analysis
- Edge-case testing

---

# How to Run

Open VS Code terminal:

    python day21_sprint_challenge.py

---

# Real-World Impact

Understanding low-level logic helps engineers reason about how algorithms work internally.

These concepts are useful for:

- Debugging
- Compilers
- Expression processing
- Data structures
- System design
- Performance optimization
