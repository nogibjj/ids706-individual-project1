# IDS706-python-template [![CI](https://github.com/nogibjj/IDS706-python-template/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/IDS706-python-template/actions/workflows/ci.yml)

Mini-project 1. 

## Features
- Environment Setup: Utilizes .devcontainer to set up a development environment in codespaces, ensuring consistent development environments across contributors.
- Automated Workflow: Uses a Makefile to automate common tasks such as installation, testing, formatting, and linting.
- Continuous Integration: Integrated with GitHub Actions to automate testing and other checks on push or pull request.
- Base Libraries: Includes a foundational set of libraries for DevOps and web development, listed in requirements.txt.

## Repository Structure
- main.py: The main Python script of the project.
- test_main.py: Tests associated with the main.py script.
- .devcontainer: Configuration for setting up a development environment in codespaces.
- .github: Configuration for GitHub Actions and other GitHub-related settings.
- requirements.txt: Lists the Python libraries and their versions required for this project.
- Makefile: Script to automate common tasks.

## Getting Started

1. Create a New Repository: Use this repository as a template to create a new repository.
2. Clone the Repository: Clone the new repository to your local machine.
3. Branching: Always create a new branch for your tasks or features.
4. Development: Make the necessary changes or additions to the project.
5. Commit and Push: Commit your changes and push them to the repository.
6. Pull Requests: Create a pull request to merge your changes into the main branch.
7. Code Review: Ensure your code is reviewed and all checks pass before merging.
8. Clean-Up: After merging, delete the feature or task branch to keep the repository clean.

## Contribution
Contributions are welcome! Please ensure you follow the outlined process for development and adhere to best practices.



# Rubric
Project #1: Continuous Integration using GitHub Actions of Python Data Science Project
Lead Instructor: Noah Gift
Requirements:
The project structure must include the following files:
Jupyter Notebook with:
 Cells that perform descriptive statistics using Polars or Panda.
Tested by using nbval plugin for pytest
Python Script performing the same descriptive statistics using Polars or Panda
lib.py file that shares the common code between the script and notebook
Makefile with the following:
Run all tests (must test notebook and script and lib)
Formats code with Python black
Lints code with Ruff
Installs code via:  pip install -r requirements.txt
test_script.py to test script
test_lib.py to test library
Pinned requirements.txt
GitHub Actions performs all four Makefile commands with badges for each one in the README.md

Grading Rubric for Project #1: Continuous Integration using GitHub Actions of Python Data Science Project

Project Structure (15 points): Proper organization and inclusion of all required files.

Jupyter Notebook: 4 points
Python Script: 4 points
lib.py file: 4 points
Makefile: 3 points

Content of Jupyter Notebook and Python Script (20 points): Cells/scripts that perform descriptive statistics using Polars or Panda.

Correct and efficient use of Polars or Panda: 10 points
Accuracy of descriptive statistics: 10 points

Testing with nbval plugin for pytest (10 points): Correct usage and implementation of the nbval plugin for pytest in the Jupyter Notebook.

Shared code in lib.py (10 points): The lib.py file correctly shares the common code between the script and notebook.

Makefile Commands (15 points): The Makefile correctly includes and executes all required commands.

Running all tests (notebook, script, lib): 5 points
Formatting code with Python black: 5 points
Linting code with Ruff: 5 points

Test Scripts (10 points): The test_script.py and test_lib.py files accurately and efficiently test the Python script and library.

test_script.py: 5 points
test_lib.py: 5 points

Requirements.txt (5 points): The requirements.txt file is correctly pinned and installed via pip install -r requirements.txt.

GitHub Actions (10 points): GitHub Actions correctly performs all Makefile commands and displays badges for each one in the README.md.

Demo Video (15 points): A 2-5 minute video is included, explaining the project and demonstrating its functionality. The video should be of high quality (both audio and visual), not exceed the given time limit, and be linked in the README via a private or public YouTube link.

Clarity of explanation: 5 points
Quality demonstration of the project: 5 points
Quality of video and audio: 5 points


Total: 100 points
