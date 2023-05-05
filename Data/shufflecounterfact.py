import json
import random

# Read the list of dictionaries from the input file
with open('counterfact_re.json', 'r') as input_file:
    data = json.load(input_file)

# Check if the list has at least 5000 dictionaries
if len(data) < 560:
    print("Error: There are too less dictionaries in the input file.")
else:
    # Randomly select 5000 dictionaries
    selected_data = random.sample(data, 560)

    # Save the selected dictionaries to the output file
    with open('counterfact_resmall.json', 'w') as output_file:
        json.dump(selected_data, output_file)

    print("Successfully extracted dictionaries and saved them to the output file.")
