from os import path
from setuptools import find_packages, setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    DESCRIPTION = f.read()


tests_deps = [
    "pytest>=4.0.0,<5.0.0",
    "httpretty>=0.9.6,<1.0.0",
]

scripts_deps = [
    'yweather>=0.1,<1.0'
]


setup(
    name="salahs-twitterbot",
    version="1.3.0",
    description="twitterbot to remove/view favorites/tweets and view trending tweets",
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: MIT License",
    ],
    author="Salah Ahmed",
    author_email="salah93@crosscompute.com",
    url="https://github.com/salah93/twitterbot",
    keywords="web twitterbot twitter",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=["pytest-runner"],
    install_requires=[
        "oauth2>=1.9.0.post1,<2.0.0"
    ],
    tests_require=tests_deps,
    extras_require={
        'test': tests_deps,
        'scripts': scripts_deps,
    },
    entry_points={
        "console_scripts": {
            "delete_old_tweets = twitterbot.scripts.delete_tweets:main",
            "get_trending_tweets = twitterbot.scripts.get_trending:main",
            "remove_favorites = twitterbot.scripts.remove_favorites:main",
        }
    },
)
