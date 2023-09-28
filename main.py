import discord
from discord.ext import commands
import certifi, ssl
from daily import *
from latlong import *
from time_zone import *
from aqi import *
import os
from dotenv import load_env
load_env()

# boturl = https://discord.com/api/oauth2/authorize?client_id=1136366300013273138&permissions=8&scope=bot

ssl_context = ssl.create_default_context(cafile=certifi.where())

'''
Make a .env file and put your token there in a variable and fetch that varialbe here in getenv method
'''
token = os.getenv('DISCORD_TOKEN') 
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents, ssl_context=ssl_context)

@bot.event
async def on_ready():
    print(bot.user)
    print(bot.user.id)

@bot.command()
async def ping(ctx):
    '''
    This function is just to check if the bot is responding or not
    '''
    await ctx.send('pong')

@bot.command()
async def current(ctx, *loc):
    '''
    This function returns the current weather status of the given Location
    '''
    
    global final_location
    final_location = ' '.join(loc)
    lat = get_location_metadata(final_location)['lat']
    lon = get_location_metadata(final_location)['lon']
    
    current_weather_data = get_weather_data(lat,lon)['main']

    temp = current_weather_data['temp']
    max_temp = current_weather_data['temp_max']
    min_temp = current_weather_data['temp_min']
    feels_like = current_weather_data['feels_like']
    timezone = get_weather_data(lat,lon)['timezone']

    final_string = f'Current weather conditions in {final_location.title()}\nTemp - `{temp}°C` \nMax Temp - {max_temp}°C \nMin Temp - {min_temp}°C \nFeels like - {feels_like}°C'
    await ctx.send(final_string)


@bot.command()
async def timezone(ctx, *loc):
    '''
    Get the timezone of the given location
    '''
    final_location = ' '.join(loc)
    lat = get_location_metadata(final_location)['lat']
    lon = get_location_metadata(final_location)['lon']
    offset_seconds = get_weather_data(lat, lon)['timezone']
    formated_timezone = format_timezone(offset_seconds)
    await ctx.send(f'Timezone of {final_location.title()} is GMT {formated_timezone}')

@bot.command()
async def time(ctx, *loc):
    final_location = ' '.join(loc)
    lat = get_location_metadata(final_location)['lat']
    lon = get_location_metadata(final_location)['lon']

    current_time_at_location = get_current_time(str(final_location))
    await ctx.send(f'{final_location} : {current_time_at_location}')

@bot.command()
async def aqi(ctx, *loc):
    final_location = ' '.join(loc)
    aqi_data = get_aqi(final_location)
    await ctx.send(f'Air Quality Index at {final_location.title()} is `{aqi_data}`')

@bot.command()
async def aqiforecast(ctx, *loc):
    final_location = ' '.join(loc)
    aqi_data = get_aqi_data(final_location)
    forecast = aqi_data['data']['forecast']
    await ctx.send(f'{forecast}')

if __name__ == '__main__':
    bot.run(token)






















