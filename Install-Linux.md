# Install Graph Programming on Linux

## Ubuntu (or systems with apt-get)

You only need git. Whereas you know github you might already have it installed. If not install it.
```bash
sudo apt-get install git
```

Now clone the repository.
```bash
cd /path/to/where/you/want/gp/installed
git clone https://github.com/GraphProgramming/GraphProgramming.git
```

Now you can use gpm in the commandline.
```bash
./gpm
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
./gpm install GPWebUI
```

Furthermore an execution environment is usefull. For starters pyGP is recommended, but if you need special features of lua, java, javascript or c++ choose luaGP, jGP, jsGP or cppGP.
```bash
./gpm install pyGP
```

This will install an execution kernel for graph programs. However, on most systems this kernel will not run yet, because of missing dependencies. To install them run the install-deps script with admin permissions.
```bash
sudo gpm install-deps GPWebUI
sudo gpm install-deps pyGP
```

Now everything is installed. Try it.
```bash
cd GPWebUI
./editor.sh
```

Continue to the first steps guide.

# Non apt-get Systems
You only need git. Whereas you know github you might already have it installed. If not install it.
```bash
# install git
```

Now clone the repository.
```bash
cd /path/to/where/you/want/gp/installed
git clone https://github.com/GraphProgramming/GraphProgramming.git
```

Now you can use gpm in the commandline.
```bash
./gpm
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
./gpm install GPWebUI
```

Furthermore an execution environment is usefull. For starters pyGP is recommended, but if you need special features of lua, java, javascript or c++ choose luaGP, jGP, jsGP or cppGP.
```bash
./gpm install pyGP
```

This will install an execution kernel for graph programs.
However, on most systems this kernel will not run yet, because of missing dependencies.
Now it get's tricky. Because the dependencies may change over time there is not listed what you need here.
But you can read the install-deps.sh inside of the package folder and transate it to your system.

For example read and translate the GPWebUI/install-deps.sh and the pyGP/install-deps.sh.

When everything is installed. It should work.
```bash
cd GPWebUI
./editor.sh
```

Continue to the first steps guide.
