from setuptools import setup, find_packages

setup(
    name="dev-utility-lab",
    version="1.0.0",
    description="A realistic professional Python utility package with maintainable architecture.",
    author="dev-utility-lab Contributors",
    packages=find_packages(include=["dev_utils", "dev_utils.*"]),
    install_requires=[],
    python_requires=">=3.8",
)