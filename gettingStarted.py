from __future__ import print_function
import subprocess
import sys
import os


SETUP_DIR = '.'
MAKE_ENV = 'python3 -m venv env'
JOIN_ENV = 'source env/bin/activate'
UPDATE = 'pip install --upgrade pip'
SETUP = 'pip install -e {}'.format(SETUP_DIR)
# RECURSE = 'find $PWD -type f -name setup.py -exec sh -c "echo PATH:; dirname \"{}\"; echo pip install -e $(dirname \"{}\"); echo;" \;'
RECURSE = 'find $PWD -type f -name setup.py | xargs -I \"{}\" dirname \"{}\" | xargs -I \"{}\" pip install -e \"{}\"'

COMMAND = '; '.join([MAKE_ENV, JOIN_ENV, UPDATE, RECURSE])

def process(command, shell=False):
    # Run command
    make_env = subprocess.Popen(
        command,
        shell=shell,
        stderr=subprocess.PIPE
    )

    # Capture command output
    _stdout, _stderr = make_env.communicate()

    # Check for error running command
    if _stderr != '':
        print ('ERROR: ', _stderr)
        sys.exit(1)

def main():
    process(COMMAND, shell=True)


if __name__ == '__main__':
    main()