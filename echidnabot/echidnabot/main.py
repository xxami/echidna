import discord

class EchidnaBot(discord.Client):

  async def on_ready(self):
    print(f'logged in as {self.user}')

  async def on_message(self, message):
    if message.author == self.user:
      return
    print(f'{message.author}: {message.content}')
    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')

def init():
  print('Running Echidnabot..')
  bot = EchidnaBot()
  bot.run('<your token here>')
