from setuptools import setup, find_packages

setup(
    name="dev-utility-lab",
    version="0.2.0",
    description="A realistic professional Python utility package with maintainable architecture.",
    author="dev-utility-lab Contributors",
    packages=find_packages(include=["dev_utils", "dev_utils.*"]),
    install_requires=[],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="utility tools cli developer",
    entry_points={
        "console_scripts": [
            "dev-utils=dev_utils.cli:main",
        ],
    },
)