import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eratools",
    version="0.0.1",
    license="LGPL",
    author="Michael Binder",
    author_email="michael.binder94@gmail.com",
    description="Processing of ERA5 data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michibinder/eratools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
        "xarray",
        "netcdf4"
    ]
)
