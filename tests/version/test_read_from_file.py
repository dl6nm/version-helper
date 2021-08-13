import pytest

from version_helper import Version


class TestReadFromFile:

    def test_read_file_value_error_wrong_py_separator(self, shared_datadir):
        """Test for getting a ValueError if the .py separator is a wrong one"""
        with pytest.raises(ValueError, match='Only "=" is allowed as separator for .py files. Could not parse file.'):
            Version.read_from_file(
                file=shared_datadir/'__version__.py',
                variable_name='__version__',
                separator=':',
            )

    @pytest.mark.parametrize(
        argnames=['separator'],
        argvalues=[
            [None],
            [''],
        ],
        ids=[
            'None',
            'empty string'
        ],
    )
    def test_read_file_value_error_none_separator(self, shared_datadir, separator):
        """Test for getting a ValueError if the separator is None and a variable_name is set"""
        with pytest.raises(ValueError, match='None value for separator. Could not parse file.'):
            Version.read_from_file(
                file=shared_datadir/'__version__.py',
                variable_name='__version__',
                separator=separator,
            )

    @pytest.mark.parametrize(
        argnames=['variable_name'],
        argvalues=[
            [None],
            [''],
        ],
        ids=[
            'None',
            'empty string'
        ],
    )
    def test_read_file_value_error_none_variable_name(self, shared_datadir, variable_name):
        """Test for getting a ValueError if the variable_name is None and a separator is set"""
        with pytest.raises(ValueError, match='None value for variable_name. Could not parse file.'):
            Version.read_from_file(
                file=shared_datadir/'__version__.py',
                variable_name=variable_name,
                separator='=',
            )

    def test_read_from_file(self, shared_datadir, rw_file_parameters):
        """Test for reading and parsing a version from a file"""
        filename = rw_file_parameters.get('filename')
        variable_name = rw_file_parameters.get('variable_name')
        separator = rw_file_parameters.get('separator')
        full_version = rw_file_parameters.get('full_version')

        file = shared_datadir/filename
        version = Version.read_from_file(
            file=file,
            variable_name=variable_name,
            separator=separator,
        )
        assert version.full == full_version
