#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Master module for metest
"""

__author__ = "K. Hintz"
__copyright__ = "Danish Meteorological Institute"

__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "K. Hintz"
__email__ = "kah@dmi.dk"
__status__ = "Development"

import sys
import argparse
from argparse import ArgumentDefaultsHelpFormatter

def test(test:None) -> None:
    """summary

    Parameters
    ----------
    test : None
        description
    """
    return

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)





if __name__ == '__main__':
    parser = MyParser(description='Test, check and compare logs and data from meteorological computations.',
                  formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help='Print actions to console')

    args = parser.parse_args()

    if args.verbose:
        print('Verbose mode: ON', flush=True)
