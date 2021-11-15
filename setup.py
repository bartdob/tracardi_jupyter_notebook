from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tracardi-jupyter-notebook',
    version='0.1',
    description='plugin to connect tracardi with jupiter notebook and run all cells',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='bartosz dobrosielski',
    author_email='bdobrosielski@edu.cdv.pl',
    packages=['tracardi_jupyter_notebook'],
    install_requires=[
        'tracardi-plugin-sdk',
        'tracardi'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords=['tracardi', 'plugin'],
    include_package_data=True,
    python_requires=">=3.8",
)