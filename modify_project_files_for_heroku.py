import tomlkit


# Modify pyproject.toml to specify Python version
def modify_pyproject_toml():
    with open("pyproject.toml", "r+", encoding="utf-8") as file:
        data = tomlkit.load(file)
        data["tool"]["poetry"]["dependencies"]["python"] = "3.11.7"  # Specify Python 3.11.7
        file.seek(0)
        tomlkit.dump(data, file)
        file.truncate()


# Modify poetry.lock to specify Python version
def modify_poetry_lock():
    with open("poetry.lock", "r+", encoding="utf-8") as file:
        content = file.readlines()
        modified_content = []
        for line in content:
            if 'python-versions = "' in line:  # Find the line with the Python version
                modified_content.append('python-versions = "3.11.7"\n')  # Replace it
            else:
                modified_content.append(line)
        file.seek(0)
        file.writelines(modified_content)
        file.truncate()


modify_pyproject_toml()
modify_poetry_lock()
