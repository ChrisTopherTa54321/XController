''' Controls XInput rumble motors '''

# fmt: off
import argparse
import logging
import sys

# fmt: on

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger("XController")



def main( args: argparse.Namespace ):
    pass

def parseArgs():
    parser = argparse.ArgumentParser(description="XInput Rumbler",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    return parser.parse_args()


###############################
# program entry point
#
if __name__ == "__main__":
    args = parseArgs()
    main(args)
