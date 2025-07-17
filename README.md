# Employee Salary Analysis

This project demonstrates how to analyze employee salary data using Python and Jupyter notebooks. It includes tools for data loading, statistical analysis, and visualization of employee compensation data.

This uses Amazon Bedrock Code AgentCore Interpreter -https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-file-operations.html 

## Project Overview

The project consists of:
- A Jupyter notebook for interactive data analysis
- A sample dataset of 100 employee salaries
- Python code for statistical analysis

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Lab or Jupyter Notebook
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone this repository or download the files
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Launch Jupyter Lab:
   ```bash
   jupyter lab
   ```

## Project Structure

```
.
├── README.md                 # This file
├── notebook.ipynb            # Main Jupyter notebook for analysis
├── employee_salaries.csv     # Sample dataset with employee salary information
├── requirements.txt          # Python dependencies
└── stats.py                  # Optional Python module for additional analysis
```

## Data Description

The `employee_salaries.csv` file contains:
- `employee_id`: Unique identifier for each employee (format: EMPxxx)
- `salary_usd`: Annual salary in US dollars

## Features

The notebook provides:
- Basic statistical analysis (mean, median, min, max, standard deviation)
- Salary distribution visualization
- Data validation and error handling

## Usage

1. Open `notebook.ipynb` in Jupyter Lab/Notebook
2. Run the cells sequentially to:
   - Load the employee salary data
   - Calculate key statistics
   - View the salary distribution

## Extending the Project

You can extend this project by:
- Adding more advanced visualizations (histograms, box plots, etc.)
- Incorporating additional employee data (department, tenure, etc.)
- Performing comparative analysis across different employee segments
- Building predictive models for salary forecasting

## License

This project is available for educational and personal use.

## Acknowledgments

- This project was created as a demonstration of data analysis using Python and Jupyter notebooks.