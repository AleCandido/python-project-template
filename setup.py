from pathlib import Path

from setuptools import setup, find_packages

here = Path(__file__).absolute().parent
with open(here / "README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    # the name to be used for pip package, not the python one
    name="<package-name>",
    version="<package-version>",
    description="<brief-description>",
    long_description=long_description,
    url="<docs/relevant-website>",
    author="<Name Surname>",
    author_email="<your-email>",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="<some-tags>",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[],
    setup_requires=["wheel"],
    project_urls={"Title": "another-relevant.url", "Title2": "or-even-more-than.one"},
)
