from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(name='finvizlite',
      version='0.1',
      description='A lightweight finviz screener scraper',
      long_description=README,
      long_description_content_type="text/markdown",
      url='https://github.com/andr3w321/finvizlite',
      author='Andrew Rennhack',
      author_email='andr3w321@gmail.com',
      license='MIT',
      install_requires=[
          'requests',
          'bs4',
          'lxml',
          'pandas'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      packages=['finvizlite'])
