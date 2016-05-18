from setuptools import setup


setup(
	name="tsc_cli",
	version='0.1',
	pymodules=['tsc'],
	install_requires=[
		'Click',

	],
	entry_points='''
		[console_scripts]
		tsc=tsc:tsc_cli
	''',

	)
