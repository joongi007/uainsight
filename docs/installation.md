# Installation Guide

This guide will help you install useragent_parser in your Python environment.

## Requirements

useragent_parser requires Python 3.9 or later.

## Installation Methods

### Using Poetry (Recommended)

If you're using Poetry for dependency management (which we recommend), you can add useragent_parser to your project with:

```bash
poetry add useragent-parser
```

### Using pip

If you prefer using pip, you can install useragent_parser with:

```bash
pip install useragent-parser
```

## Verifying the Installation

After installation, you can verify that useragent_parser is correctly installed by running Python and trying to import it:

```python
import useragent_parser
print(useragent_parser.__version__)
```

This should print the version number of useragent_parser without any errors.

## Installing for Development

If you want to contribute to useragent_parser or install the latest development version, you can clone the repository and install it in editable mode:

```bash
git clone https://github.com/joongi007/useragent-parser.git
cd useragent-parser
poetry install
```

Or if you're using pip:

```bash
pip install -e .
```

## Next Steps

Now that you have useragent_parser installed, you can start using it in your projects. Check out the [Usage Guide](usage.md) for examples and best practices.