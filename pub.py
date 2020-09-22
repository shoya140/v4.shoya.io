import os
import json
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

with open('./reference.bib') as f:
    bdata = bibtexparser.load(f)

for entry in bdata.entries:
    output = ''
    key =  entry['ID']
    authors_data = entry['author'].split(' and ')
    for i, author in enumerate(authors_data):
        name = ' '.join(reversed([n.strip() for n in author.split(',')]))
        if i == 0:
            output = name
        elif i == len(authors_data) - 1:
            output += ' and ' + name
        else:
            output += ', ' + name
    output += '. <b>&#147;<a href="#' + key + '" class="anchor-title">' + entry['title'] + '</a>&#148;</b>. '

    if 'journal' in entry.keys():
        output += ' ' + entry['journal'] + ', '
        if 'volume' in entry.keys() and 'number' in entry.keys():
            output += entry['volume'] + ' (' + entry['number'] + '), '

    if 'booktitle' in entry.keys():
        output += 'In ' + entry['booktitle']
        if 'series' in entry.keys():
            output += ' (' + entry['series'] + '), '
        else:
            output += ', '
    if 'pages' in entry.keys():
        pages = entry['pages']
        if '--' in pages:
            prefix = 'pp.&nbsp;'
        else:
            prefix = 'p.&nbsp;'
        output += prefix + entry['pages'] + ', '
    output += entry['year'] + '.'

    if 'to appear' not in output:
        output += ' <a href="/bibtex/' + key + '.bib" target="_blank">BibTeX</a>'
    if os.path.exists('./static/preprint/' + key + '.pdf'):
        output += ' <a href="/preprint/' + key + '.pdf" target="_blank">PDF</a>'

    output = output.replace('{\\ss}', '&szlig;')
    output = output.replace('{\\"O}', '&Ouml;')
    output = output.replace('{\\&}', '&amp;')
    output = output.replace('--', '&ndash;')
    output = output.replace('Shoya Ishimaru', '<u>Shoya Ishimaru</u>')
    output = '<p><span class="anchor-position" id="' + key + '"></span>' + output + '</p>'

    with open('./layouts/partials/publications/' + key + '.html', "w") as f:
        f.write(output)

    bout = BibDatabase()
    bout.entries = [entry]
    with open('./static/bibtex/' + key + '.bib', 'w') as f:
        f.write(BibTexWriter().write(bout))
