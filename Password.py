# password generator using python in 30 seconds

import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#%&*/\|//{}()[]~<>+=-_"

string = lower_case + upper_case + number + symbols
len = 6

password = "".join(random.sample(string,len))
print("Generate password is:",password)
