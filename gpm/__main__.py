import sys
import argparse
import os
import shutil


GPM_HOME = os.path.dirname(os.path.realpath(__file__))
PACKAGES = ["GPWebUI", "pyGP", "pyGP-computervision", "pyGP-slam", "pyGP-ros", "luaGP", "juliaGP", "jGP"]


def get_path(file, context=None):
    if context is None:
        path = os.path.join(GPM_HOME, file)
    else:
        path = os.path.join(GPM_HOME, context, file)
    if os.path.exists(path):
        return path
    elif os.path.exists(file):
        return file
    else:
        return None


def parse_args():
    parser = argparse.ArgumentParser(description='Graph Programming Manager')

    parser.add_argument("--install", help="Install a package")
    parser.add_argument("--url", help="Url used for cloning (on install)")
    parser.add_argument("--upgrade", help="Upgrade a package")
    parser.add_argument("--uninstall", help="Completely uninstall a package removing all data")
    parser.add_argument("--list", help="Print a list of all availible packages")

    args = parser.parse_args()

    if args.install is None and args.upgrade is None and args.uninstall is None and args.list is None:
        parser.print_help()
    return args


def get_package_path(package):
    target_path = GPM_HOME
    package_dir = package
    if len(package.split("-")) > 1:
        split = package.split("-")
        target_path = os.path.join(GPM_HOME, split[0], "extlib")
        package_dir = split[1]
    path = os.path.join(target_path, package_dir)
    return path

def install(package, url=None):
    if url is None:
        url = "https://github.com/GraphProgramming/{}.git".format(package)
    path = get_package_path(package)
    if not os.path.exists(path):
        clone = "git clone {} {}".format(url, path)
        os.system(clone)
    else:
        print("Package {} already installed try upgrading.".format(package))

def uninstall(package):
    path = get_package_path(package)
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        print("Package {} not installed.".format(package))

def upgrade(package):
    path = get_package_path(package)
    if os.path.exists(path):
        os.chdir(path)
        os.system("git pull")
    else:
        print("Package {} not installed.".format(package))

def list_packages():
    print("Official Packages:")
    print("------------------")
    print("\n".join(PACKAGES))

def main():
    args = parse_args()
    if args.install is not None:
        install(args.install, url=args.url)
    if args.upgrade is not None:
        upgrade(args.upgrade)
    if args.uninstall is not None:
        uninstall(args.uninstall)
    if args.list is not None:
        list_packages()

if __name__ == "__main__":
    main()
