#c16

#c15
# Assume a sequence of characters resembles a credit card number if it passes the following steps:
# 1. Working right to left, double every second digit
# 2. If a resulting product has two digits, treat the digits independently.
# 3. Sum each individual digit from step 2, including the non-doubled digits.
# 4. If the result from step 3 is a multiple of 10, assume the number is a credit card.




# String Compression: Given a string like "aaabbbaaffff" write a function that will retun the string "a3b3a2f4"
