import random
import string


# for coding the msg
user = input("You want to code the message or decode the message (C/D) --> ").upper()

if user == 'C' or user == 'D':
    a = input("Enter your message --> ")
    print(a)
    b = list(a)
    print("In list --> ", b)

    # for coding the message
    if user[0] == 'C':
        # checking the length of input string if it is having more than 3 words then append the first
        # letter to the end of the word
        if len(b) > 3:
            first_letter = b[0]
            b.remove(first_letter)
            print(b)
            b.append(first_letter)
            print("Code first to last --> ", b)
            # 3 random characters for adding to the front and ending of the word
            # adding in the front of the word
            character = string.ascii_letters
            # list comprehensions
            front = (random.choice(character) for i in range(3))
            front = list(front)
            front.extend(b)
            b = front
            print(f"First added {b}")

            # adding at the ending of the word
            end = (random.choice(character) for i in range(3))
            end = list(end)
            b.extend(end)
            print(f"end added {b}")

            # changing the list to string
            b = ''.join(i for i in b)
            print("Coded Message --> ", b)
            # LSdantoMiPG
        # for less than 3 letters word --> we will reverse that words
        else:
            b.reverse()
            b = ''.join(i for i in b)
            print("Code --> ", b)

    # for decoding the message
    else:
        if len(b) < 3:
            b.reverse()
            b = ''.join(i for i in b)
            print("Message after decoding --> ", b)
        else:
            # removing the first 3 letters
            b = b[3:]
            print(b)

            # removing the last 3 letters
            b = b[:-3]
            print(b)

            # removing last letter ad add to first
            last = b[-1]
            del b[-1]
            print(b)
            b.insert(0,last)
            print(b)

            b = ''.join(i for i in b)
            print("Message after Decoding finally --> ", b)
else:
    raise ValueError("Enter only C or D!")

