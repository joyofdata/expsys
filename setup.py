from setuptools import setup

setup(
    name="expsys",
    version="0.1",
    description="Expert System Shell",
    packages=["expsys"],
    install_requires=["click>=8.0.0", "pydantic>=1.8.0",],
)
