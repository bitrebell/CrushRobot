
<h1 align="center">
   ──「 Ｃｒｕｓｈ Ｒｏｂｏｔ“̯ 🐼💗 |℡ 」── 

</h1>

<p align="center">
  <img src="https://te.legra.ph/file/a54760fc48c940cdfeae9.jpg">
</p>

<p align="center">
    Ａ ＳUＰＰＯＲＴ ＧＲＯUＰ ＡＮＤ ＲＥＡＤＹ-ＴＯ-UＳＥ ＲUＮＮＩＮＧ ＩＮＳＴＡＮＣＥ Ｏf ＴＨＩＳ ＢＯＴ ＣＡＮ ＢＥ fＯUＮＤ ＯＮ ＴＥＬＥＧＲＡＭ .𖤐 <br>
    <a href="https://t.me/crush_managmentbot"> CrushRobot </a> | 
    <a href="https://t.me/CrushBotSupport"> CrushSupport </a>
</p>

<p align="center">
<a href="https://github.com/Darkranger00/CrushRobot/stargazers"><img src="https://img.shields.io/github/stars/Darkranger00/CrushRobot?color=black&logo=github&logoColor=black&style=for-the-badge" alt="Stars" /></a>
<a href="https://github.com/Darkranger00/CrushRobot/network/members"> <img src="https://img.shields.io/github/forks/Darkranger00/CrushRobot?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<a href="https://github.com/Darkranger00/CrushRobot/blob/main/LICENSE"> <img src="https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge" alt="License" /> </a>
<a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Written%20in-Python-orange?style=for-the-badge&logo=python" alt="Python" /> </a>
<a href="https://pypi.org/project/Pyrogram/"> <img src="https://img.shields.io/pypi/v/pyrogram?color=yellow&label=pyrogram&logo=python&logoColor=green&style=for-the-badge" /></a>
<a href="https://Darkranger00/CrushRobot/commits/Darkranger00"> <img src="https://img.shields.io/github/last-commit/Darkranger00/CrushRobot?color=blue&logo=github&logoColor=green&style=for-the-badge" /></a> 
</p>

<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ 」─
</h3>

<p align="center"><a href="https://dashboard.heroku.com/new?template=https://github.com/Darkranger00/CrushRobot"> <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>


<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ᴏᴋᴛᴇᴛᴏ 」─
</h3>

<p align="center"><a href="https://cloud.okteto.com/deploy?repository=https://github.com/Darkranger00/CrushRobot"><img src="https://img.shields.io/badge/Deploy%20On%20Okteto-black?style=for-the-badge&logo=Okteto" width="220" height="38.45"/></a></p>

<h3 align="center">
    ─「 sᴜᴩᴩᴏʀᴛ 」─
</h3>

<p align="center">
<a href="https://telegram.me/CrushBotSupport"><img src="https://img.shields.io/badge/-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

<p align="center">
<a href="https://telegram.me/aadilllll"><img src="https://img.shields.io/badge/%20YOUR CRUSH-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>
<h2 align="center"> 
   ⇝ Install Locally Or On A VPS ⇜
</h2>

```console
CrushRobot@arch:~$ git clone https://github.com/Darkranger00/CrushRobot
CrushRobot@arch:~$ cd CrushRobot
CrushRobot@arch:~$ pip3 install -U -r requirements.txt
CrushRobot@arch:~$ cp sample_config.py config.py
```
 
<h3 align="center"> 
    Edit <b>config.py</b> with your own values
</h3>

<h2 align="center"> 
   ⇝ Run Directly ⇜
</h2>

```console
CrushRobot@arch:~$ python3 -m CrushRobot
```

<h3 align="center"> 
   Generating Pyrogram Session For Heroku
</h3>

```console
CrushRobot@arch:~$ git clone https://github.com/Darkranger00/CrushRobot
CrushRobot@arch:~$ cd Syrabot
CrushRobot@arch:~$ pip3 install pyrogram TgCrypto
CrushRobot@arch:~$ python3 str_gen.py
```

<h1 align="center"> 
   ⇝ Docker ⇜
</h1>

```console
CrushRobot@arch:~$ git clone https://github.com/Darkranger00/CrushRobot
CrushRobot@arch:~$ Syrabot
CrushRobot@arch:~$ cp sample_config.env config.env
```

<h3 align="center"> 
    Edit <b> config.env </b> with your own values
</h3>

```console
syrabot@arch:~$ sudo docker build . -t CrushRobot
syrabot@arch:~$ sudo docker run CrushRobot
```

<h2 align="center"> 
   ⇝ Write new modules ⇜
</h2>

```py
# Add license text here, get it from below

from syrabot import app # This is bot's client
from syrabot import app2 # userbot client, import it if module is related to userbot
from pyrogram import filters # pyrogram filters
...


# For /help menu
__MODULE__ = "Module Name"
__HELP__ = "Module help message"


@app.on_message(~filters.edited & filters.command("start"))
async def some_function(_, message):
    await message.reply_text("Heyy Baby!! I'm already up!!")

# Many useful functions are in, CrushRobot/utils/, CrushRobot, and CrushRobot/core/
```

<h3 align="center"> 
   And put that file in CrushRobot/modules/, restart and test your bot.
</h3>
<h3 align="center">
    ─「 ᴄʀᴇᴅɪᴛs 」─
</h3>

<p align="center">
<a href="https://github.com/pyrogram/pyrogram"> <img src="https://img.shields.io/badge/Pyrogram-black?style=for-the-badge&logo=github" alt="Pyrogram" /> </a>
<a href="https://github.com/pytgcalls/pytgcalls"> <img src="https://img.shields.io/badge/PyTgCalls-black?style=for-the-badge&logo=github" alt="Pytgcalls" /> </a>
<a href="https://github.com/Darkranger00"> <img src="https://img.shields.io/badge/Darkranger-black?style=for-the-badge&logo=github" alt="Anonymous" /> </a>
<a href="https://github.com/darkrager"> <img src="https://img.shields.io/badge/AAdil-black?style=for-the-badge&logo=github" alt="Shikhar" /> </a>
<a href="https://github.com/TheHamkerCat"> <img src="https://img.shields.io/badge/TheHamkerCat-black?style=for-the-badge&logo=github" alt="TheHamkerCat" /> </a>
</p>
