import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="sterling-utils",
    version="0.1.6",
    author="Folayemi Bello",
    author_email="fola@bepeerless.co",
    packages=setuptools.find_packages(),
    include_package_data=True,
    description="A utility package for sterling core",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/sterling-retailcore-team/retailcore-shared-python.git",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
