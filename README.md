![Fabric](./images/fabric.png)  ![](./images/plus.png) ![Raspberry Pi](./images/raspi.png)

# piman
> Manage multiple raspberry pis with Python and a little help from Fabric

I have several Raspberry Pis around the office, doing various things (Pihole, Picroft, etc.).
Trying to keep them updated was tedious until I threw together a simple [Fabric][10] script that
allows me to manage them all from a single set of commands.

## Installing

**NOTE:**  Installation is assumed to be on the box from which you want to manage your Pis.  
_This is **not** installed on the Pis themselves._

1.  Clone this repo
2.  Change to the repo directory
3.  Install dependencies via `pip`
4.  Create and edit a file `config.json` with the names of your Pi's:

Or start here ...

```shell
git clone https://github.com/ScottJWalter/piman.git
cd piman
pip install -r requirements.txt
nano config.json
```

... paste the following into your editor window for `config.json` ...

```shell
{
    'hosts': [
        'raspberrypi',
        'mypi'
        ...
    ]
}
```

... and you're ready to go.

## Usage

To get a list of available commands:

```shell
cd piman
fab --list
```

### Per-host commands:

Per-host commands require a host name passed in:

```shell
cd piman
fab <command> <-H|--host> <hostname>
```

Host names can be either the qualified name or the IP address.

Available commands:

* `ping` &mdash; Pings the host
* `reboot` &mdash; Reboots the specified host
* `update` &mdash; Runs `sudo apt-get update` on the specified host
* `update-and-upgrade` &mdash; Both `update`s and `upgrade`s the specified host
* `upgrade` &mdash; Runs `sudo apt-get upgrade --yes` on the specified host

### All-host commands:

All-host commands take no parameters and apply the same tasks to all known hosts:

```shell
cd piman
fab <command>
```

Available commands:

* `list-hosts` &mdash; Returns a list of known hosts
* `update-all` &mdash; Runs `sudo apt-get update --yes` on all hosts
* `upgrade-all` &mdash; Runs `sudo apt-get upgrade --yes` onall hosts

## Licensing

This software is released under the [MIT License](LICENSE.md).


[10]: http://www.fabfile.org/
