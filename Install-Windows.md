# Install Graph Programming on Windows

## Install Requirements

You need git and python (anaconda in a virtualenv is recommended).
If you happen to have python and git you can skip this step.


### Install Git

Install git by downloading it from this site and following the install instructions.
https://git-scm.com/

### Anaconda (Python)

Download Anaconda Python for Python 3.x (preferably 64 bit) from here: https://www.anaconda.com/download/

Follow the install instructions on screen. Hint: Check the box that allows usage of anaconda from the commandline.


### Create a virtualenv

TODO

## Setting up Graph Programming

First activate your virtual environment created above.

```bash
> activate venv
````

Now clone the repository.
```batch
(venv)> cd C:\path\to\where\you\want\gp\installed
(venv)> git clone https://github.com/GraphProgramming/GraphProgramming.git
```

Now you can use gpm in the commandline.
```batch
(venv)> cd GraphProgramming
(venv)> gpm.bat
```

You should see some output similar to:
```bash
Usage: gpm COMMAND

Availible COMMANDs:
  install PKG     # install a package
  install-deps PKG # install the dependencies of a package
  update          # update gpm
  upgrade         # update all installed packages
  upgradepkg PKG  # update only the package provided
  status          # show the status of all packages
[...]
```

This means that gpm (GraphProgramming Package Manager) works. To get you a minimal working setup you need to install some modules (packages).

First an IDE would be usefull. Install the GPWebUI package.
```bash
(venv)> gpm.bat install GPWebUI
```

Furthermore an execution environment is usefull. For starters pyGP is recommended, but if you need special features of lua, java, javascript or c++ choose luaGP, jGP, jsGP or cppGP.
```bash
(venv)> gpm.bat install pyGP
```

This will install an execution kernel for graph programs. However, on most systems this kernel will not run yet, because of missing dependencies. To install them run the install-deps script with admin permissions.
```bash
(venv)> gpm.bat install-deps GPWebUI
(venv)> gpm.bat install-deps pyGP
```

Now everything is installed. Try it.
```bash
cd GPWebUI
./editor.bat
```

Continue to the first steps guide.
