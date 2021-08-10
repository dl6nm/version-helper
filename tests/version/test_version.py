import pytest

from version_helper import Version


def test_construction():
    """Test the Version() constructor"""
    assert Version(1, 2, 3)
    assert Version(1, 2, 3, 'beta', 'a1b2c3d4')
    assert Version(1, 2, 3, None, 'build-246')


@pytest.mark.parametrize(
    argnames=['version', 'expected'],
    argvalues=[
        [Version(1, 2, 3), '1.2.3'],
        [Version(1, 2, 3, 'alpha.1'), '1.2.3-alpha.1'],
        [Version(1, 2, 3, None, None), '1.2.3'],
        [Version(1, 2, 3, 'beta', 'a1b2c3d4'), '1.2.3-beta+a1b2c3d4'],
        [Version(1, 2, 3, None, 'build-246'), '1.2.3+build-246'],
    ],
)
def test_dunder_methods(version, expected):
    """Test the Version() dunder methods __str__ and __repr__"""
    assert version.__str__() == expected
    assert version.__repr__() == expected


@pytest.mark.parametrize(
    argnames=['version_string', 'major', 'minor', 'patch', 'prerelease', 'build'],
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
    ],
)
def test_version_parser(version_string, major, minor, patch, prerelease, build):
    """Version parser test

    The version string looks like the following schema:
    {major: int}.{minor: int}.{patch: int}[-{prerelease: str}][+{build: str}]
    """
    version = Version.parse(version_string)
    assert version.major == major
    assert version.minor == minor
    assert version.patch == patch
    assert version.prerelease == prerelease
    assert version.build == build


@pytest.mark.parametrize(
    argnames='version_string',
    argvalues=[
        '46467a2',
        '1.2-beta.1',
        '1.2.3.1',
        '1.2.3.4.5',
        '1.2.3.4-alpha.1',
        '1.2.3.beta.1',
        'this.is.a.new.version',
        'my-version',
    ],
)
def test_version_parser_value_error(version_string):
    """Raise error when parsing an invalid version string

    GIVEN some invalid version strings
    WHEN the string is parsed into a semantic version
    THEN a ValueError will be raised
    """
    with pytest.raises(ValueError, match='`version_string` is not valid to Semantic Versioning Specification'):
        Version.parse(version_string)


@pytest.mark.parametrize(
    argnames=['major', 'minor', 'patch', 'prerelease', 'build', 'core'],
    argvalues=[
        [0, 1, 2, None, None, '0.1.2'],
        [1, 2, 3, None, None, '1.2.3'],
        [1, 2, 3, 'beta.4', None, '1.2.3'],
        [1, 2, 3, None, 'build.321', '1.2.3'],
        [1, 2, 3, 'beta.4', 'build.321', '1.2.3'],
    ],
)
def test_version_core(major, minor, patch, prerelease, build, core):
    """Test the core property output of a Version object"""
    version = Version(major=major, minor=minor, patch=patch, prerelease=prerelease, build=build)
    assert version.core == core


@pytest.mark.parametrize(
    argnames=[
        'version_string', 'is_from_git_describe', 'expected_semver',
        'expected_version'
    ],
    argvalues=[
        [
            '0.1.2-alpha.0-3-gf0a9091-dirty', True, '0.1.2-alpha.0+3-gf0a9091-dirty',
            Version(major=0, minor=1, patch=2, prerelease='alpha.0', build='3-gf0a9091-dirty')
        ],
        [
            '1.2.3-beta.4-3-gf0a9091', True, '1.2.3-beta.4+3-gf0a9091',
            Version(major=1, minor=2, patch=3, prerelease='beta.4', build='3-gf0a9091')
        ],
        [
            '1.2.3-3-gf0a9091', True, '1.2.3+3-gf0a9091',
            Version(major=1, minor=2, patch=3, prerelease=None, build='3-gf0a9091')
        ],
        [
            '0.1.2-alpha.0+3-gf0a9091-dirty', False, '0.1.2-alpha.0+3-gf0a9091-dirty',
            Version(major=0, minor=1, patch=2, prerelease='alpha.0', build='3-gf0a9091-dirty')
        ],
    ],
)
def test_version_from_git(version_string, is_from_git_describe, expected_semver, expected_version):
    """Test the version parser with parameter is_from_git_describe set to True or False"""
    version = Version.parse(string=version_string, is_from_git_describe=is_from_git_describe)

    assert str(version) == expected_semver
    assert version.full == expected_semver

    assert version.major == expected_version.major
    assert version.minor == expected_version.minor
    assert version.patch == expected_version.patch
    assert version.prerelease == expected_version.prerelease
    assert version.build == expected_version.build


@pytest.mark.parametrize(
    argnames=['major', 'minor', 'patch', 'prerelease', 'build', 'expected_semver', 'expected_version'],
    argvalues=[
        [0, 1, 2, None, None, '0.1.2', Version(0, 1, 2)],
        [0, 1, 2, 'beta-1', None, '0.1.2-beta-1', Version(0, 1, 2, prerelease='beta-1')],
        [0, 1, 2, None, 'b4711', '0.1.2+b4711', Version(0, 1, 2, build='b4711')],
        [0, 1, 2, 'alpha.1', '123', '0.1.2-alpha.1+123', Version(0, 1, 2, 'alpha.1', '123')],
    ],
)
def test_version_set(major, minor, patch, prerelease, build, expected_semver, expected_version):
    """Test for setting new values to a `Version` object"""
    version = Version(major=major, minor=minor, patch=patch)
    version.set(major=major, minor=minor, patch=patch, prerelease=prerelease, build=build)

    assert str(version) == expected_semver
    assert version.full == expected_semver

    assert version.major == expected_version.major
    assert version.minor == expected_version.minor
    assert version.patch == expected_version.patch
    assert version.prerelease == expected_version.prerelease
    assert version.build == expected_version.build


def test_get_version_from_git_describe(git_describe_parameters):
    """Test for getting a `Version` object from collecting/parsing the git describe output"""
    args = git_describe_parameters.get('args')
    expected_version: Version = git_describe_parameters.get('expected_version')

    if expected_version is None:
        with pytest.raises(ValueError, match='`version_string` is not valid to Semantic Versioning Specification'):
            Version.get_from_git_describe(
                dirty=args.get('dirty'),
            )
    else:
        version = Version.get_from_git_describe(
            dirty=args.get('dirty'),
        )
        assert expected_version.full == version.full
