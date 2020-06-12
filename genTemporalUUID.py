#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## @package genTemporalUUID
#  Generate UUID's that will sort chronologically (χρονικός)
#
#
import sys
import uuid
import re

def genTemporalUUID():
    uuTime=str(uuid.uuid1()).split("-")
    uuRand=str(uuid.uuid4()).split("-")

    uuTemporal="-".join((uuTime[2]+uuTime[1],uuTime[0][0:4],uuTime[0][4:],uuRand[3],uuRand[4]))

    return uuTemporal

def main(args):
    """
    Main control function when module is called as a script
    """
    # operate on just the first CLI arg for now
    numUUIDs = int(args[0])
    # assume we are passing in a project ID to use with generateIGOBasedPortalUUID

    if numUUIDs < 100:
        uuids=[genTemporalUUID() for x in range(numUUIDs)]
        print("\n".join(uuids))
    else:
        for ii in range(numUUIDs):
            try:
                print(genTemporalUUID())
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
