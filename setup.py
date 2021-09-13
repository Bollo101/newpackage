from setuptools import setup, find_packages

setup(
    name='newpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description= open('readme.MD').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package_name>',
    author = 'Robert Mackintosh',
    author_email='robmack101@gmail.com'
)