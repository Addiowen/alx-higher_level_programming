#!/usr/bin/python3
"""Print ASCII alphabet, in lowercase, not followed by a new line excluding letters q and e"""

for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
