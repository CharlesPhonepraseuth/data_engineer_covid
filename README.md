# Data Engineer Covid

- Copiez le fichier `.env.example`, renommez le `.env` et ajoutez les valeurs

Le projet est relativement lourd. Pour pouvoir l'utiliser convenablement sauf si votre machine a assez de ressource, il faudra lancer les conteneurs dans un ordre précis.

- Pour lancer le projet, placez-vous sur la racine du projet et exécutez les commandes suivantes :
  - `./setup.sh build`
  - `./setup.sh init-es` : attendre que les conteneurs `es-init-indexer` et `es-init-seeder` s'achèvent par un `exited with code 0`
  - `./setup.sh init-pg` : attendre que le conteneur `pg-init-seeder` s'achève par un `exited with code 0`
  - `./setup.sh airflow`
  - `./setup.sh app`

## Arrêt du projet

- Pour arrêter le projet, placez-vous sur la racine du projet et exécutez la commande `./clear.sh`

`Attention ! La commande va supprimer tous les containers, images et volumes en cours`

## Configuration de pgAdmin

- Connectez-vous sur le port `5050`
- Clic droit sur Servers > Register > Server...
- General > Name : `de_project`
- Connection > Host name/ address : `pg_container`
- Connection > Username : la valeur de votre variable d'environnement `POSTGRES_USER`
- Connection > Password : la valeur de votre variable d'environnement `POSTGRES_PASSWORD`
- Save

## Accéder à Kibana

- Connectez-vous sur le port `5601`

## Accéder à Airflow

- Connectez-vous sur le port `8080`

## Accéder au dashboard

- Connectez-vous sur le port `8050`

## Accéder à Jupyter Notebook

- Connectez-vous sur le port `8888`
- Rajoutez la Query string token dans l'url, l'information se trouve dans le terminal à la fin du lancement de Jupyter Notebook (ex: host:8888/?token=[TOKEN])

## Accéder à Fastapi

- Connectez-vous sur le port `8000/docs`
