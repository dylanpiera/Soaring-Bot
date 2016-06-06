import discord
from discord import user
import asyncio
import random
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def join(message):
    join_link = message.content.strip('!join')
    print ("This is the join link -- %s" % join_link)
    client.accept_invite(join_link)
    client.send_message(message.channel, "The bot has joined the channel")

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!ping'):
        print("Pinging %s" % message.author)
        await client.send_message(message.channel, 'Pong!')
        print("-----")
    elif message.content.startswith('!pong'):
        print("Pinging %s" % message.author)
        await client.send_message(message.channel, 'Ping!')
        print("-----")

    elif message.content.startswith('!help'):
        print("Attempting to help %s" % message.author)
        server = message.server
        #print (repr(server))
        if server == None:
            await client.send_message(message.author, "A list of commands can be found here:\n!help - Get this message\n!ping - The bot will show his ping\n!create_channel [channel name] - Creates a new channel\n!d [max_dice_roll] - Rolls a dice")
        else:
            await client.send_message(message.channel, "Sending help to you in a PM!")
            await client.start_private_message(message.author)
            await client.send_message(message.author, "A list of commands can be found here:\n!help - Get this message\n!ping - The bot will show his ping\n!create_channel [channel name] - Creates a new channel\n!d [max_dice_roll] - Rolls a dice")
        print("-----")

    elif message.content.startswith('!create_channel'):
        try:
            channel_name = message.content.strip("!create_channel")
            channel_name = channel_name.strip()
            print("Trying to create channel with name -- %s" % channel_name)
            await client.create_channel(message.server, channel_name)
            await client.send_message(message.channel, "Channel \"%s\" has been created" % channel_name)

        except AttributeError:
            await client.send_message(message.channel, "You can't create channels in a PM!")
        except discord.errors.Forbidden:
            await client.send_message(message.channel, "I'm sorry, I don't have permission to do this!")
        except discord.errors.HTTPException:
            await client.send_message(message.channel, "You have to fill in a channel title! !create_channel [name]")
        print("-----")


    elif message.content.startswith('!d'):
        try:
            num = message.content.strip("!d")
            num = num.strip()
            number = random.randrange(1,int(num))
            await client.send_message(message.channel, number)
        except discord.errors.HTTPException:
            await client.send_message(message.channel, "An unknown error occured.")
        except ValueError:
            await client.send_message(message.channel, "I don't know what you're trying to roll. But you're definetly doing it wrong.")


		
client.run('MTgyMDczOTk0Njg4NzI0OTky.CjLx0A.RzZkVofL85eHVDrReNR2093TDzo')
