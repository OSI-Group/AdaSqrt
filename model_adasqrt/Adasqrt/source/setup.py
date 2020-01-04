### setup files 

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="source-YOUR-emmanuel", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="egabeli@aimsammi.com",
    description="Implementation of Adasqrt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OSI-Group/AdaSqrt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
