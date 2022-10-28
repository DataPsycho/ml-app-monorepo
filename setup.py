from setuptools import setup, find_packages


DESCRIPTION = 'Machine Learning - Training package'
LONG_DESCRIPTION = 'Machine learning package for training and parameter optimisation'
PACKAGE_NAME = "winepredictor"


def get_package_version():
    package_path = "src/winepredictor"
    # todo: Reda the version from the __init__.py file and return the version
    return "0.0.3"


# setting up
setup(
    name='winepredictor',
    version=get_package_version(),
    author='Adam Hertelendi',
    description=DESCRIPTION,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=['numpy', 'pandas', 'scikit-learn'],
    keywords=['python', 'machine learning', 'training', 'grid search'],
    classifiers=[
      "Development Status :: 1 - Planning",
      "Intended Audience :: Data Science",
      "Programming Language :: Python :: 3",
      "Operating System :: MacOS :: MacOS X",
      "Operating System :: Microsoft :: Windows"
      ]
)

