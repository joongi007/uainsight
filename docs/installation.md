# Installation Guide

This guide will help you install uainsight in your Python environment.

## Requirements

uainsight requires Python 3.9 or later.

## Installation Methods

### Using Poetry (Recommended)

If you're using Poetry for dependency management (which we recommend), you can add uainsight to your project with:

```bash
poetry add uainsight
```

### Using pip

If you prefer using pip, you can install uainsight with:

```bash
pip install uainsight
```

## Verifying the Installation

After installation, you can verify that uainsight is correctly installed by running Python and trying to import it:

```python
import uainsight
print(uainsight.__version__)
```

This should print the version number of uainsight without any errors.

## Installing for Development

If you want to contribute to uainsight or install the latest development version, you can clone the repository and install it in editable mode:

```bash
git clone https://github.com/joongi007/uainsight.git
cd uainsight
poetry install
```

Or if you're using pip:

```bash
pip install -e .
```

## Next Steps

Now that you have uainsight installed, you can start using it in your projects. Check out the [Usage Guide](usage.md) for examples and best practices.