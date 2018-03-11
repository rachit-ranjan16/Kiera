from setuptools import setup, find_packages

ver = "9.9.9"
with open("README.md", mode='r') as f:
    long_description = f.read()

with open("Makefile", mode='r') as f:
    ver = f.read().split('\n')[0].split('=')[1][1:]

setup(
   name='Kiera',
   version=ver,
   url='https://github.com/rachit-ranjan16/Kiera',
   description='A Deep Learning Application for Traffic Sign Recognition',
   long_description=long_description,
   license='GNU',
   author='rachit-ranjan16',
   author_email='rachit.ranjan93@gmail.com',
   classifiers=[
       "Development Status :: 3 - Alpha",
       "Intended Audience :: Developers",
       "Topic :: Software Development",
       "License :: OSI Approved :: GNU General Public License (GPL)",
       "Programming Language :: Python :: 3.6.3",
       ],
   keywords='deep learning',
   packages=find_packages(),  # same as name
   install_requires=['tensorflow', 'keras', 'numpy', 'django', 'celery', 'scikit-image', 'protobuf', 'enum34'],
   python_requires='~=3.6.3'
)