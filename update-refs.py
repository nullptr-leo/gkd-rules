import execjs
import json
import os

# update 3rdparty rules
os.system(r'curl -o 3rdparty/AIsouler_gkd.json -L https://registry.npmmirror.com/@aisouler/gkd_subscription/latest/files/dist/AIsouler_gkd.json5')
os.system(r'curl -o 3rdparty/Adpro_gkd.json -L https://registry.npmmirror.com/@adpro/gkd_subscription/latest/files/dist/Adpro_gkd.json5')

# process one by one
for filename in os.listdir('3rdparty'):
    file_path = os.path.join('3rdparty', filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            rule = execjs.eval(file.read())
            output_path = os.path.join('rules', filename)
            with open(output_path, 'w', encoding='utf-8') as norm_file:
                json.dump(rule, norm_file, indent=4, ensure_ascii=False)
