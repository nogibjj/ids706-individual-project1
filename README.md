# IDS706-Individual-Project1
- [![format](https://github.com/nogibjj/ids706-individual-project1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/ids706-individual-project1/actions/workflows/format.yml)
- [![install](https://github.com/nogibjj/ids706-individual-project1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Iids706-individual-project1/actions/workflows/install.yml)
- [![lint](https://github.com/nogibjj/ids706-individual-project1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/ids706-individual-project1/actions/workflows/lint.yml)
- [![test](https://github.com/nogibjj/ids706-individual-project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/ids706-individual-project1/actions/workflows/test.yml)

## Project Description
This project uses the `Pandas` library to perform descriptive statistics on the Iris dataset. The dataset is well-known in the field of machine learning and statistics for its simplicity and utility in classification tasks.

The project utilizes `matplotlib` to generate scatter plots that aid in visualizing the relationships between different features of the dataset.

The features of the Iris dataset are:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
- Species

**The objective of this project is to provide a Python-based pipeline for performing descriptive statistics, with the future scope of extending it to more advanced statistical analyses and machine learning tasks.**

In accordance with the grading rubric for Project #1, the project includes:
- A Jupyter Notebook (`descriptive_statistics.ipynb`) that demonstrates the use of the `nbval` plugin for `pytest`.
- A Python script (`descriptive_statistics.py`) that serves as the main entry point for the program.
- A `lib.py` file that contains shared utility functions.
- A `Makefile` that automates various tasks such as running tests and formatting code.
- Test scripts (`test_script.py` and `test_lib.py`) that perform unit tests on the project's functionalities.
- A `requirements.txt` file that lists all the project dependencies.
- Integration with GitHub Actions for continuous integration.



**Duke IDS706 Individual Project 1 Requirements:**

The project structure must include the following files:
- Jupyter Notebook with:
  - Cells that perform descriptive statistics using Polars or Panda.
  - Tested by using nbval plugin for pytest
- Python Script performing the same descriptive statistics using Polars or Panda
- A lib.py file that shares the common code between the script and notebook
- Makefile with the following:
  - Run all tests (must test notebook and script and lib)
  - Formats code with Python black
  - Lints code with Ruff
  - Installs code via:  pip install -r requirements.txt
- A test_script.py to test script
- A test_lib.py to test library
- Pinned requirements.txt
- GitHub Actions performs all four Makefile commands with badges for each one in the README.md



# Rubric
# Grading Rubric for Project #1: Continuous Integration using GitHub Actions of Python Data Science Project

## Table of Contents
- [Project Structure (15 points)](#project-structure-15-points)
- [Content of Jupyter Notebook and Python Script (20 points)](#content-of-jupyter-notebook-and-python-script-20-points)
- [Testing with nbval plugin for pytest (10 points)](#testing-with-nbval-plugin-for-pytest-10-points)
- [Shared code in lib.py (10 points)](#shared-code-in-libpy-10-points)
- [Makefile Commands (15 points)](#makefile-commands-15-points)
- [Test Scripts (10 points)](#test-scripts-10-points)
- [Requirements.txt (5 points)](#requirementstxt-5-points)
- [GitHub Actions (10 points)](#github-actions-10-points)
- [Demo Video (15 points)](#demo-video-15-points)

## Project Structure (15 points)

- **Jupyter Notebook**: 4 points
- **Python Script**: 4 points
- **lib.py file**: 4 points
- **Makefile**: 3 points

## Content of Jupyter Notebook and Python Script (20 points)

- **Correct and efficient use of Polars or Panda**: 10 points
- **Accuracy of descriptive statistics**: 10 points

## Testing with nbval plugin for pytest (10 points)

- **Correct usage and implementation of the nbval plugin for pytest in the Jupyter Notebook**.

## Shared code in lib.py (10 points)

- **The lib.py file correctly shares the common code between the script and notebook**.

## Makefile Commands (15 points)

- **Running all tests (notebook, script, lib)**: 5 points
- **Formatting code with Python black**: 5 points
- **Linting code with Ruff**: 5 points

## Test Scripts (10 points)

- **test_script.py**: 5 points
- **test_lib.py**: 5 points

## Requirements.txt (5 points)

- **The requirements.txt file is correctly pinned and installed via `pip install -r requirements.txt`**.

## GitHub Actions (10 points)

- **GitHub Actions correctly performs all Makefile commands and displays badges for each one in the README.md**.

## Demo Video (15 points)

- **Clarity of explanation**: 5 points
- **Quality demonstration of the project**: 5 points
- **Quality of video and audio**: 5 points


# Run commands
make clean
make install
make format
make lint
make test
make run