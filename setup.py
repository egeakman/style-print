import contextlib
import json
import urllib.request
from setuptools import setup, find_packages


def latest_version(package_name):
    url = f"https://pypi.python.org/pypi/{package_name}/json"
    with contextlib.suppress(Exception):
        response = urllib.request.urlopen(urllib.request.Request(url), timeout=1)
        data = json.load(response)
        versions = data["releases"].keys()
        versions = sorted(versions)
        return f">={versions[-1]}"
    return ""


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="style-print",
    author="Ege Akman",
    author_email="me@egeakman.dev",
    url="https://github.com/egeakman/style-print",
    description="Print with style from the command line!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="2023.2.11",
    license="AGPLv3",
    download_url="https://github.com/egeakman/style-print/archive/2023.2.11.tar.gz",
    packages=find_packages(where="."),
    python_requires=">=3.5",
    entry_points={"console_scripts": ["style-print=style_print.style_print:main"]},
    install_requires=[
        f"setuptools{latest_version('setuptools')}",
        f"printy{latest_version('printy')}",
    ],
    keywords=["print", "console", "terminal", "style", "color", "printy", "utility"],
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
    ],
    project_urls={
        "Homepage": "https://github.com/egeakman/style-print",
        "Issues": "https://github.com/egeakman/style-print/issues",
    },
)
