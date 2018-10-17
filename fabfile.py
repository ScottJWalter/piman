from fabric import Connection
from fabric import task

import subprocess
from capturer import CaptureOutput

_my_hosts = [
    'dockerpi',
    'minecraftpi',
    'picroft',
    'pihole',
    'gateway'
    ]

_pi_user = 'pi'


def valid_host(host_name):
    return host_name in _my_hosts


def sudo_wrapper(c, command):
    if valid_host(c.host):
        return c.sudo(command, warn=True)
    else:
        print("\nUNKNOWN HOST '{host}'".format(host=c.host))


@task
def list_hosts(c):
    print(_my_hosts)


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
    else:
        print("\nUnknown host '{host}'".format(host=c.host))


@task
def upgrade(c):
    if valid_host(c.host):
        print("\nUpgrading '{host}' ...".format(host=c.host))
        sudo_wrapper(c, 'apt-get upgrade -y')
    else:
        print("\nUnknown host '{host}'".format(host=c.host))


@task
def update_and_upgrade(c):
    if valid_host(c.host):
        update(c)
        upgrade(c)
    else:
        print("\nUnknown host '{host}'".format(host=c.host))


@task(hosts=_my_hosts)
def update_all(c):
    with Connection(host=c.host, user=_pi_user) as conn:
        update(conn)


@task(hosts=_my_hosts)
def upgrade_all(c):
    with Connection(host=c.host, user=_pi_user) as conn:
        update(conn)
        upgrade(conn)
