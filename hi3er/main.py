from os import getenv
from discord import Intents, Client, Message, Embed,DMChannel
from dotenv import load_dotenv
from db import db_helper
from model import Valk

 
db_client = db_helper()

intents: Intents =Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_msg(message: Message, user_msg: str) -> None:
    if not user_msg:
        print('empty msg')
        return
    if user_msg.lower() == 'faq':
        valks: list[Valk] = db_client.get_all_valks()
        embed = embed_card('All Valks')
        valk_names = ''
        acronyms = ''
        print(valks)
        for valk in valks:
            valk_names += f"{valk.name}\n"
            acronyms += f"{valk.acronym}\n"
        embed.add_field(name='Names',value=valk_names)
        embed.add_field(name='Acronym',value=acronyms)

        await message.channel.send(embed=embed)
    if user_msg.lower() in db_client.ACRONYM:
        valk: Valk = db_client.get_valk_by_acronym(user_msg.lower())
        embed = embed_card(valk.name,valk.color_hex,valk.image)
        
        
        keys = []
        for signet in valk.build:
            if not signet.category in keys:

                embed.add_field(name=signet.category,value='')
                keys.append(signet.category)
        
        for signet in valk.build:
            for embed_field_index in range(len(embed.fields)):
                if(embed.fields[embed_field_index].name == signet.category):
                    new_embed = embed.fields[embed_field_index].value + '\n' + signet.name
                    embed.set_field_at(embed_field_index,name=embed.fields[embed_field_index].name,value= new_embed)
                    
        await message.channel.send(embed=embed)
        
def embed_card(title:str,color_hex=0xEB459F,thumbnail = 'https://cdn.discordapp.com/attachments/1224297288730542100/1224327874278850623/Miracle__Magical_Girl_Chibi.png?ex=661d1730&is=660aa230&hm=86ed08d3c5cc8daca36ecdcd0e528ad7aab163ea78c093c7deb3893455131f6b&'):
    embed = Embed(
        colour=color_hex,
    )
    embed.set_author(name='SyBlue',url='https://discord.gg/ajsXYDf9')
    embed.title = title
    embed.set_thumbnail(url=thumbnail)
    return embed


@client.event
async def on_ready() -> None :
    print(f'{client.user} is now running')
    
    
@client.event
async def on_message(message:Message) -> None :
    if message.author == client.user:
        return
    if isinstance(message.channel, DMChannel):
        return
    if message.channel.name != 'hi3er':
        return
    await send_msg(message,str(message.content))
    
def main() -> None:
    load_dotenv()
    client.run(token=getenv('DISCORD_TOKEN'))
    
if __name__ == '__main__':
    main()