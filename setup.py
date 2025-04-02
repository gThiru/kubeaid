# setup.py
from setuptools import setup, find_packages

setup(
    name="kubeaid",
    version="0.1.0",
    author="Thirunavukkarasu Ganesan",
    description="AI-powered Kubernetes diagnosis and auto-remediation CLI tool",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "kubernetes>=25.3.0",
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "argparse",
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "kubeaid=main:run_diagnosis"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
