import xlrd
from common.config_value import ConfigUtils

conf = ConfigUtils()
workbook = xlrd.open_workbook(conf.get_elements_url)
sheet = workbook.sheet_by_name('MainPage')

elements_info={}
for i in range(1,sheet.nrows):
    element_info = {}
    element_info['element_name']=sheet.cell_value(i,1)
    element_info['locator_type']=sheet.cell_value(i,2)
    element_info['locator_value']=sheet.cell_value(i,3)
    element_info['timeout']=int(sheet.cell_value(i,4))
    elements_info[sheet.cell_value(i,0)]=element_info
print(elements_info)
