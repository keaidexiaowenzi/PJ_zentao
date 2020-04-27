import os
import xlrd
from common.config_value import ConfigUtils
import xlrd

conf = ConfigUtils()
elements_path=conf.get_elements_url

class ElementExcelData:
    def __init__(self, sheet_name, element_path=elements_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(self.element_path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)
        self.row_count = self.sheet.nrows

    def get_element_info(self):
        elements_info={}
        for i in range(1, self.row_count):
            element_info = {}
            element_info['element_name'] = self.sheet.cell_value(i, 1)
            element_info['locator_type'] = self.sheet.cell_value(i, 2)
            element_info['locator_value'] = self.sheet.cell_value(i, 3)
            element_info['timeout'] = int(self.sheet.cell_value(i, 4))
            elements_info[self.sheet.cell_value(i, 0)] = element_info
        return elements_info


def get_page_info(sheet_name):
    element_data = ElementExcelData(sheet_name)
    elements = element_data.get_element_info()
    return elements


if __name__ == '__main__':
    # print(get_page_info('login_page'))
    print(__name__)