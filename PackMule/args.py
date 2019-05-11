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


from .          import PROGRAM_INFO
from argparse   import ArgumentParser
from re         import match
from sys        import argv


'''
Notes:
    argparse can't handle the switching style I prefer.
    I will have to build the parser from the ground up.
'''


SWITCH_TYPES    = {
        "short" : "-"   ,
        "long"  : "--"  ,
        }
IS_LONG_SWITCH  = {
        "short" : False ,
        "long"  : True  ,
        }

PRIMARY_SWITCHES   = {
        "B" : {
            "name"      : "build"                                   , 
            "one arg"   : False                                     ,
            "bool"      : False                                     ,
            "help"      : """
            Build RPM packages.  Pass package rott directories as 
            arguments.
            """                                                     ,
            }   ,
        "C" : {
            "name"      : "create"                                      ,
            "one arg"   : True                                          ,
            "bool"      : False                                         ,
            "help"      : """
            Specify the repository, or package group (-g) which will be
            operated upon.
            """                                                         ,
            }   ,
        "D" : {
            "name"      : "databases"                   ,
            "one arg"   : False                         ,
            "bool"      : False                         ,
            "help"      : """
            Manage local PackMule databases and caches.
            """                                         ,
            }   ,
        "I" : {
            "name"  : "info"                            ,
            "one arg" : False                           ,
            "bool"      : False                         ,
            "help"  : """
            Manage local PackMule databases and caches.
            """                                         ,
            }   ,
        "Q" : { 
            "name"      : "query"                                       ,
            "one arg"   : False                                         ,
            "bool"      : False                                         ,
            "help"      : """
            Query remote details from packages and package groups in a
            remotely hosted repository.  Also, query information for
            remotely hosted repositories
            """                                                         ,
            }   ,
        "R" : { 
            "name"      : "remove"                                      ,
            "one arg"   : False                                         ,
            "bool"      : False                                         ,
            "help"      : """
            Remove a package or package group which has been installed
            on the local system.
            """                                                         ,
            }   ,
        "S" : {
            "name"      : "sync"                    ,
            "one arg"   : False                     ,
            "bool"      : False                     ,
            "help"      : """
            Synchronize packages from a repository
            """                                     ,
            }   ,
        "U" : {
            "name"      : "update"                      ,
            "one arg"   : False                         ,
            "bool"      : False                         ,
            "help"      : """
            Update packages, and repository databases.
            """                                         ,
            }   ,
        "V" : { 
            "name"      : "version"                                     ,
            "one arg"   : False                                         ,
            "bool"      : True                                          ,
            "help"  : """
            Display version information, or other details on the current
            installed version of PackMule.  If no additional switches 
            are provided, then only the version number is displayed.
            This operation will queue at the end of all other operations.
            """                                                         ,
            }   ,
        }

"""
    Secondary switches all store a bool.
    Some conflict with each other.
    Info and query contain repo and package group switches.  These do
    not conflict.  If the switch is present, and the repo or package group
    can be found, then ignore if a repo is not a package, etc.  If the
    switch is not present, then show that a package (etc...) is not found.
"""
SECONDARY_SWITCHES  = {
        PRIMARY_SWITCHES[ "B" ] : {    ,
        PRIMARY_SWITCHES[ "C" ] : {
            "a" : {
                "value"     : bool()                ,
                "conflicts" : None                  ,
                "name"      : "pkg add"             ,
                "help"      : """
                Add a package to local repository
                """                                 ,
                }   ,
            "d" : {
                "value"     : bool()                                ,
                "conflicts" : None                                  ,
                "name"      : "delete"                              ,
                "help"      : """
                Delete a package from the local repository.  
                Additionally, this may be paired with group (-g) or 
                repo (-r).
                """                                                 ,
                }   ,
            "f" : {
                "value"     : bool()                                    ,
                "conflicts" : None                                      ,
                "name"      : "force"                                   ,
                "help"      : """
                Force an operation.  I'm not 100% on what this will 
                entail with each primary swith.
                """                                                     ,
                }   ,
            "g" : {    ,
                "value"     : bool()        ,
                "conflicts" : ( "r" , )     ,
                "name"      : "pkg group"   ,
                "help"      : """
                Create or operate upon a package group in the repository.
                Additionally, add delete(-d) or upgrade (-u) to remove
                or upgrade the packages in the package group.
                """                         ,
                }    ,
            "r" : {    ,
                "value"     : bool()                                    ,
                "conflicts" : ( "g" , )                                 ,
                "name"      : "repo"                                    ,
                "help"      : """
                Build a new repository, or delete (-d) an existing
                repository, from the local system.  Create will manage 
                the given repository if this is not specified.
                """                                                     ,
                }    ,
            "u" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            }                           ,
        PRIMARY_SWITCHES[ "D" ] : {
            "c" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "e" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "f" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            }                           ,
        PRIMARY_SWITCHES[ "I" ] : {
            "d" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "g" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "l" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "r" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "u" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "w" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            }                           ,
        PRIMARY_SWITCHES[ "Q" ] : {
            "d" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "g" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "l" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "r" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "u" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "w" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            }                           ,
        PRIMARY_SWITCHES[ "R" ] : {
            "c" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "f" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "g" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "l" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "p" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "r" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            }                           ,
        PRIMARY_SWITCHES[ "S" ] : {
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            }                           ,
        PRIMARY_SWITCHES[ "U" ] : {
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            "" : {    ,
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }    ,
            }                           ,
        PRIMARY_SWITCHES[ "V" ] : {
            "" : {
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }   ,
            "" : {
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }   ,
            "" : {
                "value"     : bool()    ,
                "conflicts" : None      ,
                "name"      : "" ,
                "help"      : """
                """                     ,
                }   ,
            }       ,
        }




def _switch_parse( arg ):
    """
        If the argument is a switch, return a dictionary of the current
        switch's properties, or else return None.

        switch_properties dict
            primary : primary switch name
            secondary: dict()

    """
    # Determine if switch is long, short, or not a switch
    switch_len , switch_long    = int() , bool()
    for switch_type in SWITCH_TYPES:
        if arg[
                :SWITCH_TYPES[ switch_type ]
                ] == SWITCH_TYPES[ switch_type ] and len( 
                        SWITCH_TYPES[ switch_type ]
                        ) >= switch_len:
            switch_len , switch_long = len(
                    SWITCH_TYPES[ switch_type ]
                    ) , IS_LONG_SWITCH[ switch_type ]
        else:
            # It's not a switch
            return False

        # d
        if



    if arg[
            :len(
                SWITCH_TYPES[ "short" ]
                )
            ] == SWITCH_TYPES[ "short" ]:
        if arg[
                :len(
                    SWITCH_TYPES[ "long" ]
                    )
                ] == SWITCH_TYPES[ "long" ]:
            
        else:
            return ( True , False )
    else:
        return False




####  DEPRICATED - argparse is not suitable #####

# Declare variables and constants
PRIMARY_SWITCHES    = {
        "build"         : {
            "title"         : "Build"                                   , 
            "description"   : """
            Build an RPM package.
            """                                                         ,
            }           ,
        "create"        : {
            "title"         : "Create"                                  ,
            "description"   : """
            Create and manage a locally (remotely?) built package
            repository
            """                                                         ,
            }           ,
        "databases"      : {
            "title"         : "Databases"                               ,
            "description"   : """
            Clean and maintain the local databases
            """                                                         ,
            }           ,   
        "info"          : {
            "title"         : "Information"                             ,
            "description"   : """
            Display package, package group, and repository information 
            from packages, package groups, and repositories installed 
            or setup locally on the system
            """                                                         ,
            }           ,
        "query"         : {
            "title"         : "Query"                                   ,
            "description"   : """
            Query package, package group, and repository information
            from a remote package repository
            """                                                         ,
            }           ,
        "remove"        : {
            "title"         : "Remove"                                  ,
            "description"   : """
            Remove packages and package groups from the local system.
            Delete locally created package repositories off of the
            system.
            """                                                         ,
            }           ,
        "sync"          : {
            "title"         : "Sync"                                    ,
            "description"   : """
            Syncronize and packages from a repository
            """                                                         ,
            }           ,
        "update"        : {
            "title"         : "Update"                                  ,
            "description"   : """
            Update and upgrade local repository database and packages
            from remote repositories.
            """                                                         ,
            }           ,
        "version"       : {
            "title"         : "Version"                                 ,
            "description"   : """
            Display PackMule version, and other details
            """                                                         ,
            }
        }


def argparser():
    """
        Command line arguments for PackMule
    """
    # Declare parser and groups
    parser              = ArgumentParser( **PROGRAM_INFO )
    '''
        If I can't use required in add_argument_group, then I
        may need to put the group inside a required mutually 
        exclusive group with only primay switches as it's member.
    '''
    primary_switches    = parser.add_argument_group()
    '''
        Can I add argument groups connected to each primary swith?
    '''
    build               = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "build" ]
                )
            )
    create              = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "create" ]
                )
            )
    create_du           = (
            create.add_mutually_exclusive_group()
            )
    databases           = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "databases" ]
                )
            )
    info                = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "info" ]
                )
            )
    query               = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "query" ]
                )
            )
    remove              = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "remove" ]
                )
            )
    sync                = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "sync" ]
                )
            )
    update              = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "update" ]
                )
            )
    version             = (
            primary_switches.add_argument_group(
                PRIMARY_SWITCHES[ "version" ]
                )
            )

    '''
        To fix:
            Argument groups will not allow for the same letters in other
            groups.  Parsing may become more comlicated...
    '''
    # Build
    build.add_argument(
            "-B"                    ,
            "--build"               ,
            nargs       = "1"       ,
            help        = """
            Build an RPM package.
            """                     ,
            )

    build.add_argument(
            "-r"                                                        ,
            "--pkg-root"                                                ,
            action      = "store_true"                                  ,
            required    = True                                          ,
            help        = """
            Root directory of files to be packaged.  This is required.
            """                                                         ,
            )

    '''
        Make sure that this being required will not also make
        -B a required argument!
    '''

    # Create
    create.add_argument(
            "-C"                                                        ,
            "--create"                                                  ,
            nargs       = "1"                                           ,
            help        = """
            Specify the repository, or package group (-g) which will be
            operated upon.
            """                                                         ,
            )

    create.add_argument(
            "-a"                                ,
            "-add-pkg"                          ,
            action      = "store_true"          ,
            help        = """
            Add a package to local repository
            """                                 ,
            )

    '''
        Add and delete are not mutually exclusive.  The operations will
        be queued.  First, an existing package will be deleted, then
        the new will add, even if the same package is listed.  Any 
        number of packages can be added or removed from a repo, or 
        package group.

        Delete and upgrade will need to be mutually exclusive.
    '''
    create_du.add_argument(
            "-d"                                                        ,
            "--delete"                                                  ,
            action      = "store_true"                                  ,
            help        = """
            Delete a package from the local repository.  Additionally,
            this may be paired with group (-g) or repo (-r).
            """                                                         ,
            )

    create.add_argument(
            "-f"                                                        ,
            "--force"                                                   ,
            action      = "store_true"                                  ,
            help        = """
            Force an operation.  I'm not 100% on what this will entail
            with each primary swith.
            """                                                         ,
            )

    create.add_argument(
            "-g"                                                        ,
            "--pkg-group"                                               ,
             # List packages to operate upon
            nargs       = "+"                                           , 
            help        = """
            Create or operate upon a package group in the repository.
            Additionally, add delete(-d) or upgrade (-u) to remove
            or upgrade the packages in the package group.
            """                                                         ,
            )

    create.add_argument(
            "-r"                                                        ,
            "--repo"                                                    ,
            action  = "store_true"                                      ,
            help    = """
            Build a new repository, or delete (-d) an existing
            repository, from the local system.  Create will manage the
            given repository if this is not specified.
            """                                                         ,
            )

    create_du.add_argument(
            "-u"                                                        ,
            "--upgrade"                                                 ,
            action      = "store_true"                                  ,
            help        = """
            Upgrade a package in a repostory, or group (-g) on the
            local system.
            """                                                         ,
            )

    # Databases
    databases.add_argument(
            "-D"                                        ,
            "--databases"                               ,
            action          = "store_true"              ,
            help            = """
            Manage local PackMule databases and caches.
            """                                         ,
            )
            
    databases.add_argument(
            "-c"                            ,
            "--clean"                       ,
            action  = "store_true"          ,
            help    = """
            Clean local database metadata.
            """                             ,
            )
            
    databases.add_argument(
            "-e"                        ,
            "--empty"                   ,
            action      = "store_true"  ,
            help        = """
            Empty the PackMule cache.
            """                         ,
            )

    databases.add_argument(
            "-f"                                                        ,
            "--force"                                                   ,
            action      = "store_true"                                  ,
            help        = """
            Force an operation.  I'm not 100% on what this will entail
            with each primary swith.
            """                                                         ,
            )

    # Info
    info.add_argument(
            "-I"                                                    ,
            "--info"                                                ,
            nargs   = "+"                                           ,
            help    = """
            Display information from  locally installed packages or
            package groups.  Also, display information for locally
            hosted repositories.
            """                                                     ,
            )

    info.add_argument(
            "-d"                        ,
            "--details"                 ,
            action      = "store_true"  ,
            help        = """
            Display package details.
            """                         ,
            )
    '''
    Details, package group, and repo are not mutually exclusive. 
    Packages, package groups, and repositories cannot have the same name 
    (check yum compatibility).  The listed arguments will queue
    (package, package group, repo) and will list details of each provided
    argument that was passed into info.
    '''

    info.add_argument(
            "-g"                            ,
            "--pkg-group"                   ,
            action          = "store_true"  ,
            help            = """
            Display package group details.
            """                             ,
            )

    info.add_argument(
            "-l"                                                        ,
            "--list-installed"                                          ,
            action              = "store_true"                          ,
            help                = """
            List the files installed from teh provided package.  This
            can also be used with package group (-g) and repo (-r).
            """                                                         ,
            )

    info.add_argument(
            "-r"                                        ,
            "--repo"                                    ,
            action  = "store_true"                      ,
            help    = """
            Display locally hosted repository details.
            """                                         ,
            )

    info.add_argument(
            "-u"                                                    ,
            "--update"                                              ,
            action  = "store_true"                                  ,
            help    = """
            Update local repository databases prior to checking the
            details of any provided argument.
            """                                                     ,
            )

    info.add_argument(
            "-w"                                                        ,
            "--what-provides"                                           ,
            action  = "store_true"                                      ,
            help    = """
            List what package provides the specified file.  This can
            be used along side other switches, which seek information
            on packages listed in the arguments.
            """                                                         ,
            )
    '''
    What provides (-w) is not mutually exclusive to any other swith
    provided with the primary swith.  If what provides is included
    with other switches, then file names will be ignored by other queued
    operations, but only if the file actuall exists in the filesystem;
    Otherwise, an exception will be raised.  If a file is passed without
    the what provides swith, an exception will be raised.
    '''

    # Query
    query.add_argument(
            "-Q"                                                        ,
            "--query"                                                   ,
            nargs       = "+"                                           ,
            help        = """
            Query remote details from packages and package groups in a
            remotely hosted repository.  Also, query information for
            remotely hosted repositories.
            """                                                         ,
            )

    query.add_argument(
            "-d"                        ,
            "--details"                 ,
            action      = "store_true"  ,
            help        = """
            Display package details.
            """                         ,
            )
    '''
    Details, package group, and repo are not mutually exclusive. 
    Packages, package groups, and repositories cannot have the same name 
    (check yum compatibility).  The listed arguments will queue
    (package, package group, repo) and will list details of each provided
    argument that was passed into info.
    '''

    query.add_argument(
            "-g"                            ,
            "--pkg-group"                   ,
            action          = "store_true"  ,
            help            = """
            Display package group details.
            """                             ,
            )

    query.add_argument(
            "-l"                                                        ,
            "--list-installed"                                          ,
            action              = "store_true"                          ,
            help                = """
            List the files installed from teh provided package.  This
            can also be used with package group (-g) and repo (-r).
            """                                                         ,
            )

    query.add_argument(
            "-r"                                        ,
            "--repo"                                    ,
            action  = "store_true"                      ,
            help    = """
            Display locally hosted repository details.
            """                                         ,
            )

    query.add_argument(
            "-u"                                                    ,
            "--update"                                              ,
            action      = "store_true"                              ,
            help        = """
            Update local repository databases prior to checking the
            details of any provided argument.
            """                                                     ,
            )

    info.add_argument(
            "-w"                                                        ,
            "--what-provides"                                           ,
            action  = "store_true"                                      ,
            help    = """
            List what package provides the specified file.  This can
            be used along side other switches, which seek information
            on packages listed in the arguments.
            """                                                         ,
            )
    '''
    What provides (-w) is not mutually exclusive to any other swith
    provided with the primary swith.  If what provides is included
    with other switches, then file names will be ignored by other queued
    operations, but only if the file actuall exists in the filesystem;
    Otherwise, an exception will be raised.  If a file is passed without
    the what provides swith, an exception will be raised.
    '''
    
    # Remove
    remove.add_argument(
            "-R"                                                        ,
            "--remove"                                                  ,
            action      = "store_true"                                  ,
            help        = """
            Remove a package or package group which has been installed
            on the local system.
            """                                                         ,
            )

    remove.add_argument(
            "-c"                                ,
            "--clean"                           ,
            action      = "store_true"          ,
            help        = """
            Clean up PackMule's package cache
            """                                 ,
            )

    remove.add_argument(
            "-f"                                                        ,
            "--force"                                                   ,
            action      = "store_true"                                  ,
            help        = """
            Force an operation.  I'm not 100% on what this will entail
            with each primary swith.
            """                                                         ,
            )

    remove.add_argument(
            "-g"                                            ,
            "--pkg-group"                                   ,
            action          = "store_true"                  ,
            help            = """
            Remove a package group from the local system.
            """                                             ,
            )

    remove.add_argument(
            "-l"                                                        ,
            "--lock"                                                    ,
            action  = "store_true"                                      ,
            help    = """
            Remove the lock file for PackMule.  Use this if PackMule
            exited in an uncontrolled manner, which may leave the lock
            file in place.  Running this command will also attempt to
            terminate any running PackMule process.
            """                                                         ,
            )

    remove.add_argument(
            "-p"                                                    ,
            "--purge"                                               ,
            action      = "store_true"                              ,
            help        = """
            Also remove any dependancy that is only required by the
            package being removed.
            """                                                     ,
            )

    remove.add_argument(
            "-r"                                                            ,
            "--repo"                                                        ,
            action  = "store_true"                                          ,
            help    = """
            Remove a locally hosted repository.  This is interchangeable
            with running Create delete repo (-Cdr).
            """                                                             ,
            )

    # Sync
    sync.add_argument(
            "-S"                                    ,
            "--sync"                                ,
            nargs   = "+"                           ,
            help    = """
            Synchronize packages from a repository
            """                                     ,
            )

    sync.add_argument(
            "-d"                                                            ,
            "--downgrade"                                                   ,
            action          = "store_true"                                  ,
            help            = """
            Downgrade a package, from a remotely hosted repository, to
            either a specified version, or date.  Multiple date formats
            are accepted, and automatically determined, providing the
            date format is synactically correct, and a recognized format.
            A Unix epocal timestamp is an acceptable date format.
            """                                                             ,
            )

    sync.add_argument(
            "-f"                                                        ,
            "--force"                                                   ,
            action  = "store_true"                                      ,
            help    = """
            Force an operation.  I'm not 100% on what this will entail
            with each primary swith.
            """                                                         ,
            )

    sync.add_argument(
            ""  ,
            ""  ,
            action  = "store_true"  ,
            help    = """
            """                     ,
            )

    sync.add_argument(
            ""  ,
            ""  ,
            action  = "store_true"  ,
            help    = """
            """                     ,
            )


    sync.add_argument(
            ""  ,
            ""  ,
            action  = "store_true"  ,
            help    = """
            """                     ,
            )

    sync.add_argument(
            ""  ,
            ""  ,
            action  = "store_true"  ,
            help    = """
            """                     ,
            )

    # Update
    update.add_argument(
            "-U"                                        ,
            "--update"                                  ,
            nargs       = "*"                           ,
            help        = """
            Update packages, and repository databases.
            """                                         ,
            )

    update.add_argument(
            "-d"                                                        ,
            "--downgrade"                                               ,
            action          = "store_true"                              ,
            help            = """
            Downgrade either all or any specified packages to a supplied
            date.  Several date formats will be accepted, include epocal
            timestamps.
            """                                                         ,
            )

    update.add_argument(
            "-f"                                                        ,
            "--force"                                                   ,
            action      = "store_true"                                  ,
            help        = """
            Force an operation.  I'm not 100% on what this will entail
            with each primary swith.
            """                                                         ,
            )

    update.add_argument(
            "-g"                                                            ,
            "--pkg-group"                                                   ,
            nargs           = "+"                                           ,
            help            = """
            Upgrade the provided package groups. If no additional
            packages are provided to upgrade, then only the packages from
            the provided package groups will be upgraded.
            """                                                             ,
            )

    update.add_argument(
            "-r"                                                            ,
            "--reinstall-pkgs"                                              ,
            action              = "store_true"                              ,
            help                = """
            Either reinstall all packages, or the packages provided. This
            can be combined with package group (-g), to reinstall both the
            provided groups, and any listed packages.
            """                                                             ,
            )

    update.add_argument(
            "-u"                                ,
            "--update"                          ,
            action      = "store_true"          ,
            help        = """
            Update repository package databases.
            """                                 ,
            )

    # Version
    version.add_argument(
            "-V"                                                            ,
            "--version-info"                                                ,
            action          = "store_true"                                  ,
            help            = """
            Display version information, or other details on the current
            installed version of PackMule.  If no additional switches are
            provided, then only the version number is displayed.  This
            operation will queue at the end of all other operations.
            """                                                             ,
            )

    version.add_argument(
            "-a"                                                        ,
            "--all"                                                     ,
            action  = "store_true"                                      ,
            help    = """
            Display all information for the currently installed version
            of PackMule.
            """                                                         ,
            )

    version.add_argument(
            "-d"                                                        ,
            "--describe"                                                ,
            action      = "store_true"                                  ,
            help        = """
            Display a description of the currently installed version of
            PackMule.
            """                                                         ,
            )

    version.add_argument(
            "-w"                            ,
            "--written-by"                  ,
            action          = "store_true"  ,
            help            = """
            Display PackMule's authors.
            """                             ,
            )

    return parser.parse_args()


__all__ = [ argparser , ]
