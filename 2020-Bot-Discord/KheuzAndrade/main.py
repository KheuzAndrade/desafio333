#discordapp.com/oauth2/authorize?client_id=723496835997630475&scope=bot&permissions=8
import discord
import pandas
from urllib.request import urlretrieve
from random import randint

class MyClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.commands = ["!dado"]

    async def on_ready(self):
        print(self.user.name + " Online!")

    async def on_member_join(self, member):
        message = "Bem vindo {}".format(member.mention)
        await member.channel.send(message)

    async def on_message(self, message):
        if message.author == self.user:
            return

        # COMANDOS
        if message.content[0] == "!":
            command = message.content.split(",")

            # Sistema de jogar dados
            if command[0] == "!dado":
                num = str(randint(1,6))
                await message.channel.send("`Número Sorteado: "+num+"`")

            # Casos confirmados COVID-19
            elif command[0] == "!casos confirmados covid-19":
                url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
                urlretrieve(url, 'data/global_cases_covid19.csv')

                df_covid_cases = pandas.read_csv('data/global_cases_covid19.csv')
                df_covid_cases_country = df_covid_cases.groupby('Country/Region').sum()

                try:
                    country = command[1]

                    if country[0] == " ":
                        country = country[1:len(country)]
                    country = country.title()

                    cases = str(int(df_covid_cases_country.loc[country].values[-1]))
                    await message.channel.send("`"+country+": "+cases+"`")
                except:
                    await message.channel.send("`Ainda não tenho essa informação ou "+country+" não é um país.`")

            # Mortes por COVID-19
            elif command[0] == "!mortes por covid-19":
                url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
                urlretrieve(url, 'data/global_deaths_covid19.csv')

                df_covid_deaths = pandas.read_csv('data/global_deaths_covid19.csv')
                df_covid_deaths_country = df_covid_deaths.groupby('Country/Region').sum()

                try:
                    country = command[1]

                    if country[0] == " ":
                        country = country[1:len(country)]
                    country = country.title()

                    deaths = str(int(df_covid_deaths_country.loc[country].values[-1]))
                    await message.channel.send("`"+country+": "+deaths+"`")
                except:
                    await message.channel.send("`Ainda não tenho essa informação ou "+country+" não é um país.`")

            # Casos recuperados COVID-19
            elif command[0] == "!casos recuperados covid-19":
                url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
                urlretrieve(url, 'data/global_recovered_covid19.csv')

                df_covid_recovered = pandas.read_csv('data/global_recovered_covid19.csv')
                df_covid_recovered_country = df_covid_recovered.groupby('Country/Region').sum()

                try:
                    country = command[1]

                    if country[0] == " ":
                        country = country[1:len(country)]
                    country = country.title()

                    recovered = str(int(df_covid_recovered_country.loc[country].values[-1]))
                    await message.channel.send("`"+country+": "+recovered+"`")
                except:
                    await message.channel.send("`Ainda não tenho essa informação ou "+country+" não é um país.`")

            else:
                await message.channel.send("`Error: Comando desconhecido.`")

client = MyClient()
client.run('TOKEN')
