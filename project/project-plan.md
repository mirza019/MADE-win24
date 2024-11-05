# Project Plan

## Title
Analyzing Gun Death Demographics and Incident Characteristics in America

## Main Question
1. What demographic and circumstantial patterns are associated with gun violence in the U.S., and how do they vary by age, race, intent, and incident characteristics?

## Description
This project uses two datasets to analyze gun-related deaths in the U.S., with an emphasis on demographic factors (age, race, gender, intent) and incident characteristics (gun type, number of fatalities, and injuries). By combining insights from FiveThirtyEight's gun deaths data and Jamesqo’s incident-level gun violence data, we aim to uncover trends, identify high-risk groups, and explore incident severity across different demographics and situations.

## Datasources

### Datasource 1: FiveThirtyEight Gun Deaths Dataset
- **URL**: [https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/full_data.csv](https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/full_data.csv)
- **Description**: Contains details on gun-related deaths in the U.S., including demographics (age, race, gender), intent (homicide, suicide, accidental), and place.
- **Key Columns**: `year`, `month`, `intent`, `age`, `race`, `sex`, `place`, `education`

### Datasource 2: Jamesqo Gun Violence Incident Data
- **URL**: [https://github.com/jamesqo/gun-violence-data/raw/master/DATA_01-2013_03-2018.tar.gz](https://github.com/jamesqo/gun-violence-data/raw/master/DATA_01-2013_03-2018.tar.gz)
- **Description**: Contains incident-level data on gun violence in the U.S., with information on fatalities, injuries, gun type, and incident characteristics.
- **Key Columns**: `date`, `state`, `city_or_county`, `n_killed`, `n_injured`, `incident_characteristics`, `gun_type`

## Work Packages

### Work Package 1: Data Collection
- [**Issue #1: Data Import**](https://github.com/your-repo/issues/1): Automate data fetching from GitHub URLs and load them into pandas DataFrames.
- [**Issue #2: Data Documentation**](https://github.com/your-repo/issues/2): Document the structure of each dataset, including column descriptions and initial observations.

### Work Package 2: Data Cleaning
- [**Issue #3: Handle Missing Values**](https://github.com/your-repo/issues/3): Identify and handle missing values in key columns.
- [**Issue #4: Data Type Standardization**](https://github.com/your-repo/issues/4): Standardize data types and formats (e.g., datetime conversion).
- [**Issue #5: Column Renaming and Selection**](https://github.com/your-repo/issues/5): Clean column names, select relevant columns, and drop unnecessary ones.

### Work Package 3: Exploratory Analysis
- [**Issue #6: Intent Patterns by Demographics**](https://github.com/your-repo/issues/6): Analyze patterns in gun death intent by age, race, and gender.
- [**Issue #7: Seasonal and Monthly Trends**](https://github.com/your-repo/issues/7): Examine monthly trends in gun deaths to identify any seasonal patterns.
- [**Issue #8: Incident Characteristics and Severity**](https://github.com/your-repo/issues/8): Investigate how characteristics like mass shootings and domestic violence correlate with fatalities.

### Work Package 4: Data Pipeline
- [**Issue #9: Pipeline Design**](https://github.com/your-repo/issues/9): Create an automated data pipeline for data ingestion, cleaning, and transformation.
- [**Issue #10: Storage Setup**](https://github.com/your-repo/issues/10): Set up storage solutions for processed data.
- [**Issue #11: Pipeline Automation**](https://github.com/your-repo/issues/11): Implement automation for regular data refresh and updates.

### Work Package 5: Reporting and Documentation
- [**Issue #12: Generate Report**](https://github.com/your-repo/issues/12): Summarize findings, trends, and visualizations in a comprehensive report.
- [**Issue #13: Create Visualizations**](https://github.com/your-repo/issues/13): Develop charts and graphs to represent data insights.
- [**Issue #14: Prepare Presentation**](https://github.com/your-repo/issues/14): Create a presentation summarizing the project’s findings.

## Timeline

| Phase                         | Description                                          | Duration    |
|-------------------------------|------------------------------------------------------|-------------|
| **Phase 1: Data Collection**  | Collect and load data from GitHub sources            | 1 week      |
| **Phase 2: Data Cleaning**    | Clean and preprocess data                            | 2 weeks     |
| **Phase 3: Exploratory Analysis** | Explore demographic and incident trends               | 2 weeks     |
| **Phase 4: Data Pipeline**    | Build ETL pipeline for data processing               | 3 weeks     |
| **Phase 5: Reporting**        | Document insights and prepare visualizations         | 1 week      |

## Data Exploration (Prepare for Project Work 3)

### Available Data
- **FiveThirtyEight Dataset**: Provides demographic and intent details on gun-related deaths.
- **Jamesqo Dataset**: Provides incident-level details, including fatalities, injuries, and characteristics of incidents.

### Potential Errors
- Missing data in key fields, such as age and intent.
- Inconsistencies in date formats between datasets.
- Differences in terminology between datasets (e.g., variations in incident types).

### Data Limitations
- The absence of `state` in FiveThirtyEight data limits location-specific analysis.
- The Jamesqo data might lack demographic details, making it harder to merge directly on all fields.
- Both datasets may not represent all incidents, as they rely on recorded data.

### Relevant Data Types
- **DateTime**: Needed for time-series analysis (e.g., year, month).
- **Categorical**: For columns like `intent`, `race`, `sex`, `incident_characteristics`.
- **Numerical**: For counts (e.g., `n_killed`, `n_injured`) and continuous fields like `age`.

### Summary
This document outlines the initial plan for analyzing gun-related deaths in the U.S. The data pipeline and analysis will focus on identifying trends in demographics, intent, and incident characteristics. Findings will be compiled in a final report with visualizations to answer the project’s main question.

---

