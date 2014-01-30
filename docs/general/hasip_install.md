# Overview

- Operating System
    - General (Raspberry Pi)
    - Packages
    - Python
    - Application User
- Hasip
    - General
    - Configuration
    - Startup scripts
    - Module Configuration


**Note:** All Commands you have to execute have a ***prefix*** in front of the command. Depending of that you have to execute the command as ***root*** or as ***application user***.

The **#** (hash sign) indicates that you should run this command as **root**, e.g.:

    # id
    uid=0(root) gid=0(root) ...

The **$** (dollar sign) indicates that you should run this command as **application user**, e.g.:

    $ id
    uid=1001(hasip) gid=1004(hasip) ...

# Operating System

## General

Hasip was developed to run on nearly any linux based distribution. This installation guide shows you how to install it on a Debian and it's derivates (e.g. Ubuntu, Raspbian).

**Note:** If you are planing to use FS20 with the [CUL](docs/modules/module_cul.md) module please refer to the module module documentation itself for further informations.


## Packages

Install the required packages by executing the following command:

    # apt-get install git git-core


## Python

### Distribution packages (preferred method)

Here you will use the python packages provided by your distribution. This packages are well tested. Install the required packages with the following command:

    # apt-get install python python-pip

### Python version manager

You can also use a Python version manager to install an up to date version of python

E.g.:

* [PyEnv](https://github.com/yyuu/pyenv).


## Application User

Hasip will be installed as a non privileged user. Add the user by exectuting the following command.

    # adduser --disabled-login --gecos 'Hasip Application User' hasip

# Hasip
## General

Cloning the source:

    $ cd /home/hasip
    $ git clone git@github.com:thehasip/hasip.git -b stable_1.0 hasip
    $ chmod +x hasip/hasip/hasip.py

**Note:** You can change ``stable_1.0`` to ``master`` if you want the bleeding edge version, but it's not recommended to run this on a production system.

Installing python dependency:

    # cd /home/hasip/hasip/
    # pip install -r requirements.txt

## Configuration

Copy the example configuration and adapt it for your needs:

    $ cd /home/hasip
    $ cp config/hasip.config.example config/hasip.config

## Startup Scripts

    # cp /home/hasip/hasip/support/init.d/hasip /etc/init.d/hasip
    # chmod +x /etc/init.d/hasip
    # update-rc.d hasip defaults

## Module Configuration

Now you should have a running installation of hasip. To get started please refer to the [module documentaion](docs/modules/README_modules.md) where you can find more informations how to configure the system for your needs.
