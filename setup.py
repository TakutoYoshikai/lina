from setuptools import setup, find_packages

setup(
    name = 'lina',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/lina.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'lina is a steganography program. It can hide a binary file or a text file into multiple png images.',
    install_requires = ['setuptools', "pycrypto"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "lina = lina.lina:main",
        ]
    }
)
