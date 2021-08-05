import pytest

from subprocess import CompletedProcess

from version_helper import Git


@pytest.fixture
def mock_git_call_process(monkeypatch, request) -> CompletedProcess:
    def fake_call_process(*args, **kwargs):
        return CompletedProcess(
            args=request.param.get('args'),
            returncode=request.param.get('returncode'),
            stdout=request.param.get('stdout'),
            stderr=request.param.get('stderr'),
        )
    monkeypatch.setattr(Git, '_call_process', fake_call_process)
    return Git._call_process()
