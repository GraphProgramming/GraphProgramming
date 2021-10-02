# GraphProgramming
The meta git for graph programming. Contains the installer and the specification.

Easy pip install (requires git installed on systemlevel).
```bash
pip install gpm
```

## Usage

You can install packages like the pyGP package.
```bash
gpm --install pyGP
```

Upgrade packages.
```bash
gpm --upgrade pyGP
```

Remove packages.
```bash
gpm --uninstall pyGP
```

And list all availible official packages.
```bash
gpm --list
```

## Two important packages

### Web IDE

`ide` is a Web-IDE for Graph Programming.
```bash
cd  /path/to/workspace
gpm ide
```

### pyGP

`pyGP` is a kernel to run graphs in python.
```bash
cd  /path/to/workspace
gpm pyGP HelloWorld.graph.json
```

## Install on Ubuntu (or systems with apt-get)

You only need git. Whereas you know github you might already have it installed. If not install it.
```bash
sudo apt-get install git
```

Now install gpm (ideally in a venv)
```bash
(venv)> pip install gpm
```

Now you can use gpm in the commandline.
```bash
(venv)> gpm --help
```

## Install Graph Programming on Windows

### Install Requirements

You need git and python (anaconda in a virtualenv is recommended).
If you happen to have python and git you can skip this step.


#### Install Git

Install git by downloading it from this site and following the install instructions.
https://git-scm.com/

#### Anaconda (Python)

Download Anaconda Python for Python 3.x (preferably 64 bit) from here: https://www.anaconda.com/download/

Follow the install instructions on screen. Hint: Check the box that allows usage of anaconda from the commandline.


#### Create a virtualenv

```bash
conda create -n venv python=3.8
```

### Setting up Graph Programming

First activate your virtual environment created above.

```bash
> activate venv
````

Now clone the repository.
```batch
(venv)> pip install gpm
```

Now you can use gpm in the commandline.
```batch
(venv)> gpm --help
```
