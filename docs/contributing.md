# Contributing to useragent_parser

We welcome contributions to useragent_parser! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork locally:

        git clone https://github.com/joongi007/useragent-parser.git
        cd useragent-parser    

3. Ensure you have Poetry installed. If not, install it following the instructions at [Poetry Installation](https://python-poetry.org/docs/#installation)
    
    3.1. Additionally, you can install the "poetry-bumpversion" plug-in to help you manage the version. Follow the instructions in["poetry-bumpversion" Plugin Installation](https://github.com/monim67/poetry-bumpversion)

4. Install the project dependencies:

        poetry install

## Development Workflow

1. Create a new branch for your feature or bug fix:

        git checkout -b feature-or-fix-name

2. Make your changes and commit them with a clear commit message.
3. Push your changes to your fork:

        git push origin feature-or-fix-name

4. Open a pull request against the main repository.

## Coding Standards

- We use [Black](https://black.readthedocs.io/) for code formatting. Please run `poetry run black .` before committing.
- We use [Ruff](https://beta.ruff.rs/docs/) for linting. Run `poetry run ruff check . --fix` to check your code.
- Write clear, readable code and include comments where necessary.
- Write meaningful commit messages.

## Testing

- Write tests for new features or bug fixes using pytest.
- Ensure all tests pass before submitting a pull request:

        poetry run pytest


## Documentation

We use MkDocs for our documentation. Here's how you can work on, contribute to, and deploy the documentation:

1. **Setup**: Ensure you have all dependencies installed:

        poetry install

2. **Local Development**: To work on the documentation locally and see your changes in real-time:

        poetry run mkdocs serve

    This will start a local server, typically at `http://127.0.0.1:8000/`. You can view your changes live as you edit the documentation.

3. **Writing Documentation**: 
    - Documentation files are located in the `docs/` directory.
    - We use Markdown for our documentation. Please refer to the MkDocs documentation for specific formatting guidelines.
    - Update existing files or create new ones as needed.
    - Use clear and concise language in your documentation.

4. **Building Documentation**: To build the documentation:

        poetry run mkdocs build

    This will create a `site/` directory with the built HTML files.

5. **Submitting Changes**: 
    - Commit your changes to your feature branch.
    - Push the changes to your fork.
    - Open a pull request with a clear description of the documentation changes.

6. **Documentation Review**: 
    - The maintainers will review your documentation changes.
    - Be prepared to make adjustments based on feedback.

7. **Deployment**: 
    1. Ensure all changes have been reviewed and merged into the main branch.
    2. Run the following command:

            poetry run mkdocs gh-deploy

    3. This command builds the documentation and pushes it to the `gh-pages` branch, which GitHub Pages uses to serve the site.

Note: The ability to deploy documentation is typically restricted to project maintainers. If you're a contributor without deployment permissions, your documentation changes will be deployed once they're merged into the main branch.

Remember to update the documentation whenever you add new features, change existing functionality, or fix bugs that affect user interaction with the library.

If you have any questions about working on or deploying the documentation, please open an issue and we'll be happy to help!

## Submitting Changes

1. Push your changes to your fork on GitHub.
2. Submit a pull request to the main repository (https://github.com/joongi007/useragent-parser).
3. The core team will review your pull request and may request changes or ask questions.

## Reporting Issues

- Use the GitHub issue tracker to report bugs.
- Include as much detail as possible: steps to reproduce the issue, error messages, Python version, operating system, etc.

## Feature Requests

We're always looking for suggestions to improve useragent_parser. If you have an idea for a new feature:

1. Check if the feature has already been suggested or discussed in the issues.
2. If not, open a new issue describing the feature and its potential benefits.

## Questions?

If you have any questions about contributing, please open an issue and we'll be happy to help!

Thank you for contributing to useragent_parser!