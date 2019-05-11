# Packmule
A Python3 package manager for RHEL variaties

## Concepts
* Entirely Python3 dependant
* Similar features to Yum
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
* Import settings from yum configurations


## Dependancies
* python >= 3.6 (preferably 3.7 to be honest)
* systemd >= 62 (RHEL core)
* curl	(RHEL core)
* sqlite3 (RHEL core)
* Distro
	* CentOS >= 7.6
	* RHEL >= 7.6
	* Fedora >= 30

## File structure
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

* Service files
	* ``/usr/lib/systemd/system``	
