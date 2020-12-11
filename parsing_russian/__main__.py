from nltk.parse.generate import generate
from nltk import CFG
import os

BASEPATH = os.path.dirname(__file__)

with open(os.path.join(BASEPATH, "subject_adjectives.txt")) as f:
    subject_adjectives = CFG.fromstring(f.read())