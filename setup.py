from setuptools import setup, find_packages
import subprocess, os

def setup_script():
    setup(
        name='SILENCE TOR',
        version='0.1.0',
        description='',
        url="",
        author='',

        license='MIT',
        packages=find_packages(exclude=('tests', 'docs')),

        install_requires=[

        ],

    )


def install_shell():
    subprocess.call("sudo apt install tor -y")
    subprocess.call("pip3 install requests", shell=True)
    subprocess.call("pip3 install colorama")
