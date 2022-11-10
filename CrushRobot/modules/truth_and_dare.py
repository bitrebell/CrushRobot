from telegram import Update
from telegram.ext import CallbackContext

from CrushRobot import dispatcher
from CrushRobot.modules.disable import DisableAbleCommandHandler

from TruthDarePy import TD

love = TD()


def truth(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(love.truth(lang="en"))


def dare(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text(love.dare(lang="en"))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)


__help__ = """
*Truth & Dare*

 ❍ /truth *:* Sends a random truth string.
 ❍ /dare *:* Sends a random dare string.
"""

__mod_name__ = "Tʀᴜᴛʜ-Dᴀʀᴇ"
