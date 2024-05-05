from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.url("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/PiroHackz"),
                               Button.url("sᴜᴘᴘᴏʀᴛ", url="https://t.me/The_Helping_Club")],
                              [Button.inline("sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ", data="set"),
                               Button.inline("ʀᴇᴍᴏᴠᴇ ᴛʜᴜᴍʙɴᴀɪʟ", data="rem")],
                              [Button.url("sᴜʙsᴄʀɪʙᴇ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ", url="https://www.youtube.com/@TrickyAyush")]]) 
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="t.me/im_piro")]])
    
