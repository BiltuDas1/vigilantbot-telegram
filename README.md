# VigilantBot
A self hosted group management bot for large groups, which can automatically restrict, filter some kind of message and helps group administrator to stay AFK. Just give full permission to the bot and your are ready to go.

Demo: [@vigilant_tg_bot](https://telegram.me/vigilant_tg_bot)

# Environments
Here are some environments which required to pass to the docker image or need to provide to the `.env` files to work perfectly

|Environment Name|Used for|
|----------------|---------|
|`TG_BOT_TOKEN`|Telegram bot token for interacting with bot|
|`SPAMWATCH_API_KEY`|API Key for [SpamWatch](https://telegram.me/SpamWatchBot), for filtering scammers in Telegram|

# Usability
## Docker image
Check the documentation in official [Docker Hub](https://hub.docker.com/r/biltudas1/vigilantbot)

## Running from source
1. At first clone the repository using `git clone https://github.com/BiltuDas1/vigilantbot-telegram` and switch to the cloned repository
2. Into the repository you will find a `.env` file, edit the file with any kind of text editor and give value to the environments according to the environment table mentioned before. When you are done then save the file.
3. Now install all the dependencies by using the `pip install -r requirements.txt`
4. Finally start the bot by using the command `python main.py`