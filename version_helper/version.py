import re


SEMVER_PATTERN = r'(\d+)\.(\d+)\.(\d+)(?:\-((?:[\w\d\-]+\.?)+))?(?:\+((?:[\w\d\-]+\.?)+))?'


class Version:
    def __init__(self, major: int, minor: int, patch: int,
                 prerelease: str = None, build: str = None):
        self.major: int = major
        self.minor: int = minor
        self.patch: int = patch
        self.prerelease: str = prerelease
        self.build: str = build

    def __str__(self):
        return self.full

    def __repr__(self):
        return self.full

    @property
    def full(self) -> str:
        """
        Full Semantic Version string including prerelease and build

        :return: Full version string with all it's Semantic Versioning parts
        """
        semver = f'{self.major}.{self.minor}.{self.patch}'
        if self.prerelease:
            semver += f'-{self.prerelease}'
        if self.build:
            semver += f'+{self.build}'
        return semver
    @staticmethod
    def parse(version_string: str) -> 'Version':
        """
        Parse a version string into it's individual Semantic Versioning parts

        :param version_string: A Semantic Versioning string
        :return: A `Version` class object
        """
        match = re.fullmatch(SEMVER_PATTERN, version_string.strip())
        if match:
            return Version(
                major=int(match.group(1)),
                minor=int(match.group(2)),
                patch=int(match.group(3)),
                prerelease=match.group(4),
                build=match.group(5),
            )

        else:
            raise ValueError('`version_string` is not valid to Semantic Versioning Specification')

    def set(self, major: int, minor: int, patch: int,
            prerelease: str = None, build: str = None):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.prerelease = prerelease
        self.build = build

    @property
    def core(self) -> str:
        return f'{self.major}.{self.minor}.{self.patch}'
