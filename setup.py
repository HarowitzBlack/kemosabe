

from setuptools import setup

setup(name="kemosabe",
      version='0.8.2',
      description='A Bot Development framework that bot development easy.',
      url='http://github.com/harowitzblack/kemosabe',
      author='Joel Benjamin (Harowitz Black)',
      author_email='joelbenjamin093@gmail.com',
      license='MIT',
      packages=['kemosabe'],
      install_requires=[
          'Flask','requests','gunicorn'
      ],
      zip_safe=False
)
