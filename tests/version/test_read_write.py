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
    # TODO: Add test for ValueError(f'Only "=" is allowed as separator for .py files. Could not parse file.')
    # TODO: Add test for ValueError('None value for separator. Could not parse file.')
    # TODO: Add test for ValueError('None value for variable_name. Could not parse file.')


    def test_write_file(self, tmp_path, filename, versions, var_name, separator):
        version: Version = versions
        file = tmp_path/filename
    def test_read_file(self, datadir, read_file_parameters):
        filename = read_file_parameters.get('filename')
        variable_name = read_file_parameters.get('variable_name')
        separator = read_file_parameters.get('separator')
        full_version = read_file_parameters.get('full_version')

        # @todo: append the versio to the file
        # @todo: overwrite the version in the file
        # @todo: choose the type of the version to write

        version.write_file(
        file = datadir/filename
        version = Version.read_from_file(
            file=file,
            variable_name=variable_name,
            separator=separator,
        )

        read_version = Version.read_file(file=file, variable_name=var_name, separator=separator)
        assert read_version == version.full
        assert False
        assert version.full == full_version
