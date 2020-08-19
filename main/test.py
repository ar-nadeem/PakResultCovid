import requests



content = ""

table_start_index = content.find('<table class="wikitable')
table_end_index = content.find("= all cases have had an outcome (there are no active cases)</div></div>")

print(table_start_index)
print(table_end_index)
#print(content)

global_table = content[table_start_index:table_end_index + 69]