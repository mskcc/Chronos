#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## @package chronos
#  Generate UUID's that will sort chronologically (χρονικός)
#

import sys
import uuid
import re

def uuidT():

    uuTime=str(uuid.uuid1()).split("-")
    uuRand=str(uuid.uuid4()).split("-")

    uuTemporal="-".join((uuTime[2]+uuTime[1],uuTime[0][0:4],uuTime[0][4:],uuRand[3],uuRand[4]))

    return uuid.UUID("urn:uuid:"+uuTemporal)


