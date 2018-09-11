#
import fabric


_hosts = [
    'dockerpi',
    'minecraftpi',
    'picroft',
    'pihole',
]

_pi_user = "pi"


def update_host(c):
    print("\nUpdating '{host}' ...".format(host=c.host))
    c.sudo('apt-get update')


def upgrade_host(c):
    print("\nUpgrading '{host}' ...".format(host=c.host))
    c.sudo('apt-get upgrade -y')


for h in _hosts:
    conn = fabric.Connection(host=h, user=_pi_user)
    update_host(conn)
    upgrade_host(conn)
