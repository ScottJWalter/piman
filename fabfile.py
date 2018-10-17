#!/usr/bin/env python
from fabric import Connection
from fabric import task
import subprocess
from capturer import CaptureOutput

PI_USER = 'pi'
CONFIG_FILE = 'config.json'
MY_HOSTS = []

try:
    with open(CONFIG_FILE) as f:
        # for some reason, trying to JSON.loads() throws an error, so we eval() it instead.
        # Not really good, but ...
        MY_HOSTS = eval(f.read())['hosts']
except ValueError:
    print('Unable to load hosts file')


def valid_host(host_name):
    return host_name in MY_HOSTS


def sudo_wrapper(c, command):
    if valid_host(c.host):
        return c.sudo(command, warn=True)
    else:
        print("\nUNKNOWN HOST '{host}'".format(host=c.host))


@task
def list_hosts(c):
    print(MY_HOSTS)


@task
def ping(c):
    _status = ['UP', 'UNREACHABLE']

    with CaptureOutput(relay=False):
        if subprocess.call(["ping", "-q", "-c", "1", c.host]) == 0:
            return_value = 0
        else:
            return_value = 1

    print("{host} is {status}".format(host=c.host, status=_status[return_value]))

    return return_value


@task
def reboot(c):
    if valid_host(c.host):
        print("\nRebooting '{host}' ...".format(host=c.host))
        sudo_wrapper(c, 'reboot -h now')
    else:
        print("\nUnknown host '{host}'".format(host=c.host))


@task
def update(c):
    if valid_host(c.host):
        print("\nUpdating '{host}' ...".format(host=c.host))
        sudo_wrapper(c, 'apt-get update')
        print("\nUpdating '{host}' ... DONE!".format(host=c.host))
    else:
        print("\nUnknown host '{host}'".format(host=c.host))


@task
def upgrade(c):
    if valid_host(c.host):
        print("\nUpgrading '{host}' ...".format(host=c.host))
        sudo_wrapper(c, 'apt-get upgrade -y')
        print("\nUpgrading '{host}' ... DONE!".format(host=c.host))
    else:
        print("\nUnknown host '{host}'".format(host=c.host))


@task
def update_and_upgrade(c):
    if valid_host(c.host):
        update(c)
        upgrade(c)
    else:
        print("\nUnknown host '{host}'".format(host=c.host))


@task(hosts=MY_HOSTS)
def update_all(c):
    with Connection(host=c.host, user=PI_USER) as conn:
        update(conn)


@task(hosts=MY_HOSTS)
def upgrade_all(c):
    with Connection(host=c.host, user=PI_USER) as conn:
        update(conn)
        upgrade(conn)
