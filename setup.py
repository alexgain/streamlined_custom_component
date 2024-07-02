from setuptools import setup, find_packages

setup(
    name="streamlined_custom_component",
    version="0.2.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
    ],
    description="A package to create custom Streamlit components easily.",
    author="Alex Gain",
    author_email="alexzgain@gmail.com",
    url="https://github.com/alexgain/streamlined_custom_component",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)