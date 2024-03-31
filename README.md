# Systeme-Expert
Introduction : 

Ce rapport documente le processus de conception et de développement d'un système expert destiné à aider au diagnostic des pannes d'un ordinateur personnel (PC). L'objectif principal était de créer un système capable d'identifier les défaillances matérielles en se basant sur les symptômes observés par l'utilisateur. 

 Système expert Un système expert (SE)  

est un outil capable de reproduire les mécanismes cognitifs d'un expert, dans un domaine particulier. Un système expert est un logiciel capable de répondre à des questions, en effectuant un raisonnement à partir de faits et de règles connus. Il peut servir notamment comme outil d'aide à la décision 

1-Choix de la Présentation des Connaissances 

Pour représenter les connaissances nécessaires au diagnostic des pannes d'un PC, nous avons opté pour une approche basée sur des règles. Les règles sont des déclarations logiques qui relient les symptômes aux organes potentiellement défectueux de l'ordinateur. Par exemple, une règle pourrait indiquer que si l'ordinateur ne démarre pas du tout et que l'utilisateur entend des bips au démarrage, il pourrait y avoir un problème avec la carte mère ou la RAM. ceci est représenteé à travers un fichier base.txt sous la forme de : 

“Symptôme : organe en panne “ .
2-Type de Raisonnement et Stratégie Utilisée 

Nous avons choisi d'implémenter un raisonnement à chaînage avant pour notre système expert. Le chaînage avant commence par les faits initiaux fournis par l'utilisateur, puis parcourt les règles pour déduire de nouveaux faits jusqu'à ce qu'une conclusion soit atteinte. Cette stratégie est efficace pour diagnostiquer les pannes en se basant sur les symptômes observés. 

3-Conception 

L'application est conçue avec une interface utilisateur conviviale grâce à Tkinter. Elle est divisée en plusieurs parties principales : 

    Authentification : Permet à l'expert de se connecter à l'application en saisissant un nom d'utilisateur et un mot de passe. 

    Interface Expert : Fournit à l'expert des fonctionnalités avancées pour gérer les règles de diagnostic et consulter les symptômes utilisateur. 

    Interface Utilisateur : Permet aux utilisateurs de signaler des symptômes et d'obtenir un diagnostic automatique. 

 

  Pannes Détaillées d'un Micro-ordinateur 

La base de connaissances du système comprend une variété de pannes potentielles, telles que des problèmes de démarrage, des écrans bleus de la mort, des erreurs de RAM, des pannes de disque dur, etc. Chaque panne est associée à une série de symptômes caractéristiques et à des organes matériels possibles impliqués 

Réalisation : 

Outils Utilisés 

    Python : Le langage de programmation principal utilisé pour développer l'application. 

    Tkinter : Une bibliothèque Python pour créer des interfaces graphiques utilisateur (GUI). 

    Fichiers texte : Utilisés pour stocker les règles de diagnostic et les symptômes signalés par les utilisateurs. 

    Messagebox de Tkinter : Pour afficher des messages d'erreur, d'avertissement et d'information à l'utilisateur. 

Fonctionnalités Principales 

    Authentification Expert : Permet à l'expert de se connecter à l'application pour gérer les règles de diagnostic. 

    Diagnostic Automatique : Analyse les symptômes signalés par l'utilisateur et propose des organes matériels potentiels en panne. 

    Gestion des Règles de Diagnostic : Permet à l'expert d'ajouter, de supprimer et de modifier les règles de diagnostic à partir de l'interface graphique. 

    Gestion des Symptômes Utilisateur : Permet à l'expert de consulter les symptômes signalés par les utilisateurs et d'associer des organes matériels aux symptômes. 
