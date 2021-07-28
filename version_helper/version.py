import re


class Version:
    major: int = None
    minor: int = None
    patch: int = None
    pre_release: str = None
    build: str = None

    @staticmethod
    def parse(version_string: str) -> 'Version':
        pattern = r'(\d+)\.(\d+)\.(\d+)(?:\-((?:[\w\d\-]+\.?)+))?(?:\+((?:[\w\d\-]+\.?)+))?'
        match = re.fullmatch(pattern, version_string.strip())
        if match:
            Version.major = int(match.group(1))
            Version.minor = int(match.group(2))
            Version.patch = int(match.group(3))
            Version.pre_release = match.group(4)
            Version.build = match.group(5)
        else:
            raise ValueError('`version_string` is not valid to Semantic Versioning Specification')

        return Version()

    @staticmethod
    def core() -> str:
        return f'{Version.major}.{Version.minor}.{Version.patch}'
