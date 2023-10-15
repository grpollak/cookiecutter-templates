# Python Cookiecutter Template

This is a Cookiecutter template for generating a Python project structure. It follows a standardized project layout and includes essential files to kickstart your Python project.

## Install Cookiecutter

```bash
pip install cookiecutter 
```

## Usage

To create a new Python project using this template, run the following command with Cookiecutter:

```bash
cookiecutter gh:grpollak.com/cookiecutter_termplates#default
```

You'll be prompted to enter project details such as project name, author, version, and description.

## License

This template provides the following licenses for your project:

- **MIT License**: A permissive open-source license that allows you to use, modify, and distribute the code with very few restrictions.

- **Apache License 2.0**: A widely-used open-source license that grants extensive permissions to users for using, modifying, and distributing the software.

- **GNU Affero General Public License 3.0 (AGPL-3.0)**: A copyleft license that ensures any modified version of the software remains under the AGPL-3.0 license.

- **The Unlicense (Unlicense)**: A public domain dedication that allows contributors to waive all their copyright and related rights in their works.

For more information on each license and to choose the appropriate one for your project, refer to [choosealicense.com](https://choosealicense.com/).

## Project Structure

The generated project structure will follow the standard Python project layout to organize your code in a clean and maintainable way. Here's a brief overview:

- `{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}`: Your project directory.
  - `__init__.py`: Initialization file for the package.
  - `pyproject.toml`: Poetry configuration file.
  - `README.md`: Project README file.
  - `src/`: Source code directory.
    - `__init__.py`: Initialization file for the source code package.
    - `main.py`: Main application file.
