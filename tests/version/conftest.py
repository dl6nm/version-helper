import pytest


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
            'filename': 'config.txt',
            'variable_name': 'VERSION',
            'separator': '=',
            'full_version': '0.2.0-alpha.2+build-1357',
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
        'config.txt',
        'version',
        'version.txt',
    ]
)
def read_file_parameters(request):
    return request.param
