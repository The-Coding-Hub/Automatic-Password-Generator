# Programme Topic: Automatic Password Generator using Python

import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    # print(s1)

    s2 = string.ascii_uppercase
    # print(s2)

    s3 = string.digits
    # print(s3)

    s4 = string.punctuation
    # print(s4)

    try:
        pass_len = int(input("Enter the length for your password: "))

        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # print(s)
        # print(len(s))

        random.shuffle(s)
        # print(s)

        password = "".join(s[0:pass_len])
        print(f"Your password is below: \n{password}")
    except Exception as e:
        print("Sorry you didn't enter a number!!!")
