import pytest

from pathlib import Path
from subprocess import CompletedProcess

from version_helper import Git


@pytest.fixture(scope='function')
def mock_subprocess(monkeypatch, subprocess_parameters) -> CompletedProcess:
    """Mock a command line call (subprocess)"""
    def fake_subprocess(*args, **kwargs):
        return subprocess_parameters.get("process")
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
def subprocess_parameters(request):
    """Fixture for returning subprocess parameters"""
    return request.param
