from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hr_egypt/__init__.py
from hr_egypt import __version__ as version

setup(
	name="hr_egypt",
	version=version,
	description="HR Egypt",
	author="Mahmoud",
	author_email="erpnext@zamiltec.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
