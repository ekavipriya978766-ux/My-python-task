def is_even(n):
    return n%2==0
def is_odd(n):
    return n%2!= 0
def maximum(a,b):
    return max(a,b)
def minimum(a,b):
    return min(a,b)
def average(a,b):
    return (a+b)/2
def reverse_string(text):
    return text[::-1]
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count +=1
    return count
def fahrenheit_to_celsius(f):
    return (f-32)*5/9
def celsius_to_fahrenheit(c):
    return (c*9/5)+32
def kg_to_pounds(kg):
    return kg*2.20462
def pounds_to_kg(lb):
    return lb/2.20462
def is_palindrome(text): 
    text=str(text)
    return text == text[::-1]