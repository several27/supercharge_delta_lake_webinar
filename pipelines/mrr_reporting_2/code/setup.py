from setuptools import setup, find_packages
setup(
    name = 'mrr_reporting_2',
    version = '1.0',
    packages = find_packages(include = ('mrr_reporting_2*', )) + ['prophecy_config_instances.test_123123123'],
    package_dir = {'prophecy_config_instances.test_123123123' : 'configs/resources/test_123123123'},
    package_data = {'prophecy_config_instances.test_123123123' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.16'],
    entry_points = {
'console_scripts' : [
'main = mrr_reporting_2.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
