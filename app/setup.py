from setuptools import setup


setup(
	name="tbs_cli",
	version='0.1',
	pymodules=['runner'],
	install_requires=[
		'Click',

	],
	entry_points='''
		[console_scripts]
		runner=runner:tbs_cli
	''',

	)
