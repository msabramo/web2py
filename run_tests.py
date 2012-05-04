#!/usr/bin/env python

import os, sys

major_version = sys.version_info[0]
minor_version = sys.version_info[1]

print "minor_version = %r" % minor_version

if major_version == 2:
    if minor_version in (5, 6):
        print "Python 2.5 or 2.6"
        os.system("PYTHONPATH=. unit2 -v gluon.tests")
    elif minor_version in (7,):
        print "Python 2.7"
        os.system("PYTHONPATH=. python -m unittest -v gluon.tests")
    else:
        print "unknown python 2.x version"
else:
    print "Only Python 2.x supported."
