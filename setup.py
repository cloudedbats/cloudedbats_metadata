from setuptools import setup

from metadata4bats import __version__

setup(name='metadata4bats',
    version=__version__,
    description='Metadata for bats, a part of the CloudedBats.org project.',
    url='https://github.com/cloudedbats/cloudedbats_metadata',
    author='Arnold Andreasson',
    author_email='info@cloudedbats.org',
    license='MIT',
    packages=['metadata4bats'],
    install_requires=[
        'guano',
    ],
    zip_safe=False)
