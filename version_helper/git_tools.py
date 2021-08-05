import subprocess


class Git:

    @staticmethod
    def _call_process(*args, **kwargs) -> subprocess.CompletedProcess:
        print('_call_process')
        return subprocess.run(*args, **kwargs, capture_output=True)

    @staticmethod
    def exec_path() -> str:
        """Get the installation path of git or None if not found"""
        args = ['git', '--exec-path']
        proc = Git._call_process(args)
        return proc.stdout.strip().decode('utf-8')

    @staticmethod
    def get_version():
        """ Get the current application version from git describe """
        return subprocess.check_output(['git', 'describe']).strip().decode('utf-8')
