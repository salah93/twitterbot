from setuptools import find_packages, setup


with open("README.rst") as f:
    DESCRIPTION = "\n".join(f.readlines())

setup(
    name="salahs-twitterbot",
    version="1.0",
    description="twitterbot to search hashtags",
    long_description=DESCRIPTION,
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
    tests_require=[
        "pytest>=4.0.0,<5.0.0",
        "httpretty>=0.9.6,<1.0.0",
    ],
    entry_points={
        "console_scripts": {"delete_old_tweets = twitterbot.scripts.delete_tweets:main"}
    },
)
