"""
This script get the input as:
The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. This video was captured by one of our heroes who wishes peace.

 and gives:

2:Persian
3:League
15:Iran
17:Persian
18:League


Author: Mojtaba Hassanzadeh
Date: March 9, 2024
"""

import re

numbers = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
    'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
    'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
    'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
    'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000,
    'million': 1000000, 'billion': 1000000000
}

txt = input()

pattern = r'\b(?<![.]\s)[A-Z][a-zA-Z]*\b' # negative lookbehind assertion : (?<!pattern)
cap_words = re.findall(pattern, txt)
all_words = re.findall('[a-zA-Z]+', txt)
all_words = all_words[1:]
cap_words = cap_words[1:]
if not cap_words:
    print("None")
else:
    for index, item in enumerate(all_words):
        if item in cap_words and item.lower() not in numbers.keys():
            print(f"{index+2}:{item}")
