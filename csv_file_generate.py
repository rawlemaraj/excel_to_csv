import pandas as pd
from jinja2 import Environment, FileSystemLoader

def generate_file_from_template(csv_file, template_file, output_dir, row_number):
    # Load the data from the CSV file
    data = pd.read_csv(csv_file)

    # Check if row_number is valid
    if row_number < 0 or row_number >= len(data):
        raise ValueError(f"row_number must be between 0 and {len(data) - 1}")

    # Load the template
    env = Environment(loader=FileSystemLoader('/path/to/templates')) # Put the path of your template file's directory here
    template = env.get_template(template_file)

    # Render the template with the data from the specified row
    output = template.render(data.iloc[row_number].to_dict())

    # Save the rendered template to a file
    output_file = f"{output_dir}/output_{row_number}.txt"
    with open(output_file, 'w') as f:
        f.write(output)

    print(f"File saved to {output_file}")

# Usage
generate_file_from_template('input.csv', 'template.j2', '/path/to/output', 0)
