from setuptools import setup, find_packages
packages_to_include = find_packages(exclude = ['test.*', 'test', 'test_manual'])
setup(
    name = 'prophecy_webinar_supercharge_delta_lake',
    version = '86',
    packages = packages_to_include,
    description = '',
    install_requires = [],
    data_files = ["resources/extensions.idx"]
)
