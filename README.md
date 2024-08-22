# Surveillance Automatisée d'Adresses Solana avec Télégram

Ce script permet de surveiller une adresse Solana permanente, d'identifier les transactions effectuées depuis cette adresse, et de suivre les adresses de réception pour détecter d'autres transactions. Lorsque trois transactions successives sont détectées, et que la dernière transaction concerne un token sur [pump.fun](https://pump.fun), le script va automatiquement investir sur ce token et le revendre à un profit de 20%. Après cette opération, le script revient à la surveillance de l'adresse permanente initiale.

⚠️ **Attention :** Ce script est hautement personnalisé pour un comportement spécifique lié à un "serial-rugger". Il est recommandé de l'utiliser à des fins éducatives ou de l'adapter à vos propres besoins.

## Fonctionnalités du Script

1. **Surveillance de la première adresse Solana permanente** : Le script commence par surveiller une adresse définie.
2. **Surveillance des transactions** : Lorsqu'une transaction est détectée, le script commence à surveiller l'adresse de réception.
3. **Investissement automatique** : Lorsqu'une transaction sur un token spécifique est détectée sur [pump.fun](https://pump.fun), le script investit automatiquement et revend à 20% de profit.
4. **Retour à l'adresse permanente** : Après l'investissement, le script retourne à la surveillance de l'adresse permanente.

## Prérequis

### Installation de Python et des Librairies

1. **Installation de Python** :
    - Téléchargez et installez Python depuis [python.org](https://www.python.org/downloads/).

2. **Installation des librairies nécessaires** :
    - Une fois Python installé, ouvrez un terminal ou une invite de commande, puis exécutez la commande suivante pour installer la librairie `telethon` :

    ```bash
    pip install telethon
    ```

### Configuration du Script

1. **Obtenir l'API Telegram** :
    - Vous devez avoir un compte Telegram et obtenir un `api_id` et un `api_hash`. Pour cela, créez une application sur le [site des développeurs de Telegram](https://my.telegram.org/auth).

2. **Modifier le Script** :
    - Ouvrez le script dans un éditeur de texte.
    - Modifiez les variables suivantes :
        - `api_id` : Remplacez-le par l'API ID que vous avez obtenu.
        - `api_hash` : Remplacez-le par l'API Hash que vous avez obtenu.
        - `phone_number` : Remplacez-le par le numéro de téléphone associé à votre compte Telegram.
        - `maestro_username` : Remplacez-le par le nom d'utilisateur Telegram qui doit recevoir les notifications.
        - `target_user` : Remplacez-le par le nom d'utilisateur du bot Telegram que vous surveillez.

## Exécution du Script

1. **Lancer le Script** :
    - Pour exécuter le script, utilisez la commande suivante dans votre terminal ou invite de commande :

    ```bash
    python nom_du_script.py
    ```

    - Remplacez `nom_du_script.py` par le nom de votre fichier script.

2. **Fonctionnement** :
    - Le script commencera par ajouter l'adresse Solana permanente.
    - Il surveillera ensuite les transactions successives et effectuera les actions nécessaires.
    - Si le script détecte une transaction  sur [pump.fun](https://pump.fun), il investira automatiquement et vendra lorsque le profit atteint 20%.
    - Le script reviendra ensuite à la surveillance de l'adresse Solana permanente.

## Vidéo Démonstrative

Pour voir une démonstration du script en action, consultez cette vidéo : [Démonstration Vidéo](https://x.com/i/status/1826342930421788883)

---

## Remarque

Ce script est conçu pour un cas d'utilisation très spécifique et peut nécessiter des ajustements pour être utilisé dans d'autres contextes. Assurez-vous de bien comprendre son fonctionnement avant de l'utiliser en production.
