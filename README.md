![Logo of the project](./images/raspberry_pi.png)

# piman
> Manage multiple raspberry pis

I have several Raspberry Pis around the office, doing various things (Pihole, Picroft, etc.).
Trying to keep them updated was tedious until I threw together a simple Fabric script that
allows me to manage them all from a single set of commands.

## Installing

1.  Clone this repo
2.  Change to the repo directory
3.  Install dependencies via `pip`
4.  Create and edit a file `config.json` with the names of your Pi's:

Or start here ...

```shell
git clone https://github.com/ScottJWalter/piman.git
cd piman.git
pip install -r requirements.txt
nano config.json
```

... paste the following into your editor window for `config.json` ...

```json
{
    'hosts': [
        'raspberrypi',
        'mypi'
        ...
    ]
}
```

... and you're ready to go.

```shell
commands here
```

Here you should say what actually happens when you execute the code above.

## Developing

### Built With

* Fabric

## Configuration

The only configuration required is the creation of a `config.json` file in the project
root directory.  The file lists all known hosts, and is structured as follows:

```shell
{
    'hosts': [
        'raspberrypi',
        'mypi'
        ...
    ]
}
```

## Licensing

State what the license is and how to find the text version of the license.
