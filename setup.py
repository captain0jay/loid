from setuptools import setup, find_packages

setup(
    name='loid',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'keyring>=23.5.0',
        'tabulate>=0.9.0',
        'rich>=13.7.0',
        'requests>=2.25.1'
    ],
    entry_points={
        'console_scripts': [
            'loid=loid.cli:main',
        ],
    },
)
