# Packmule
A Python3 package manager for RHEL variaties

## Concepts
* Entirely Python3 dependant
* Similar features to Yum
	* Read yum.repos.d
* Use switching closer to pacman
	* You don't always need to sync repos

# Dependancies
* python >= 3.6 (preferably 3.7 to be honest)
* curl

# File structure
* Cache
	* ``/var/cache/packmule``
* Config
	* Main
		* ``/etc/packmule/packmule.conf``
	* Repos
		* ``/etc/packmule/repos.d/``
		* ``/etc/yum.repos.d/``
