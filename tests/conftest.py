import pytest



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
