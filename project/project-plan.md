# Project Plan

## Project Title
**Gun Deaths in America Analysis**

## Project Description
This project analyzes gun-related deaths in the United States to identify trends and insights related to circumstances, demographics, and geographic patterns associated with these incidents. Using FiveThirtyEight's dataset on gun deaths in America, we aim to explore factors like age, race, intent, and place of occurrence.

## Objectives
1. Understand and clean the dataset to ensure consistency.
2. Explore demographic patterns and trends across different years and states.
3. Identify correlations between various factors, such as intent, age, and race.
4. Build a data pipeline for continuous data ingestion, transformation, and loading for scalability.

## Project Timeline

| Phase                         | Description                                          | Duration    |
|-------------------------------|------------------------------------------------------|-------------|
| **Phase 1: Data Collection**  | Ingest gun deaths data from GitHub                   | 1 week      |
| **Phase 2: Data Cleaning**    | Clean and preprocess data for consistent analysis    | 2 weeks     |
| **Phase 3: Exploratory Analysis** | Explore demographic and intent patterns               | 2 weeks     |
| **Phase 4: Data Pipeline**    | Implement ETL (Extract, Transform, Load) processes   | 3 weeks     |
| **Phase 5: Reporting**        | Document insights and prepare visualizations         | 1 week      |

## Work Packages

### Work Package 1: Data Collection
- **Issue #1**: Fetch data from the GitHub URL and import it into a pandas DataFrame.
- **Issue #2**: Document the structure of the dataset, including column descriptions and initial observations.

### Work Package 2: Data Cleaning
- **Issue #3**: Handle missing values, remove duplicates, and standardize data types.
- **Issue #4**: Validate data accuracy and consistency (e.g., ensure age values are reasonable).
- **Issue #5**: Create a data dictionary that describes each field and its characteristics.

### Work Package 3: Exploratory Analysis
- **Issue #6**: Analyze the distribution of gun deaths by intent (e.g., homicide, suicide).
- **Issue #7**: Explore demographic trends by age, race, and gender.
- **Issue #8**: Identify any geographic patterns, such as common locations of incidents.

### Work Package 4: Data Pipeline
- **Issue #9**: Design a pipeline for data extraction and transformation, with modular cleaning steps.
- **Issue #10**: Implement database or storage for structured storage of the processed data.
- **Issue #11**: Automate data ingestion to refresh analysis with updated data as needed.

### Work Package 5: Reporting and Documentation
- **Issue #12**: Summarize findings and trends in a final report.
- **Issue #13**: Create visualizations (charts, graphs) to represent data insights.
- **Issue #14**: Prepare a presentation or summary document.

## Data Exploration (Prepare for Project Work 3)

### Dataset Overview
- **Source**: [FiveThirtyEight’s GitHub Repository](https://github.com/fivethirtyeight/guns-data)
- **URL**: [https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/full_data.csv](https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/full_data.csv)
- **Columns**:
  - `year`, `month`: Time of the incident.
  - `intent`: The intent behind the incident (e.g., homicide, suicide).
  - `police`: Whether police were involved.
  - `sex`, `age`, `race`: Demographics of the victim.
  - `place`: Location type of the incident (e.g., home, street).
  - `education`: Education level of the victim.

### Data Exploration Tasks
1. **Load and Describe Data**:
   - Check the number of records and columns.
   - Examine data types and ensure that columns like `year` and `month` are in a consistent date format.
  
2. **Identify Data Issues**:
   - Check for missing or inconsistent values, especially in `age`, `race`, and `education`.
   - Confirm reasonable ranges for numeric columns (e.g., age).

3. **Assess Data Limitations**:
   - The dataset is limited to recorded gun deaths, which may not represent all gun-related incidents.
   - Categories in `intent` may have subjective interpretations.
   - Coverage by `race` may limit demographic analysis.

4. **Determine Relevant Data Types**:
   - Categorical: `intent`, `police`, `sex`, `race`, `place`, `education`.
   - Numerical: `age`, `year`, `month`.

### Summary
This document serves as the initial plan for the analysis of gun deaths in the U.S., detailing the project’s scope, objectives, and phased approach. The data pipeline will be continuously refined as new insights emerge from exploratory analysis.

---
