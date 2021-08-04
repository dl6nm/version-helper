import pytest

from subprocess import CompletedProcess


@pytest.fixture
def git_installed() -> CompletedProcess:
    """
    Mock an installed git instance, returning the installation path
    """
    return CompletedProcess(
        args=['git', '--exec-path'],
        returncode=0,
        stdout=b'C:/Git',
        stderr=b'',
    )


@pytest.fixture
def git_not_installed() -> CompletedProcess:
    """
    Mock a not installed git instance, returning an error
    """
    return CompletedProcess(
        args=['git', '--exec-path'],
        returncode=127,
        stdout=b'',
        stderr=b'Der Befehl "git" ist entweder falsch geschrieben oder konnte nicht gefunden werden.',
    )


@pytest.fixture
def git_describe_fatal_error():
    """
    Mock a fatal error produced by git describe, if the .git directory is missing in repository

    :return: A mocked CompletedProcess object
    """
    from subprocess import CompletedProcess
    return CompletedProcess(
        args=['git', 'describe'],
        returncode=128,
        stdout=b'',
        stderr=b'fatal: not a git repository (or any of the parent directories): .git\n'
    )
