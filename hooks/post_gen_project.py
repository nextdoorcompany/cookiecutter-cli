import subprocess

subprocess.call(["{{cookiecutter.root_python_exe}}", "-m", "venv", "env"])

subprocess.call(
    [
        "env/{{cookiecutter.scripts_or_bin}}/python",
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt",
        "-U",
    ]
)
