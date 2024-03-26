import nox
from nox_poetry import Session, session

py_versions = ["3.9", "3.10", "3.11"]

nox.needs_version = ">= 2021.6.6"
nox.options.sessions = (
    "tests",
)


@session(python=py_versions)
def tests(s: Session):
    """ Run unit tests """
    s.install(".")
    s.install(
        "asyncio",
        "pytest",
        "pytest-asyncio"
    )
    # run tests
    s.run(
        "pytest",
        "test/horreum_client_test.py",
        *s.posargs
    )


@session(python=py_versions)
def its(s: Session):
    """ Run integration tests """
    s.install(".")
    s.install(
        "asyncio",
        "pytest",
        "pytest-asyncio"
    )
    # run tests
    s.run(
        "pytest",
        "test/horreum_client_it.py",
        *s.posargs
    )
