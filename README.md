## Project Overview

This repository contains scripts and data files for a database project aimed at processing and analyzing bulk data. The project involves several steps, from data preparation to visualization and providing a web interface for interaction.

---

## Project Structure

### Data Files:
- `bulk_data_2009_2010.csv`: Initial dataset containing raw data.
- `bulk_with_primary.csv`: Updated dataset with additional columns, including a unique reference.

### Scripts:
- `add_columns.py`: Python script to add new columns to the dataset.
- `insert_elements.py`: Python script to populate the database with data from the updated dataset.
- `data_visualisation.py`: Python script to visualize data through charts and graphs.
- `interface.py`: Python script to launch a Flask-based web interface for interacting with the database.

### Reports:
- `RaportProjetBDD`: Report detailing instructions for setting up the database schema (written in French).

---

## Project Workflow

### 1. Data Preparation

Execute the following script to add necessary columns to the dataset:


### 2. Database Setup

Refer to the `RaportProjetBDD` report for detailed instructions on setting up the database schema. Then, execute the following script to populate the database:


### 3. Data Analysis

Utilize the following script to generate visualizations such as charts and graphs for data analysis:


### 4. Web Interface

Launch the Flask-based web interface using the following command:


Access the web interface by navigating to `http://127.0.0.1:5000` in your web browser.

---

## Usage

1. Clone the repository to your local machine.
2. Execute the scripts in the specified order as per the project workflow.
3. Ensure that Python and necessary libraries are installed to run the scripts.
4. Follow the instructions in the `RaportProjetBDD` report for setting up the database schema.
5. Use the provided scripts for data manipulation, visualization, and interaction with the database.
