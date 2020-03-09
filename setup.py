import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Thomas Thelen",
    version="0.0.1",
    author="Thomas Thelen",
    author_email="thelen@nceas.ucsb.edu",
    description="A client for querying SDTL from C2Metadata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thomasthelen/sdtlpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)