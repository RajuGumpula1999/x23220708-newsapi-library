from setuptools import setup, find_packages

setup(
    name='newsapi',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',  # Add other dependencies as needed
    ],
    author='Raju Gumpula',
    author_email='rajugumpula033@gmail.com',
    description='A simple Python client for NewsAPI',
    long_description=open('README.md').read(),
    license='MIT',
    url='http://github.com/yourusername/newsapi'
)