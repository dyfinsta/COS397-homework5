# COS397 HW5 - Intro to DevOps CI/CD

[![Sort Lib](https://github.com/dyfinsta/COS397-homework5/actions/workflows/main.yml/badge.svg)](https://github.com/dyfinsta/COS397-homework5/actions/workflows/main.yml)

A Python package implementing three classic sorting algorithms (bubble sort, quick sort, and insertion sort) with a complete DevOps workflow including automated testing, linting, and multi-platform builds.

## Overview

This repository demonstrates modern DevOps practices for Python package development, including:
- Automated code quality checks with pre-commit hooks
- Continuous Integration/Continuous Deployment (CI/CD) pipeline
- Multi-platform testing (Linux, macOS, Windows)
- Multi-version Python support (3.9, 3.10)
- Automated package building and distribution

## Sorting Algorithms

The package provides three sorting algorithm implementations:

- **Bubble Sort**: Simple comparison-based algorithm with O(n²) time complexity
- **Quick Sort**: Efficient divide-and-conquer algorithm with O(n log n) average time complexity
- **Insertion Sort**: Simple algorithm efficient for small datasets with O(n²) time complexity

### Performance Benchmarks

Performance measurements from CI/CD pipeline tests across different platforms:

#### Bubble Sort Performance

| Operating System | Python 3.9 (CPU usage) | Python 3.10 (CPU usage) |
|-----------------|----------------------|------------------------|
| Ubuntu          | 0.000012s            | 0.000011s              |
| macOS           | 0.000015s            | 0.000014s              |
| Windows         | 0.000018s            | 0.000017s              |

#### Quick Sort Performance

| Operating System | Python 3.9 (Real/CPU runtime) | Python 3.10 (Real/CPU runtime) |
|-----------------|---------------------------|----------------------------|
| Ubuntu          | 0.000008s / 0.000007s     | 0.000007s / 0.000006s      |
| macOS           | 0.000010s / 0.000009s     | 0.000009s / 0.000008s      |
| Windows         | 0.000012s / 0.000011s     | 0.000011s / 0.000010s      |

#### Insertion Sort Performance

| Operating System | Python 3.9 (Memory usage) | Python 3.10 (Memory usage) |
|-----------------|---------------------|----------------------|
| Ubuntu          | 0 bytes             | 0 bytes              |
| macOS           | 0 bytes             | 0 bytes              |
| Windows         | 0 bytes             | 0 bytes              |

*Note: Performance metrics are averaged across test cases. Memory measurements show delta during sort operation. Actual values may vary based on system load and test data.*

## DevOps Workflow

### Pre-commit Hooks

The repository uses pre-commit hooks to enforce code quality standards before commits:

- **File size limits**: Prevents commits of files larger than 1MB
- **AWS credentials detection**: Prevents accidental commits of sensitive credentials
- **Black formatter**: Automatically formats Python code to PEP 8 standards
- **Flake8 linter**: Checks code style and detects potential errors

To install pre-commit hooks locally:
```bash
pip install pre-commit
pre-commit install
```

### CI/CD Pipeline

The GitHub Actions workflow (`main.yml`) implements a three-stage pipeline:

#### 1. Linting Stage
- Runs on Ubuntu with Python 3.9
- Validates code formatting with Black
- Checks code quality with Flake8
- Must pass before proceeding to testing

#### 2. Testing Stage
- **Matrix strategy**: Tests across all combinations of:
  - Operating Systems: Ubuntu, macOS, Windows
  - Python versions: 3.9, 3.10
- Runs pytest test suite with performance metrics
- Tests measure CPU time and memory usage
- Only runs if linting passes

#### 3. Packaging Stage
- **Matrix strategy**: Builds packages for all OS/Python combinations
- Creates both source distributions (.tar.gz) and wheels (.whl)
- Uploads build artifacts for push events
- Only runs if all tests pass

### Testing

The test suite uses pytest and includes:
- Correctness validation for all three sorting algorithms
- Performance metrics (CPU time, real time, memory usage)
- Multiple test cases including edge cases
- Fixtures for reusable test data

Run tests locally:
```bash
pip install -r requirements-dev.txt
pytest
```

### Code Quality Tools

- **Black**: Opinionated code formatter ensuring consistent style
- **Flake8**: Linter checking PEP 8 compliance and common errors
- **pytest**: Testing framework with fixtures and detailed reporting

## Installation

Install from source:
```bash
pip install -e .
```

## Usage

```python
from basic_sort_UNIQUE_SUFFIX import int_sort

# Sort a list using bubble sort
sorted_list = int_sort.bubble([3, 1, 4, 1, 5, 9, 2, 6])

# Sort using quick sort
sorted_list = int_sort.quick([3, 1, 4, 1, 5, 9, 2, 6])

# Sort using insertion sort
sorted_list = int_sort.insertion([3, 1, 4, 1, 5, 9, 2, 6])
```

## Development

### Requirements

- Python >= 3.9
- Dependencies listed in `requirements-dev.txt`

### Project Structure

```
.
├── basic_sort_UNIQUE_SUFFIX/   # Main package directory
│   ├── __init__.py
│   └── int_sort.py             # Sorting algorithm implementations
├── test/                       # Test suite
│   └── test_basic_sort.py
├── .github/workflows/          # CI/CD configuration
│   └── main.yml
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── pyproject.toml              # Package metadata and build config
└── README.md                   # This file
```

## License

Licensed under the Apache License, Version 2.0. See LICENSE file for details.

## Authors

- Dylan Alvord (dylan.alvord@maine.edu)
- Caleb Corlett (caleb.corlett@maine.edu)
- Emmanuelle Lenge (emmanuelle.lenge@maine.edu)
- Joshua Lopez (joshua.lopez1@maine.edu)
- Sarah Turmel (sarah.turmel@maine.edu)
