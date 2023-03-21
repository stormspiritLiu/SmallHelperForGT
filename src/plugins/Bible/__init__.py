from nonebot.plugin import on_message
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

async def match(bot: Bot, event: Event) -> bool:
    friends = await bot.get_friend_list()
    condition1 = "311842761" in event.get_session_id()  or event.get_user_id() in str(friends)
    condition2 = "暗炮" in event.get_plaintext() or "圣经" in event.get_plaintext()
    return condition1 and condition2

bible = on_message(match, priority=50)

@bible.handle()
async def bible_handle(bot: Bot, event: Event):
    await bible.finish(Message(
        f'[CQ:at,qq=912883181]首先，暗属性伤害本身就高，但克制他的还是光，光暗互相克制，但光属性略胜一筹，不过也要看职业，我想说的是，你需要一个光属性，如果说主培养角色优先培养哪个属性，我建议光暗，因为不受克制影响，所以，只要你练度高，就可以吊打一切'))
