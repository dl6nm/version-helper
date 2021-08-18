from subprocess import CompletedProcess

from version_helper import Git


def test_construction():
    """Test the Git() constructor"""
    assert Git()


def test_call_process():
    """Test the static method _call_process()"""
    proc = Git._call_process(['git', '--version'])
    assert isinstance(proc, CompletedProcess)
    assert proc.stdout.startswith(b'git version')
    assert proc.stderr == b''


def test_call_process_git_exec_path(git_exec_path_parameters):
    """Test for calling a process from the Git class (git --exec-path)"""
    proc = Git._call_process()
    expexted_process: CompletedProcess = git_exec_path_parameters.get('process')

    assert proc == expexted_process
    assert proc.args == expexted_process.args
    assert proc.returncode == expexted_process.returncode
    assert proc.stdout == expexted_process.stdout
    assert proc.stderr == expexted_process.stderr


def test_git_exec_path(git_exec_path_parameters):
    """Test (mock) if git is installed on the system by calling --exec-path"""
    assert Git.exec_path() == git_exec_path_parameters.get('exec_path')


def test_call_process_git_describe(git_describe_parameters):
    """Test for calling a process from the Git class (git --exec-path)"""
    proc = Git._call_process()
    expexted_process: CompletedProcess = git_describe_parameters.get('process')

    assert proc.args == expexted_process.args
    assert proc.returncode == expexted_process.returncode
    assert proc.stdout == expexted_process.stdout
    assert proc.stderr == expexted_process.stderr


def test_git_describe(git_describe_parameters):
    """Test (mock) if git describe returns the expected values"""
    description = Git.describe(
        dirty=git_describe_parameters.get('args').get('dirty'),
        always=git_describe_parameters.get('args').get('always'),
    )
    assert description == git_describe_parameters.get('expected')
