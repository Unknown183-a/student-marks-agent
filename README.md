# Student Marks Analyzer — Multi-Agent Pipeline

A beginner-friendly Python project that analyzes student marks and generates subject-wise improvement recommendations using two independent agents.

## Overview

The project demonstrates how multiple Python modules can work together in a simple pipeline. One agent analyzes marks, while another recommends improvements based on each subject's score.

## Features

- Calculates total and average marks.
- Identifies the lowest-scoring subject.
- Recommends improvement for subjects scoring below 60.
- Encourages students to maintain and improve subjects scoring 60 or above.
- Uses separate Python files for each agent.
- Requires no external Python packages.

## Architecture

```text
                 User Input
                     |
                     v
              +-------------+
              |   main.py   |
              | Orchestrator|
              +-------------+
                     |
           +---------+---------+
           |                   |
           v                   v
   +---------------+   +----------------+
   | marks_agent.py|   |advisor_agent.py|
   |               |   |                |
   | Total, Average|   | Recommendations|
   | Lowest Subject|   | Subject-wise    |
   +---------------+   +----------------+
           |                   |
           +---------+---------+
                     |
                     v
              Student Report
```

## Project Structure

```text
AI Agents/
├── main.py
├── marks_agent.py
├── advisor_agent.py
└── README.md
```

## Technologies Used

- Python 3
- Python modules and imports
- Functions and dictionaries
- Basic conditional logic

## Getting Started

### Prerequisites

Install Python 3.9 or later.

Check your Python version:

```bash
python3 --version
```

### Run the Project

Clone the repository:

```bash
git clone https://github.com/Unknown183-a/student-marks-agent.git
cd student-marks-agent
```

Run the application:

```bash
python3 main.py
```

Enter the number of subjects, subject names, and marks out of 100 when prompted.

## How It Works

### Agent 1: Marks Analyzer

**File:** `marks_agent.py`

- Calculates total marks.
- Calculates average marks.
- Identifies the lowest-scoring subject.
- Returns the analysis as a Python dictionary.

### Agent 2: Improvement Advisor

**File:** `advisor_agent.py`

- Examines every subject's marks.
- If marks are below 60, recommends focused revision and practice.
- If marks are 60 or above, encourages the student to maintain and improve performance.
- Returns a list of recommendations.

### Pipeline Orchestrator

**File:** `main.py`

- Collects input from the user.
- Calls the Marks Analyzer.
- Calls the Improvement Advisor.
- Combines the results into a final student report.

## Example

Suppose the user enters:

| Subject | Marks |
|---|---:|
| Mathematics | 45 |
| Physics | 72 |
| Chemistry | 88 |
| English | 55 |

The application calculates:

- **Total marks:** 260
- **Average marks:** 65.0
- **Lowest-scoring subject:** Mathematics
- **Subjects requiring improvement:** Mathematics and English

The advisor recommends focused revision and practice for Mathematics and English, while encouraging the student to maintain performance in Physics and Chemistry.

## Learning Objectives

This project helps practise:

- Modular Python programming.
- Importing functions across files.
- Separation of responsibilities.
- Basic pipeline orchestration.
- Conditional decision-making.
- Returning and processing structured data.

## Future Improvements

- Integrate an LLM for personalized recommendations.
- Add input validation and exception handling.
- Write unit tests for both agents.
- Introduce structured outputs and logging.
- Explore LangGraph for explicit agent workflow orchestration.

## Current Limitations

This is a **rule-based prototype**, not yet an LLM-powered autonomous agent. The agents execute predefined Python logic without making model-driven decisions.

## License

This project is available for learning and educational purposes.

Built By - AMIT KUMAR 
From - Himachal Pradesh
