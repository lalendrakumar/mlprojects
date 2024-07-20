from setuptools import find_packages, setup

setup(
name = 'mlprojects',
version = '0.0.1',
author = 'Lalendra'
author_email = 'lalendrakumar4@gmail.com'
packages = find_packages()
install_requires=['pandas','numpy','seaborn']
install_package = get_requirements('requirements.txt')



)