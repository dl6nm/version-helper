import pytest


@pytest.fixture(
    params=[
        {
            'filename': '__version__.py',
            'variable_name': '__version__',
            'separator': '=',
            'full_version': '1.2.3-beta.1+build-987',
            'quote_version': True,
        },
        {
            'filename': 'app_version.py',
            'variable_name': 'APP_VERSION',
            'separator': '=',
            'full_version': '0.1.2+build-345',
            'quote_version': True,
        },
        {
            'filename': 'config.txt',
            'variable_name': 'VERSION',
            'separator': '=',
            'full_version': '0.2.0-alpha.2+build-1357',
            'quote_version': True,
        },
        {
            'filename': 'version',
            'variable_name': None,
            'separator': None,
            'full_version': '2.1.0-rc.1+build-3456',
            'quote_version': False,
        },
        {
            'filename': 'version.txt',
            'variable_name': 'version',
            'separator': ':',
            'full_version': '1.2.3-beta.1+build-987',
            'quote_version': False,
        },
    ],
    ids=[
        '__version__.py',
        'app_version.py',
        'config.txt',
        'version',
        'version.txt',
    ]
)
def rw_file_parameters(request):
    """Fixture for reading and writing to a file"""
    return request.param
