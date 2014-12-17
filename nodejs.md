# Nodejs

# Windows 

## Problème lors de la configuration 

L'erreur suivante apparait :

`npm config set proxy http://127.0.0.1:3168`
`Error: ENOENT, stat 'C:\Users\PACE07711\AppData\Roaming\npm'`

La solution est la création du répertoire `C:\Users\PACE07711\AppData\Roaming\npm`

### Modules installés globalement

Ces modules installés avec l'option -g : `npm install -g module_name`
sont stockés dans le répertoire `C:\Users\PACE07711\AppData\Roaming\npm\node_modules`
