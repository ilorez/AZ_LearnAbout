import discord
import responses
from oriente_filier import OrieteF

UOFObj = {} # users oriente filier objs ==> for users that want try our oriete bot
async def controlle(message,username,check=[]):
        if UOFObj[f"{username}"].done():
                await message.author.send("Done should try:\n`!filier`:recommanded filier\n`!restart`:restart questions")
                return
        if check != []:
                UOFObj[f"{username}"].stock(username,check)
        if UOFObj[f"{username}"].done():
                r = responses.get_response("!filier",str(message.author))
                m = f"Merci d'avoir utilisé notre chatbot d'orientation ! En fonction de vos réponses, nous avons identifié l\'option de carrière suivante qui correspond à vos intérêts,{r}. Nous vous encourageons à explorer cette option pour en savoir plus sur elle, et à consulter des professionnels pour obtenir des conseils sur la façon de poursuivre cette carrière. Nous espérons que cette expérience vous a été utile et vous a aidé à explorer de nouvelles idées pour votre avenir professionnel."
                await message.author.send(m)
                return
        q_c = UOFObj[f"{username}"].get_q_c()
        await message.author.send(q_c)

async def send_message(message,user_message,is_private):
        try:
                response = responses.get_response(user_message,str(message.author))
                await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:    
                print(e)

def run_discord_bot():
        global UOFObj
        with open(".token.txt", 'r', encoding='utf8') as token:
                TOKEN = token.readline()
        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
                print(f"{client.user} is now running")
        
        @client.event
        async def on_member_join(member):
                await member.send("Hi there")
                
        @client.event
        async def on_message(message):
                if message.author == client.user:
                        return 
                username = str(message.author)
                user_message = str(message.content)
                channel = str(message.channel)
                if user_message[0] in ['1','2','3','4','5','6','7','8','9']:
                        try: 
                                s_m = user_message.split(',')
                                check = []
                                for nb in s_m:
                                        check.append(int(nb)-1)
                                await controlle(message,username,check)
                        except :pass
                if user_message[0] not in ['!','?']:
                        return
                
                print(f"{username} siad:{user_message} ({channel})")
                
                if user_message in ["!start","!restart"]:
                        UOFObj[f"{username}"] = OrieteF(f"{username}")
                        await controlle(message,username)
                        return
                if user_message[0] == '?':
                        user_message = user_message[1:]
                        await send_message(message,user_message,True)
                else:
                        await send_message(message,user_message,False)
        
        
        client.run(TOKEN)

                
