from setuptools import setup, find_packages


with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name="test_email",
    version="0.01",
    packages=find_packages(),
    install_requires=install_requires,

    # metadata to display on PyPI
    author="Emil Harvey",
    author_email="emil@email.com",
    description="Example demonstrating SMTP and SMTPD",
    keywords="",
    url="https://github.com/emil-h-harvey/python_email_example",
)
