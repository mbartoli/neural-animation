#!/usr/bin/python
__author__ = 'mbartoli'

import argparse
import subprocess
import sys
import os
import errno


def make_sure_path_exists(path):
    '''
    make sure input and output directory exist, if not create them.
    If another error (permission denied) throw an error.
    '''
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def main(input, output, image_type):
    make_sure_path_exists(input)
    make_sure_path_exists(output)

    nrframes =len([name for name in os.listdir(input) if os.path.isfile(os.path.join(input, name))])
    if nrframes == 0:
        print("no frames to process found")
        sys.exit(0)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Implementing neural art on video.')
    parser.add_argument(
        '-i','--input',
        help='Input directory where extracted frames are stored',
        required=True)
    parser.add_argument(
        '-o','--output',
        help='Output directory where processed frames are to be stored',
        required=True)
    parser.add_argument(
        '-it','--image_type',
        help='Specify whether jpg or png ',
        required=True)

    args = parser.parse_args()

    main(args.input, args.output, args.image_type)
