from setuptools import setup

setup(
    name='simple_paths_algorithm',
    version='0.0.1',
    description='implementation of simple paths algorithm',
    url='https://github.com/andrew-lee2/simple_paths_algorithm',
    author='Andrew Lee, Douglas Shier',
    author_email='leeandrew2@gmail.com',
    license='MIT',
    packages=['simple_paths_algorithm'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'pandas',
        'networkx',
    ],

)
