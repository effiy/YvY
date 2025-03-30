# 原始URL: https://gptpmt.com/preface/basics_probability

# 抓取时间: 2025-03-30 21:27:50

[GPTPrompt](https://gptpmt.com/)
`CTRL K`
[GitHubGitHub (opens in a new tab)](https://github.com/CarGod/gptpmt)
`CTRL K`
  * [项目介绍](https://gptpmt.com/)
  * [先导篇](https://gptpmt.com/preface)
    * [Hello ChatGPT](https://gptpmt.com/preface/hello)
    * [什么是Tokens？](https://gptpmt.com/preface/basics_token)
    * [概率和温度](https://gptpmt.com/preface/basics_probability)
  * [基础篇](https://gptpmt.com/foundation)
    * [获得优质输出的六大技巧](https://gptpmt.com/foundation/grammar)
    * [结构化Prompt模板与技巧](https://gptpmt.com/foundation/structured)
    * [让GPT输出JSON数据](https://gptpmt.com/foundation/json_format)
  * [进阶篇](https://gptpmt.com/advance)
    * [善用XML标签](https://gptpmt.com/advance/use_xml)
    * [思维链提示](https://gptpmt.com/advance/let_think)
  * [实战篇](https://gptpmt.com/practice)
  * [关于此项目](https://gptpmt.com/about)
  * [关于我](https://gptpmt.com/contact)


  * [项目介绍](https://gptpmt.com/)
  * [先导篇](https://gptpmt.com/preface)
    * [Hello ChatGPT](https://gptpmt.com/preface/hello)
    * [什么是Tokens？](https://gptpmt.com/preface/basics_token)
    * [概率和温度](https://gptpmt.com/preface/basics_probability)
      * [复习一下](https://gptpmt.com/preface/basics_probability#复习一下)
      * [句子是怎么产生的？](https://gptpmt.com/preface/basics_probability#句子是怎么产生的)
      * [温度(temperature)](https://gptpmt.com/preface/basics_probability#温度temperature)
  * [基础篇](https://gptpmt.com/foundation)
    * [获得优质输出的六大技巧](https://gptpmt.com/foundation/grammar)
    * [结构化Prompt模板与技巧](https://gptpmt.com/foundation/structured)
    * [让GPT输出JSON数据](https://gptpmt.com/foundation/json_format)
  * [进阶篇](https://gptpmt.com/advance)
    * [善用XML标签](https://gptpmt.com/advance/use_xml)
    * [思维链提示](https://gptpmt.com/advance/let_think)
  * [实战篇](https://gptpmt.com/practice)
  * [关于此项目](https://gptpmt.com/about)
  * [关于我](https://gptpmt.com/contact)


中文
System
On This Page
  * [复习一下](https://gptpmt.com/preface/basics_probability#复习一下)
  * [句子是怎么产生的？](https://gptpmt.com/preface/basics_probability#句子是怎么产生的)
  * [温度(temperature)](https://gptpmt.com/preface/basics_probability#温度temperature)
  * [为什么模型的输出不一致？](https://gptpmt.com/preface/basics_probability#为什么模型的输出不一致)
  * [温度的作用？](https://gptpmt.com/preface/basics_probability#温度的作用)
  * [如何调整温度？](https://gptpmt.com/preface/basics_probability#如何调整温度)


[Question? Give us feedback → (opens in a new tab)](https://github.com/CarGod/gptpmt/issues/new?title=Feedback%20for%20%E2%80%9C%E6%A6%82%E7%8E%87%E5%92%8C%E6%B8%A9%E5%BA%A6%E2%80%9D&labels=feedback)[Edit this page](https://github.com/CarGod/gptpmt/pages/preface/basics_probability.zh.mdx)
[先导篇](https://gptpmt.com/preface)
概率和温度
# 概率和温度
## 复习一下[](https://gptpmt.com/preface/basics_probability#复习一下)
上节课我们讲了 ChatGPT 的 Tokens 和 Token IDS，就像我们小时候学习说话的时候，老师总是从最基本的字和词教起，当我们积累了足够多的字和词后，才能学会如何组装成句子。
在训练过程中，ChatGPT 会使用 BPE 算法将大量的文本资料拆分成基本的 “字和词(token)”，这些字和词还会有一个唯一的 ID。
如果觉得不能理解，可以回过头去看上一章节的内容。
## 句子是怎么产生的？[](https://gptpmt.com/preface/basics_probability#句子是怎么产生的)
现在，ChatGPT 已经拥有了足够多的 token，但它是如何把这些 token 组装成句子的呢？
思考一下人类说话的过程，当我想表达自己喜欢一个东西的时候，我会说：
Luffy
```
我喜欢gptpmt
```

这一切看起来那么的简单和自然，但是对于计算机来说无比的复杂。以中文为例，常用的汉字有 3500 个，哪怕让它们两两组合，都可以产生 2^3500 次方个组合，计算出来的结果大概是这样的：
2的3500次方计算结果
```
402702961953621844286950607555369624422784868935557056881131335461307658701727371551406721502307932123276358395008895125652
043531209418099658895323804953421455502359439932416245276659698167468088937570774479761417692998541764456595941884384880600
102787969744607942278005344329659944902212055120534831056155566296908941240558524043054812784309119298489621361046430678313
566109525110538452853054430839857155846105630169165566758950183947324955260740763926892668470396323574248496692684009312249
052922911490770564765036629340924434941440277974966684311625406958698534967519709470161586090763966964691950363765288731535
684692199342872936240602328625671612857527958722799557444770545725755417136296135977255647153119878181440110593529655379472
903525700943247456832124407971558524965730661045026185674462056105044630573746839553952570745211879290387589347246867522065
584726369942916093728137773105488374703562705889962546268226061545128021323184760695318697037612212579413382773618361971983
3273016852325232832105702331094682317528819996876363073536047370469376
```

这还仅仅只是两个字的组合，如果是三个字、四个字的组合，那么计算出来的结果就更恐怖了。而一个句子，几十个字；一段话几百个字；一篇文章几千个字。这样的组合是一个天文数字，比地球上的砂砾数量还要多。
计算机绝对不可能记忆并理解每个句子或每个词的意思，那我们如何让计算机正确回答我们的问题呢？
这在过去困扰了人们很久，而 GPT 使用了一种非常巧妙和简单的方法。
还记得上节课我们说的：人类是一个字一个字，一个词一个词的说话吗？
ChatGPT 在使用 BPE 算法将大量文本内容拆分成 token 的时候，还会给每个 token 一个概率，当我们组装一个句子发给 ChatGPT，它就会调用自身的模型询问：这句话的下一个 token 应该是什么？
例如：
Prompt
```
I love
```

ChatGPT 内部会拿着 `I love` 去请求自己的模型，并得到一个 token 的列表，因为是英文，我们得到的可能刚好是一个英文单词：
I love
```
"you" - 概率约为 0.15
"it" - 概率约为 0.08
"him" - 概率约为 0.06
"her" - 概率约为 0.05
"this" - 概率约为 0.04
```

ChatGPT 会随机选择一个 token，例如选择了 `you`，这句话就变成了 `I love you`，然后 ChatGPT 会拿着`I love you`继续请求自己的模型，再次得到一个 token 列表：
I love you
```
"too" - 概率约为 0.20
"so" - 概率约为 0.10
"more" - 概率约为 0.08
"very" - 概率约为 0.06
"always" - 概率约为 0.05
```

假如选择了 `too` 继续：
I love you too
```
"." - 概率约为 0.40
"!" - 概率约为 0.10
"," - 概率约为 0.08
"!" - 概率约为 0.05
"!" - 概率约为 0.04
```

假如选择了 `.` 继续：
I love you too.
```
"<eos>" - 表示句子结束的特殊token，概率约为 0.80
"!" - 概率约为 0.05
"?" - 概率约为 0.04
"," - 概率约为 0.03
"..." - 概率约为 0.02
```

假如选择了 `<eos>`，ChatGPT 就会把最终的话返回给我们：`I love you too.`
整个过程是 ChatGPT 内部的匹配机制，无论我们发送什么 Prompt 过去，ChatGPT 都是一个 token 一个 token 匹配的过程，最终返回给我们一段完整的内容。
ChatGPT内部处理过程
```
I love
I love you
I love you too
I love you too.
<eos>
```

这个处理过程我们是看不到的，最终只能看到它输出了 `I love you too.`，但我们要清楚它内部是这么处理的。
## 温度(temperature)[](https://gptpmt.com/preface/basics_probability#温度temperature)
一个有意思的猜想：ChatGPT 每次都是选择概率最高的那个 token 吗？
我们来试一下。
Prompt
```
从前有一个小王子
```

ChatGPT
```
从前有一个小王子，他生活在一个遥远的星球上。这个星球很小，上面只有一朵玫瑰花和一颗火山。
小王子对他的玫瑰花非常宠爱，花朵也对他展示出骄傲和娇气的性格。但小王子感到孤独，他渴望探索更广阔的世界，于是他离开了自己的星球。
他开始了一段冒险之旅，途中他遇到了各种各样的奇特和有趣的生物，包括一只狐狸和一位善良的飞行员。通过和这些生物的相处，小王子学到了许多关于友谊、爱和责任的重要教训。
在他的旅程中，小王子来到了地球，他遇见了各种不同类型的人类，包括一个自大狂的国王、一个贪婪的商人和一个渴望权力的人。这些经历让小王子对人类的行为感到困惑和悲伤。
最终，小王子明白了真正的价值和意义，并且渴望回到自己的星球，重新与他的玫瑰花相聚。他意识到，真正重要的东西不是外在的物质，而是心灵的纯净和真挚的情感。
小王子的故事以一种寓言的方式传达了成长、人性和爱的主题。它提醒我们关注内心的声音，珍惜真挚的情感，并在追求物质财富的过程中不要忘记自己真正的目标。这个故事至今仍然深受人们喜爱，它带给读者们许多关于生活和人性的启示。
```

![ChatGPT聊天](https://gptpmt.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbasics_probability1.dc817d51.png&w=1920&q=75)
可以看到 ChatGPT 输出了一大段内容，如果我们再发送同样的 Prompt 给它会发生什么呢？
为了保证测试不受上一次数据的影响，我们需要 **新开一个** ChatGPT 聊天窗口。
Prompt
```
从前有一个小王子
```

ChatGPT
```
从前有一个小王子，他来自一个遥远的星球。他的星球非常小，上面只有一朵玫瑰花和一些奇特的小动物作为陪伴。
小王子对他的星球感到厌倦，他渴望冒险和新的经历。于是他决定离开家乡，去探索宇宙的奥秘。
他穿过了一个个陌生的星球，遇到了各种各样的人和事物。他遇到了一个自大狂妄的国王，一个贪婪的商人，一个自以为是的地理学家，还有一个酒鬼。
然而，小王子最珍惜的是他在一颗小行星上遇到的一只狐狸。他和狐狸成为了朋友，并且学到了一些重要的人生智慧。狐狸告诉小王子，只有用心才能看清真正重要的事物，而且只有与某个人建立了深厚的情感关系，这个人才会变得独一无二。
小王子也在地球上遇到了一个飞行员，他们成为了好朋友。飞行员帮助小王子修理了他的飞船，并且与他分享了许多关于人类的故事和思考。
最终，小王子决定回到自己的星球，重新和他那唯一的一朵玫瑰花团聚。他明白了对于他来说，家庭和友谊才是最重要的东西。
小王子的故事告诉我们要珍惜身边的人和事物，用心去体验生活中的美好，而不是追求无尽的追求和物质财富。他的冒险经历让他成长，并且让我们思考人类存在的意义和价值。
```

![ChatGPT聊天](https://gptpmt.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbasics_probability2.83339419.png&w=1920&q=75)
我们发现两次输出的内容虽然一开始有些相似，但后面的内容就不太一样了。如果真的 ChatGPT 默认就选择概率最高的 token，那按理说每次输出的结果都是一样的。
所以结果只有一个可能：ChatGPT 的概率并不是固定的。
这一点在 OpenAI 的官方文档里也能找到答案：
### 为什么模型的输出不一致？[](https://gptpmt.com/preface/basics_probability#为什么模型的输出不一致)
![ChatGPT temperature](https://gptpmt.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbasics_probability3.a66156dd.png&w=1920&q=75)
文档里提到了一个有意思的参数：temperature，中文直译过来可以称为：温度。
[官方文档：Why are model outputs inconsistent? (opens in a new tab)](https://platform.openai.com/docs/guides/gpt/why-are-model-outputs-inconsistent)
### 温度的作用？[](https://gptpmt.com/preface/basics_probability#温度的作用)
![ChatGPT temperature](https://gptpmt.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbasics_probability4.4e100447.png&w=1920&q=75)
[官方文档：Understanding tokens and probabilities (opens in a new tab)](https://platform.openai.com/docs/quickstart/adjust-your-settings)
不难看出，temperature 的作用是来控制结果的多样性的，temperature 越高，结果的多样性越大，temperature 越低，结果的多样性越小。
当我们想要 ChatGPT 每次都给一个匹配度最高的结果时，可以将 temperature 设置为 0，这将大概率得到概率最高的结果，多次发送 Prompt 得到的结果也大概率是一致的。
如果我们想要 ChatGPT 输出的内容更多样化，例如在 文案、创意素材 生成方面，就可以把 temperature 设置为 0.7 或 0.8 以获得更高的创造力。
### 如何调整温度？[](https://gptpmt.com/preface/basics_probability#如何调整温度)
temperature 范围：**0~2** ，通常建议设置为 0.7，当 temperature 超过 1 的时候，结果会非常的随机，几乎无法正常使用。
假如我们使用的是 ChatGPT 网页版，默认的 temperature 是**0.7** ，所以 ChatGPT 网页聊天还是非常具有创造力的。但遗憾的是这个值我们无法修改，这是在调用 OpenAI 接口的时候，接口中有一个 temperature 的参数，通过这个参数可以传递具体的值。
如果你不是一位开发者，**不用担心** ，了解了这个原理将帮助你更好的使用 ChatGPT 解决各种问题。如果你是一位开发者，并已经在使用 OpenAI 的接口，可以尝试调整一下 temperature 的值，或许对你的结果会更有帮助。
💬
恭喜学完本章节，欢迎到 [Github issues (opens in a new tab)](https://github.com/CarGod/gptpmt/issues/new?labels=feedback) 发表学习心得以及反馈问题 👏🏻
微信扫码关注公众号，开启专属于你的
Ai 新纪元
🎉
现在关注，获取最新更新通知，免费解锁更多粉丝专属福利～
![车神大讲堂-微信公众号](https://gptpmt.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fofficial-wechat.616d90eb.png&w=1920&q=75)
Last updated on 2024年5月21日
[什么是Tokens？](https://gptpmt.com/preface/basics_token "什么是Tokens？")[基础篇](https://gptpmt.com/foundation "基础篇")
中文
System
Copyright © 2023 Luffy Liu
