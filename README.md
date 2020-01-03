# shoya.io

[![Netlify Status](https://api.netlify.com/api/v1/badges/e0486fd4-3525-46ef-9f84-e111ffe3bab5/deploy-status)](https://app.netlify.com/sites/hungry-archimedes-92ccca/deploys)

## Set up

1. Download Hugo v0.54.0-extended from [Hugo releases](https://github.com/gohugoio/hugo/releases)

2. Install python package `bibtexparser`

## Update publications

1. Update `./reference.bib`

2. Put preprints into `./static/preprint/`

3. Run the following script
```
$ python pub.py
>> ./layouts/partials/publications/* and ./static/bibtex/* will be generated
```

## Serve the contents

```
$ hugo serve -D
```
