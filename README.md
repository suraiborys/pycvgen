# Developer CV - Minimalistic SSG

A minimalistic CV generator for developers with light/dark theme support and English/Ukrainian localization.

## Translations

```aiignore
pybabel extract -F babel-mapping.ini -o locale/messages.pot ./
pybabel init -d locale -l en -i locale/messages.pot
pybabel init -d locale -l uk -i locale/messages.pot
pybabel update -i locale/messages.pot -d locale
pybabel compile -d locale -l en
pybabel compile -d locale -l uk
```


## License

Copyleft - Feel free to use and modify as needed.
