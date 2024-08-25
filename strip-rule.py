import execjs
import json
from openpyxl import load_workbook

rule_path = 'rule.json'
rule_strip_path = 'rule-strip.json'

# load pkg defs
strip_list = [ ]
workbook = load_workbook('pkg-info.xlsx')
worksheet = workbook.active
for row in worksheet.iter_rows(min_row=1, max_col=3, values_only=True):
    if row[2] == 1:
        strip_list.append(row[0])

with open(rule_path, 'r', encoding='utf-8') as file:
    rule = execjs.eval(file.read())
    app_list = rule['apps']
    app_list_strip = list(filter(lambda x: x['id'] not in strip_list, app_list))
    rule['apps'] = app_list_strip

    with open(rule_strip_path, 'w', encoding='utf-8') as strip_file:
        json.dump(rule, strip_file, indent=4, ensure_ascii=False)
