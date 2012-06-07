from setuptools import setup, find_packages

setup(
    name = "PROJECT_NAME",
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
