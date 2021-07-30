import pytest

from version_helper import Git


def test_is_git_available():
    """
    Test if git is available on the system
    """
    pass


def test_git_describe_fatal_error(mock_git_describe_fatal_error):
    """
    Check if git describe returns a fatal error on stderr
    """
    proc = mock_git_describe_fatal_error

    # Git.describe() is expected to raise an error

    assert proc.args == ['git', 'describe']
    assert proc.returncode == 128
    assert proc.stdout.decode().strip() == ''
    assert proc.stderr.decode().strip() == 'fatal: not a git repository (or any of the parent directories): .git'


@pytest.fixture(
    params=[
        '46467a2',
        '0.1.2-alpha.0-3-gf0a9091-dirty',
        '1.2.3-beta.4-3-gf0a9091',
    ]
)
def mock_git_describe():
    pass


@pytest.mark.parametrize(
    argnames=['expected'],
    argvalues=[
        ['46467a2'],
        ['0.1.2-alpha.0-3-gf0a9091-dirty'],
        ['1.2.3-beta.4-3-gf0a9091'],
    ],
)
def test_git_describe(mock_git_describe, expected):
    pass
    # git_describe = Git.describe(dirty=False)
    # assert git_describe == expected
