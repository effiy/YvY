# 原始URL: https://hub.baai.ac.cn/papers

# 抓取时间: 2025-03-30 21:40:08

[![](https://hub.baai.ac.cn/_nuxt/img/logo.a2943de.svg) ](https://hub.baai.ac.cn/)
[ 活动 ](https://hub.baai.ac.cn/events)[ 论文 ](https://hub.baai.ac.cn/papers)[ 风云人物 ](https://hub.baai.ac.cn/rankings)[ 专栏 ](https://hub.baai.ac.cn/)
  * [ 项目](https://hub.baai.ac.cn/projects)
  * [ 社交](https://baai.org/l/linklocal)


[![](https://hub-cache.baai.ac.cn/hub-banner/baai-banner.png)](https://baai.org/l/deepm)
取消
登录/注册
**已选（0/39）**
重选
  * #### 
热门主题
    * NLP
    * Rob
    * Multimodal
    * Embodied AI
    * Agent
  * #### 
领域
    * ML
    * CV
    * PR
    * AI
    * SEC
    * ImgVideo
    * Symbolic
    * HCI
    * DistComp
    * SoftEng
  * #### 
互动
    * 智源大会
    * 智源Talk
    * 智源专访
    * Workshop


社群
加入
[社区指南 ](https://hub.baai.ac.cn/view/259) 电话：(010) 5095 5974 邮箱：press@baai.ac.cn © 2024 北京智源人工智能研究院 ICP备案号：[京ICP备19012194号](https://beian.miit.gov.cn)
每天 0 点更新数据，热度根据全网互动数计算
最热 · 今天
  * 今天
  * 本周
  * 本月


最新
![](https://hub.baai.ac.cn/_nuxt/img/paper_bg.03eb463.png)
###### [VHELM: A Holistic Evaluation of Vision Language Models Tony Lee , Haoqin Tu , Chi Heem Wong , ... 2024年10月10日  ![](https://simg.baai.ac.cn/papers/converted_page_c3b5c242f1eaed9ad1431d2bc5323984-02.jpg) 目前评估视觉语言模型（VLMs）的基准往往集中在它们的感知或解决问题的能力上，而忽略了其他关键方面，如公平性、多语言性或毒性。此外，它们在评估程序和评估范围上存在差异，使得比较模型变得困难。为了解决这些问题，我们扩展了HELM框架到VLMs，提出了视觉语言模型的全面评估（VHELM）。VHELM聚合了各种数据集，涵盖了9个方面：视觉感知、知识、推理、偏见、公平性、多语言性、鲁棒性、毒性和安全性。通过这样做，我们提供了一个跨越这些重要因素的综合性、多维度的VLMs能力视图。此外，我们标准化了标准推理参数、提示方法和评估指标，以实现模型之间的公平比较。我们的框架设计轻量化和自动化，以便评估运行便宜快速。我们的初步运行评估了22个VLMs在21个现有数据集上，以提供模型的全面快照。我们发现了新的关键发现，例如，聚焦于效率的模型（例如，Claude 3 Haiku或Gemini 1.5 Flash）在偏见基准测试中表现显著劣于它们的完整模型（例如，Claude 3 Opus或Gemini 1.5 Pro），但在评估其他方面时则不然。为了透明度，我们在我们的网站上发布了原始模型生成和完整结果（https://crfm.stanford.edu/helm/vhelm/v2.0.1）。VHELM旨在成为一个活跃的基准，我们希望随着时间的推移继续添加新的数据集和模型。 **2422** 热度](https://hub.baai.ac.cn/paper/5253d223-cf0a-43e2-8828-150a4eef413f)
[CV](javascript:;)[AI](javascript:;)[PR](javascript:;)
PDF
解读
![](https://hub.baai.ac.cn/_nuxt/img/paper_bg.03eb463.png)
###### [Optimizing ML Training with Metagradient Descent Logan Engstrom , Andrew Ilyas , Benjamin Chen , ... 2025年03月18日  ![](https://simg.baai.ac.cn/papers/converted_page_d2b9feee6dbdcb1ae39db9be86d22494-15.jpg) 训练大规模机器学习模型的主要挑战之一是配置训练过程以最大化模型性能，也就是说，从巨大的设计空间中找到最佳的训练设置。在本研究中，我们提出了一种基于梯度的方法来解决这一问题。首先，我们引入了一种算法，可以高效地计算大规模场景下的元梯度（即通过模型训练过程的梯度）。接着，我们提出了一种“平滑模型训练”框架，该框架使得利用元梯度进行有效优化成为可能。通过元梯度下降（MGD），我们显著改进了现有的数据集选择方法，将抗精度退化的数据投毒攻击性能提升了数量级，并且自动找到了具有竞争力的学习率调度方案。 **780** 热度](https://hub.baai.ac.cn/paper/835937ed-178a-446b-ad49-13600b91c5e4)
[stat.ML](javascript:;)[AI](javascript:;)[ML](javascript:;)
PDF
解读
![](https://hub.baai.ac.cn/_nuxt/img/paper_bg.03eb463.png)
###### [Wan: Open and Advanced Large-Scale Video Generative Models WanTeam , : , Ang Wang , ... 2025年03月26日  ![](https://simg.baai.ac.cn/papers/converted_page_5c3cabf0674d34eb87bea3285c611b3a-04.jpg) 本报告介绍了Wan，这是一套全面且开放的视频基础模型集合，旨在推动视频生成技术的边界。Wan基于主流的扩散变换器范式构建，并通过一系列创新实现了生成能力的重大突破，这些创新包括我们提出的新型VAE、可扩展的预训练策略、大规模数据整理以及自动评估指标。这些贡献共同提升了模型的性能和灵活性。具体来说，Wan具有以下四个关键特点： **领先性能**：Wan的140亿参数模型在包含数十亿图像和视频的大规模数据集上进行训练，展示了视频生成在数据量和模型规模方面的扩展规律。在多个内部和外部基准测试中，该模型始终优于现有的开源模型以及最先进的商业解决方案，展现出显著的性能优势。 **全面性**：Wan提供了两个高效且强大的模型，分别拥有13亿和140亿参数，分别侧重于效率和效果。它还涵盖了多种下游应用，包括图像到视频转换、指令引导的视频编辑以及个性化视频生成，总共支持多达八项任务。 **消费级效率**：13亿参数的模型表现出卓越的资源效率，仅需8.19 GB显存，能够与广泛的消费级GPU兼容。 **开放性**：我们开源了整个Wan系列，包括源代码和所有模型，以促进视频生成社区的发展。这种开放性旨在显著拓展行业中视频制作的创意可能性，并为学术界提供高质量的视频基础模型。所有代码和模型均可在以下地址获取：https://github.com/Wan-Video/Wan2.1。 **694** 热度](https://hub.baai.ac.cn/paper/83d9bea1-75f4-4ba0-9a25-dc4ad7094ba1)
[CV](javascript:;)[DDPM](javascript:;)[Gen AI](javascript:;)
PDF
解读
![](https://hub.baai.ac.cn/_nuxt/img/paper_bg.03eb463.png)
###### [Gemma 3 Technical Report Gemma Team , Aishwarya Kamath , Johan Ferret , ... 2025年03月25日  ![](https://simg.baai.ac.cn/papers/converted_page_aeb1925fccceda6bacf25c225f587b43-01.jpg) 我们推出了 Gemma 3，这是 Gemma 系列轻量级开源模型的多模态扩展版本，其规模从 10 亿到 270 亿参数不等。此版本引入了视觉理解能力、更广泛的多语言支持以及更长的上下文处理能力——至少可达 128K 个标记（tokens）。同时，我们改进了模型架构，以减少在处理长上下文时容易激增的 KV 缓存内存占用。这一目标通过增加局部注意力层与全局注意力层的比例，并保持局部注意力的跨度较短来实现。Gemma 3 模型通过知识蒸馏进行训练，在预训练和指令微调版本上均优于 Gemma 2。特别是我们的新型后训练方法显著提升了模型的数学计算、对话交互、指令遵循及多语言处理能力，使得 Gemma3-4B-IT 能够与 Gemma2-27B-IT 相媲美，而 Gemma3-27B-IT 在多项基准测试中表现接近 Gemini-1.5-Pro。我们已向社区开放所有模型。 **568** 热度](https://hub.baai.ac.cn/paper/09466782-b90e-4400-bc37-9925c8832cb0)
[NLP](javascript:;)[AI](javascript:;)[Multimodal](javascript:;)
PDF
解读
![](https://hub.baai.ac.cn/_nuxt/img/paper_bg.03eb463.png)
###### [Gemini Robotics: Bringing AI into the Physical World Gemini Robotics Team , Saminda Abeyruwan , Joshua Ainslie , ... 2025年03月26日  ![](https://simg.baai.ac.cn/papers/converted_page_6c8843f3c6afb192b344c0fa497e1333-01.jpg) 近期大型多模态模型的发展，使得数字领域中涌现出了显著的通用能力，但这些能力在物理代理（如机器人）上的应用仍面临重大挑战。本报告介绍了一组专为机器人设计的新型人工智能模型，该模型基于Gemini 2.0构建。我们提出了Gemini Robotics，这是一款先进的视觉-语言-动作（VLA）通用模型，能够直接控制机器人。Gemini Robotics执行流畅且反应灵敏的动作，以应对各种复杂的操作任务，同时对物体类型和位置的变化具有较强的鲁棒性，能够在未知环境中运行，并遵循多样化的开放词汇指令。我们展示了通过额外的微调，Gemini Robotics可以扩展到新的能力，包括解决长时序、高灵巧性任务，从最少100个演示中学习新的短时序任务，以及适应完全新型的机器人形态。这一能力的实现得益于Gemini Robotics建立在Gemini Robotics-ER模型之上，这是我们工作中引入的第二个模型。Gemini Robotics-ER（具身推理）将Gemini的多模态推理能力扩展到物理世界，增强了其空间和时间理解能力。这使得与机器人相关的能力得以实现，包括物体检测、指向、轨迹和抓取预测，以及多视角对应关系和3D边界框预测。我们展示了这种新颖的组合如何支持多种机器人应用。此外，我们还讨论并解决了与这类新型机器人基础模型相关的关键安全问题。Gemini Robotics系列标志着向开发通用机器人迈出了重要一步，实现了人工智能在物理世界的潜力。 **449** 热度](https://hub.baai.ac.cn/paper/6856af30-b174-4723-bc93-f7e075095d81)
[Rob](javascript:;)[Multimodal](javascript:;)[Embodied AI](javascript:;)
PDF
解读
![](https://hub.baai.ac.cn/_nuxt/img/paper_bg.03eb463.png)
###### [Cut Your Losses in Large-Vocabulary Language Models Erik Wijmans , Brody Huval , Alexander Hertzberg , ... 2024年11月14日  ![](https://simg.baai.ac.cn/papers/converted_page_3c9beba39a56f929f7d33e9ae889dd7f-01.jpg) 随着语言模型规模的不断增大，它们的词汇量也在增加。这导致了在训练过程中，大型语言模型（LLM）的内存占用不成比例地集中在一层：损失计算中的交叉熵。交叉熵构建了一个包含每个输入标记与词汇项对的logit矩阵，对于小型模型来说，其内存消耗比整个LLM的其他部分高出一个数量级。我们提出了一种称为Cut Cross-Entropy（CCE）的方法，该方法在不将所有标记的logit值存储到全局内存中的情况下计算交叉熵损失。相反，CCE仅计算正确标记的logit，并实时评估所有logit的log-sum-exp。我们实现了一个自定义内核，在闪存中执行词汇表上的矩阵乘法和log-sum-exp归约，从而使交叉熵计算的全局内存消耗变得微不足道。这一方法产生了显著的效果。以Gemma 2（2B）模型为例，CCE将损失计算的内存占用从24 GB减少到1 MB，分类器头部的总训练时间内存消耗从28 GB减少到1 GB。为了提高CCE的吞吐量，我们利用了softmax的固有稀疏性，建议跳过对梯度贡献可忽略不计（即低于数值精度）的梯度计算元素。实验表明，这种显著的内存消耗减少并没有牺牲训练速度或收敛性。 **391** 热度](https://hub.baai.ac.cn/paper/60016226-1025-4d91-99dc-70e3d3c5290f)
[ML](javascript:;)[NLP](javascript:;)
PDF
解读
![](https://hub.baai.ac.cn/_nuxt/img/paper_bg.03eb463.png)
###### [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models Iman Mirzadeh , Keivan Alizadeh , Hooman Shahrokhi , ... 2024年10月08日  ![](https://simg.baai.ac.cn/papers/converted_page_a7ccbf3e08472cbd35296f321310c342-01.jpg) 最近大型语言模型（LLM）的进展引起了人们对它们的形式推理能力的兴趣，特别是在数学方面。GSM8K基准广泛用于评估模型在小学级别问题上的数学推理能力。虽然LLM在GSM8K上的表现在最近几年中显着提高，但它们的数学推理能力是否真正提高仍不清楚，这引发了对报告指标可靠性的质疑。为了解决这些问题，我们对几个SOTA开放和封闭模型进行了大规模研究。为了克服现有评估的局限性，我们引入了GSM-Symbolic，这是一个基于符号模板的改进基准，可以生成各种各样的问题。GSM-Symbolic能够进行更可控的评估，提供关键见解和更可靠的度量，以衡量模型的推理能力。我们的研究发现，LLM在回答同一问题的不同实例时表现出明显的差异。具体而言，当只改变GSM-Symbolic基准中问题中的数值时，所有模型的性能都会下降。此外，我们研究了这些模型中数学推理的脆弱性，并表明随着问题子句数量的增加，它们的性能显着下降。我们假设这种下降是因为当前的LLM无法进行真正的逻辑推理；它们复制训练数据中的推理步骤。即使一个似乎与问题相关的子句不对最终答案所需的推理链做出贡献，添加一个单子句也会导致所有最先进的模型的性能显着下降（高达65％）。总的来说，我们的工作提供了对LLM在数学推理方面能力和局限性的更细致的理解。 **297** 热度](https://hub.baai.ac.cn/paper/fec378f7-9ccd-41d8-8725-cf0f58e4eef3)
[ML](javascript:;)[AI](javascript:;)[PR](javascript:;)
PDF
解读
![](https://hub.baai.ac.cn/_nuxt/img/paper_bg.03eb463.png)
###### [The Llama 3 Herd of Models Abhimanyu Dubey , Abhinav Jauhri , Abhinav Pandey , ... 2024年08月01日  ![](https://simg.baai.ac.cn/papers/converted_page_8f235a3e7e123ff5439ac09ee873b0d8-01.jpg) 现代人工智能（AI）系统的动力源是基础模型。本文介绍了一组新的基础模型，称为Llama 3。它是一群语言模型，本地支持多语言、编码、推理和工具使用。我们最大的模型是一个密集的Transformer，有405B个参数和最多128K个标记的上下文窗口。本文对Llama 3进行了广泛的实证评估。我们发现，在众多任务中，Llama 3与领先的语言模型（如GPT-4）提供了可比较的质量。我们公开发布了Llama 3，包括405B参数语言模型的预训练和后训练版本，以及我们的Llama Guard 3模型，用于输入和输出的安全性。本文还介绍了实验结果，在其中我们通过组合方法将图像、视频和语音功能集成到Llama 3中。我们观察到这种方法在图像、视频和语音识别任务上表现出与最先进技术相竞争的水平。由此产生的模型尚未广泛发布，因为它们仍在开发中。 **249** 热度](https://hub.baai.ac.cn/paper/bb525f20-4d2d-4e79-8968-b0e03bbbf211)
[AI](javascript:;)[NLP](javascript:;)[CV](javascript:;)
PDF
解读
![](https://hub.baai.ac.cn/_nuxt/img/paper_bg.03eb463.png)
###### [All That Glitters is Not Novel: Plagiarism in AI Generated Research Tarun Gupta , Danish Pruthi 2025年02月23日  ![](https://simg.baai.ac.cn/papers/converted_page_a1ab6f1d8c646cf17d1581f99b2080e1-02.jpg) 将科学研究自动化被视为科学的终极前沿。 最近，有几篇论文声称自主研究代理能够生成新的研究想法。 在普遍乐观的氛围中，我们记录了一个关键问题：相当一部分此类研究文件是巧妙地抄袭而来的。 与过去专家评估研究想法的新颖性和可行性不同，我们要求13位专家根据不同的情境逻辑操作：识别大型语言模型（LLM）生成的研究文件与现有工作之间的相似性。 令人担忧的是，专家们发现，在评估的50份研究文件中，有24%要么是被改写过的（具有一对一的方法论映射），要么是从现有工作中大量借鉴的。这些报告的实例由源论文的作者进行了交叉验证。 问题在于，这些由大型语言模型生成的研究文件并未承认原始来源，并且绕过了内置的剽窃检测器。 最后，通过受控实验，我们证明了自动剽窃检测器在捕捉来自大型语言模型故意剽窃的想法方面是不足的。 我们建议仔细评估由大型语言模型生成的研究，并讨论我们的发现对研究和学术出版的影响。 **179** 热度](https://hub.baai.ac.cn/paper/3ab43dfa-74a0-438f-a094-29daf4ccc367)
[NLP](javascript:;)[PR](javascript:;)[AI Safety](javascript:;)
PDF
解读
![](https://hub.baai.ac.cn/_nuxt/img/paper_bg.03eb463.png)
###### [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving Kefan Dong , Tengyu Ma 2025年02月01日  ![](https://simg.baai.ac.cn/papers/converted_page_f1ed374715f324a145fa588b5e13b17d-02.jpg) 大型语言模型（LLMs）在形式化定理证明中的一个基本挑战是缺乏高质量的训练数据。尽管强化学习或专家迭代通过交替进行LLM生成证明和在正确生成的证明上微调，部分缓解了这一问题，但由于正确证明的稀缺性（奖励稀疏），性能很快就会停滞不前。为了在有限的数据下继续改进模型，我们从数学家的工作中汲取灵感。数学家们不断开发新的成果，部分是通过提出新颖的猜想或练习（这些通常是已知结果的变体）并尝试解决它们。我们设计了自我对弈定理证明器（STP），它同时承担两个角色：猜想者和证明者，每个角色为另一个提供训练信号。猜想者迭代地在之前生成的、当前证明者勉强可以证明的猜想上进行训练，这激励它随着时间生成越来越具有挑战性的猜想。证明者则尝试使用标准的专家迭代来证明这些猜想。我们在Lean和Isabelle形式验证器上评估了STP。在Lean的训练过程中生成了198亿个标记，STP证明了LeanWorkbook数据集中26.3%的陈述，这是之前通过专家迭代取得的最佳结果13.2%的两倍。最终模型在miniF2F-test（61.1%，pass@3200）、Proofnet-test（23.1%，pass@3200）和PutnamBench（8/644，pass@64）的完整证明生成方法中达到了最先进的性能。 **172** 热度](https://hub.baai.ac.cn/paper/ed027fc6-a6f1-49f5-96fe-a1f3c3e35d50)
[ML](javascript:;)[AI](javascript:;)[cs.LO](javascript:;)
PDF
解读
![](https://hub.baai.ac.cn/_nuxt/img/backtop.3d51554.png)
查看【】的搜索结果
Network Error
