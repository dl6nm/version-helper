import pytest

from version_helper import Version


@pytest.mark.skip("This test is not fully implemented yet and won't be working")
@pytest.mark.parametrize(
    argnames=['filename', 'var_name', 'separator'],
    argvalues=[
        ['version.txt', None, None],
        ['__version__.py', '__version__', '='],
        ['__version__.py', 'APP_VERSION', '='],
        ['version.py', 'version', ':'],
        ['version', None, '='],
    ],
)
class TestReadWriteFile:

    def test_read_file(self, tmp_path, filename, var_name, separator):
        # @todo: add fixture files for reading a version from a file
        file = tmp_path/filename
        version = Version.read_from_file(
            file=file,
            variable_name=var_name,
            separator=separator,
        )
        assert False

    def test_write_file(self, tmp_path, filename, versions, var_name, separator):
        version: Version = versions
        file = tmp_path/filename

        # @todo: append the versio to the file
        # @todo: overwrite the version in the file
        # @todo: choose the type of the version to write

        version.write_file(
            file=file,
            variable_name=var_name,
            separator=separator,
        )

        read_version = Version.read_file(file=file, variable_name=var_name, separator=separator)
        assert read_version == version.full
        assert False
