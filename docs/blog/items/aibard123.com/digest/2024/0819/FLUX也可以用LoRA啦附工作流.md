# 原始 URL: https://aibard123.com/digest/2024/0819/FLUX也可以用LoRA啦附工作流/

# 抓取时间: 2025-03-30 21:42:09

[ AI 文摘 ](https://aibard123.com/digest/)
FLUX 也可以用 LoRA 啦！附工作流

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3QvnmX3Irufdl37iaJaZJ72eaBr2TRU7UDGhFgZAgpvWj9IvIe3xaLptCrA/640?wx_fmt=png&from=appmsg)

随着 FLUX 开源模型的发布，曾经对 SD3 寄予厚望的 AI 绘画爱好者们，迅速转向 FLUX。
再加上张吕敏对 FLUX 的量化，大大降低了显卡的门槛，FLUX 的再创大模型也层出不穷。
最近，基于 FLUX 的 LoRA 也开始发布，在 pony 之后，一个全新的生态茁壮成长。
今天推荐一个 LoRA 和相应的工作流。
LoRA 的名字叫：Aesthetic LoRA for FLUX。
作者在 C 站称：
增加了经过 10k 步训练的更强大的 Lora 模型，并附有直接比较图像（左边是 Lora 强度 0，右边是 Lora 强度 1.2）。由于 Lora 实际上并不会让图像更像动漫，所以从名称中去掉了误导性的（动漫）。

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_jpg/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3QvnoKgalyvy4TlOOffVv1Z0kfNLb5GS2xtMicniaPnwibPqEM9sxiazXSeMiaQ/640?wx_fmt=jpeg&from=appmsg)

推荐的使用强度真的取决于你的工作流程！
目的：以牺牲一些连贯性为代价，赋予更具有绘画性和狂野感的外观。它是在不关心细节的绘画风格鲜明的动漫艺术上训练的。
这是一个为 Flux 的概念验证风格的 Lora。而且仅仅是一个概念验证！
它应该由以下内容触发：
动漫艺术中的女孩/女性 但这并不总是必要的。
注意：对于某些提示，它会有戏剧性的效果，对于其他…可能什么也没有，可能需要一个更大和更多样化的数据集，而不是我使用的那个。
一、工作流介绍
工作流网盘下载：
<https://pan.quark.cn/s/6e4bbc99ee58>

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3QvneDpe7Chv0HnYpEUHmIrwfBfyxsTfCCe8icE3F9SwYBI7IBS5J8sFoDA/640?wx_fmt=png&from=appmsg)

工作流看起来比较复杂，我简单介绍下。
1、FLUX 模型加载器、CLIP 加载器和加载 VAE。
如果你对 FLUX 模型不熟悉，请向前找 FLUX 安装的文章。

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3QvnxVpSOlyB4jnArFt3FzJ4F3cU8S32o3VI8icsiaF1fJIVq9krPygp5fqQ/640?wx_fmt=png&from=appmsg)

2、加载 LoRA，LoRA 安装在 models\lora 目录下即可，和 SDXL 的 LoRA 放在一起。
然后在 LoRA 加载器选择本文演示的 LoRA：Aesthetic10k.safetensors
网盘下载：https://pan.quark.cn/s/64393329230f

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3QvnInN5Vu7bqVEVyLw0iaibibic8K8oianw9TsMlZNUMuNcPjY9sshibhM0bU7A/640?wx_fmt=png&from=appmsg)

3、放大模型，选择你常用的放大模型即可

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3QvnZIcmWkYwrVP2PHSEIvRWYFq4d68dpfsNLqHNt9sCWwtNsgb1m28XBA/640?wx_fmt=png&from=appmsg)

二、效果展示
1、持剑少女
提示词：
masterpiece, best quality, 1girl, portrait, closeup
ultra-realistic mix fantasy,(1 giant chimera monster:1.3) behind an asian woman holding a glowing sword,void energy diamond sword, in the style of dark azure and light azure, mixes realistic and fantastical elements, vibrant manga, uhd image, glassy translucence, vibrant illustrations, ultra realistic, long hair, straight hair, light purple hair,head jewelly, jewelly, shawls,light In eyes, red eyes, portrait, firefly, bokeh, mysterious, fantasy, cloud, abstract, colorful background, night sky, flame, very detailed, high resolution, sharp, sharp image, 4k, 8k, masterpiece, best quality, magic effect, (high contrast:1.4), dream art, diamond, skin detail, face detail, eyes detail, mysterious colorful background, dark blue themes

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3QvnN7RAMDOTyTUCt09Ghl6kbYS6f82fXYS5ohAbhEbXXtXd4U3fGYpuCw/640?wx_fmt=png&from=appmsg)

FLUX 画手是真的完美，但这个身体仔细看是有问题的… …
2、女孩与火
提示词：
fantasy full-body-shot character of a posing timid cute female warlock with piercing green eyes with tiny glowing amethyst earrings and hip length disheveled dark sooty brown hair decorated by small rope braids wearing a gold trimmed contoured khaki robe illuminated by fire embers. Background of burning embers ash and soot flying through the air in a grim medieval port town with sunset in the distance.

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3QvnibRVQhk6AiaS18aniaSbslTIwnKaTl4YFbWGefQ7S3MwWQQ44ibFibV8FZQ/640?wx_fmt=png&from=appmsg)

3、手捧微光
提示词：
anime art of a delicate and ethereal illustration of a woman holding a small lit candle. The style blends fine line art with soft, warm lighting that emanates from the candle, casting a golden glow on the woman's face and upper body. Her eyes are closed, and her expression is serene, as if she is in a moment of deep contemplation or peace. The lines that define her hair and features are intricate, giving a sense of movement and lightness, while the glowing light adds depth and warmth to the overall composition. The contrast between the gentle lines and the warm, glowing light creates a dreamlike and soothing atmosphere.

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3QvnKzxCg9Dz3TEWOU2aVQ5tfHkyQOicjQPGBBctJelCqJP74DNbO9fCvuw/640?wx_fmt=png&from=appmsg)

4、美女与野兽
提示词：
Professional portrait photography. A breathtaking, award-winning movie still captures an ethereal winter scene. An 18-year-old girl, dressed in flowing, light white garments that blend seamlessly with the snowy landscape, sits gracefully on a pristine blanket of snow. Her delicate face, framed by soft, loose strands of hair, gently presses against the neck of a snow-white fox, whose fur glistens in the soft, diffused light. The fox is perched protectively behind her, its head nuzzling her right shoulder with a comforting, intimate gesture. The background is adorned with a subtle bokeh effect, creating a dreamlike atmosphere. White snowflakes float gently down from the sky, adding a sense of tranquility and magic to the scene. The overall composition exudes beauty and serenity, with the visuals blending elements of dream and reality, evoking deep emotions and a sense of otherworldly calm This is a breathtaking portrait.

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3Qvn5E4D5t4Atooyb8zqt4x3pPPFC0VPDbUlf2qVw0UjibGTiclzk7MoMbvg/640?wx_fmt=png&from=appmsg)

5、小精灵
提示词：
(Full Body Shot) Whimsical fairy, wide-eyed wonder. Messy golden hair, freckled face. Translucent dragonfly wings, flower crown. Pointed ears, open-mouthed surprise. Huge green eyes, dilated pupils. Soft ethereal lighting, forest backdrop. Hyper-realistic 3D rendering. Delicate skin texture, visible pores. Wisps of hair catching light. Macro detail on wings and flowers. Magical sparkles, bokeh effect. Vibrant colors, warm tones.

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/PclvAZEsuoC3pL2Mxia5GhFFbxQhr3Qvn9Jfyu4nFSwpPictiaecP77OE60jglIA3lNv9WpVtsBhYGjQ6PuJFjuXg/640?wx_fmt=png&from=appmsg)

<https://pan.quark.cn/s/64393329230f>
