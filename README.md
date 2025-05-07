# Developer CV - Minimalistic SSG

## About
A minimalistic online CV generator with light/dark theme support and English/Ukrainian localization.

## Executing commands

- Install [Taskfile](https://taskfile.dev/)
```aiignore
task --list # List all available tasks
```

## Translations

```aiignore
pybabel extract -F babel-mapping.ini -o locale/messages.pot ./
pybabel init -d locale -l en -i locale/messages.pot
pybabel init -d locale -l uk -i locale/messages.pot
pybabel update -i locale/messages.pot -d locale
pybabel compile -d locale -l en
pybabel compile -d locale -l uk
```

## Nginx && ufw rules
```aiignore
sudo ufw allow ssh
sudo ufw app list
sudo ufw allow 'Nginx HTTP'
sudo ufw enable
sudo ufw status
sudo ufw status numbered
sudo ufw delete [1, 2, 3, 4]
curl -4 icanhazip.com
```


## License

Copyleft - Feel free to use and modify as needed.
