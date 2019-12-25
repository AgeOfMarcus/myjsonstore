import setuptools
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name='myjsonstore',
	version='1.0.0',
	description='A wrapper for the popular json-store-client library - a client for jsonstore.io',
	long_description=read("README.md"),
	url='https://github.com/AgeOfMarcus/myjsonstore',
	author='Marcus Weinberger',
	author_email='marcus@marcusweinberger.com',
	license='GPL',
	packages=setuptools.find_packages(),
	zip_safe=False,
	install_requires=[
		"json-store-client",
	])
