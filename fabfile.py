from fabric import Connection
from fabric import task


_my_hosts = [
    'dockerpi',
    'minecraftpi',
    'picroft',
    'pihole',
    ]

_pi_user = 'pi'


def valid_host(host_name):
    return host_name in _my_hosts


def sudo(c, command):
    if valid_host(c.host):
        return c.sudo(command)
    else:
        print("\nUNKNOWN HOST '{host}'".format(host=c.host))


@task
def known_hosts(c):
    print(_my_hosts)


@task
def update(c):
    print("\nUpdating '{host}' ...".format(host=c.host))
    sudo(c, 'apt-get update')


@task
def upgrade(c):
    print("\nUpgrading '{host}' ...".format(host=c.host))
    sudo(c, 'apt-get upgrade -y')


@task
def update_and_upgrade(c):
    update(c)
    upgrade(c)


@task
def upgrade_all(c):
    for host in _my_hosts:
        conn = Connection(host=host, user=_pi_user)
        update(conn)
        upgrade(conn)
