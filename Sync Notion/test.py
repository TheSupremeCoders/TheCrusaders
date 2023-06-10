import json
# load a json file 'problems_mapped_pages.json'
problems_mapped_pages = json.load(open('problems_mapped_pages.json'))
print(problems_mapped_pages['1'])