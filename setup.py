import json
from pathlib import Path
from setuptools import setup, find_packages

MODULE_DIR = Path(__file__).resolve().parent

with open(MODULE_DIR.joinpath("setup.json")) as handle:
    SETUP_JSON = json.load(handle)

TESTING = ["pytest~=5.4", "pytest-cov~=2.10", "codecov~=2.1", "pgtest~=1.3,>=1.3.1"]
DEV = ["pylint~=2.5", "black~=19.10b0", "pre-commit~=2.6", "invoke~=1.4"] + TESTING

setup(
    long_description=open(MODULE_DIR.joinpath("README.md")).read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests", "profiles"]),
    python_requires=">=3.6",
    install_requires=[
        "aiida-core~=1.3.0",
        "fastapi~=0.59.0",
        "lark-parser~=0.9.0",
        "optimade[mongo]~=0.9.8",
        "pydantic~=1.6",
        "uvicorn~=0.11.5",
        "click~=7.1",
        "click-completion~=0.5.2",
    ],
    extras_require={"dev": DEV, "testing": TESTING},
    entry_points={
        "console_scripts": [
            "aiida-optimade = aiida_optimade.cli.cmd_aiida_optimade:cli",
        ],
    },
    **SETUP_JSON
)
