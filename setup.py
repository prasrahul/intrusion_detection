
from setuptools import setup

setup(
    name='Intrusion-Detection',
    version='0.0.1',
    description='Software for detecting the intrusion of a person',
    author='Prasanna Venkatesh',
    author_email='prasrahul6@gmail.com',
    packages=['src'],
    install_requires=[
        'pyyaml'
        'opencv-python',
        'onnxruntime'
    ]
)