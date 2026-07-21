import yaml
from jinja2 import Environment, FileSystemLoader

# Load the YAML file
with open('parameters.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

# Prepare the Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('jsonSerializerCpp_tmpl.jinja2')

# Render the template with data from the YAML file
output = template.render(parameters=data['Parameters'])

# Save the rendered output to a file
with open(f'{data["Parameters"]["name"]}.cpp', 'w') as cpp_file:
    cpp_file.write(output)