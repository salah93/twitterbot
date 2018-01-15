from os.path import abspath, dirname, join
from setuptools import find_packages, setup


FOLDER = dirname(abspath(__file__))
DESCRIPTION = '\n\n'.join(open(join(FOLDER, x)).read().strip() for x in [
    'README.rst'])
setup(
    name='salahs-twitterbot',
    version='0.1',
    description='twitterbot to search hashtags',
    long_description=DESCRIPTION,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'License :: OSI Approved :: MIT License',
    ],
    author='Salah Ahmed',
    author_email='salah93@crosscompute.com',
    url='https://github.com/salah93/twitterbot',
    keywords='web twitterbot twitter',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'oauth2==1.9.0.post1',
    ])
