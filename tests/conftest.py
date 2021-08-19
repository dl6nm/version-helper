import pytest

from pathlib import Path
from subprocess import CompletedProcess

from version_helper import Git, Version


@pytest.fixture(scope='function')
def mock_subprocess(monkeypatch, request) -> CompletedProcess:
    """Mock a command line call (subprocess)"""
    try:
        # params are directly given
        params = request.param
    except AttributeError:
        # params derived from a parent request
        params = request._parent_request.param

    def fake_subprocess(*args, **kwargs):
        return params.get("process")
    monkeypatch.setattr(Git, '_call_process', fake_subprocess)
    return Git._call_process()


@pytest.fixture(
    params=[
        {
            'process': CompletedProcess(
                args=['git', '--exec-path'],
                returncode=0,
                stdout=r'C:\Program Files\Git',
                stderr='',
            ),
            'exec_path': Path(r'C:\Program Files\Git'),
        },
        {
            'process': CompletedProcess(
                args=['git', '--exec-path'],
                returncode=0,
                stdout=br'C:\Program Files\Git',
                stderr=br'',
            ),
            'exec_path': Path(r'C:\Program Files\Git'),
        },
        {
            'process': CompletedProcess(
                args=['git', '--exec-path'],
                returncode=0,
                stdout=b'/usr/bin/git',
                stderr=b'',
            ),
            'exec_path': Path('/usr/bin/git'),
        },
        {
            'process': CompletedProcess(
                args=['git', '--exec-path'],
                returncode=127,
                stdout=b'',
                stderr=b'Der Befehl "git" ist entweder falsch geschrieben oder\nkonnte nicht gefunden werden.\n',
            ),
            'exec_path': None,
        },
    ],
    ids=['installed on win [str]', 'installed on win [bytes]', 'installed on linux', 'not installed'],
)
def git_exec_path_parameters(request, mock_subprocess):
    """Fixture for returning subprocess parameters for `git --exec-path`"""
    return request.param


@pytest.fixture(
    params=[
        {
            'args': {
                'dirty': False,
                'always': False
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags'],
                returncode=0,
                stdout=b'0.0.1',
                stderr=b'',
            ),
            'expected': '0.0.1',
            'expected_semver': '0.0.1',
            'expected_version': Version(major=0, minor=0, patch=1, prerelease=None, build=None),
        },
        {
            'args': {
                'dirty': False,
                'always': False
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags'],
                returncode=0,
                stdout=r'0.0.1-31-gdc27049',
                stderr=r'',
            ),
            'expected': '0.0.1-31-gdc27049',
            'expected_semver': '0.0.1+31-gdc27049',
            'expected_version': Version(major=0, minor=0, patch=1, prerelease=None, build='31-gdc27049'),
        },
        {
            'args': {
                'dirty': False,
                'always': False
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags'],
                returncode=0,
                stdout=r'0.0.1-alpha.1-31-gdc27049',
                stderr=r'',
            ),
            'expected': '0.0.1-alpha.1-31-gdc27049',
            'expected_semver': '0.0.1-alpha.1+31-gdc27049',
            'expected_version': Version(major=0, minor=0, patch=1, prerelease='alpha.1', build='31-gdc27049'),
        },

        {
            'args': {
                'dirty': True,
                'always': False
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags', '--dirty'],
                returncode=0,
                stdout=r'0.2.1-dirty',
                stderr=r'',
            ),
            'expected': '0.2.1-dirty',
            'expected_semver': '0.2.1+dirty',
            'expected_version': Version(major=0, minor=2, patch=1, prerelease=None, build='dirty'),
        },
        {
            'args': {
                'dirty': True,
                'always': False
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags', '--dirty'],
                returncode=0,
                stdout=r'0.0.1-31-gdc27049-dirty',
                stderr=r'',
            ),
            'expected': '0.0.1-31-gdc27049-dirty',
            'expected_semver': '0.0.1+31-gdc27049-dirty',
            'expected_version': Version(major=0, minor=0, patch=1, prerelease=None, build='31-gdc27049-dirty'),
        },
        {
            'args': {
                'dirty': True,
                'always': False
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags', '--dirty'],
                returncode=0,
                stdout=r'0.1.0-rc.3-31-gdc27049-dirty',
                stderr=r'',
            ),
            'expected': '0.1.0-rc.3-31-gdc27049-dirty',
            'expected_semver': '0.1.0-rc.3+31-gdc27049-dirty',
            'expected_version': Version(major=0, minor=1, patch=0, prerelease='rc.3', build='31-gdc27049-dirty'),
        },
        {
            'args': {
                'dirty': True,
                'always': True
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags', '--dirty', '--always'],
                returncode=0,
                stdout=r'0.0.1-31-gdc27049-dirty',
                stderr=r'',
            ),
            'expected': '0.0.1-31-gdc27049-dirty',
            'expected_semver': '0.0.1+31-gdc27049-dirty',
            'expected_version': Version(major=0, minor=0, patch=1, prerelease=None, build='31-gdc27049-dirty'),
        },
        {
            'args': {
                'dirty': True,
                'always': True
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags', '--dirty', '--always'],
                returncode=0,
                stdout=r'46467a2-dirty',
                stderr=r'',
            ),
            'expected': '46467a2-dirty',
            'expected_semver': None,
            'expected_version': None,
        },
        {
            'args': {
                'dirty': False,
                'always': True
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags', '--always'],
                returncode=0,
                stdout=r'46467a2',
                stderr=r'',
            ),
            'expected': '46467a2',
            'expected_semver': None,
            'expected_version': None,
        },

        {
            'args': {
                'dirty': False,
                'always': False
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags'],
                returncode=128,
                stdout=r'',
                stderr=r'fatal: not a git repository (or any of the parent directories): .git',
            ),
            'expected': None,
            'expected_semver': None,
            'expected_version': None,
        },
        {
            'args': {
                'dirty': False,
                'always': False
            },
            'process': CompletedProcess(
                args=['git', 'describe', '--tags'],
                returncode=128,
                stdout=r'',
                stderr=r'fatal: No names found, cannot describe anything.',
            ),
            'expected': None,
            'expected_semver': None,
            'expected_version': None,
        },
    ],
    ids=[
        'ok: default tag',
        'ok: default+commits',
        'ok: default+pre+build',

        'ok: dirty',
        'ok: +build-dirty',
        'ok: dirty+pre+build',
        'ok: dirty+always w/ tags',
        'ok: dirty+always w/o tags',
        'ok: always w/o tags',

        'fatal: not a git repository',
        'fatal: No names found',
    ],
)
def git_describe_parameters(request, mock_subprocess):
    """Fixture for returning subprocess parameters for `git describe`"""
    return request.param


@pytest.fixture(
    params=[
        Version(0, 1, 2),
        Version(1, 2, 3, 'beta.1'),
        Version(1, 2, 3, 'beta.1', 'build-987'),
        Version(1, 2, 3, None, 'build-987'),
        Version(1, 2, 3, None, 'dirty'),
    ],
    ids=[
        'core',
        'core-pre',
        'core-pre+build',
        'core+build',
        'core+dirty',
    ]
)
def versions(request):
    """Return Version objects for testing"""
    return request.param
