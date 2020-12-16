from typing import TextIO

from pcfg import PCFG
import os

BASEPATH: str = os.path.dirname(__file__)

f: TextIO
with open(os.path.join(BASEPATH, "subject_adjectives.txt")) as f:
    subject_adjectives: PCFG = PCFG.fromstring(f.read())

n: int = int(input("How many sentences do you want generated? "))
sentence: str
for sentence in subject_adjectives.generate(n):
    print()
    print(sentence.capitalize())
