import pytest

from pathlib import Path
from subprocess import CompletedProcess

from version_helper import Git


def test_construction():
    """Test the Git() constructor"""
    assert Git()


@pytest.mark.parametrize(
    argnames=['mock_subprocess', 'expected'],
    argvalues=[
        [
            CompletedProcess(
                args=['git', '--exec-path'],
                returncode=0,
                stdout=r'C:\Program Files\Git',
                stderr='',
            ),
            Path(r'C:\Program Files\Git'),
        ],
        [
            CompletedProcess(
                args=['git', '--exec-path'],
                returncode=0,
                stdout=br'C:\Program Files\Git',
                stderr=br'',
            ),
            Path(r'C:\Program Files\Git'),
        ],
        [
            CompletedProcess(
                args=['git', '--exec-path'],
                returncode=0,
                stdout=b'/usr/bin/git',
                stderr=b'',
            ),
            Path('/usr/bin/git'),
        ],
        [
            CompletedProcess(
                args=['git', '--exec-path'],
                returncode=127,
                stdout=b'',
                stderr=b'Der Befehl "git" ist entweder falsch geschrieben oder\nkonnte nicht gefunden werden.\n',
            ),
            None,
        ],
    ],
    indirect=['mock_subprocess'],
    ids=['installed on win [str]', 'installed on win [bytes]', 'installed on linux', 'not installed']
)
def test_is_git_installed(mock_subprocess, expected):
    """Test (mock) if git is installed on the system"""
    assert Git.exec_path() == expected


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
