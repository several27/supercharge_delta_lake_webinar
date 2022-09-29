from setuptools import setup, find_packages
setup(
    name = 'ingest_customers',
    version = '1.0',
    packages = find_packages(include = ('ingest_customers*', )) + ["prophecy_config_instances"],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.3.5'],
    entry_points = {
'console_scripts' : [
'main = ingest_customers.pipeline:main', ], },
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
