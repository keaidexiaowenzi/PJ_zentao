import yaml
from common.config_value import ConfigUtils

conf = ConfigUtils()
elements_yaml_url=conf.get_elements_yaml_url

class ElementYamlData:
    def __init__(self, sheet_name, element_path=elements_yaml_url):
        self.sheet_name =sheet_name
        # 打开yaml文件
        self.file = open(element_path, 'r', encoding='utf-8')
        # 读出yaml文件全部内容
        self.yaml_content = self.file.read()

    def read_yaml(self):
        yaml_list = yaml.load(self.yaml_content,Loader=yaml.FullLoader)
        elements = yaml_list[self.sheet_name]
        return elements


if __name__ == '__main__':
    element_infos = ElementYamlData('login_page')
    element_infos.read_yaml()
    print(element_infos)