# Config Setter Project

This module can be able to read .yaml, .cfg, .conf configuration file formats, read the configurations and generate a flat dictionary out of it.

Depending on the requirement, the module should be able to write the configurations in the .env file, .json file or it should also be able to set the configurations in the os environment.

## Dependency installation
Install requirements like yaml, coverage using the below command
```
pip install -r requirements.txt
```

## Usage

Access the module from outer python files using the following command
```
from config_setter import config_setter

cs = config_setter('input_file.yaml')
cs.write(config_setter.JSON)

```

## Running Test:
```
coverage run --omit='venv/*' -m unittest discover

coverage report
```