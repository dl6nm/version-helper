import pytest

from pathlib import Path
from subprocess import CompletedProcess

from version_helper import Git


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
            'process': CompletedProcess(
                args=['git', 'describe'],
                returncode=0,
                stdout=r'0.0.1-31-gdc27049',
                stderr=r'',
            ),
            'expected': '0.0.1-31-gdc27049',
        },
        {
            'process': CompletedProcess(
                args=['git', 'describe'],
                returncode=128,
                stdout=r'',
                stderr=r'fatal: not a git repository (or any of the parent directories): .git',
            ),
            'expected': None,
        },
    ],
    ids=['success', 'fatal error'],
)
def git_describe_parameters(request, mock_subprocess):
    """Fixture for returning subprocess parameters for `git describe`"""
    return request.param
