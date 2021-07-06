import json
import os

import yaml

from src.errors import Errors


class ConfigSetterUtils(object):
    @staticmethod
    def read_yaml(filename):
        try:
            with open(filename, 'r') as file:
                return yaml.load(file, Loader=yaml.FullLoader)
        except yaml.scanner.ScannerError:
            raise ValueError(Errors.INVALID_YAML_FILE)


    @staticmethod
    def read_cfg(filename):
        return ConfigSetterUtils.read_conf(filename)

    @staticmethod
    def read_conf(filename):
        result = {}
        with open(filename, 'r') as file:
            for line in file.readlines():
                line = line.strip()
                if line and not (line.startswith(';') or line.startswith('#')):
                    try:
                        key, value = line.split(' ')[0], line.split(' ')[1]
                    except IndexError:
                        key = line.split(' ')[0]
                        value = None
                    result[key] = value
            return result

    @staticmethod
    def flat_dict(data, lkey=''):
        ret = {}
        for rkey, val in data.items():
            key = lkey + rkey
            if isinstance(val, dict):
                ret.update(ConfigSetterUtils.flat_dict(val, key + '_'))
            else:
                ret[key] = val
        return ret

    @staticmethod
    def write_env(data, file_path=None):
        file_path = file_path or 'config.env'
        with open(file_path, 'w+') as f:
            for key, value in data.items():
                f.writelines('{}="{}"\n'.format(key, value or ''))
        return file_path

    @staticmethod
    def write_json(data, file_path):
        file_path = file_path or 'config.json'
        with open(file_path, 'w+') as f:
            f.write(json.dumps(data))
        return file_path

    @staticmethod
    def write_os(data, file_path=None):
        for key, value in data.items():
            os.environ.setdefault(key, value or '')
        return True
