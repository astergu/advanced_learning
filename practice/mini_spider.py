#coding=utf8

import sys
import os
import argparse
import urllib2
import logging


_VERSION = "MiniSpider 1.0"
logger = logging.getLogger(__name__)

def parse_urls(confpath):
    with open(confpath) as fin:
        for line in fin:
            try:
                response = urllib2.urlopen(line)
                html = response.read()
                print html
            except Exception e:
                print >> sys.stderr, e

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", type=str, help="Attach a configure file to initiate the program")
    parser.add_argument("-v", "--version", help="Print out the version", action="store_true")
    args = parser.parse_args()
    if args.version:
        print _VERSION
    if args.config:
        config_loc = args.config
        if os.path.exists(config_loc) and os.path.isfile(config_loc):
            print >> sys.stderr, "%s doesn't exist!" % config_loc
        else:
            parse_urls(config_loc)
