import unittest

from src.main import ConfigSetter


class TestConfigSetter(unittest.TestCase):

    def test_without_input_file(self):
        with self.assertRaises(TypeError):
            ConfigSetter()

    def test_with_invalid_input_file_format(self):
        with self.assertRaises(TypeError):
            ConfigSetter('test.json')

    def test_with_not_exists_input_file(self):
        with self.assertRaises(FileNotFoundError):
            ConfigSetter('test1.yaml')

    def test_with_invalid_write_option(self):
        cs = ConfigSetter('tests/test_inputs/test.yaml')
        with self.assertRaises(TypeError):
            cs.write(ConfigSetter.YAML)

    def test_with_invalid_yaml_and_write_to_json(self):
        cs = ConfigSetter('tests/test_inputs/test_invalid.yaml')
        with self.assertRaises(ValueError):
            cs.write(ConfigSetter.JSON)

    def test_with_valid_yaml_and_write_to_json(self):
        cs = ConfigSetter('tests/test_inputs/test.yaml')
        self.assertEqual(cs.write(ConfigSetter.JSON), 'config.json')

    def test_with_valid_conf_and_write_to_os(self):
        cs = ConfigSetter('tests/test_inputs/test.conf')
        self.assertTrue(cs.write(ConfigSetter.OS))

    def test_with_valid_yaml_and_write_to_env(self):
        cs = ConfigSetter('tests/test_inputs/test.yaml')
        self.assertEqual(cs.write(ConfigSetter.ENV), 'config.env')
