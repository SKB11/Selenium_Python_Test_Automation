import configparser

class ConfigParser :
    def _init_(self, config_file_path) :
        self.config_file_path = config_file_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)

    def get_value(self, section, key) :
        try :
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError) :
            return None