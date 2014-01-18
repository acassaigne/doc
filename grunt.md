# Grunt

## Installation de grunt

La commande à utiliser est :

    npm install -g grunt-cli

## Comment çà marche

### initier un projet avec npm

npm doit avoir un fichier `package.json` décrivant le projet. 
Pour créer ce fichier utiliser la commande  `npm init`.

Pour initier un projet, il suffit donc de taper ces commandes 
```shell
mkdir mon_projet
cd mon_projet
npm init
npm install grunt --save-dev
```

La derniere commande permet d'installer grunt localement.

### gruntifier votre projet
Les tâches et la configuration de grunt est défini dans le fichier `Gruntfile.js`
Ce fichier permet de définir les pluging, les tâches etc...

On peut par exemple définir deux tâches extrement simple 
```javascript
module.exports = function(grunt) {

  // A very basic default task.
  grunt.registerTask('default', 'Log some stuff.', function() {
    grunt.log.write('Logging some stuff...').ok();
  });

  grunt.registerTask('anthony', 'Log some stuff.', function() {
    grunt.log.write('Hello Anthony...').ok();
  });

};
```

### copier des fichiers avec grunt

Installer le module `grunt-contrib-copy` via la commande 
    
    npm install grunt-contrib-copy --save-dev

Ensuite ajouter dans Gruntfile.js `grunt.loadNpmTasks('grunt-contrib-copy');` et
définir les tâches de copie 

```javascript
grunt.initConfig({
    copy: {
      main: {
        src: 'source/*.txt',
        dest: 'dest/',
        filter: 'isFile',
        flatten: true,
        expand: true
      }
    }
  });
```

Pour plus d'informations voir ici [grunt-contrib-copy](https://github.com/gruntjs/grunt-contrib-copy) 

### Déployer via ssh

Pour déployer via ssh il convient d'utiliser : https://github.com/andrewrjones/grunt-ssh
Pour lancer une commande shell voir `grunt.util.spawn`, 
inspiré par [stackoverflow](http://stackoverflow.com/questions/10456865/running-a-command-in-a-grunt-task)
```javascript
grunt.util.spawn({
  cmd: ['rm'],
  args: ['-rf', '/tmp'],
}, function done() {
  grunt.log.ok('/tmp deleted');
});
```
Ou utiliser le package [grunt-shell](https://github.com/sindresorhus/grunt-shell) 

### Utiliser des commandes shell via grunt-shell

Exemple de grunt-shell 
Ajouter la ligne `grunt.loadNpmTasks('grunt-shell');` à votre fichier Gruntfile.js
un exemple de configuration 
```javascript
 shell: {                                // Task
        dir: {                        // Target
            options: {                        // Options
                stdout: true,
                failOnError: true,
                execOptions: {
                  cwd: '../doxc/autre'
                }
            },
            command: 'dir'
        }
      }
```

http://devomato.com/blog/blog-assembling/
http://handlebarsjs.com/