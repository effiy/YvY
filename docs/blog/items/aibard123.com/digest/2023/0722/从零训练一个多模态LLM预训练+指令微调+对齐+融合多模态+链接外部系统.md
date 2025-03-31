# 原始 URL: https://aibard123.com/digest/2023/0722/从零训练一个多模态LLM预训练+指令微调+对齐+融合多模态+链接外部系统/

# 抓取时间: 2025-03-30 21:40:06

[ AI 文摘 ](https://aibard123.com/digest/)
从零训练一个多模态 LLM：预训练+指令微调+对齐+融合多模态+链接外部系统

- By [AiBard123](https://aibard123.com/about)
- July 22, 2023 - 2 min read

![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1HO1knXr40pyPibibGnjoic5pEiarmUIkpIhAdBtHssVlAnNddun41icKibIg/640?wx_fmt=png)
作者： AINLP 来源： [AINLP](https://mp.weixin.qq.com/s/JSW5vkKppp_bhzeUm45cBw)
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_jpg/nW2ZPfuYqSJuK8UUBxdZXj1c20hUg374YPgXibgDGytAy87YxvVk4WCRFWrdKJPshStrlPJp4vGEGUQodxt7ibOw/640?wx_fmt=jpeg)
作者：逃脱鱼子酱
原文链接：https://zhuanlan.zhihu.com/p/643611622
本文尝试梳理**一个完整的多模态 LLM 的训练流程** 。包括模型结构选择、数据预处理、模型预训练、指令微调、对齐、融合多模态以及链接外部系统等环节。

#### 一、准备阶段

#### 1 模型结构

目前主要有三种模型架构，基于 Transformer 解码器，基于 General Language Model，以及混合专家模型。这一步可以直接选择开源的的基座模型，例如基于 Transformer 解码器架构的 LLaMA 模型族，模型结构及一些重要参数如下图。假设选择 LLaMA-65B，Tokenizer 选择 LLaMA 的基于 BPE 算法构造的 tokenizer。如果想要扩展词表，可以在目标语言上训练好词表后和 LLaMA 的词表 merge 在一起。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1kaB1FBCmMPEpibZmYIcEy8uPNRPOOEc9qAhvyz66bGGtjEx9rtLVorw/640?wx_fmt=png)

#### 二、预训练数据

#### 1 数据源

根据 Chinchilla 的 scaling law，要达到最优的计算利用率，65B 模型对应的训练 token 数量应该达到 1.4T。当前用于训练 LLM 的数据来源很多，但其中的高质量数据有限，该数据是提升模型性能的关键。另外，有文章指出，代码数据有助于提升模型的推理能力。因此，需要混合多种数据来源的数据，并合理分配每周数据的占比。如下图，可以参考 LLaMA 的数据源和比例，其中 Disk size 表示可用的数据总量，Sampling prop 表示在总训练 token 中的占比，epochs 表示采样的次数。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1l78xT0GoqmezO0L2Eia90A3826xx2H3BXMjT1W3jruX3F8c0Ez2tECg/640?wx_fmt=png)

#### 2 数据处理

想要提升模型的性能，除了利用已有的开源数据集，例如 The Pile，C4，OSCAR 等，还可以自己构建数据集。在论文 RefinedWeb 中提到，从网页数据中创建的数据集也可以达到和精心收集的数据集同等的效果。Wikipedia，Books，GitHub，ArXiv，以及 StackExchange 等高质量数据的处理方法可以参考论文 The Pile 。下面介绍从 Common Crawl 构建数据集的方法，CC 是一个海量的、非结构化的、多语言的网页数据集，拥有超过 8 年的网络爬虫数据集，包括原始网页数据（WARC）、元数据（WAT）和文本提取（WET）。每个月都会发布包括一个 20~30 TB 未压缩纯文本的快照，包含了随机搜索和采样的 URL 所获得的网页，不同月份发布的数据之间只有非常少量的数据重合，8 年以来所有爬下来的数据总和是 PB 级别的。如下图，数据处理流程包含文档准备，过滤以及去重三个步骤，做法参考 RefinedWeb 论文。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1iabwhiahBI5uEuGA7bH03ttbJmNP8tak76U19jq3WBLX8kAx3JGN4Kjw/640?wx_fmt=png)

#### 2.1 文档准备

包括数据读取、过滤 url、提取文本和语言识别；
**数据读取**
文本数据既可以从 WET 文件也可以从 WARC 文件中读取。直接使用 WET 文件可以省略从 HTML 文件中提取文本的工作，但是包含一些不相关信息。因此可以从 WARC 文件中读取文本。
**过滤 URL**
在正式处理文本数据之前，首先要对 URL 执行第一次过滤，过滤的目标是欺诈和成人网站(主要是色情、暴力、与赌博有关的网站等)。基于两个规则进行过滤：(1)一个包含 460 万个域名的屏蔽列表；(2) URL 评分，基于收集到的特定单词列表，并按严重程度进行权衡。同时，可以按照需要过滤掉包含在高文本数据集中的数据来源，例如 Wikipedia 和 arXiv 等。
**提取文本**
目的是提取 HTML 页面中的主要内容，忽略菜单、页眉、页脚和广告等。可以采用 trafilatura，jusText 等库，结合正则表达式进行文本提取。最终将新行限制为连续的两行，并删除所有 URL 链接。
**语言识别**
语言识别可以在去重之前也可以在去重之后进行。但当文档数量比较少的时候，先识别会导致部分语言分类错误。可以采用 fastText 语言分类器进行语言分类，该分类器是在 Wikipedia、Tatoeba 和 SETimes 上面训练的，使用 n-grams 来作为特征，并采用层级 softmax，支持 176 种语言的分类，最后输出一个 0~1 的分数。删除最高语言分数低于设定阈值的文档。通过改变阈值，可以调整保留的文档比例。

#### 2.2 过滤

从网页提取的文档质量低下，过滤的目的是移除重复段落，无关内容，非自然语言等等，提高文本质量。包括文档级别和行级过滤；
**包含重复的文档移除**
可以在去重阶段进行，但在早期进行代价更低，也更容易。一般采用启发式方法，制定一系列规则删除任何具有过多行、段落或 n-gram 重复的文档，做法可以参考论文 BLOOM 。
**文档过滤**
主要的目的是保留人类写给人类的自然语言文档，移除机器生成的垃圾邮件，主要由关键字列表、样板文本或特殊字符序列组成。这样的文档不适合语言建模。采用质量过滤启发式算法，做法可以参考论文 BLOOM。重点是根据文档长度、符号与单词的比率和其他标准方面去除异常值，以确保文档是由真正的自然语言构成。
**行级过滤**
通过 trafilatura 库提取的文本避免了大部分无关的内容，但仍然有遗漏。通过一个线性校正过滤器继续过滤和正文无关的内容(例如点赞数，导航按钮等)。

#### 2.3 去重

过滤之后，数据质量得到了提高，但很多文档是重复的。可以通过模糊文档匹配和精确序列删除对文档进行去重。
**模糊去重**
可以采用 SimHash，MinHash 算法删除相似的文档：对于每个文档，计算其与其他文档的近似相似性，并删除高重叠的文档对。通过更改哈希算法的参数，可以调整去重的比例。
**精确去重**
一般采用精确子字符串去重，是序列级去重。通过使用后缀数组查找字符串之间的精确匹配，删除重复超过给定阈值的连续 token 的段落。
**URL 去重**
进一步删除跨 CC 转储重复访问的 URL。

#### 二、模型预训练

基于 Transformer 解码器架构的 LM 的预训练的方法是让模型做 Next Token Prediction 任务。基于 GLM 的 LM 的预训练方法是让模型做自回归空白填充任务。LLM 由于规模大，权重维度高，参数量以及数据量多，因此会带来训练不稳定，难以收敛，耗时长，计算资源庞大等问题。下面从模型结构和训练技巧方面介绍一些提升模型的训练速度以及提高训练稳定性的方法。

#### 1 结构改进

采用 Pre-normalization， 例如 RMSNorm，在残差连接前对参数归一化，有一部分参数直接与后面的参数相加，可以防止梯度爆炸或消失。用 SwiGLU 激活替代 ReLU，提高模型性能。相较于常规的绝对位置编码，相对位置编码在长序列上性能更好，例如 RoPE 和 ALiBi 编码方法。常规的自注意力查询需要大量的计算和存储资源，通过采用 Multi Query Attention 和 Flash Attention 可以减少计算，提升训练速度。

#### 2 训练技巧

具体方法可以参考之前的模型训练篇：大规模语言模型（LLMs）预训练-大模型加速。首先可以采用混合精度减少计算量，即模型权重以及梯度使用 float16 表示，优化器使用 float32 表示参数；同时进行通信和计算，提高训练效率。
如下图，当 LLM 由于规模庞大，无法在单张 GPU 上运行或者单卡的利用率低时，需要采取并行策略加速训练。首选张量并行，其次是进一步结合流水线并行。在计算资源丰富的情况下，进一步结合 ZeRO 数据并行实现 3D 并行，多张 GPU 并行训练，参考论文 Megatron-Turing 和 BLOOM。
在单卡显存不足时，还可以结合一些小技巧，例如 CPU offload 技术，将计算的中间激活结果暂时放到内存（CPU）中，需要的时候再放回显存（GPU）中，用额外的通讯开销换取显存；或者采用 checkpointing (recompute)，在前向传播时，删除一些暂时用不到的中间激活结果以降低存储空间，在反向传播时，再根据需要临时进行前向计算或者从 checkpoint 中加载。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1qaJJRW1ySvYKSR8C2DFKmIsicQjIRZfBHuevl5SibDngulg6cg9vVibYw/640?wx_fmt=png)

#### 3 评测

预训练之后，需要评价模型的性能。LM 的常用评价指标 PPL 主要用于评价 LM 生成的句子是否流畅和通顺。除此之外，更重要的是评测 LLM 的知识蕴含能力，包括常识推理，问答，代码处理，数学推理，阅读理解等多种能力。

#### 3.1 prompt 设计

和以往专家模型的“预训练+微调”范式不同，当前 LLM 主要采用“预训练+上下文学习”的范式，因此需要对每个下游任务选择合适的 prompt 模板，帮助模型回忆起自己预训练学到的知识，做到下游任务和预训练任务的统一。模板结构是一个文本字符串，有两个槽：一个输入槽 [X]，用于输入问题，一个输出槽 [Z]，用于中间生成的答案文本 Z。在实际操作中，为了让模型理解任务，用问题和答案填充模板得到几个学习样例。然后用实际输入填充模板并和学习样例组合起来，得到完整的 prompt 一起输入模型。在情感分析任务中，模板的形式可以采用"[X], it is [Z].”。假设 x=“I like this dish”，则完整的 prompt 则是“I like this dish, it is [Z].”。填充的答案在文本中间称为完形填空提示（cloze prompt,），在文本末尾称为前缀提示（prefix prompt）。然后将生成的答案转换成任务需要的输出。下表展示了更多的示例。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_jpg/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1w2GgNXAII7ITutv1bI90ZsgBWNPDoUaFPmsy53Ye5pLFbdianIRu01g/640?wx_fmt=other)

#### 3.2 评测基准集

参考论文 LLaMa，主要从以下几个方面评价模型的性能：常识推理（BoolQ、PIQA、SIQA、HellaSwag、WinoGrande 、ARC easy 和 challenge 以及 OpenBookQA ），闭卷问答（Natural Questions 和 TriviaQA ），阅读理解（RACE 阅读理解基准），数学推理（MATH 和 GSM8k），代码生成（HumanEval 和 MBPP），大规模多任务语言理解基准 MMLU ，该基准集由多项选择题组成，涵盖了人文科学、STEM 和社会科学等各个知识领域，以及 C-Eval（一个中文知识能力测试数据集，涵盖 1.4 万道选择题，共 52 个学科。在该数据集用于评测模型的中文能力）。

#### 三、自然语言众包指令微调

经过预训练之后的 LLM 具有广泛的知识储备，拥有强大的自然语言推理和代码处理能力。但在某些任务上的 Zero-Shot 能力很差。为了进一步提高 LLM 在未见任务上的指令泛化能力，即 Zero-Shot 能力，需要在自然语言众包指令数据上微调预训练模型，参考论文 FLAN 。微调数据集来自于通用的 NLP 基准集，通过指令模板改造输入输出的格式得到 CoT 和非 CoT 任务的指令数据集，见下图。微调后可以显著提高在各种模型类(PaLM、T5、U-PaLM)、各种学习样例设置(Zero-Shot、Few-Shot、CoT)和各种未见评估基准(MMLU、BBH、TyDiQA、MGSM、开放式生成、RealToxicityPrompts)上的性能。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1kTibMFcdC1BzMkPiaaUvDmbmmpaNkeUCqw3WQzuPAa42BiaZJfNe6ZxicA/640?wx_fmt=png)

#### 1 数据集构造

从自然语言总包收集的一共 1836 个数据集，分为 Muffin、T0-SF、NIV2 和 CoT 推理四个任务集。然后将每条数据使用任务创建者给出的模板改造成指令 prompt 形式，举例来说，针对同一个翻译任务，普通 prompt：“我带女朋友去桂林旅游” 的英文翻译是**\_；指令 prompt：翻译这句话：输入：我带女朋友去桂林旅游，输出：**\_\*\*\*\*。下面给出 CoT 推理指令 prompt：
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1z53QxKj357nrIP2puSSe6hVVsNjYHOc4voofkzr1o1Wiad27B8oEkBw/640?wx_fmt=png)

#### 2 微调

将多个样例组合在一起得到单个序列，直到满足最大序列长度，做 Next token prediction 训练。

#### 3 评测集

目的是评测指令微调后的模型在未见任务上的泛化能力。评测集包括：（1）MMLU，来自数学、历史、法律和医学等 57 个领域的试题。(2) BBH，来自 BIG-Bench 的 23 个具有挑战性的任务；(3) TyDiQA，一个跨 8 种不同语言的问答基准集；(4) MGSM，数学单词问题的多语言基准集。

#### 四 对齐

该步骤的目的是使模型和人类对齐。通过使用用户的真实反馈对模型训练（SFT / RLHF），使 LLM 的输出更符合人类偏好，并与用户意图保持一致。这既包括明确的意图，如遵循指示，也包括隐含的意图，如保持诚实，不偏见，或其他有害的价值观。最关键的是步骤是收集真实多样的指令以及回复，得到指令跟随数据集（问答形式）。同时，可以混合一些对话形式的指令跟随数据（把之前发生的所有对话都写进下一个问题的提示中），让 LLM 能够以对话形式和用户交流。

#### 1 SFT

首先收集大量的<指令，回复>数据对，得到一个指令跟随数据集。然后用指令数据集通过有监督的方式对前面训练得到的 LLM 进行指令调优，得到 SFT 模型。到这一步得到的 SFT 模型已经能实现和人类很好的对齐。

#### 1.1 数据集构造

InstructGPT 的做法是搜集大量用户提交到 API 接口的查询，并耗费巨资聘请专业团队给用户查询生成回复，得到指令跟随数据集。但这种做法基本很难复现。除了用一些开源的指令数据集，例如 Alpaca 和 BELLE，也可以参照 self instruct 的方法让 ChatGPT 等高质量 LLM 构建想要的指令跟随数据集。具体的方法是先人工构造一些训练数据样例让 ChatGPT 看，利用 ChatGPT 的续写功能，让其不断地举一反三产生新的训练数据样例。
A. 首先人工构造丰富的种子任务，让 ChatGPT 学习并提出新的任务指令，如下图：![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1CTHGIgiaia0nWtXmtbWDQZ0aRePKojskTq65BjthkOlOn7kRcerR73Ug/640?wx_fmt=png)然后，让 ChatGPT 为提出的新任务根据人工构造的学习样例产生输入（问题）和输出（答案），得到新的训练数据样例：![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1ssEWrPhYyvfWkp4ibfrLLH6wnRo9Jy82qBJYjMaxxu0Sb5Eib88NCMqw/640?wx_fmt=png)最后，过滤掉一些低质量的数据样例，得到指令跟随数据集。
B. 进一步，可以参考论文 Evol-Instruct ，如下图，从一系列人工创建的指令开始，引导 ChatGPT/GPT-4 逐步生成更复杂的指令。然后，采用 ChatGPT/GPT-4 对进化得到的指令生成回复。进一步，混合所有生成的指令数据来微调语言模型。![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu13Ehia06pLiav37gVLWKKF9NbCG3Pj4sk599rSMfZSgQNTjjDkKdl6g5g/640?wx_fmt=png)
下图展示了一个 Evol-Instruct 的例子。从一个简单的初始指令“1+1=?”开始，使用 pprompt 提示 LLM 随机选择深度进化(蓝色指示线)或广度进化(红色指示线)，从简单的指令开始逐步增加难度。广度进化包括添加约束、深化、具体化、增加推理步骤和使输入复杂化。广度进化旨在增强主题覆盖、技能覆盖和整体数据集的多样性，使生成的指令是全新的，更加 long-tailed。由于进化的指令是由 LLMs 生成的，有时进化会失败，因此需要过滤掉失败的指令。重复这个进化过程几轮，以获得足够的包含各种复杂性的指令数据。![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu18OB5KibxrdTYBYryGFHI1BlZrRfIfUt8Z92xwDShicCHhowK7oLzicQAg/640?wx_fmt=png)

#### 1.2 微调

标准指令微调：将训练集中的所有提示和答案连接起来，使用一个特殊的 token 来分隔提示和答案片段，利用自回归目标，不计算来自用户提示的 token 部分的损失，只对回复的 token 进行反向传播。

#### 1.3 评测

评测的主要目的确保在对齐指令上微调后，SFT 模型在预训练阶段获得的通用能力以及上下文学习能力没有大幅下降。注意不能在一堆 benchmark 上看平均分数，因为平均值差异不大，并且很多任务没有代表性；只在核心的有区分度的 benchmark 评测，包括：知识蕴含能力（MMLU），推理能力（GSM8k / BBH ），代码能力（Human Eval / MBPP） 以及数学能力（MATH ）。另一方面，需要评测模型生成的回复是否和人类对齐。对齐能力可以通过人工评测，评价的内容包括真实性，有用性，无害性（helpfulness，harmlessness，honesty）等等，也可以通过一个足够大的，已经训练好了的 RM 进行评测。

#### 2 RLHF

为了实现更好的对齐，可以继续用强化学习训练 SFT 模型。收集一组真实的指令集合，用 SFT 模型对每条指令生成回复，基于标注人员对回复按照多个指标进行人类偏好排序。用排序结果训练一个符合人类偏好的打分模型（Reward Model, RM）。最后，使用 PPO 算法用 RM 的打分优化 SFT 模型。

#### 2.1 Reward Model

一种方法是参考论文 InstructGPT ，将 SFT 模型作为初始模型，移除最后的非嵌入层，训练打分模型接收指令和回复，输出标量的奖励分数。训练数据是输入指令相同，但回复不同的比较数据（接受或拒绝）。使用二元排序损失，将不同的回复作为标签，奖励分数的差异代表了人类标记者更喜欢一种回复的对数几率。如下图，首先收集一些真实的用户指令，让 SFT 模型生成回复，利用专家根据相关性、信息性和有害信息等标准对回复进行排序。然后用排序结果训练一个打分模型。训练的的方式是对于一组训练数据，假设人工排序中回复 1 排在回复 2 前面，那么训练的目标是鼓励 RM 模型对<指令,回复 1>的打分要比<指令,回复 2>的打分更高，这样训练出来的打分模型和标注人员的偏好一致。打分模型的规模应该尽量大，例如用 175B 的 RM 去 PPO 7B 的 SFT 模型。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu13Ae5me2n2ZKLDtlhLzdibX8PUH4uy2NJiaIOp4JEwA3AuFzRyOniaNVYg/640?wx_fmt=png)
另一种做法参考论文 Anthropic LLM ，通过三个阶段的训练，包括语言模型预训练，偏好模型预训练，以及偏好模型微调。首先在大规模语料上进行语言模型的预训练，这一步直接采用指令微调后得到的 LLM。然后从 StackExchange/Reddit/Wikipedia 等获取混合对比数据集，进行偏好模型的预训练。最后在人类反馈对比数据上进行微调，训练符合人类偏好的打分模型。在第二、三阶段的训练时，在样本的末尾附加一个特殊的“上下文结束”标记，作为预测的得分。

#### 2.2 PPO

以 SFT 为初始策略，基于 RM 对策略打分，使用强化学习优化策略，得到强化版本的模型 PPO。训练的目标是使得 PPO 生成的答案能够获得高回报。训练的方法是根据 RM 的打分来更新 PPO 的参数。为了防止模型被 RM 过度优化，需要在奖励中增加了一个 KL 惩罚，保持学到的模型 PPO 与初始策略 SFT 模型相差不至太远。同时，可以在优化目标的梯度中混入一些预训练梯度，进一步保证学习到的模型保留 SFT 的通用能力。具体的方法可以参考论文 instructGPT。

#### 2.3 在线 PPO 训练

随着 SFT 被优化，得到的 PPO 模型生成的回复越来越符合人类偏好，最开始训练得到的奖励模型在这种高质量回复上不够鲁棒。为了缓解这个问题，参考论文 Anthropic LLM，可以进一步采用在线迭代训练：使用每一轮强化学习得到的最好的 PPO 模型生成比较数据进行人工标注。将新的比较数据与已有的数据混合，重新训练一个新的奖励模型，最后用新的奖励模型进行新一轮的 PPO 训练。

#### 2.4 评测

参考 SFT 环节的评测。

#### 五、融合多模态

为了进一步让 LLM 获得图像理解能力，需要在 LLM 中融合多模态。一种做法是利用预训练的大型语言模型以及视觉编码器来构建多模态的统一模型。

#### 1 模型结构

参考论文 LLaVA ，MiniGPT-4 ，BLIP2 和 mPLUG-Owl ，模型结构如下图所示，由一个视觉编码器，一个投影层，一个语言模型（前文训练好的 LLM）构成。视觉编码器的作用是提取图像特征，一般采用 ViT-L/14。投影层的作用是实现视觉特征空间和文本特征空间的对齐，可以选择简单的线性层，也可以选择更加复杂的结构，例如 BLIP2 中的 Query Transformer（Q-Former），该结构的作用是使用一组可学习的查询向量从冻结的视觉编码器中提取视觉特征，以充当视觉编码器和文本编码器之间的瓶颈。也可以参考论文 mPLUG-Owl，使用一个视觉抽象模块替换投影层，将视觉基础模型提取到的稠密的视觉特征汇总到几个可学习的令牌中，从而获得更高的语义视觉表示并减少计算。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1HO1knXr40pyPibibGnjoic5pEiarmUIkpIhAdBtHssVlAnNddun41icKibIg/640?wx_fmt=png)

#### 2 视觉特征空间和文本特征空间的对齐

#### 2.1 数据集构造

训练数据是来自多个数据集的图像标题对数据，包括 LAION-400M、COYO-700M、Conceptual Captions 和 MSCOCO 等。

#### 2.2 模型预训练

第一阶段的预训练是为了使视觉模型能够有效地捕获低级和高级语义视觉信息，并将其与预训练的语言模型对齐，而不影响语言模型的性能。在训练时，冻结视觉编码器和 LLM 的参数，只改变投影层的参数，训练的目标是使得视觉编码器提取到的视觉特征和 LLM 嵌入层得到的文本嵌入对齐。比较简单的训练方式是将图像输入视觉编码器，将经过投影层提取到的文本视觉信息输入 LLM，让 LLM 做 Next token prediction，生成图像标题。另一种方式是预先构造一些让 LLM 简单描述图像信息的指令，在训练时，从其中采样指令和视觉特征一起构造成指令 prompt 输入 LLM，让 LLM 生成图像标题。

#### 3 对齐

在完成前一阶段后，模型能够获取图像的文本知识并对人类的查询产生响应，但在产生连贯的语言回复方面仍然存在挑战。需要在图像-文本指令跟随数据上进一步微调，以促进模型与人类指令和意图之间的更好对齐。

#### 3.1 数据集构造

可以直接利用开源的数据集，例如 LLaVA。也可以通过 self instruct 的方式，引导 GPT-4/ChatGPT 等高质量的多模态模型生成图像-文本指令跟随数据，用来训练多模态语言模型，将 ChatGPT 的知识蒸馏到自己的模型上。
参考论文 LLaVA。首先从预训练数据中采样一些图像-文本对作为原始数据。然后，人工构造多种形式的指令并标注一些图像-指令跟随数据作为学习样例。对于每个原始数据，采样一些指令和标注数据，让 GPT-4/ChatGPT 根据图片信息（包括 Captions 和 Bounding boxes）生成对应的回复，构造图像-文本指令跟随数据集。构造的数据形式包括三种：对话，详细的描述以及复杂的推理。下面给出一个引导 GPT-4/ChatGPT 生成对话数据的实例。
首先人工构造一些学习样例，如下图：
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1mFZLyvq8nlw95aWXpGpEgN9JG4eDN6xAoKWocs6f1CrDge199D9dibw/640?wx_fmt=png)
然后，将采样的学习样例和指令、以及图片信息一起按照指令 prompt 的格式组合在一起输入 GPT-4，让其生成对应的回复，如下图：
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1wKL9cF4nKQgUg5yx6bI2ou3FvhKAT4LbflvItGPQiaKiaO72Ouv1IOqg/640?wx_fmt=png)

#### 3.2 微调

保持视觉编码器的权值不变，更新投影层和 LLM 的权值。训练的方法是让模型做 Next token prediction。针对普通问答数据和对话数据有两种不同的训练方式。
问答数据的方法参考论文 MiniGPT-4，输入如下格式的指令 prompt，让模型生成回复，其中 ImageFeature 代表经过投影层变换的图像特征。

```
###Human: <Img><ImageFeature></Img> <Instruction> ###Assistant:

```

对话数据首先要将收集到的指令跟随数据改造成以下格式，该对话有两轮，每轮都包括一个指令和回复。在训练时，让模型预测图中绿色的部分。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1RN07nyKxe5j1qOjFAqw3p0EKRVhQrfFZevYyBdryI8fDVFxIuTnicnw/640?wx_fmt=png)

#### 4 评测

可以利用 GPT-4 来衡量目标模型生成的回复的质量。让目标模型以及 GPT-4 根据问题、ground-truth 边界框和标题分别生成回复。然后将问题、视觉信息(以标题和边界框的格式)以及两个回复一起输入 GPT-4，让 GPT-4 根据回答的有用性、相关性、准确性和细节等方面从 1 到 10 分进行打分。并且要求 GPT-4 提供一个全面的解释，以便更好地了解目标模型。

#### 六、链接外部系统

经过前面几个步骤训练出来的多模态 LLM 已经具有非常强大的理解和推理能力，但仍然存在一些不足，例如无法获取最新的知识，容易产生虚假的输出，难以理解低资源的语言，缺乏数学知识等等，可以通过在模型中链接外部工具弥补其只能利用静态知识的限制。主要有两种方法，一种是通过提示将外部工具集成到 LLM 中，这种方法容易受到输入长度的限制。另一种方法是通过在<指令，API>数据集上有监督的微调 LLM，实现其在广泛 APIs 集合上的准确调用。

#### 1 基于微调的方法

#### 1.1

参考论文 Gorilla ，通过 self instruct 的方式让 GPT-4 生成大量的<指令，API>数据对 LLM 进行有监督的微调，实现其在广泛 APIs 集合上的准确调用，如下图。在推理时，LLM 输出的是某个要调用的 API，不涉及具体的执行过程。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1icicPwCBlZAIHDl2y0mByZUzOJWSCn8rwy9KQtCibYye8ldgsTuS6Ygiaw/640?wx_fmt=png)
**数据集构造**
API 数据收集：通过对 HuggingFace, Torch Hub, 以及 TensorFlow Hub 中的模型调用进行过滤，收集多个 API。然后，将每个 API 的模型卡转换为具有以下字段的 json 对象：{domain, framework, functionality, api_name, api_call, api_arguments, environment_requirements, example_code, performance, and description.}。指令数据构造：通过上下文学习的方法给出一些学习样例以及一个需要调用的 API 参考文档，提示 GPT-4 生成调用该 API 的真实指令。然后将<指令, API>改造成用户代理聊天式对话，如下图：
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1ynxReZDWuETibps4synVBV5XCLMPZbTm6xlXW6BrKOnU7wLbn29mEjg/640?wx_fmt=png)
**微调**
执行标准的指令微调。
**评测**
对同一个指令，存在多个正确的 API 调用，并且很难通过单元测试来判断正在使用的 API 是否在功能上等同于参考 API。一种方法是比较其与收集的数据集之间的功能等效性。为了追踪 LLM 调用的是数据集中哪个 API，采用 AST 树匹配策略，通过检查候选 API 调用的 AST 是否是参考 API 调用的子树可以确定使用的是哪个 API，如下图：
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1KMQm0YCBZl4Xic61eGqdenPcpTZWjBxCOlUfI3aFhtShXe7KnJ65tzQ/640?wx_fmt=png)

#### 1.2

参考论文 Toolformer ，不针对特定任务，让 LLM 自主决定调用哪些 API（包括计算器，问答系统，搜索引擎，翻译系统和日历）、何时调用它们、传递哪些参数以及如何最好地将结果合并到未来的 token 预测中。具体的方法是首先将纯文本数据集转换成一个扩充了 API 调用的数据集。这分几步完成，如下图所示：首先，利用 GPT-4 等的上下文学习能力对大量潜在的 API 调用进行采样。然后执行这些 API 调用，最后对产生的 API 调用进行过滤，产生增强数据集对 LLM 进行微调，过滤的原则是 API 调用以及回复是否有助于预测未来的 token。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu14CgaVu236VbibX785oVNQibsib7lhjrhyzAO6onl6bzdGkb5XCx3G6Gcw/640?wx_fmt=png)
**数据集构造**
首先定义了特殊字符“”, “” and “→”，如下图，通过上下文学习的方式，让模型生成包含 API 调用的句子。具体的做法是，对于输入文本的每个位置进行采样，如果输出的概率大于阈值，则作为候选位置。从候选位置中选出 top-k 个位置，执行调用，得到回复。最后，如果在输入文本的对应位置插入 API 调用及回复后对原始输入的后续 tokens 有积极作用，则保留。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1ZdqSuggYpZAdGXec2w9satBF6jqhPFjQfkAVGcwmtp2Po2Iyop9XzQ/640?wx_fmt=png)
**微调**
执行标准的指令微调。
**推理**
推理时，当 LLM 解码生成调用 API 的符号时，停止解码，启动 API 调用生成回复，当插入回复以及 token 后，继续解码。为了避免模型的生成陷入循环，每个句子只调用一次 API。

#### 1.3 评测

在具体的下游任务上评测。

#### 2 集成的方法

参考论文 HuggingGPT ，通过制定规则和提示模板，将专家信息用自然语言描述，使得 LLMs 能够调用专家模型解决任务。具体来说，通过将 LLM 链接到 Hugging Face 等公开 ML 社区，然后提取模型描述合并到提示中，LLM 作为管理 AI 模型(如计划、调度和合作)的大脑，调用这些外部模型来解决具体的任务。如下图所示，整个过程分为四步，包括任务规划，模型选择，任务执行以及回复生成。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1HOQUFP2dLLMoD1j40r4GicJB5FGKZ5cmdnDf2xtvoOOT0WFCGe4a74A/640?wx_fmt=png)

#### 2.1 任务规划

如表 1 所示，基于专用模板（由规范的指令和演示解析组成）提示 LLM 分析用户请求，将其分解为结构化任务的集合，包括任务的依赖关系和执行顺序，以构建它们的连接。

#### 2.2 模型选择

如表 1 所示，在解析了任务之后，LLM 根据模型描述选择托管在 huggFace 上的专家模型来执行任务。由于上下文长度限制，具体的做法是筛选出 top-K 个最相关的候选模型，将其模型描述写入 prompt 中，让 LLM 选择最合适的专家模型。

#### 2.3 任务执行

在选定模型之后，调用并执行每个选定的模型，并将结果返回给 LLM。由于先决条件任务的输出是动态生成的，因此还需要在启动任务之前动态地指定任务的依赖资源。

#### 2.4 生成回复

最后，利用 LLM 整合所有模型的预测并为用户生成回复。如表 1 所示，LLM 将前三个阶段(任务规划、模型选择和任务执行)的所有信息集成为这一阶段的简明总结作为生成的回复。
![](https://api.allorigins.win/raw?url=https://mmbiz.qpic.cn/mmbiz_png/gKaxjIx6baia46icjgRnLE9l1pkcGJSLu1fibfBgd3ze3qoZkNJGDqebLiaySwvlT85fIeuSmvTk7wtweficx8XPz5g/640?wx_fmt=png)
