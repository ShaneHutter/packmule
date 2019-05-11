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

Capitals are in a mutually exclusive group, and required\
Optional lowercase sub switches

* -C,	Create/manage repository
	* -r,	build / delete ( -d ) a local package repository
	* -g,	create / delete (with -d) / upgrade (-u) a package group in local repo
	* -f,	force
	* -a,	add a package to the repository
	* -u,	upgrade a package in a local repository
	* -d,	delete a package (or package group / repo)
* -I,	Info	(local)
	* -d,	package details
	* -g,	package group
	* -l,	list installed
	* -r,	repository information
	* -u,	update local db
* -Q,	Query	(remote)
	* -d,	package details
	* -g,	package group
	* -l,	list installed
	* -r,	repository information
	* -u,	update local db
* -R,	Remove
	* -f,	force
	* -g,	package group
	* -p,	purge
	* -r,	delete local repository (also in -C, your choice mate)
* -S,	Sync
	* -f,	force
	* -g,	package group
	* -r,	reinstall
	* -u,	update local db
* -U,	Update
	* -f,	force
	* -g,	package group
	* -u,	update local db

## Additional Notes:
* I'm not sure if my coding style with Python is fully PEP8; however, I am to conform to the standard, providing that a requirement doesn't bug the crap out of me.
