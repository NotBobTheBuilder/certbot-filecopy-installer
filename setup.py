from setuptools import find_packages, setup

version='0.9.0'

setup(
    name='certbot-filecopy-installer',
    version=version,
    maintainer='Jack Wearden',
    maintainer_email='jack@jackwearden.co.uk',
    description='Simple file copy installer for certbot',
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
