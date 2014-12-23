try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'College Chances Calculator',
	'author': 'Dmitri Kyle Brereton',
	'url': 'https://github.com/blacknyancat/chance-me',
	'download_url': 'https://github.com/blacknyancat/chance-me',
	'author_email': 'mitrikyle@yahoo.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'chanceme'
}
setup(**config)