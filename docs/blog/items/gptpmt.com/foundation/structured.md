# 原始 URL: https://gptpmt.com/foundation/structured

# 抓取时间: 2025-03-30 21:27:51

# 结构化 Prompt 模板与技巧

- [无规矩不成方圆](https://gptpmt.com/foundation/structured#无规矩不成方圆)
- [一个好的 Prompt 应该包含什么？](https://gptpmt.com/foundation/structured#一个好的prompt应该包含什么)
- [买一个牛肉饼](https://gptpmt.com/foundation/structured#买一个牛肉饼)
- [Prompt 标准化结构](https://gptpmt.com/foundation/structured#prompt标准化结构)
- [角色（Role）](https://gptpmt.com/foundation/structured#角色role)
- [技能（Skills）](https://gptpmt.com/foundation/structured#技能skills)
- [行动（Action）](https://gptpmt.com/foundation/structured#行动action)
- [限制（Constrains）](https://gptpmt.com/foundation/structured#限制constrains)
- [格式（Format）](https://gptpmt.com/foundation/structured#格式format)
- [示例（Example）](https://gptpmt.com/foundation/structured#示例example)
- [Prompt Engineer Assistant](https://gptpmt.com/foundation/structured#prompt-engineer-assistant)

## 无规矩不成方圆[](https://gptpmt.com/foundation/structured#无规矩不成方圆)

在正式开始本文之前，大家是否还记得在小学的时候，老师经常让我们给“李明”写信。开头往往是让我们写 `你好`，末尾有时还会加上 `此致敬礼` 等标识。特别是考试的时候，少一项就要扣两分。
那时总在想，为什么我们需要这么繁琐，直接像写小纸条那样写自己想说的话不好吗？
工作了以后经常需要写邮件，一开始没有按照那种固定格式去写，后来就发现有时候一着急就容易 **遗漏** 。不是漏了自己的名字，就是漏了日期，要么就是忘记向对方问候。
久而久之又重新开始像小孩子那样按照一种**固定格式** 去写，哪怕很忙很慌乱，也不会出错。
同样的道理也出现在各行各业，经常看到电视上护士和空姐的培训和考核。明明是一个很简单的事情，但他们总会按照固定的套路，确认这个确认那个，像在背顺口溜一样。
为什么要这样？
因为人非圣贤，总会有疏漏的时候，但如果有一套形成肌肉记忆的流程，哪怕慌乱也不会遗漏。
写 Prompt 也是一样，我们思考每一个 Prompt 都不可能面面俱到，总会遗漏一些东西，一旦有遗漏，就会导致这个 Prompt 的效果不好。
那我们有没有可能设计一个 Prompt 的模板，按照这个标准格式来写，就一定能不遗漏，并且达到最佳效果？

## 一个好的 Prompt 应该包含什么？[](https://gptpmt.com/foundation/structured#一个好的prompt应该包含什么)

前面我们讲了[**获得优质输出的六大技巧** (opens in a new tab)](https://gptpmt.com/foundation/grammar)，那是不是我的 Prompt 里面就要包含所有的东西，越详细越好吗？
记得《武林外传》中，燕小六经常说的一句话就是：“姓嘛？叫嘛？从哪来？到哪去？家里几口人？人均几亩地？地里几头牛？”，可以说是非常的具体了，但其实有很多信息是没必要的，过多的信息有时候反而会形成干扰。
我们要做的是：提取关键动作，以现实中的一个场景举例 **让张三帮忙买一个牛肉饼** 。

### 买一个牛肉饼[](https://gptpmt.com/foundation/structured#买一个牛肉饼)

假设一个场景

```
我想让朋友张三现在去楼下的罗森便利店，买两个7块钱的牛肉饼，加热好用纸袋分别装起来，20分钟之内帮我送回来。
```

这里面有哪些关键信息？
首先让谁去买，得有一个主人公吧，不能我站在人群里说：“帮我买两个牛肉饼”，张三也不知道说的就是他啊，万一是李四呢？ **角色**
时间和地点：不然张三明天去买，后天去买。或者不是楼下这家店，又或者是别的店。 **行动**
价格、物品名、数量：张三要知道自己买的是什么，多少个，多少钱。 **限制条件**
操作：需要加热。 **技能**
交付方式：两个分开装纸袋里。 **格式**
时限要求：20 分钟内。 **限制条件**
假如我直接告诉张三：“去帮我买点东西”，张三能按上面我心里想的，去楼下罗森买两个 7 块钱加热好的牛肉饼，分开装，并且在 20 分钟之内送过来吗？
不排除这个可能性，如果真这样，张三就太厉害了。
人尚且如此，那 AI 呢？思考一下我们现在很多时候是怎么用 GPT 的？假如我让想让它帮我写一篇小说，或者写一篇论文，就直接告诉它：帮我写一篇小说；帮我写一篇论文。
高级一些的，可能会说：你现在是一个作家，帮我写一篇科幻小说。
这跟我们让张三去买东西有啥区别，无非就是直接让张三去买东西和让张三去罗森买东西的区别罢了。那结果显而易见，大概率不是我们想要的。于是乎就有人觉得：这 AI 不行啊。
这还只是一个生活化的场景，在现实生活中我们也经常忘记这个忘记那个，会突然打电话给张三，告诉他刚才忘记了什么什么。在 Prompt 工程里，更容易出现遗漏，所以我们就需要一个满足所有大语言模型需求的 Prompt 标准化结构，基于这个标准化结构无论是 GPT 还是其他的大语言模型，都能很好的理解我们真正想要的是什么。

## Prompt 标准化结构[](https://gptpmt.com/foundation/structured#prompt标准化结构)

### 角色（Role）[](https://gptpmt.com/foundation/structured#角色role)

所有的大语言模型，都有一个庞大的知识库，当我们需要执行一个任务时，往往只需要某一个行业或某一个领域的专业知识。这时，其他领域的知识就会成为干扰因素，可能会把一些不相关领域的知识也加到结果里了。这显然不是我们想要的，所以在一开始就限制 GPT 的角色，可以起到屏蔽其他领域知识的作用，让 GPT 的知识库更加的纯粹。
这里就写你希望 GPT 扮演什么角色，例如：资深作家；法律顾问；拥有 15 年经验的 Java 开发工程师；用户评论打标器；资深市场运营 ...

### 技能（Skills）[](https://gptpmt.com/foundation/structured#技能skills)

有了角色，就要给这个角色配备技能。大语言模型除了拥有庞大的知识库以外，还有一个庞大的“技能库”，世界上有的技能，GPT 都有。那这么多的技能同样会对我们的结果造成干扰，所以直接限制它拥有什么技能是最好的做法。
这里就写你希望 GPT 拥有哪些技能，例如：分析总结能力；优秀的写作能力；Java 编码能力；市场分析能力；精通多国语言 ...

### 行动（Action）[](https://gptpmt.com/foundation/structured#行动action)

有了角色和技能，就要下达任务，告诉 AI 我们需要它做什么，行动是什么。
例如：基于用户的写作主题，创作科幻类型的小说；帮助用户检查代码中的错误；帮我总结会议内容，形成会议纪要 ...

### 限制（Constrains）[](https://gptpmt.com/foundation/structured#限制constrains)

用来限制 AI 的边界，防止输出一些不符合我们预期的内容。
例如：内容不超过 150 个字；使用中文回复；避免政治敏感内容；不确定的部分不要瞎编 ...
💡
还记得前面我们讲的内容吗？使用 GPT 来限制字数是不可靠的，这里的 150 个字只能让 GPT 尽可能的控制自己的输出长度，并不能保证一定是 150 个字以内，事实上大部分情况下都会远远超出 150 个字。

### 格式（Format）[](https://gptpmt.com/foundation/structured#格式format)

期望 GPT 输出的格式，可以是格式要求，也可以是一个格式示例。

### 示例（Example）[](https://gptpmt.com/foundation/structured#示例example)

可以通过一个示例，告诉 GPT 你想要的输出结果是什么样的，帮助它更好的理解你的诉求。
基于上面的格式，下面是一个示例的 Prompt：
Prompt

```
# Role
资深科幻小说作家
## Skills
- 丰富的想象力和创造力
- 熟悉科幻文学和相关领域的知识
- 能够进行有效的故事结构和情节设计
- 出色的文字表达能力
## Action
帮助用户构思和撰写科幻小说的内容，包括角色设计、情节发展、世界观构建等
## Format
文本格式，包括但不限于故事大纲、角色简介、情节段落等
## Constrains
- 请避免使用已有的科幻小说中的知名角色或情节
- 确保内容符合逻辑，即使是在构建的虚拟世界中
## Example
角色简介：艾尔是一名星际航行者，拥有读心术和时空穿梭的能力。他的使命是防止宇宙中的时间裂缝扩大，保护各个文明免受时空混乱的影响。
情节段落：在一次执行任务时，艾尔意外穿越到了一个未知的平行宇宙。在这里，他发现了一个正处于科技爆炸前夜的文明，但这个文明的发展方向却可能导致整个宇宙的毁灭。艾尔必须找到一种方法，既能引导这个文明走向繁荣，又不干预其自然发展的轨迹。
```

这里展示了一个基础版的结构化 Prompt 示例，或许对于很多同学来说，写这样一个 Prompt 还是会有难度，那有没有更简便的方法呢？

## Prompt Engineer Assistant[](https://gptpmt.com/foundation/structured#prompt-engineer-assistant)

考虑到这种情况，我为大家做了一个 GPT 的应用，只需要把我们的诉求告诉它，它就可以生成这样结构化的 Prompt。
事实上，上面的示例 Prompt 就是我通过这个 GPT 应用生成的。
大家感兴趣可以免费试用这个应用，分别在 GPT Store 商店，和 Coze 商店发布了该应用，大家可以根据自己的情况，选择合适的进行访问：
[GPT Store (opens in a new tab)](https://chat.openai.com/g/g-NggrHHU0O-prompt-engineer-assistant)
[Coze Store (opens in a new tab)](https://www.coze.com/store/bot/7337566244675289094)
使用示例：
![Prompt智能助手](https://gptpmt.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fstructured-1.b9d5f8a0.png&w=1920&q=75)
基于 AI 创作的初版结构化 Prompt，稍做修改就能满足日常大部分的使用场景了 🍻
