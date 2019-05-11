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

# Declare variables and constants
PRIMARY_SWITCHES    = {
        "build"     : {
            "title"         : "Build"                                   , 
            "description"   : """
            Build an RPM package.
            """                                                         ,
            }
        "create"    : {
            "title"         : "Create"                                  ,
            "description"   : """
            Create and manage a locally (remotely?) built package
            repository
            """                                                         ,
            }
        "database"    : {
            "title"         : "Database"                                ,
            "description"   : """
            Clean and maintain the local databases
            """                                                         ,
            }
        "info"      : {
            "title"         : "Information"                             ,
            "description"   : """
            Display package, package group, and repository information 
            from packages, package groups, and repositories installed 
            or setup locally on the system
            """                                                         ,
            }           ,
        "query"     : {
            "title"         : "Query"                                   ,
            "description"   : """
            Query package, package group, and repository information
            from a remote package repository
            """                                                         ,
            }           ,
        "remove"    : {
            "title"         : "Remove"                                  ,
            "description"   : """
            Remove packages and package groups from the local system.
            Delete locally created package repositories off of the
            system.
            """                                                         ,
            }           ,
        "sync"      : {
            "title"         : "Sync"                                    ,
            "description"   : """
            Syncronize and packages from a repository
            """                                                         ,
            }           ,
        "update"    : {
            "title"         : "Update"                                  ,
            "description"   : """
            Update and upgrade local repository database and packages
            from remote repositories.
            """                                                         ,
            }           ,
        "version"    : {
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
    primary_swicthes    = (
            parser.add_argument_group( required = True )
            )
    '''
        Can I add argument groups connected to each primary switch?
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
        Will I run into conflicts with similair switches?
        Does creating groups avoid this?
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
            '''
                Make sure that this being required will not also make
                -B a required argument!
            '''
            help        = """
            Root directory of files to be packaged.  This is required.
            """                                                         ,
            )

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
            witch each primary switch.
            """                                                         ,
            )

    create.add_argument(
            "-g"                                                        ,
            "--pkg-group"                                               ,
             # List packages to operate upon
            action      = "+"                                           , 
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
            witch each primary switch.
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
            witch each primary switch.
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
            "-S"  ,
            "--sync"  ,
            nargs   = "+"  ,
            help    = """
            Synchronize packages from a repository
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
            "-f"                                                        ,
            "--force"                                                   ,
            action  = "store_true"                                      ,
            help    = """
            Force an operation.  I'm not 100% on what this will entail
            witch each primary switch.
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
            "-f"                                                        ,
            "--force"                                                   ,
            action  = "store_true"                                      ,
            help    = """
            Force an operation.  I'm not 100% on what this will entail
            witch each primary switch.
            """                                                         ,
            )

    update.add_argument(
            ""  ,
            ""  ,
            action  = "store_true"  ,
            help    = """
            """                     ,
            )

    update.add_argument(
            ""  ,
            ""  ,
            action  = "store_true"  ,
            help    = """
            """                     ,
            )

    update.add_argument(
            ""  ,
            ""  ,
            action  = "store_true"  ,
            help    = """
            """                     ,
            )

    # Version
    version.add_argument(
            ""  ,
            ""  ,
            action  = "store_true"  ,
            help    = """
            """                     ,
            )

    version.add_argument(
            ""  ,
            ""  ,
            action  = "store_true"  ,
            help    = """
            """                     ,
            )

    return parser.parse_args()
