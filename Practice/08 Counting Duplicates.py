"""
Count the number of Duplicates
Write a function that will return the count of
distinct case-insensitive alphabetic characters and numeric digits that
occur more than once in the input string.
The input string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits.
"""


def duplicate_count(text):
    cnt = {}
    text=text.lower()
    for elem in text: cnt[elem] = cnt.get(elem, 0) + 1
    doub = {el: count for el, count in cnt.items() if count > 1}
    print(len(doub.keys()))
    return len(doub.keys())


duplicate_count("abccddeeaB")
