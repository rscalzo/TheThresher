#!/usr/bin/env python
"""
This is the main user entry point for our lucky imaging pipeline.

I hope that the name of this file changes soon!

"""

import os
import sys
import logging

# This heinous hack let's me run this script without actually installing the
# `lucky` package. I learned this from Steve Losh at:
#     https://github.com/sjl/d/blob/master/bin/d
try:
    import lucky
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..')))
    import lucky

if __name__ == '__main__':
    import argparse

    # Start by parsing the command line arguments.
    desc = "Run online blind de-mixing on a lucky imaging data stream."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("basepath", type=str,
            help="The root directory for the imaging data")
    parser.add_argument("-o", "--output", type=str, default=None,
            help="The directory for the output files.")
    parser.add_argument("--size", type=int, default=100,
            help="The size of the inferred scene.")
    parser.add_argument("--psf_hw", type=int, default=13,
            help="The half width of the inferred PSF image.")
    parser.add_argument("--log", type=str, default="lucky.log",
            help="The filename for the log.")
    parser.add_argument("-v", "--verbose", action="store_true",
            help="Enable verbose logging.")
    args = parser.parse_args()

    if args.output is None:
        outdir = os.path.join(args.basepath, "out")
    else:
        outdir = args.output

    try:
        os.makedirs(outdir)
    except os.error:
        pass

    logfn = os.path.join(outdir, args.log)
    loglevel = logging.INFO
    if args.verbose:
        loglevel = logging.DEBUG
    logging.basicConfig(filename=logfn, level=loglevel)
