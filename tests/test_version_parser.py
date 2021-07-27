import pytest

from version_helper import Version

@pytest.mark.parametrize(
    argnames=['version_string', 'major', 'minor', 'patch', 'pre_release', 'build'],
    argvalues=[
        ['0.1.2', 0, 1, 2, None, None],
        ['1.2.3', 1, 2, 3, None, None],
        ['1.2.3-alpha', 1, 2, 3, 'alpha', None],
        ['1.2.3-alpha.1', 1, 2, 3, 'alpha.1', None],
        ['1.2.3-beta', 1, 2, 3, 'beta', None],
        ['1.2.3-beta.2', 1, 2, 3, 'beta.2', None],
        ['1.2.3-beta.2.dev', 1, 2, 3, 'beta.2.dev', None],
        ['1.2.3+gf0a9091', 1, 2, 3, None, 'gf0a9091'],
        ['1.2.3+4.gf0a9091', 1, 2, 3, None, '4.gf0a9091'],
        ['1.2.3+4.gf0a9091.dirty', 1, 2, 3, None, '4.gf0a9091.dirty'],
        ['1.2.3-alpha+gf0a9091', 1, 2, 3, 'alpha', 'gf0a9091'],
        ['1.2.3-alpha.1+gf0a9091', 1, 2, 3, 'alpha.1', 'gf0a9091'],
        ['1.2.3-alpha.1.dev+gf0a9091', 1, 2, 3, 'alpha.1.dev', 'gf0a9091'],
        ['1.2.3-alpha+4.gf0a9091', 1, 2, 3, 'alpha', '4.gf0a9091'],
        ['1.2.3-alpha.1+4.gf0a9091', 1, 2, 3, 'alpha.1', '4.gf0a9091'],
        ['1.2.3-alpha.1.dev+4.gf0a9091', 1, 2, 3, 'alpha.1.dev', '4.gf0a9091'],
        ['1.2.3-alpha+4.gf0a9091.dirty', 1, 2, 3, 'alpha', '4.gf0a9091.dirty'],
        ['1.2.3-alpha.1+4.gf0a9091.dirty', 1, 2, 3, 'alpha.1', '4.gf0a9091.dirty'],
        ['1.2.3-alpha.1.dev+4.gf0a9091.dirty', 1, 2, 3, 'alpha.1.dev', '4.gf0a9091.dirty'],

        ['46467a2', None, None, None, None, '46467a2'],
    ],
)
def test_version_parser(version_string, major, minor, patch, pre_release, build):
    """
    {major}.{minor}.{patch}[-{pre-release}][+{build}]
        >> {major}: int, {minor}: int, {patch}: int, {pre-release}: str, {build}: : str

    RegExpr -> ((\d+)\.(\d+)\.(\d+))(\-(([\w\d]+\.?)*))?(\+(([\w\d]+\.?)*))?
    Replace -> ['$&', $2, $3, $4, '$6', '$9'],
    """
    version = Version.parse(version_string)

    assert version.major == major
    assert version.minor == minor
    assert version.patch == patch
    assert version.pre_release == pre_release
    assert version.build == build
