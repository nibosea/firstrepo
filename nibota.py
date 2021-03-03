import discord 

client = discord.Client()

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.content == "!join":
        if message.author.voice is None:
            await message.channel.send("You don't connect voice channel")
            return
        # connect to VC
        await message.author.voice.channel.connect()
        await message.channel.send("connected")
    elif message.content == "!leave":
        if message.guild.voice_client is None:
            await message.channel.send("Not connected")
            return 
        await message.guild.voice_client.disconnect()
        await message.channel.send("Disconnected")
    if message.content == "!play":
        if message.guild.voice_client is None:
            await message.channel.send("Not Connected")
            return
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("pekora_shout.mp3"), volume = 5.0)
        message.guild.voice_client.play(source)
client.run("ODE2MTQxMzI1NTI2MTA2MTMy.YD2o1w.vOoK88UxBHAJU8pmn9_n9CosXmY")
