from setuptools import setup, find_packages
setup(
    name = 'cleanup_orders',
    version = '1.0',
    packages = find_packages(include = ('cleanup_orders*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.16'],
    entry_points = {
'console_scripts' : [
'main = cleanup_orders.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
