import pytest

from subprocess import CompletedProcess

from version_helper import Git


@pytest.fixture
def mock_subprocess(monkeypatch, request) -> CompletedProcess:
    """Mock a command line call (subprocess)"""
    def fake_subprocess(*args, **kwargs):
        return CompletedProcess(
            args=request.param.get('args'),
            returncode=request.param.get('returncode'),
            stdout=request.param.get('stdout'),
            stderr=request.param.get('stderr'),
        )
    monkeypatch.setattr(Git, '_call_process', fake_subprocess)
    return Git._call_process()
