import shutil
import subprocess
from pathlib import Path

DOIT_CONFIG = {
    "default_tasks": [
        "test",
        "lint",
        "flake8",
        "isort",
        "black",
    ],
    "continue": True,
}


cwd = Path(".")
python_files = list(cwd.glob("*.py"))
test_files = list(cwd.glob("test*.py"))


def task_flake8():
    for f in python_files:
        yield {
            "name": f.name,
            "actions": [
                [r"env\{{cookiecutter.scripts_or_bin}}\python", "-m", "flake8", f]
            ],
            "file_dep": [f],
        }


def task_lint():
    for f in python_files:
        yield {
            "name": f.name,
            "actions": [
                [
                    r"env\{{cookiecutter.scripts_or_bin}}\python",
                    "-m",
                    "pylint",
                    "--output-format=parseable",
                    f,
                ]
            ],
            "file_dep": [f],
        }


def task_test():
    for f in test_files:
        yield {
            "name": f.name,
            "actions": [
                [r"env\{{cookiecutter.scripts_or_bin}}\python", "-m", "pytest", f]
            ],
            "file_dep": [f],
        }


def task_isort():
    for f in python_files:
        yield {
            "name": f.name,
            "actions": [
                [
                    r"env\{{cookiecutter.scripts_or_bin}}\python",
                    "-m",
                    "isort",
                    "--profile",
                    "black",
                    "--check",
                    f,
                ]
            ],
            "file_dep": [f],
        }


def task_black():
    for f in python_files:
        yield {
            "name": f.name,
            "actions": [
                [
                    r"env\{{cookiecutter.scripts_or_bin}}\python",
                    "-m",
                    "black",
                    "--check",
                    "--quiet",
                    f,
                ]
            ],
            "file_dep": [f],
        }


def task_build():
    def python_build():
        build_folder = Path("build")
        if build_folder.exists():
            shutil.rmtree(build_folder)
        build_folder.mkdir()
        subprocess.call(
            ["py", "-m", "pip", "wheel", "--wheel-dir", "build", "--no-deps", "."]
        )
        return True

    return {"actions": [python_build]}


def task_upload():
    def python_upload():
        source_dir = Path("build")
        target_dir = Path("{{cookiecutter.local_wheels_repo}}")
        if target_dir.exists():
            shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)
            return True
        return False

    return {"actions": [python_upload]}


def task_upgrade_deps():
    def python_upgrade_deps():
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
        return True

    return {"actions": [python_upgrade_deps]}
