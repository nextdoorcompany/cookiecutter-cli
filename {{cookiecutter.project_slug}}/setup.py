from setuptools import setup

setup(
    name="{{cookiecutter.project_slug}}",
    version="1",
    py_modules=["main"],
    install_requires=[],
    entry_points={"console_scripts": ["{{cookiecutter.project_slug}}=main:cli"]},
)
