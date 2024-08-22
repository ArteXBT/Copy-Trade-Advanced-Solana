import asyncio
from telethon.sync import TelegramClient
import time

# Configuration avec vos informations
# Remplacez les valeurs ci-dessous par vos informations personnelles
api_id = 'VOTRE_API_ID_ICI'
api_hash = 'VOTRE_API_HASH_ICI'
phone_number = 'VOTRE_NUMERO_DE_TELEPHONE_ICI'
maestro_username = 'NOM_UTILISATEUR_DE_MAESTRO_ICI'  # Nom d'utilisateur de Maestro

# Cible de l'utilisateur
target_user = 'ray_purple_bot'  # Nom d'utilisateur du bot cible

# Créez le client Telegram
client = TelegramClient('session_name', api_id, api_hash)

def extract_solana_address(message_text):
    """
    Extrait l'adresse Solana d'un message textuel.
    On suppose que l'adresse est située entre le dernier '/' et la dernière ')'.
    """
    last_slash_index = message_text.rfind('/')
    closing_paren_index = message_text.rfind(')')
    
    if last_slash_index != -1 and closing_paren_index != -1:
        # Extrait et retourne le segment qui est supposé être l'adresse Solana
        address_segment = message_text[last_slash_index + 1:closing_paren_index].strip()
        return address_segment
    return None

async def main():
    """
    Point d'entrée principal du script.
    Ce script démarre en ajoutant l'adresse Solana permanente (wallet1) 
    et commence à surveiller les messages du bot cible.
    """
    try:
        print("Connexion au client Telegram...")
        await client.start(phone_number)  # Démarre le client avec le numéro de téléphone fourni
        print("Client connecté avec succès!")

        print(f"Résolution de l'entité pour {target_user}...")
        entity = await client.get_entity(target_user)  # Obtient l'entité correspondant au bot cible
        print(f"Entité résolue : {entity.id}")

        # Étape 1 : Ajouter le wallet1 permanent
        wallet1 = "ADRESSE_WALLET_1_ICI"  # Remplacez cette adresse par l'adresse Solana permanente
        print(f"Ajout du portefeuille : {wallet1}")
        await client.send_message(entity, f"/add {wallet1}")  # Envoie la commande d'ajout au bot

        # Commencez la surveillance des messages
        await monitor_messages(entity, wallet1)

    except Exception as e:
        # Capture les erreurs et les affiche
        print(f"Une erreur inattendue s'est produite : {e}")

async def monitor_messages(entity, wallet1):
    """
    Surveille les messages du bot cible pour détecter une nouvelle adresse Solana.
    Si aucune activité n'est détectée pendant 3 heures, le script réinitialise et revient au début.
    """
    print("Surveillance des messages pour une nouvelle adresse Solana...")
    start_time = time.time()  # Enregistre l'heure de début pour le suivi du temps écoulé
    
    while True:
        await asyncio.sleep(2)  # Pause de 2 secondes entre chaque vérification de message
        elapsed_time = time.time() - start_time
        
        if elapsed_time > 10800:  # 3 heures (10800 secondes)
            print("Aucune activité détectée pendant 3 heures. Réinitialisation.")
            await client.send_message(entity, f"/delete {wallet1}")  # Supprime le wallet1
            await main()  # Retour au début du script
            return

        # Récupère le dernier message envoyé par le bot
        new_message = await client.get_messages(entity, limit=1)
        message = new_message[0]

        if message:
            # Extrait l'adresse Solana du message
            wallet2 = extract_solana_address(message.text)
            if wallet2:
                print(f"Adresse Solana détectée : {wallet2}")

                # Suppression de wallet1
                print(f"Suppression du portefeuille initial : {wallet1}")
                await client.send_message(entity, f"/delete {wallet1}")
                
                # Mise à jour de wallet1 avec wallet2
                wallet1 = wallet2  

                # Ajout de wallet2
                print(f"Ajout du nouveau portefeuille : {wallet2}")
                await client.send_message(entity, f"/add {wallet2}")

                # Surveiller les messages après avoir ajouté le wallet2
                await monitor_second_wallet(entity, wallet2)

async def monitor_second_wallet(entity, wallet2):
    """
    Surveille les messages pour une nouvelle adresse Solana après l'ajout du deuxième wallet.
    Si aucune activité n'est détectée pendant 3 heures, le script réinitialise et revient au début.
    """
    print("Surveillance du deuxième message pour une nouvelle adresse Solana...")
    start_time = time.time()  # Enregistre l'heure de début pour le suivi du temps écoulé
    
    while True:
        await asyncio.sleep(2)  # Pause de 2 secondes entre chaque vérification de message
        elapsed_time = time.time() - start_time
        
        if elapsed_time > 10800:  # 3 heures (10800 secondes)
            print("Aucune activité détectée pendant 3 heures. Réinitialisation.")
            await client.send_message(entity, f"/delete {wallet2}")  # Supprime le wallet2
            await main()  # Retour au début du script
            return

        # Récupère le dernier message envoyé par le bot
        new_message = await client.get_messages(entity, limit=1)
        message = new_message[0]

        if message:
            # Extrait l'adresse Solana du message
            wallet3 = extract_solana_address(message.text)
            if wallet3:
                print(f"Nouvelle adresse Solana détectée : {wallet3}")
                
                # Suppression directe de wallet2
                print(f"Suppression du portefeuille : {wallet2}")
                await client.send_message(entity, f"/delete {wallet2}")

                # Ajout du wallet3
                print(f"Ajout du portefeuille : {wallet3}")
                await client.send_message(entity, f"/add {wallet3}")

                # Surveiller le wallet3
                await monitor_third_wallet(entity, wallet3)

async def monitor_third_wallet(entity, wallet3):
    """
    Surveille les messages pour détecter une adresse Solana finale associée au wallet3.
    Envoie l'adresse finale détectée à l'utilisateur Maestro, puis revient au début du script.
    """
    print("Surveillance du troisième message pour une adresse Solana finale...")
    start_time = time.time()  # Enregistre l'heure de début pour le suivi du temps écoulé
    
    while True:
        await asyncio.sleep(2)  # Pause de 2 secondes entre chaque vérification de message
        elapsed_time = time.time() - start_time
        
        if elapsed_time > 10800:  # 3 heures (10800 secondes)
            print("Aucune activité détectée pendant 3 heures. Réinitialisation.")
            await client.send_message(entity, f"/delete {wallet3}")  # Supprime le wallet3
            await main()  # Retour au début du script
            return

        # Récupère le dernier message envoyé par le bot
        new_message = await client.get_messages(entity, limit=1)
        message = new_message[0]

        if message:
            # Extrait l'adresse Solana finale du message
            final_address = extract_solana_address(message.text)
            if final_address:
                print(f"Adresse Solana finale détectée : {final_address}")
                
                # Envoi de l'adresse Solana détectée à l'utilisateur Maestro
                print(f"Envoi de l'adresse à Maestro : {final_address}")
                maestro_entity = await client.get_entity(maestro_username)
                await client.send_message(maestro_entity, final_address)

                # Suppression du wallet3 et retour au début du script
                print(f"Suppression du portefeuille : {wallet3}")
                await client.send_message(entity, f"/delete {wallet3}")

                # Réinitialisation en recommençant le script depuis le début
                await main()

with client:
    client.loop.run_until_complete(main())
