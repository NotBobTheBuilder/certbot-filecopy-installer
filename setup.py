from setuptools import find_packages, setup
from pathlib import Path

version='0.9.0'
this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name='certbot-filecopy-installer',
    version=version,
    maintainer='Jack Wearden',
    maintainer_email='jack@jackwearden.co.uk',
    description='Simple file copy installer for certbot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='letsencrypt certbot installer',
    url='https://github.com/NotBobTheBuilder/certbot-filecopy-installer',
    license='MIT License',
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'acme',
        'certbot',
        'setuptools',
    ],
    extras_require={
        'test': [ 'pytest' ],
    },
    entry_points={
        'certbot.plugins': [
            'filecopy-installer = filecopy_installer:FilecopyInstaller',
        ],
    },
)
