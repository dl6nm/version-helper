import re


SEMVER_PATTERN = r'^(?P<major>0|(?:[1-9]\d*))(?:\.(?P<minor>0|(?:[1-9]\d*))(?:\.(?P<patch>0|(?:[1-9]\d*)))(?:\-(?P<prerelease>[\w\d\.-]+))?(?:\+(?P<meta>[\w\d\.-]+))?)?$'
GIT_DESCRIBE_PATTERN = r'^(?P<major>0|(?:[1-9]\d*))(?:\.(?P<minor>0|(?:[1-9]\d*)))(?:\.(?P<patch>0|(?:[1-9]\d*)))(?:\-(?P<prerelease>(?:[\w\d\-]+\.?)+)(?=\-(?:\d+\-[\w\d]{8}(?:\-[\d\w\-]+)?)$))?(?:\-(?P<meta>\d+\-[\w\d]{8}(?:\-[\d\w\-]+)?))?$'


class Version:
    """
    Semantic Versioning compatible class for parsing and emitting SemVer strings into a `Version` object

    More details on Semantic Versioning can be found at https://semver.org/
    """

    def __init__(self, major: int, minor: int, patch: int,
                 prerelease: str = None, meta: str = None):
        """
        Create a `Version` object with the given attributes

        :param major: MAJOR version when you make incompatible API changes
        :param minor: MINOR version when you add functionality in a backwards compatible manner
        :param patch: PATCH version when you make backwards compatible bug fixes
        :param prerelease: Pre-release version string like `alpha.0` or `beta.3`
        :param meta: Build metadata
        """
        self.major: int = major
        self.minor: int = minor
        self.patch: int = patch
        self.prerelease: str = prerelease
        self.meta: str = meta
        self._build: str = meta

    def __repr__(self):
        return self.full

    def __str__(self):
        return self.full

    @staticmethod
    def parse(string: str, is_from_git_describe: bool = False) -> 'Version':
        """
        Parse a version string into it's individual Semantic Versioning parts

        :param string: A Semantic Versioning string
        :param is_from_git_describe: Wether or not the version string is from `git describe`
        :return: A `Version` class object
        """
        pattern = SEMVER_PATTERN
        if is_from_git_describe:
            pattern = GIT_DESCRIBE_PATTERN

        match = re.fullmatch(pattern, string.strip())

        if match:
            match_dict = match.groupdict()

            return Version(
                major=int(match_dict.get('major')),
                minor=int(match_dict.get('minor')),
                patch=int(match_dict.get('patch')),
                prerelease=match_dict.get('prerelease'),
                meta=match_dict.get('meta'),
            )
        else:
            raise ValueError('`version_string` is not valid to Semantic Versioning Specification')

    def set(self, major: int, minor: int, patch: int,
            prerelease: str = None, meta: str = None):
        """
        Set `Version` attributes

        :param major: MAJOR version when you make incompatible API changes
        :param minor: MINOR version when you add functionality in a backwards compatible manner
        :param patch: PATCH version when you make backwards compatible bug fixes
        :param prerelease: Pre-release version string like `alpha.0` or `beta.3`
        :param meta: Build metadata
        """
        self.major = major
        self.minor = minor
        self.patch = patch
        self.prerelease = prerelease
        self.meta = meta
        self._build = meta

    @property
    def core(self) -> str:
        """
        Core version string including major, minor and patch

        :return: Core version string
        """
        return f'{self.major}.{self.minor}.{self.patch}'

    @property
    def full(self) -> str:
        """
        Full Semantic Version string including prerelease and build metadata

        :return: Full version string with all it's Semantic Versioning parts
        """
        semver = f'{self.major}.{self.minor}.{self.patch}'
        if self.prerelease:
            semver += f'-{self.prerelease}'
        if self.meta:
            semver += f'+{self.meta}'
        return semver
