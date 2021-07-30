import subprocess


class Git:
    pass


def get_version():
    """ Get the current application version from git describe """
    return subprocess.check_output(['git', 'describe']).strip().decode('utf-8')


__version__ = get_version()
