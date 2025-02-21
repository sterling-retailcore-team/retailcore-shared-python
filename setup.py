import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="shared-utils",
    version="0.2.1",
    author="Folayemi Bello",
    author_email="fola.bello@bepeerless.co",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={'shared_utils': [
        'templates/*.html',
        'templates/*.txt',
        'templates/*/*.html',
        'templates/*/*.txt',
        'templates/emails/layout/*.html',
        'templates/emails/layout/*.txt'
    ]},
    description="A utility package for shared utils",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/sterling-retailcore-team/retailcore-shared-python.git",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
