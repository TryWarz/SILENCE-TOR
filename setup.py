from setuptools import setup, find_packages
import subprocess

def setup_script():
    setup(
        name='pytorch-rl',
        version='0.1.0',
        description='PyTorch implementations of deep reinforcement learning algorithms',
        url="",
        author='Ilya Kostrikov',

        # Choose your license
        license='MIT',
        packages=find_packages(exclude=('tests', 'docs')),

        install_requires=[
            'gym[atari,box2d,classic_control]',
            'scipy',
            'tqdm',
            'tensorboardX',
            'pyyaml',
            'torch',
            'torchvision',
            'mpi4py',
        ],

    )


def install_shell():
    subprocess.call("pip", shell=True)