import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="v4docker",
    version="0.0.1",
    author="lethe3000",
    author_email="lethe30003000@gmail.com",
    description="Simple TUI to manage docker images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['docker==4.0.2', 'picotui==1.0.1'],
    python_requires='>=3.6',
    scripts=['src/v4docker'],
)
