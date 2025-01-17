## Geographic Hotspots and Incident Repetition Analysis of Gun Violence in the United States**

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

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.

## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones, so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to HTML: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervals, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/).

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
