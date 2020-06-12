#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## @package genTemporalUUID
#  Generate UUID's that will sort chronologically (χρονικός)
#

import sys
import uuid
import re
import chronos

def main(args):
    """
    Main control function when module is called as a script
    """
    # operate on just the first CLI arg for now
    numUUIDs = int(args[0])
    # assume we are passing in a project ID to use with generateIGOBasedPortalUUID

    if numUUIDs < 100:
        uuids=[chronos.uuidT() for x in range(numUUIDs)]
        print("\n".join(map(str,uuids)))
    else:
        for ii in range(numUUIDs):
            try:
                print(str(chronos.uuidT()))
            except BrokenPipeError:
                sys.exit(0)

def parse():
    """
    Command line arg parsing logic goes here; fill this in with argparse as needed in the future
    """
    args = sys.argv[1:]
    main(args)

if __name__ == '__main__':
    parse()
