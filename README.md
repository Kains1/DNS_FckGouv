# Gestionnaire de DNS Wi-Fi

## Description

Ce script Python permet de gérer les paramètres DNS de votre interface Wi-Fi sous Windows. Il offre une interface graphique (GUI) simple pour configurer les DNS, les réinitialiser en mode automatique ou vérifier les paramètres DNS actuels.

### Fonctionnalités :
- **Configurer DNS** : Configure les DNS pour l'interface Wi-Fi sur les serveurs publics de Google (8.8.8.8 et 8.8.4.4).
- **Réinitialiser DNS** : Réinitialise les paramètres DNS en mode automatique (DHCP).
- **Vérifier les paramètres DNS** : Affiche les paramètres DNS actuels de l'interface Wi-Fi connectée.

## Prérequis
- **Système d'exploitation** : Windows (le script utilise des commandes spécifiques à Windows).
- **Droits administrateur** : Le script nécessite des droits administrateur pour modifier les paramètres DNS.

## Installation
1. Téléchargez l'exécutable à partir de ce [lien](https://github.com/Kains1/DNS_FckGouv).
2. Placez-vous dans le dossier contenant l'exécutable.

## Utilisation
1. **Lancer l'exécutable** :
   
   Double-cliquez sur le fichier `gestionnaire_dns.exe`.

2. Lors de l'exécution, une fenêtre GUI s'ouvre vous permettant de choisir parmi les différentes actions disponibles.

3. Si vous n'avez pas lancé le script avec des privilèges administrateur, celui-ci redémarrera automatiquement avec les droits nécessaires.

### Actions disponibles :
- **Configurer DNS (8.8.8.8 et 8.8.4.4)** : Configure l'interface Wi-Fi pour utiliser les DNS publics de Google.
- **Réinitialiser DNS (mode automatique)** : Réinitialise les paramètres DNS pour utiliser ceux fournis par le DHCP.
- **Vérifier les paramètres DNS** : Affiche les paramètres DNS actuels.

## Notes
- Le script utilise la bibliothèque `ctypes` pour vérifier et élever les privilèges d'administration.
- La bibliothèque `tkinter` est utilisée pour créer l'interface graphique.

## Limitations
- Ce script est conçu pour fonctionner uniquement sous Windows.
- Il nécessite des droits administrateur pour fonctionner correctement.

## Avertissement
L'utilisation de ce script modifie les paramètres réseau de votre ordinateur. Assurez-vous de bien comprendre les actions effectuées avant de les exécuter, en particulier si vous êtes sur un réseau d'entreprise ou un réseau restreint.

## Licence
Ce projet est sous licence GPL-3.0 licence. Voir le fichier LICENSE pour plus de détails.
