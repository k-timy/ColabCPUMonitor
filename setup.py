import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Simple CPU Monitor",
    version="0.0.1",
    author="Kourosh T. Baghaei",
    author_email="",
    description="A helper package for monitoring CPU usage on Google Colab's platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/k-timy/SimpleCPUMonitor.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "psutil"
        ]
)
