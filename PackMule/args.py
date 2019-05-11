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
    parser              = ArgumentParser( **PROGRAM_INFO )
    primary_swicthes    = (
            parser.add_mutually_exclusive_group( required = True )
            )
    '''
        Can I add argument groups connected to each primary switch?
    '''
    info                = (
            primary_switches.add_argument_group()
            )
    query               = (
            primary_switches.add_argument_group()
            )
    remove              = (
            primary_switches.add_argument_group()
            )
    sync                = (
            primary_switches.add_argument_group()
            )
    update              = (
            primary_switches.add_argument_group()
            )



    return parser.parse_args()
