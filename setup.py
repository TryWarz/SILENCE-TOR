from setuptools import setup, find_packages
import subprocess, os
import src as silence_tor

def setup_script():
    setup(
        name='SILENCE TOR',
        version='0.1.0',
        description='A simple python script to run TOR in the background.',
        author='TryWarz',

        license='CC0 1.0 Universal',
        classifiers=[
            'Development Status :: 3 - Alpha',

            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',

            'License :: OSI Approved :: MIT License',

            'Programming Language :: Python :: 3.9',
        ],
        install_requires=[

        ],

    )


def install_shell():
    subprocess.call("sudo apt install tor -y")
    subprocess.call("pip3 install requests", shell=True)
    subprocess.call("pip3 install colorama")


def main():
    silence_tor.SILENCE_TOR().main()

main()