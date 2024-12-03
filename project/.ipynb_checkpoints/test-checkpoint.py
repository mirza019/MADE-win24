import os
import subprocess
import pandas as pd

# Test Case 1: Run the full ETL pipeline and validate the existence of output files
def test_etl_pipeline_end_to_end():
    print("Running the data pipeline...")
    
    # Run the pipeline using subprocess
    result = subprocess.run(['python', './project/pipeline.py'], capture_output=True, text=True)
    
    # Ensure the pipeline completes successfully
    if result.returncode != 0:
        print(f"Error: Pipeline failed with error: {result.stderr}")
        return False

    print("Pipeline ran successfully.")
    
    # Validate output files exist
    output_files = [
        './data/fivethirtyeight_cleaned.csv',
        './data/jamesqo_cleaned.csv',
        './data/fivethirtyeight_data.db',
        './data/jamesqo_data.db'
    ]
    
    for file in output_files:
        if not os.path.isfile(file):
            print(f"Error: {file} does not exist.")
            return False
        else:
            print(f"Success: {file} exists.")
    
    return True

# Test Case 2: Check that the output files are not empty
def test_file_sizes():
    print("Checking if the output files are not empty...")
    
    # Check if files are not empty
    if os.path.getsize('./data/fivethirtyeight_cleaned.csv') == 0:
        print("Error: fivethirtyeight_cleaned.csv is empty")
        return False
    if os.path.getsize('./data/jamesqo_cleaned.csv') == 0:
        print("Error: jamesqo_cleaned.csv is empty")
        return False
    
    print("Test passed: Output files are not empty.")
    return True

# Test Case 3: Check for missing values in the cleaned data
def test_no_missing_values():
    print("Checking for missing values in cleaned data...")

    # Load the cleaned data files
    fivethirtyeight_data = pd.read_csv('./data/fivethirtyeight_cleaned.csv')
    jamesqo_data = pd.read_csv('./data/jamesqo_cleaned.csv')
    
    # Assert that there are no missing values
    if fivethirtyeight_data.isnull().sum().sum() != 0:
        print("Error: Missing values in fivethirtyeight data.")
        return False
    if jamesqo_data.isnull().sum().sum() != 0:
        print("Error: Missing values in jamesqo data.")
        return False
    
    print("Test passed: No missing values in the cleaned data.")
    return True

# Main function to execute all tests
def run_tests():
    if not test_etl_pipeline_end_to_end():
        print("ETL pipeline test failed.")
        return
    if not test_file_sizes():
        print("File size test failed.")
        return
    if not test_no_missing_values():
        print("Missing value test failed.")
        return
    
    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
