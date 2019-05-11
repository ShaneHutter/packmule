#!/usr/bin/env python3
"""
PackMule
    PackMule.args

    Written By:
        Shane Hutter

    Description:
        Argument parsing for packmule

    License:
        GNU GPLv3
"""

__all__ = [ argparser , ]

from argparse   import ArgumentParser

def argparser():
    """
        Command line arguments for PackMule
    """
    parser  = ArgumentParser( **PROGRAM_INFO )

    return parser.parse_args()
