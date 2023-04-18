import re, datetime, random

from nonebot.plugin import on_message
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import MessageSegment

last_time = None

dictionary = ("你说的对，但是《原神》是由米哈游自主研发的一款全新开放世界冒险游戏。游戏发生在一个被称作「提瓦特」的幻想世界，在这里，被神选中的人将被授予「神之眼」，导引元素之力。你将扮演一位名为「旅行者」的神秘角色在自由的旅行中邂逅性格各异、能力独特的同伴们，和他们一起击败强敌，找回失散的亲人——同时，逐步发掘「原神」的真相。"
              , "因为你的素养很差，我现在每天玩原神都能赚150原石，每个月差不多5000原石的收入， 也就是现实生活中每个月5000美元的收入水平，换算过来最少也30000人民币，虽然我 只有14岁，但是已经超越了中国绝大多数人(包括你)的水平，这便是原神给我的骄傲的资本。"
              , "感觉不如原神，画质……"
              , MessageSegment.image('https://gchat.qpic.cn/gchatpic_new/912883181/3801842761-3122639652-275F4C32CD40D4CAD8213E6CDFA14D2B/0?term=2')
              , MessageSegment.image('https://gchat.qpic.cn/gchatpic_new/1518167028/3801842761-2454322312-F5558393E6791169D1E52C976D4DA386/0?term=2')
            )

async def bible_match(bot: Bot, event: Event) -> bool:
    global last_time
    if last_time is not None and (datetime.datetime.now() - last_time).total_seconds() < 120:
        return False

    friends = await bot.get_friend_list()
    condition1 = "311842761" in event.get_session_id()  or event.get_user_id() in str(friends)
    condition2 = re.search(r'[光暗]+.*(强|厉害|牛逼)+', event.get_plaintext(), re.M) is not None \
                 or re.search(r'^首先.*忘了', event.get_plaintext(), re.M) is not None
    if condition1 and condition2 :
        last_time = datetime.datetime.now()
    return condition1 and condition2

async def op_match(bot: Bot, event: Event) -> bool:
    global last_time
    if last_time is not None and (datetime.datetime.now() - last_time).total_seconds() < 120:
        return False

    friends = await bot.get_friend_list()
    condition1 = "311842761" in event.get_session_id()  or event.get_user_id() in str(friends)
    condition2 = re.search(r'^感觉不如', event.get_plaintext(), re.M) is not None \
                 or re.search(r'^你说得对.*但是', event.get_plaintext(), re.M) is not None \
                 or re.search(r'.*(原神|塞尔达|开放世界|必胜客)+', event.get_plaintext(), re.M) is not None
    if condition1 and condition2 :
        last_time = datetime.datetime.now()
    return condition1 and condition2

bible = on_message(bible_match, block=False, priority=50)
op = on_message(op_match, block=False, priority=51)

@bible.handle()
async def bible_handle(bot: Bot, event: Event):
    await bible.finish(Message(
        f'[CQ:at,qq=912883181]首先，暗属性伤害本身就高，但克制他的还是光，光暗互相克制，但光属性略胜一筹，不过也要看职业，我想说的是，你需要一个光属性，如果说主培养角色优先培养哪个属性，我建议光暗，因为不受克制影响，所以，只要你练度高，就可以吊打一切'))

@op.handle()
async def op_handle(bot: Bot, event: Event):
    await op.finish(Message(
        dictionary[random.Random().randint(0, len(dictionary)-1)]))

