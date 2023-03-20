# SmallHelperForGT
坎公骑冠剑NS服Q群小助手

## 使用指南：
+ 确保你已经具备python 3.9及以上环境
+ go-cqhttp配备的- ws-reverse:为universal: ws://127.0.0.1:10718/onebot/v11/ws
+ go-cqhttp生成的device.json里面的protocol从6改成2，机器人模拟设备为安卓手表
+ 命令行依次运行以下指令
~~~
# 项目根目录python虚拟环境搭建
python3 -m venv .venv
source .venv/bin/activate
# 成功后，shell提示符将以python虚拟环境名称作为前缀，类似于 (venv) root@debian:~$:

# Nonebot环境构建
python -m pip install pipx
python -m pipx ensurepath
pipx install nb-cli
pip install -r requirements.txt
nb run
~~~

## 参考文献
+ [使用NoneBot2搭建QQ机器人](https://www.zhihu.com/column/c_1375057475469656064)
+ [零基础QQ机器人视频教程 开源、免费、纯新手向的nonebot2.0.0beta版讲解](https://www.bilibili.com/video/BV1aZ4y1f7e2) 
+ [开源项目 NoneBot2.0.0RC 全平台保姆级新手教学](https://www.bilibili.com/video/BV1984y1b7JY)
+ [go-cqhttp官网](https://docs.go-cqhttp.org/)
+ [Nonebot官网](https://v2.nonebot.dev/)
+ [抽卡代码，特别鸣谢](https://github.com/HibiKier/nonebot_plugin_gamedraw)
