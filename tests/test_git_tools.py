import pytest

from version_helper import Git


@pytest.fixture(
    params=[
        '46467a2',
        '0.1.2-alpha.0-3-gf0a9091-dirty',
        '1.2.3-beta.4-3-gf0a9091',
    ]
)
def mock_git_describe():
    return


def test_is_git_available():
    """
    Test if git is available on the system
    """
    pass


def test_is_git_repository():
    """
    Check for existence of a .git directory in your projects root
    """
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
    git_describe = Git.describe(dirty=False)
    assert git_describe == expected
