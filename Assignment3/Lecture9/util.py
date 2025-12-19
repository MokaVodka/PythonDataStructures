# BstSet wrapper
# Done because I'm tired of Flake8 screams

import os
import sys

# Path works when respo is the opened folder in VSCode
sys.path.append(os.path.abspath('./Assignment3/Lecture7/'))

# Shaddup Flake8 >:(
import BstSet as BST


def create_BST():
    return BST.BstSet()
