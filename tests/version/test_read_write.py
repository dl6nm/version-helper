import pytest

from version_helper import Version


@pytest.mark.parametrize(
    argnames=['filename', 'var_name', 'separator', 'full_version'],
    argvalues=[
        ['__version__.py', '__version__', '=', '1.2.3-beta.1+build-987'],
        ['app_version.py', 'APP_VERSION', '=', '0.1.2+build-345'],
        ['version', None, '=', '2.1.0-rc.1+build-3456'],
        ['version.txt', None, None, '1.2.3-beta.1+build-987'],
    ],
    ids=[
        '__version__.py',
        'app_version.py',
        'version',
        'version.txt',
    ]
)
class TestReadWriteFile:

    def test_read_file(self, datadir, filename, var_name, separator, full_version):

    def test_write_file(self, tmp_path, filename, versions, var_name, separator):
        version: Version = versions
        file = tmp_path/filename

        # @todo: append the versio to the file
        # @todo: overwrite the version in the file
        # @todo: choose the type of the version to write

        version.write_file(
        file = datadir/filename
        version = Version.read_from_file(
            file=file,
            variable_name=var_name,
            separator=separator,
        )

        read_version = Version.read_file(file=file, variable_name=var_name, separator=separator)
        assert read_version == version.full
        assert False
        assert version.full == full_version
