import xlsxwriter

def dump_to_xlsx(filename, data):
     if not len(data):
         return None

     with xlsxwriter.Workbook(filename) as workbook:
         ws = workbook.add_worksheet()
         bold = workbook.add_format({'bold': True})

         headers = ['Название товара', 'Цена', 'Ссылка']
         headers.extend(data[0]['techs'].keys())

         for col, h in enumerate(headers):
             ws.write_string(0, col, h, cell_format=bold)

         for row, item in enumerate(data, start=1):
             ws.write_string(row, 0, item['name'])
             ws.write_string(row, 1, item['amount'])
             ws.write_string(row, 2, item['url'])
             for prop_name, prop_value in item['techs'].items():
                 col = headers.index(prop_name)
                 ws.write_string(row, col, prop_value)
