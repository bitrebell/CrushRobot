class Config(object):
    LOGGER = True

    API_ID = 10738943
    API_HASH = "da61e3a08b5ac78ce28b4a4cd854aeec"
    TOKEN = "6412441114:AAF5nri-Vw1kcwvMn4JT4KzXH2Fjpxv3HHA"
    OWNER_ID = 5716978554
    OWNER_USERNAME = "aadillllll"
    SUPPORT_CHAT = "CrushAssistant"
    JOIN_LOGGER = (-1001306127048)
    EVENT_LOGS = (-1001677106070)

    SQLALCHEMY_DATABASE_URI = ""
    MONGO_DB_URI = ""mongodb+srv://adil00:12345@cluster0.fyt5yoa.mongodb.net/?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = 
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = 
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = 
    WOLVES = 

    DONATION_LINK = ""
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = ""
    TIME_API_KEY = ""
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = "https://te.legra.ph/file/c899d55728cee2e8fe344.jpg"
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ARQ_API_KEY = "LJMETG-DPHBCX-DGHJCD-TMFIGB-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
