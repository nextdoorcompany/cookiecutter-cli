import subprocess

subprocess.call(["{{cookiecutter.root_python_exe}}", "-m", "venv", "env"])

subprocess.call(
    [
        "env/{{cookiecutter.scripts_or_bin}}/python",
        "-m",
        "pip",
        "install",
        "-r",
        "requirements-bootstrap.txt",
        "-U",
    ]
)

subprocess.call(
    [
        "env/{{cookiecutter.scripts_or_bin}}/pip-compile",
        "requirements.in",
    ]
)

subprocess.call(
    [
        "env/{{cookiecutter.scripts_or_bin}}/pip-sync",
    ]
)
