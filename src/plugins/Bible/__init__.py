import re, datetime

from nonebot.plugin import on_message
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

last_time = None

async def match(bot: Bot, event: Event) -> bool:
    global last_time
    if last_time is not None and (datetime.datetime.now() - last_time).total_seconds() < 600:
        return False

    last_time = datetime.datetime.now()
    friends = await bot.get_friend_list()
    condition1 = "311842761" in event.get_session_id()  or event.get_user_id() in str(friends)
    condition2 = re.search(r'[光暗]+.*(强|厉害|牛逼)+', event.get_plaintext(), re.M) is not None \
                 or re.search(r'^首先.*忘了', event.get_plaintext(), re.M) is not None
    return condition1 and condition2

bible = on_message(match, priority=50)

@bible.handle()
async def bible_handle(bot: Bot, event: Event):
    await bible.finish(Message(
        f'[CQ:at,qq=912883181]首先，暗属性伤害本身就高，但克制他的还是光，光暗互相克制，但光属性略胜一筹，不过也要看职业，我想说的是，你需要一个光属性，如果说主培养角色优先培养哪个属性，我建议光暗，因为不受克制影响，所以，只要你练度高，就可以吊打一切'))
