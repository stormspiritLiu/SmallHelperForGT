import nonebot
from nonebot_plugin_apscheduler import scheduler


# 以上都是导入对应的依赖，scheduler是一个定时器插件，配置参见官方文档

# 设定时间的要调用的函数名id
@scheduler.scheduled_job('cron', minute='30', hour='19', day='*', id='daily')
async def daily():
    (bot,) = nonebot.get_bots().values()    # 获取bot对象
    await bot.send_msg(
        # 也可设置群聊发送，详情见源码
        mseeage_type="group",
        group_id=int(311842761),     # 注意python类型转化
        message="吾日三省吾身：会战出刀了吗？共斗周打了吗？33周混了吗？"
    )
