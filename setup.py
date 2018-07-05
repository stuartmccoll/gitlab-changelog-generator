import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitlab-changelog-generator",
    version="1.0.2",
    author="Stuart McColl",
    author_email="it@stuartmccoll.co.uk",
    description="A small command line utility for generating CHANGELOG.md "
    + "files from GitLab repository commits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="gitlab changelog python",
    url="https://github.com/stuartmccoll/gitlab-changelog-generator",
    entry_points={
        "console_scripts": ["changegen=changelog_generator.entry_point:main"]
    },
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    tests_require=["unittest", "mock"],
    classifiers=(
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
