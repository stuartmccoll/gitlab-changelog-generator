import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitlab-changelog-generator",
    version="0.0.1",
    author="Stuart McColl",
    author_email="contact@stuartmccoll.co.uk",
    description="A small command line utility for generating CHANGELOG.md "
    + "files from GitLab repository commits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="gitlab changelog python",
    url="https://github.com/stuartmccoll/gitlab-changelog-generator",
    entry_points={
        "console_scripts": ["changegen=gitlab_changelog_generator.entry_point:main"]
    },
    packages=setuptools.find_packages(),
    classifiers=(
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
