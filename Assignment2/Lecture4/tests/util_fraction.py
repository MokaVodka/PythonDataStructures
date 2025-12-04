# Src file wrapper
# Done because I'm tired of Flake8 screams

import os
import sys

# Path works when respo is the opened folder in VSCode
sys.path.append(os.path.abspath('./Assignment2/Lecture4/src'))

import fraction as fr


def Fraction(numerator, denominator):
    return fr.Fraction(numerator, denominator)
