from setuptools import setup

setup(
    name = "zlac8015d",
    version = "0.0.1",
    author = "Rasheed Kittinanthapanya",
    author_email = "rasheedo.kit@gmail.com",
    url='https://github.com/rasheeddo/ZLAC8015D_python', 
    license='GPLv3',
    packages=['zlac8015d',],
    install_requires = [
        'pymodbus==2.5.3',
        'numpy==1.21',
        # 'setuptools==60.7.0'
    ]
)