import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter



nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins('echo')
nonebot.load_plugin("nonebot_plugin_bilibili_viode")
# nonebot.load_plugin("nonebot_plugin_biliav")

nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run()
