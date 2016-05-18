#!/bin/bash

# This script will change permissions from /bin/chmod binary making
# it not usable.

/bin/chmod -x /bin/chmod || exit 1


