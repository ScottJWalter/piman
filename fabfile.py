from fabric import task


my_hosts = [
    'dockerpi',
    'minecraftpi',
    'picroft',
    'pihole',
    ]


def valid_host(host_name):
    return host_name in my_hosts


def sudo(c, command):
    if valid_host(c.host):
        return c.sudo(command)
    else:
        print("\nUNKNOWN HOST '{host}'".format(host=c.host))


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
