# PackMule
A Python3 package manager for RHEL variaties

## Concepts
* Entirely Python3 dependant
* Similar features to Yum, and compatibilty
	* Import settings from yum configurations
		* A drop-in replacement for yum using Python3
	* Read yum.repos.d
* Use switching closer to pacman
	* You don't always need to sync repos
* Requires modern SystemD (i.e. systemctl)
	* Add a configurable auto-update service
		* packages
		* just db
		* alerts and confirmation ( all or package specific )
		* exclude packages
* Ensure compatibility with Cloudlinux alt-python
* Architectures
	* x86_64
	* ARM
	* no i386
* Repos
	* Maintian yum compatibility
	* Similar if not identical repository system
		* Unique metadata?
			* repo.pmmd (PackMule Meta-Data)
	* Repository generating tools
* Queue multiple operations in one command
	* ``packmule -S vim -Rf nano``


## Dependancies
* Packages
	* python >= 3.6 (preferably 3.7 to be honest)
	* systemd >= 62 (RHEL core)
	* curl	(RHEL core)
	* sqlite3 (RHEL core)
	* gpgme (RHEL core)
	* openssl (RHEL core)
* Distro
	* CentOS >= 7.6
	* RHEL >= 7.6
	* Fedora >= 30

## File structure
* Bin
	* ``/usr/bin``
* Cache
	* ``/var/cache/packmule``
* Config
	* Main
		* ``/etc/packmule/packmule.conf``
	* Repos
		* ``/etc/packmule/repos.d/``
		* ``/etc/yum.repos.d/``
* DBs
	* ``/var/lib/packmule/db``
* Logs
	* ``/var/log/packmule``
* Man pages
	* ``/usr/share/man/man1``
* Python
	* site-packages location (obviously)
* Service files
	* ``/usr/lib/systemd/system``	


## Arguments and switching

Capitals are the primary switches and at least one is required.\
Primary switches can be combined (possible?), which will cause\
tasks to queue up, and be performed in.\
the most ideal order.\
Optional lowercase sub switches

* -B,	Build an rpm package
	* -r,	package root to build from (required)
* -C,	Create/manage repository
	* -a,	add a package to the repository
	* -d,	delete a package (or package group / repo)
	* -f,	force
	* -g,	create / delete (with -d) / upgrade (-u) a package group in local repo
	* -r,	build / delete ( -d ) a local package repository
	* -u,	upgrade a package in a local repository
* -D,	Databases
	* -c,	clean local database metadata
	* -e,	empty PackMule cache
	* -f,	force
* -I,	Info	(local)
	* -d,	package details
	* -g,	package group
	* -l,	list installed.  This can be used with package group (-g) and repo (-r)
	* -r,	repository information
	* -u,	update local db
* -Q,	Query	(remote)
	* -d,	package details
	* -g,	package group
	* -l,	list installed. This can be used with package group (-g) and repo (-r)
	* -r,	repository information
	* -u,	update local db
* -R,	Remove
	* -c,	clean cache
	* -f,	force
	* -g,	package group
	* -l,	remove lockfile, if last run exited poorly.  This will kill any running packmule process!
	* -p,	purge
	* -r,	delete local repository (also in -C, your choice mate)
* -S,	Sync
	* -d,	downgrade package to previos version
	* -f,	force
	* -g,	package group
	* -l,	specify a local repositories path
	* -r,	reinstall
	* -t,	target a repository that is not added to repos.d.  The repository\
		will be added to a partial repos.d, which specifies the select packages\
		installed, allowing for the package to be included in updates.  Only\
		information on the select packages will be updated for the repos\
		database
	* -u,	update local db
* -U,	Update
	* -f,	force
	* -g,	package group
	* -r,	reinstall all installed packages (emerge -DuNe much?)
	* -u,	update local db
* -V,	Version (Display packmule version, and other program information)
	* with no arguments (Version information)
	* -a,	author details
	* -d,	description
	* ect...

## Additional Notes:
* I'm not sure if my coding style with Python is fully PEP8; however, I am to conform to the standard, providing that a requirement doesn't bug the crap out of me.
