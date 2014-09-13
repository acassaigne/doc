title: Docker
category: Docker
date: 2014-09-13
modified: 2014-09-13
tags: Docker, Virtualisation


# Docker

## Utilisateur lambda & Docker

Si vous avez l'erreur suivante 

    :::bash
    docker ps
    2014/09/13 18:03:21 Get http:///var/run/docker.sock/v1.14/containers/json: dial unix /var/run/docker.sock: permission denied

C'est probablement que vous n'appartenez au groupe unix : docker

pour cela utiliser la commande suivante 

    :::bash
    sudo usermod -a -G docker my_user

Vérifier avec la commande groups apres vous être un logout et login.
Après vous être "re-logger" vous devriez récuperer le groupe docker.
