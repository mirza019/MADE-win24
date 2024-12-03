
#!/bin/bash

echo "Running tests..."

# Mock external data download if running in CI (for faster execution)
echo "Creating mock data for testing purposes"
touch ./data/mock_data.csv  # Example of creating mock data

# Run the Python test script (assumed to be test.py)
python3 ./project/test.py

echo "Tests completed."
