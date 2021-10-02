from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '2.0.0'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='gpm',
    version=__version__,
    description='A manager package for graph programming.',
    long_description=long_description,
    url='https://github.com/GraphProgramming/GraphProgramming',
    download_url='https://github.com/GraphProgramming/GraphProgramming/tarball/' + __version__,
    license='MIT',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python',
    ],
    keywords='',
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    author='Michael Fuerst',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='mail@michaelfuerst.de',
    entry_points={
        'console_scripts': [
            'gpm = gpm.__main__:main',
        ]
    },
    extras_require={
        'dev': ['nose2', 'packaging'],
    },
)
