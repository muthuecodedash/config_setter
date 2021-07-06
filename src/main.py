import os

from src.errors import Errors
from src.utils import ConfigSetterUtils as utils


class ConfigSetter(object):
    OS = 'os'
    JSON = 'json'
    ENV = 'env'

    YAML = 'yaml'
    CFG = 'cfg'
    CONF = 'conf'

    def __init__(self, filepath=None):
        # config
        self.supported_file_types = [self.YAML, self.CFG, self.CONF]

        # Risk Check
        if not filepath or not isinstance(filepath, str):
            raise TypeError(Errors.INVALID_FILEPATH)
        elif not any([filepath.endswith('.{}'.format(file_type)) for file_type in self.supported_file_types]):
            raise TypeError(Errors.INVALID_FILE_TYPE)
        elif not os.path.isfile(filepath):
            raise FileNotFoundError(Errors.FILE_NOT_FOUND)

        # Initialization
        self.filepath = filepath
        self.file_type = filepath.split('.')[-1]

        self.read_util_map = {
            self.YAML: utils.read_yaml,
            self.CFG: utils.read_cfg,
            self.CONF: utils.read_conf,
        }

        self.write_util_map = {
            self.ENV: utils.write_env,
            self.JSON: utils.write_json,
            self.OS: utils.write_os,
        }

    def write(self, write_method, filename=None):
        if write_method not in [self.ENV, self.JSON, self.OS]:
            raise TypeError(Errors.INVALID_WRITE_OPTION)

        raw_data = self.read_util_map[self.file_type](self.filepath)
        flatten_data = utils.flat_dict(raw_data)
        return self.write_util_map[write_method](flatten_data, filename)
