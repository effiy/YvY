# 原始 URL: https://aibard123.com/digest/2024/0819/深度干货这可能是国内第一篇Flux系列模型单卡4090微调lora分享/

# 抓取时间: 2025-03-30 21:42:05

[ AI 文摘 ](https://aibard123.com/digest/)

深度干货这可能是国内第一篇 Flux 系列模型单卡 4090 微调 lora 分享！

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AEZFv5YDlw1f2Ib3pL8KvtH0wIk967SjwO8kuicNLAQOGwDUSj9tTEYg/640?wx_fmt=png&from=appmsg)

作者： AI 过年 来源： [AI 过年](https://mp.weixin.qq.com/s/5h3BDWhgk4ry_97C7PElZA)

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_jpg/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3ACKeziaFGaPgjYLABzobUzkHwjQZ6jKPRms75STshBv1XGVIyX0M1AcA/640?wx_fmt=jpeg&from=appmsg)

「彩虹之眼」整理 | 教程部分由知乎大佬「社恐患者杨老师」投稿

全网首发 | Flux 系列模型单卡 4090 微调 lora 分享（建议收藏）
**01** **/**
先卖个关子！
据说自从 FLUX.1 开源模型发布以来，大批的 Midjourney 忠实粉丝都纷纷转投 Flux
而这一切都是从前 Stability AI 核心成员 Robin Rombach 创立了一个名为 Black Forest Labs 的新公司开始，还顺带拿到 3200 万美元的融资，重新把开源文生图生态拉到巅峰！
前几天网友制作的 TEDx AI 讲师被推友们转封了，你敢相信视频中的女人是 AI 生成的吗？没错她就是 AI 生成的！

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AuJLjjwBgIciaCSiafwEpsQm5mCaxsBYHF04Pnod4Z58zWZXmiaafh4qpw/640?wx_fmt=png&from=appmsg)

视频（左）是使用 Runway Gen 3 创建的，图像（右）是使用 Flux 创建的。
看到这不知道大家是什么感受!如果有人拿着你照片干坏事，细思极恐听起来是不是很恐怖。没事不要慌，赶紧转给家人看看哈哈哈哈
简直是精准控图呀，直接把目前的 99%文生图模型按在地上摩擦呀！
！！！看到这还不是最炸裂的，有趣的是昨天 FLUX.1 直接和 Grok-2 官宣了！( 没错 Grok-2 就是马斯克的 X.AI）

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3Awichr6ZiaLY0mvttXPE7AkxawHuqYXibiawS7xxJibfD9cu46VdbccfTvMw/640?wx_fmt=png&from=appmsg)

也就是老马发布的 grok-2 的模型直接用 flux 出图，尺度之大简直不敢想象！在 FLUX 上生成图像上没有做任何限制。比如朗普、米老鼠、泰勒·斯威夫特等，这些在别的 AI 工具里根本无法生成，但是在 FLUX 上都可以干。（话不多说直接看图）

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AkkOwgibYxwZyw2Zzxn4ZCE43yRNiayUwhiaLvWRUSmILqxSxZBS7Ye5vw/640?wx_fmt=png&from=appmsg)

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3A202oFOecicPiaVMDTZhypMLUScsVElrtdA9zLqTeicAVUP6a6Q0ug7dxQ/640?wx_fmt=png&from=appmsg)

直接把我整乐了！！！老马真的是干大事的人，足够大胆，佩服！！！
于是就出现一个梗：用 flux 输入下一任美国总统永远画的是特朗普!!!
看到这是不是应该直呼离谱~
好了，下面言归正传~
**02** **/**
前几天杨老师做了一场线上 Flux 系列模型单卡 4090 微调 lora 分享！
可能也是国内首个公开分享，目前在国外跑通 Flux 系列模型单卡 4090 微调 lora 的也没几个。
训练器脚本模型环境已经全部打包上传到百度网盘。为照顾大多数人下面将从认识 Flux 开始！！！我把 Lora 训练基础教程放到文末~（大神可直接跳到文末）

#### 认识 Flux 模型

8 月 1 日 黑森林实验室发布 FLUX.1 模型套件

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3Aquoos7G2vjAO6UEeHvZc541u0FXic2gFDDaFcnWkX34dcl99ByagdEg/640?wx_fmt=png&from=appmsg)

并同步发布一篇博客：
<https://blackforestlabs.ai/announcing-black-forest-labs/>
感兴趣的朋友可以去扒一下！
随后敏神-张吕敏发了一组最新 NF4 量化 Flux 模型效果与 FP8 量化效果对比（就说有没有被惊艳到![](https://api.allorigins.win/raw?url=https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Yellowdog.png)）

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AL5DJ4m4Jppm20F1LE81d5dibxrBm5lTCIyL82DJr0h8ZibMMl24YHEaQ/640?wx_fmt=png&from=appmsg)

#### Flux 的应用场景

也顺带分享几组应用场景
Text2Img
a young woman smiling while speaking onstage from google, white background with corporate logos blurred out, tech conference

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AaX6jNF6HXXukZYO6xCTEOqAzljMVRaIgNsEypBuicbIy0ibKy8kJ0nhw/640?wx_fmt=png&from=appmsg)

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AUeaUJcC3K0UetcVMFN1mLgu7zlZ6FazeEj6YONOrDw73fcXdoGNPrg/640?wx_fmt=png&from=appmsg)

#### Img2Img

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AiavQkB3LfQjG3bFweIkS4MHvLjZUR1Cibdmib0rkRtNBJepRTCeSEh2xA/640?wx_fmt=png&from=appmsg)

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AmZlR3FOFSyq7xWA01gy8ynXJIVnV0g1hews6xZuOQkFhmX4icxggFiaA/640?wx_fmt=png&from=appmsg)

#### 噪点图生成漫画

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AwnibMT2vgzYwJtczxurO3KC1yBaMLmBlCJ0tlWhpEAqltGrHbpuWoVQ/640?wx_fmt=png&from=appmsg)

#### 使用 Flux 结合 GEN-3 or kling 制作商业广告片

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AcSfBYuaHZ7HgQP4I5Piay1BdQJXEkLM5EA4GHa02YVnf77nzdMLz6KQ/640?wx_fmt=png&from=appmsg)

#### Flux 模型能力实现角色一致性

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AEZ2AIHLK0aaazrRiaibZzpM0tpQQqxHRecic0VXx6icwCJ1YJHU6xSBjew/640?wx_fmt=png&from=appmsg)

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AXTPicsOsLPCNMOkOJ5cXUia9bhiaaV6VIS9KibnmriccKyTSrvBQphM5L5Q/640?wx_fmt=png&from=appmsg)

#### 现有的 Flux Lora 模型

Flux1.dev-AsianFemale
亚洲人像 Lora
[https://civitai.com/models/633841/flux1dev-asianfemale?t&utm_source=perplexity](https://civitai.com/models/633841/flux1dev-asianfemale?t&utm_source=perplexity)

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AEZFv5YDlw1f2Ib3pL8KvtH0wIk967SjwO8kuicNLAQOGwDUSj9tTEYg/640?wx_fmt=png&from=appmsg)

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AodSHlQkZgCRhn5zVcTWE9Mj4RfT5PVQyrP31GzGGkdxerOhQqgeHDg/640?wx_fmt=png&from=appmsg)

#### Flux-Lora-littletinies

<https://huggingface.co/pzc163/flux-lora-littletinies>

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3A1gQibgsHlmqicROdic8loAmdJibIkFKvE4prFmA6LfnRicZtluBAiaXlH4OQ/640?wx_fmt=png&from=appmsg)

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AKQuNOY0dLxs2ibtibvNCTgZnlLPNWFmAXYLXbXc74WjQdrqMjR00t9Eg/640?wx_fmt=png&from=appmsg)

#### yarn_art_Flux_LoRA

<https://huggingface.co/linoyts/yarn_art_Flux_LoRA>

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AXuuT7lia2GNfg2bhaoiaO53V3VicqR01rqOKMXdZvWHbTwVQ9Sq04Thjw/640?wx_fmt=png&from=appmsg)

#### XLabs-AI

<https://huggingface.co/XLabs-AI/flux-lora-collection>

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3A4icVQmPgic3w9BBZ4th0JqVGFWNKWL5uicRag6s9PqdhO1nK1wvmdEictA/640?wx_fmt=png&from=appmsg)

#### 基于 FLUX 的 Controlnet 模型

#### Canny

InstantX 团队正式开源基于 Flux 的 Canny 模型，之前发布的是 alpha 测试版，正式版目前已经发布，大家可以测试来看看
<https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Canny/>

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AB1ibRvfwGgNG8ViagrNoDnmwoVkOL6tG2jgwWauYc06Ld3otNQaWGOOQ/640?wx_fmt=png&from=appmsg) ####**03** **/**

#### Lora 训练基础教程

推荐训练环境
python=3.10 torch=2.4.0 Cuda=12.1
训练代码 GitHub 链接：
<https://github.com/ostris/ai-toolkit>

```
git clone https://github.com/ostris/ai-toolkit.gitcd ai-toolkitgit submodule update --init --recursivepython -m venv venv.\venv\Scripts\activatepip install torch torchvision --index-url https://download.pytorch.org/whl/cu121pip install -r requirements.txtpython run.py config/train_lora_flux_24gb.yaml
br

```

训练教程直播地址
单卡 4090 做 flux lora 训练的 B 站直播地址：

[https://www.bilibili.com/video/BV1DZ421N71n/?buvid=XX58E79562B11F9A28583DE9037E746E9EBEE&from_spmid=search.search-result.0.0&is_story_h5=false&mid=ddWLQFhb5lgJmpHIPw%2Bfbw%3D%3D&p=1&plat_id=114&share_from=ugc&share_medium=android&share_plat=android&share_session_id=61bf34e2-854f-4799-93f6-715fb00691bf&share_source=WEIXIN&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1723720904&unique_k=WrqWNQo&up_id=1069874770&vd_source=448d548227321b7116a7dcdf814407d2](https://www.bilibili.com/video/BV1DZ421N71n/?buvid=XX58E79562B11F9A28583DE9037E746E9EBEE&from_spmid=search.search-result.0.0&is_story_h5=false&mid=ddWLQFhb5lgJmpHIPw%2Bfbw%3D%3D&p=1&plat_id=114&share_from=ugc&share_medium=android&share_plat=android&share_session_id=61bf34e2-854f-4799-93f6-715fb00691bf&share_source=WEIXIN&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1723720904&unique_k=WrqWNQo&up_id=1069874770&vd_source=448d548227321b7116a7dcdf814407d2)

不同硬件配置，FLUX-dev 模型训练速度对比：
综合对比来看，性价比最高的还是 4090
A100(batch size: 4) 训练速度：0.3478 it/s

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3APpSUYBkthYZrTlwz6Q6RJV7micgVTjWg9p5QRjVFRBpw8UISr6H8pDQ/640?wx_fmt=png&from=appmsg)
H100(batch size: 4) 训练速度：0.4537 it/s

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AqowM3PfwIuSgPJqrc2wh0BWwLILVKCa0xWL4icXozBucI8L6DutCGEw/640?wx_fmt=png&from=appmsg)
单卡 4090(batch size: 1) 训练速度：0.4375 it/s

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AHV7N3C99V4JSvBxReoWZ8RIRvLlM0vFnHR5PlYp5vS9cbCWvDFepQQ/640?wx_fmt=png&from=appmsg)
L40s(batch size: 1) 训练速度：0.838 it/s

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AEzHxcWd4oiaUG3Gzp43UuDjA7IRgHEuqhe8gsic7a2IpzTzm8R1n7x4g/640?wx_fmt=png&from=appmsg)

#### 重要参数设置！！！

昨天直播的过程忘记说了 repeat 如何设置，这个参数默认的 yaml 文件中没有，需要手动添加，位置如下：
在 datasets 下面手动添加 num_repeates: 20

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3Aw6Xia1dv6NE9Jr4ykXHhqgm1ugDhIxartFSV1ns8y9ybL3KJX9ic1eDg/640?wx_fmt=png&from=appmsg)

重要！！如果不添加此项参数，默认的 repeat 会设置为 0

#### 如何根据训练数据配置参数

low_vram: true 这个一定要打开，否则会爆 OOM
占坑！
占坑！

#### 训练器压缩包

通过百度网盘分享的文件：ai-toolkit.rar

链接：<https://pan.baidu.com/s/1Yn1XmQcCr1UBupxYMuLhLg?pwd=iow7>
提取码：iow7

#### 驯服 Flux 小 tips

如何让 Flux 更好地跟随指令，并添加 negative prompt？可以尝试一下这个方法：
Flux 模型的 CFG 值必须设置为 1，CFG = 1 导致不能使用 negative prompts，如果我们增加 CFG，很快就会出现色彩过饱和和输出崩溃的情况，为了解决这个问题，我们可以使用一个 sd-dynamic-thresholding 的插件来解决。它让 Flux 跟随提示变得更好，而且现在还可以使用负 negative prompts。注意：这里的"DynamicThresholdingFull “上的参数设置并非最佳设置，如果有人能找到比这更好的设置，请与大家一起分享。
插件地址：
<https://github.com/mcmonkeyprojects/sd-dynamic-thresholding>

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AbPUABzNUJTr7bATsqvlbSnXzaMm9Nl0oic1RIZtlMVdt9EO5HtUjmTA/640?wx_fmt=png&from=appmsg)

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3AbK8Lq7haPiciagia9FGGwDk3BMtLQpI8cCtoKOUYWszNI5cwXqqdMIPbA/640?wx_fmt=png&from=appmsg)

1.CFG 与 “引导比例 “不同（默认为 3.5 ）
2.“interpolate_phi “参数负责图片的 “饱和度/去饱和度”，如果您觉得图片有问题，请调整该参数。 3.在对 mimic_mode 和 cfg_mode 进行了一些 XY 图测试后，很明显，对两者都使用 Half Cosine Up 是最好的解决方案：
4: AD + MEAN，因为与其他方法相比，它们给出的光影最柔和：

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3A6p9bl1epjkYVs1IEJibWicBX10g4HJicNwG5v0U8IuBnLyEdL4dyyOA1A/640?wx_fmt=png&from=appmsg)

5: 我选择了 interpolate_phi = 0.7 + “enable”，因为与其他方法相比，它们给出的光影也最柔和：

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/sz_mmbiz_png/3hOoVXKRjdjBKuibNpRicqqYMZBuOpzv3Ar3DzF09BeEYfiad9FI6VVKiav1caic8aLSI1esQOftjQmf2zRlyWJgMQw/640?wx_fmt=png&from=appmsg)

到这里就结束了，最后我们打造了一个 flux 开源社区，后续会持续更新有关 Flux 训练的内容，欢迎大家一起编辑共建知识库！
