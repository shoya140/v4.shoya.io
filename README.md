# shoya.io

[![Netlify Status](https://api.netlify.com/api/v1/badges/e0486fd4-3525-46ef-9f84-e111ffe3bab5/deploy-status)](https://app.netlify.com/sites/hungry-archimedes-92ccca/deploys)

## dev

```
$ hugo server -D --gc --minify
```

## update publications

1. Update `./reference.bib`

2. Put preprints to `./static/preprint/`

3. Run the script
```
$ python pub.py
>> ./layouts/partials/publications/*
>> and ./static/bibtex/* will be generated
```
