#!/usr/bin/python
from twitter_enterer import Enterer
import utils
import sys

if __name__ == "__main__":
    enterer = Enterer(sys.argv[1])
    enterer.run()