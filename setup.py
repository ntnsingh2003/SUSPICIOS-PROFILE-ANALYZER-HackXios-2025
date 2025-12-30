from setuptools import setup, find_packages

setup(
    name="suspicious-profile-analyzer",
    version="1.0.0",
    description="Cybersecurity threat detection for online profiles",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
        "Flask-CORS==4.0.0",
        "gunicorn==20.1.0"
    ],
    python_requires=">=3.11",
)