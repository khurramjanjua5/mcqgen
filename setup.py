from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Khurram Shahzad',
    author_email='khuramraja944@gmail.com',
   install_requires=['huggingface-hub','langchain','streamlit','python-dotenv','PyPdf2'],
    packages=find_packages()
)