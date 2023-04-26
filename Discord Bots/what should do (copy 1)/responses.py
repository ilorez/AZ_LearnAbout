import json
import os
def get_response(u_message:str,username:str) -> str:
    p_message = u_message.lower()

    match p_message:
        case '!way':
            return "Bienvenue sur notre chatbot d'orientation ! Pour commencer, veuillez répondre aux questions suivantes pour nous aider à mieux comprendre vos intérêts, vos compétences et vos motivations. Nous utiliserons ces informations pour vous suggérer des options de carrière qui correspondent à votre personnalité. Nous vous remercions d'avance pour votre participation ! \nSi vous êtes prêt, écrivez `!start`"
        case '!help':
            return "`!way` : notre chatbot d'orientation\n`!filier` : vos compétences et vos motivations\n`!ping` : test_server (should return \'pong\')\n`!remove` : Supprimez vos fichiers de nos données"
        case '!ping':
            return "pong :)"
        case '!remove':
            try:
                os.remove(f'./data/{username}.json')
                return 'removing Done'
            except:
                return "Aucun fichier n'a été trouvé."
        case '!filier':
            try:
                tab = ["Devellopement Digital","Infrascracture digital","Marketing Digital","Design"]
                print(username)
                with open(f'./data/{username}.json','r',encoding='UTF-8') as f:
                    data = json.load(f)
                t = [0 for i in range(4)]
                for k in data:
                    for kk in data[k]:
                        for i in range(len(data[k][kk])):
                            t[i] += data[k][kk][i]
                    
                return f"vos compétences et vos motivations: `{tab[t.index(max(t))]}`"
            except:
                return "Vous devez d\'abord répondre à quelques questions pour obtenir votre filière. Essayez !way."

    
    return 'We don\'t know what exactly you need try `!help`'
