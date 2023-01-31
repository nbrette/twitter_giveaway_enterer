#!/usr/bin/python3
from twitter_enterer import Enterer
import src.services.utils as utils
import sys
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--language', type=str,
                        help='Language to use')

    parser.add_argument('--key', type=str,
                        help='Key of the credentials you want to use from your config file')
    args = parser.parse_args()

    enterer = Enterer(args.language, args.key)
    enterer.run()
