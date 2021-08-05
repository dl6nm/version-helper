import pytest

from version_helper import Git


def test_construction():
    assert Git()


@pytest.mark.parametrize(
    argnames=['mock_git_call_process', 'expected'],
    argvalues=[
        [
            {
                'args': ['git', '--exec-path'],
                'returncode': 0,
                'stdout': b'C:/Git/asdf',
                'stderr': b'',
            },
            'C:/Git/asdf',
        ],
        [
            {
                'args': ['git', '--exec-path'],
                'returncode': 127,
                'stdout': b'',
                'stderr': b'Der Befehl "git" ist entweder falsch geschrieben oder\nkonnte nicht gefunden werden.',
            },
            None,
        ],
    ],
    indirect=['mock_git_call_process'],
    ids=['installed', 'not installed']
)
def test_is_git_installed(monkeypatch, mock_git_call_process, expected):
    """Test (mock) if git is installed on the system"""
    assert Git.exec_path() == expected


@pytest.mark.skip(reason='Not implemented yet')
def test_git_describe_fatal_error(git_describe_fatal_error):
    """
    Check if git describe returns a fatal error on stderr
    """
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
