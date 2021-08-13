import pytest

from version_helper import Version


class TestWriteToFile:

    # TODO: Add test for writing the version string to a file
    #   - FEATURE: WriteVersion - overwrite the whole file
    #   - FEATURE: WriteVersion - append the version to the file
    #   - FEATURE: WriteVersion - overwrite the version (key/value) in the file
    #   - FEATURE: WriteVersion - choose the type of the version to write

    @pytest.mark.parametrize(
        argnames=['version_type'],
        argvalues=[
            ['core'],
            ['full'],
        ],
    )
    def test_write_to_file(self, tmp_path, shared_datadir, rw_file_parameters, version_type):
        """Basic test for writing a version to a file"""
        filename = rw_file_parameters.get('filename')
        variable_name = rw_file_parameters.get('variable_name')
        separator = rw_file_parameters.get('separator')
        full_version = rw_file_parameters.get('full_version')
        quote_version = rw_file_parameters.get('quote_version')
        encoding = rw_file_parameters.get('encoding')

        version = Version.parse(full_version)
        write_file_path = tmp_path/filename

        written = version.write_to_file(
            file=write_file_path,
            variable_name=variable_name,
            separator=separator,
            version_type=version_type,
            quote_version=quote_version,
            encoding=encoding,
        )
        assert written > 0

        written_version_read = Version.read_from_file(
            file=write_file_path,
            variable_name=variable_name,
            separator=separator,
        )

        if version_type == 'core':
            assert written_version_read.full == version.core
            assert written_version_read.core == version.core
        elif version_type == 'full':
            assert written_version_read.full == full_version
            assert written_version_read.full == version.full
        else:
            assert False
