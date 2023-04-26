import discord
import responses
import way

# way code
done =False
last_q = []
async def controlle(message,username,check=[]):
        global last_q,done
        if done:
                await message.author.send("you done should try `!filier` or `!restart`")
                return
        if check != []:
                await way.stock(username,check)
        if await way.last_question():
                r = responses.get_response("!filier",str(message.author))
                m = f"Merci d'avoir utilisé notre chatbot d'orientation ! En fonction de vos réponses, nous avons identifié l\'option de carrière suivante qui correspond à vos intérêts,{r}. Nous vous encourageons à explorer cette option pour en savoir plus sur elle, et à consulter des professionnels pour obtenir des conseils sur la façon de poursuivre cette carrière. Nous espérons que cette expérience vous a été utile et vous a aidé à explorer de nouvelles idées pour votre avenir professionnel."
                await message.author.send(m)
                done = True
                return
        q_info =await way.get_info()
        q_s = q_info[0]
        for i in range(len(list(q_info[1][1]))):
                q_s += f"\n   {i+1}-{list(q_info[1][1])[i]}"
        if await way.fetch_q_num() == 0:
                q_s += "\nSélectionnez vos réponses parmi les choix ci-dessus.\n`Example:1`\nVous pouvez sélectionner plusieurs choix seulement pour certaines questions.\n`Example:1,3,5`"
        await message.author.send(q_s)
        last_q = [username,[i for i in range(len(list(q_info[1][1])))]]
# ___________

async def send_message(message,user_message,is_private):
        try:
                response = responses.get_response(user_message,str(message.author))
                await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:    
                print(e)

def run_discord_bot():
        global done
        
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
                try: 
                        s_m = user_message.split(',')
                        check = []
                        for nb in s_m:
                                if int(nb)-1 in last_q[1]:
                                        check.append(int(nb)-1)
                        if len(check) != 0:
                                await controlle(message,username,check)
                                return 
                except :pass
                if user_message[0] not in ['!','?']:
                        return
                
                print(f"{username} siad:{user_message} ({channel})")
                
                if user_message == "!start" or user_message == "!restart":
                        done = False
                        await way.stock_name(username)
                        await way.r_q_num()
                        await controlle(message,username)
                        return
                if user_message[0] == '?':
                        user_message = user_message[1:]
                        await send_message(message,user_message,True)
                else:
                        await send_message(message,user_message,False)
        
        
        client.run(TOKEN)

                
