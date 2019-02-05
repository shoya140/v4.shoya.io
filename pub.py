import bibtexparser
import json

with open('./reference.bib') as f:
    bdata = bibtexparser.load(f)

for entry in bdata.entries:
    output = ''
    authors_data = entry['author'].split('and')
    for i, author in enumerate(authors_data):
        name = ' '.join(reversed([n.strip() for n in author.split(',')]))
        if name == 'Shoya Ishimaru':
            name = '<u>' + name + '</u>'
        if i == 0:
            output = name
        elif i == len(authors_data) - 1:
            output += ' and ' + name + '. '
        else:
            output += ', ' + name
    output += '<b>&#147;' + entry['title'] + '&#148;</b>. '

    if 'journal' in entry.keys():
        output += ' ' + entry['journal'] + ', '
    if 'booktitle' in entry.keys():
        output += 'In ' + entry['booktitle'] + ', '
    if 'pages' in entry.keys():
        pages = entry['pages']
        if '--' in pages:
            prefix = 'pp.&nbsp;'
        else:
            prefix = 'p.&nbsp;'
        output += prefix + entry['pages'] + ', '
    output += entry['year']
    output = output.replace('{\\ss}', '&szlig;')
    output = output.replace('{\\"O}', '&Ouml;')
    output = output.replace('Dayan Herurkar, a', 'Dayananda Herurkar')
    output = output.replace('--', '&ndash;')
    output = '<p>' + output + '.</p>'

    with open('./layouts/partials/publications/' + entry['ID'] + '.html', "w") as f:
        f.write(output)
