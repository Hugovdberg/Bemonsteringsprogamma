import nox
import toml

python_versions = ["3.6", "3.7", "3.8"]


@nox.session(reuse_venv=True, venv_backend="conda", python=python_versions)
def tests(session):
    session.conda_install("pytest", "pytest-cov", "hypothesis")
    session.run("pytest")
