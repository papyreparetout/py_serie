# py_serie

Programmes python qt pour interface liaison série

Deux programmes l'un pour lire les données reçues l'autre pour envoyer des données sur une liaison série. L'interface Qt permet de choisir parmi les liaisons actives et la vitesse de transmission ainsi que le choix du fichier de données à envoyer.
Une fenêtre récupère les messages de suivi.

Les 2 programme "dialog_serie" utilisent qtserial et sont donc plus efficaces pour un dialogue avec le port série. Les choix de paramètrage de la liaison sont plus étendus. Le "dialog_serie_line" est dédié au dialogue sous forme de lignes terminée par un caratère, l'autre est plus dédié à un dialogue brut. Dans les 2 cas les échanges sont sauvegardés pour traitement ultérieur dans un fichier.

En complément 1 programme permettant de lister les ports disponibles sur 1 ordinateur
