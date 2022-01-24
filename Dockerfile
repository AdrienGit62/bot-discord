FROM python:3

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
RUN pip install discord
RUN pip install git+https://github.com/Rapptz/discord.py.git@master

COPY . .

CMD [ "python3", "my_discord_bot.py" ]