from os.path import abspath, dirname, join

from setuptools import find_packages, setup


def get_long_description():
    with open(
        join(dirname(abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="illallangi.tripitapi",
    version="0.0.1",
    author="Andrew Cole",
    author_email="andrew.cole@illallangi.com",
    description="TODO: SET DESCRIPTION",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/illallangi/TripItAPI",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9.1",
    entry_points={
        "console_scripts": [
            "tripit-json-to-sqlite=illallangi.tripitapi.scripts:json_to_sqlite.cli",
            "tripit-api-to-json=illallangi.tripitapi.scripts:api_to_json.cli",
        ],
    },
    project_urls={
        "Issues": "https://github.com/illallangi/TripItAPI/issues",
        "CI": "https://github.com/illallangi/TripItAPI/actions",
        "Changelog": "https://github.com/illallangi/TripItAPI/releases",
    },
    license="MIT License",
    install_requires=[
        "click",
        "diskcache",
        "loguru",
        "more_itertools",
        "peewee",
        "pytz",
        "requests",
        "requests_oauthlib",
        "tqdm",
        "yarl",
    ],
)
