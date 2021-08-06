import pytest

from subprocess import CompletedProcess

from version_helper import Git


def test_construction():
    """Test the Git() constructor"""
    assert Git()


def test_call_process(mock_subprocess, subprocess_parameters):
    """Test for calling a process from the Git class"""
    proc = Git._call_process()
    expexted_process: CompletedProcess = subprocess_parameters.get('process')

    assert proc.args == expexted_process.args
    assert proc.returncode == expexted_process.returncode
    assert proc.stdout == expexted_process.stdout
    assert proc.stderr == expexted_process.stderr


def test_git_exec_path(mock_subprocess, subprocess_parameters):
    """Test (mock) if git is installed on the system by calling --exec-path"""
    assert Git.exec_path() == subprocess_parameters.get('exec_path')


@pytest.mark.skip(reason='Not implemented yet')
@pytest.mark.parametrize(
    argnames=[],
    argvalues=[],
    ids=[],
)
def test_git_describe_fatal_error(git_describe_fatal_error):
    """Check if git describe returns a fatal error on stderr"""
    proc = git_describe_fatal_error

    # Git.describe() is expected to raise an error

    assert proc.args == ['git', 'describe']
    assert proc.returncode == 128
    assert proc.stdout.decode().strip() == ''
    assert proc.stderr.decode().strip() == 'fatal: not a git repository (or any of the parent directories): .git'


@pytest.mark.skip(reason='Not implemented yet')
@pytest.fixture(
    params=[
        '46467a2',
        '0.1.2-alpha.0-3-gf0a9091-dirty',
        '1.2.3-beta.4-3-gf0a9091',
    ]
)
def mock_git_describe():
    assert False


@pytest.mark.skip(reason='Not implemented yet')
@pytest.mark.parametrize(
    argnames=['expected'],
    argvalues=[
        ['46467a2'],
        ['0.1.2-alpha.0-3-gf0a9091-dirty'],
        ['1.2.3-beta.4-3-gf0a9091'],
    ],
)
def test_git_describe(mock_git_describe, expected):
    assert False
    # git_describe = Git.describe(dirty=False)
    # assert git_describe == expected
