from pyrogram import Clinet, filters


API_ID = "24008761"
API_HASH = "c6bb29db832216220e1234b163233cec"
BOT_TOKEN = "6692368460:AAEAEnhNL6LAtupuF6-ko4UugdL78y9rI_I"

Infinity = Client(
    name="charu",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@infinity.on_message(filters.command("start"))
async def start_cmd(Client, message):
    print("START Command")


@infinity.on_message(filters.command("help"))
async def help_cmd(Client, massage):
    print("HELP Command")
            

print("bot was started")

Infinity.run()

  

