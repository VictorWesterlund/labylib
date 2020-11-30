import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
    name="labylib",
    version="0.2.0",
    author="VicW",
    author_email="victor.vesterlund@gmail.com",
    description="API to modify LabyMod cosmetics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VictorWesterlund/labylib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)