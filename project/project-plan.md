# Project Plan

## Title
Geographic Hotspots and Incident Repetition Analysis of Gun Violence in the United States

## Main Questions
1. Which geographic locations in the U.S. experience the highest severity of gun violence incidents?
2. Are there repeated incidents over time in these high-risk areas, and do these incidents show patterns of escalation?

## Description
This project analyzes gun violence data to identify geographic hotspots for gun violence in the U.S. and examines the repetition and potential escalation of incidents over time within these locations. By combining insights from the FiveThirtyEight and Jamesqo datasets, we aim to pinpoint areas that require targeted interventions and explore trends of recurring incidents. This will inform policy recommendations and preventive measures for high-risk regions.

## Datasources

### Datasource 1: FiveThirtyEight Gun Deaths Dataset
- **Metadata URL**: [https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/README.md](https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/README.md)  *(or appropriate metadata link if available)*
- **Data URL**: [https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/full_data.csv](https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/full_data.csv)
- **Data Type**: CSV
- **Description**: This dataset contains information on gun-related deaths in the United States, including demographic details like age, race, and sex, as well as the intent of each incident (homicide, suicide, or accidental).

### Datasource 2: Jamesqo Gun Violence Incident Data
- **Metadata URL**: [https://github.com/jamesqo/gun-violence-data/blob/master/README.md](https://github.com/jamesqo/gun-violence-data/blob/master/README.md)
- **Data URL**: [https://github.com/jamesqo/gun-violence-data/raw/master/DATA_01-2013_03-2018.tar.gz](https://github.com/jamesqo/gun-violence-data/raw/master/DATA_01-2013_03-2018.tar.gz)
- **Data Type**: TAR.GZ (compressed archive containing CSV files)
- **Description**: This dataset provides incident-level information on gun violence in the U.S. from January 2013 to March 2018, including data about the location (state, city), the number of fatalities, injuries, and the date of the incident.


## Work Packages

### Work Package 1: Data Collection and Preparation
- **Issue #1: Data Ingestion**: Automate the retrieval of datasets from GitHub and load them into pandas DataFrames.
- **Issue #2: Column Standardization**: Standardize column names across both datasets to ensure consistency.
- **Issue #3: Extract Temporal Information**: Convert `date` column to datetime format and extract `year` and `month` for time-based analysis.

### Work Package 2: Data Cleaning
- **Issue #4: Handle Missing Values**: Identify and handle missing values, particularly in critical columns such as `n_killed`, `n_injured`, `state`, and `city_or_county`.
- **Issue #5: Data Type Consistency**: Ensure all columns have the correct data types (e.g., numerical, categorical).
- **Issue #6: Data Filtering**: Filter out irrelevant records or outliers that may skew the analysis.

### Work Package 3: Geographic Hotspot Analysis
- **Issue #7: Incident Aggregation by Location**: Aggregate data by `state` and `city_or_county` to calculate `total_killed` and `total_injured` for each location.
- **Issue #8: Identify Top Hotspots**: Identify locations with the highest cumulative fatalities and injuries.
- **Issue #9: Hotspot Visualization**: Create visualizations (e.g., bar charts, heatmaps) to represent high-risk areas for gun violence.

### Work Package 4: Incident Repetition and Escalation Analysis
- **Issue #10: Repeated Incident Tracking**: Track repeated incidents over time by analyzing `year` and `month` data for each location.
- **Issue #11: Severity Trend Analysis**: Assess whether incidents in repeated locations show an increasing trend in fatalities or injuries.
- **Issue #12: Time-Series Visualization**: Use line plots and FacetGrids to visualize incident counts and fatalities over time in top hotspots.

### Work Package 5: Data Pipeline
- **Issue #13: Pipeline Design**: Create an ETL pipeline to automate data ingestion, cleaning, aggregation, and transformation steps.
- **Issue #14: Storage and Reproducibility**: Set up structured storage for cleaned data and document each pipeline stage to ensure reproducibility.
- **Issue #15: Pipeline Automation**: Schedule regular updates to automatically refresh the data as new records become available.

### Work Package 6: Reporting and Insights
- **Issue #16: Key Findings Summary**: Summarize key findings, focusing on geographic hotspots and patterns of repeated incidents.
- **Issue #17: Policy Recommendations**: Provide recommendations for interventions in high-risk areas based on findings.
- **Issue #18: Create Presentation**: Prepare a presentation that highlights the project’s findings, insights, and potential policy applications.

## Timeline

| Phase                         | Description                                          | Duration    |
|-------------------------------|------------------------------------------------------|-------------|
| **Phase 1: Data Collection**  | Collect and standardize data                         | 1 week      |
| **Phase 2: Data Cleaning**    | Clean and preprocess data                            | 2 weeks     |
| **Phase 3: Geographic Analysis** | Identify and visualize hotspots                     | 2 weeks     |
| **Phase 4: Repetition Analysis** | Examine incident repetition and escalation patterns | 2 weeks     |
| **Phase 5: Data Pipeline**    | Develop and test the ETL pipeline                    | 3 weeks     |
| **Phase 6: Reporting**        | Document findings and prepare visualizations         | 1 week      |

## Data Exploration (Prepare for Project Work 3)

### Available Data
- **FiveThirtyEight Dataset**: Contains demographic and intent data for gun-related deaths, providing insight into victim profiles and incident types.
- **Jamesqo Dataset**: Provides location-based incident data, including fatalities, injuries, and dates, which is essential for identifying geographic patterns.

### Potential Issues
- **Missing Values**: Missing or incomplete records may impact the accuracy of the geographic and temporal analysis.
- **Data Standardization**: Differences in column naming and data types require standardization for seamless analysis.
- **Data Completeness**: Certain areas or types of incidents may be underreported, impacting representativeness.

### Data Limitations
- **Lack of Detailed Incident Characteristics**: The datasets may not have granular details on each incident’s characteristics, such as weapon type or motive.
- **Lack of Individual Identifiers**: Without unique identifiers for individuals involved, analyzing repeat offenders or individual incident recurrence is challenging.

### Data Types and Research Needs
- **DateTime**: Extract `year` and `month` from the `date` column for temporal analysis.
- **Categorical**: `state`, `city_or_county`, `intent` require categorical encoding for modeling and visualization.
- **Numerical**: `n_killed`, `n_injured` are continuous variables used to quantify incident severity.

### Summary
This project plan outlines a systematic approach to analyzing geographic hotspots and incident repetition in U.S. gun violence data. The project will utilize an ETL pipeline to automate data processing, enabling ongoing monitoring and updates. Findings from this analysis will inform policy recommendations aimed at reducing gun violence in high-risk areas.

---

