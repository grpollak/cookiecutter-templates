# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Usage

To run your Python application, navigate to the project's source directory and execute the main script:
```bash
cd {{ cookiecutter.project_name }}/src
python main.py
```

## License

This project is licensed under the
{% if cookiecutter.license == "MIT" %}
[MIT License](https://opensource.org/licenses/MIT)
{% elif cookiecutter.license == "Apache-2.0" %}
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
{% elif cookiecutter.license == "AGPL-3.0-only" %}
[AGPL-3.0 License](https://www.gnu.org/licenses/agpl-3.0.html)
{% elif cookiecutter.license == "Unlicense" %}
[Unlicense](http://unlicense.org/)
{% endif %}

## Author
👤 {{ cookiecutter.author_name }}
- GitHub: [{{ cookiecutter.github_username }}](https://github.com/{{ cookiecutter.github_username }})
