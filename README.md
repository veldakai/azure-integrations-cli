# Azure Integrations CLI

**Azure Integrations CLI** is a Python-based command-line tool designed to streamline the creation and management of Azure Integration Services projects. It provides scaffolding for Logic Apps, Function Apps, and configuration files, with support for global installation and shell autocompletion for enhanced developer productivity.

## Features

- Scaffold and manage Azure Integration Services projects
- Create default files and configurations for Logic Apps and Function Apps
- Global installation via pip (or optionally via Homebrew)
- Built-in version display
- Out-of-the-box shell autocompletion using Click

## Repository Structure

```plaintext
azure-integrations-cli/
├── azints/                     # Main package
│   ├── __init__.py             # Package initialization (holds version info)
│   └── cli.py                  # CLI implementation using Click
├── .gitignore                  # Typical Python .gitignore entries
├── LICENSE                     # License file
├── pyproject.toml              # Packaging configuration
├── README.md                   # Project documentation (this file)
└── requirements.txt            # List of dependencies (e.g. Click)
```

## Installation

### From repository

Clone the repository and install globally using pipx:

```shell
pipx install . --force    
```

This will install the package and make the ```azints``` command available globally.

### From PyPI (When Published)

If published to PyPI, you can install it using:

```shell
pipx install azure-integrations-cli
```

## Usage

After installation, you can run the CLI tool globally:

```shell
azints --version
```

This command displays the current version of the tool.

## Enabling Shell Autocompletion

Click provides built-in support for shell autocompletion. To enable autocompletion for Bash or Zsh, add the following line to your shell configuration file (e.g., ~/.bashrc or ~/.zshrc):

```shell
eval "$(_AZINTS_COMPLETE=source azints)"
```

Then, restart your terminal or source the configuration file to activate autocompletion.

For more advanced scenarios or support with other shells (like Fish), consider exploring the [click-completion](https://click.palletsprojects.com/en/stable/shell-completion/) package.

## Development

To contribute or extend this project:

1. Fork the repository.

1. Create a new branch for your feature or bugfix.

1. Commit your changes and push your branch.

1. Open a pull request with details about your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.