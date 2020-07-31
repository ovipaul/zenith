import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zenith", 
    version="0.0.2",
    author="Ovi Paul",
    author_email="ovipaulcs@gmail.com",
    description="A library with various functionality that can be useful in the processing of data in machine learning, computer vision, data science etc.",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url="https://github.com/ovipaul/zenith",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
