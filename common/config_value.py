import os
import configparser

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path,'..//config/config_base.ini')

class ConfigUtils:
    def __init__(self,config_path=cfgpath):
        self.__conf = configparser.ConfigParser()
        self.__conf.read(config_path, encoding='utf-8')
    def read_ini(self,sec,option):
        return self.__conf.get(sec,option)

    @property
    def get_zentao_url(self):
        value = self.read_ini('zentao', 'zentao_url')
        return value
    @property
    def get_username(self):
        value = self.read_ini('user', 'user_name')
        return value
    @property
    def get_password(self):
        value = self.read_ini('user', 'password')
        return value


conf = ConfigUtils()

if __name__ == '__main__':
    zantao_url = conf.get_zentao_url
    user_name = conf.get_username
    password = conf.get_password
    print(zantao_url, user_name, password)