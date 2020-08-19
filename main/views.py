from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.
def homepage(request):
    r = requests.get("http://coronavirus.result.pk/")
    content = r.text

    table_start_index = content.find('<table id="corona-table1">')
    table_end_index = content.find("</table>")
    pak_table = content[table_start_index:table_end_index+8]
    pak_table = pak_table.replace('<a','<ass')

    content = content[table_end_index+8:]

    table_start_index = content.find('<table id="corona-table">')
    table_end_index = content.find("</table>")

    global_table = content[table_start_index:table_end_index + 8]
    global_table_first = global_table[:global_table.find('<th colspan="10" style="text-align: left;">')]
    global_table_second = global_table[global_table.find('#FF0">News')+22:]
    global_table = global_table_first + global_table_second
    global_table = global_table.replace('<a', '<ass')

##############
    content = r.text
    global_stats = content[content.find('<h2 style="border: none; font-size: 30px; color: #444;">Total Coronavirus Cases in World</h2>'):]
    global_stats = global_stats[:global_stats.find('<div style="text-align: center; float: left; width: 100%')]

    content = r.text
    pak_stats = content[content.find('<h2 style="border: none; font-size: 25px; color: #444;">'):]
    pak_stats = pak_stats[:pak_stats.find('<div style="text-align: center; float: left; width: 100%; margin-bottom:10px;"')]



    context={
        "global_table": global_table,
        "pak_table": pak_table,
        "global_stats": global_stats,
        "pak_stats": pak_stats,
    }

    return render(request, 'main.html', context)