import pytest

from version_helper import Version


@pytest.fixture(
    params=[
        {
            'filename': '__version__.py',
            'variable_name': '__version__',
            'separator': '=',
            'full_version': '1.2.3-beta.1+build-987',
        },
        {
            'filename': 'app_version.py',
            'variable_name': 'APP_VERSION',
            'separator': '=',
            'full_version': '0.1.2+build-345',
        },
        {
            'filename': 'version',
            'variable_name': None,
            'separator': None,
            'full_version': '2.1.0-rc.1+build-3456',
        },
        {
            'filename': 'version.txt',
            'variable_name': 'version',
            'separator': ':',
            'full_version': '1.2.3-beta.1+build-987',
        },
    ],
    ids=[
        '__version__.py',
        'app_version.py',
        'version',
        'version.txt',
    ]
)
def read_file_parameters(request):
    return request.param


class TestReadWriteFile:
    # TODO: Add test for ValueError('Only "=" is allowed as separator for .py files. Could not parse file.')

    def test_read_file_value_error_wrong_py_separator(self, shared_datadir):
        with pytest.raises(ValueError, match='Only "=" is allowed as separator for .py files. Could not parse file.'):
            Version.read_from_file(
                file=shared_datadir/'__version__py',
                variable_name='__version__',
                separator=':',
            )

    # TODO: Add test for ValueError('None value for separator. Could not parse file.')
    # TODO: Add test for ValueError('None value for variable_name. Could not parse file.')

    # TODO: Add test for writing the version string to a file
    #   - FEATURE: WriteVersion - append the version to the file
    #   - FEATURE: WriteVersion - overwrite the version in the file
    #   - FEATURE: WriteVersion - choose the type of the version to write

    def test_read_file(self, shared_datadir, read_file_parameters):
        filename = read_file_parameters.get('filename')
        variable_name = read_file_parameters.get('variable_name')
        separator = read_file_parameters.get('separator')
        full_version = read_file_parameters.get('full_version')

        file = shared_datadir/filename
        version = Version.read_from_file(
            file=file,
            variable_name=variable_name,
            separator=separator,
        )
        assert version.full == full_version
