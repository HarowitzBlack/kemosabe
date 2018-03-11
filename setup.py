

from setuptools import setup

setup(name="kemosabe",
      version='0.8.1',
      description='Yet another messenger bot framework for python',
      url='http://github.com/harowitzblack/kemosabe',
      author='Joel Benjamin (Harowitz Black)',
      author_email='joelbenjamin093@gmail.com',
      license='MIT',
      packages=['kemosabe'],
      install_requires=[
          'Flask','requests'
      ],
      zip_safe=False
)
