from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='go2-webrtc-connect',
    version='1.0.0',
    author='legion1581',
    author_email='legion1581@gmail.com',
    packages=find_packages(),      
    install_requires=[
        f"aioice @ file://{os.path.join(here, 'libs/aioice')}",
        'aiortc==1.9.0', 
        'pycryptodome',
        'opencv-python',
        'sounddevice',
        'pyaudio',
        'requests',
        'wasmtime',
        'flask-socketio',
        'lz4',
        'pydub'
    ],
)
