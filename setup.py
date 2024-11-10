from setuptools import setup, find_packages

setup(
    name="pwchecker",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "pwchecker=pwchecker:main",
        ],
    },
    author="Lenard Felix",
    description="A CLI tool to check password security and if it has been pwned.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pwchecker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
