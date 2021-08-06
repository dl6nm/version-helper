import subprocess

from pathlib import Path


class Git:
    """Adding some base git functionality, if available on your system,
    to get a version string from git describe to use in version_helper later on.
    """

    @staticmethod
    def _call_process(*args, **kwargs) -> subprocess.CompletedProcess:
        return subprocess.run(*args, **kwargs, capture_output=True)

    @classmethod
    def exec_path(cls) -> Path:
        """Get the installation path of git or None if it was not found

        :return: Path object to the git executable or None
        """
        args = ['git', '--exec-path']
        proc = cls._call_process(args)
        if proc.returncode == 0:
            path_str = proc.stdout.strip()
            if type(path_str) is bytes:
                path_str = path_str.decode('utf-8')
            return Path(path_str)

    @classmethod
    def describe(cls) -> str or None:
        if cls.exec_path() is None:
            return None
        args = ['git', 'describe']
        proc = cls._call_process(args)
        if proc.returncode == 0:
            path_str = proc.stdout.strip()
            if type(path_str) is bytes:
                path_str = path_str.decode('utf-8')
            return path_str

    @staticmethod
    def get_version():
        """ Get the current application version from git describe """
        return subprocess.check_output(['git', 'describe']).strip().decode('utf-8')
