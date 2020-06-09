# cyber: 计算大网络的知识

![img](https://github.com/serejandmyself/cyber/raw/master/images/graph.png)

**抽象**

一台共识计算机允许计算可证明相关的答案，而无需任何有意见的黑盒中介，如谷歌、亚马逊或Facebook。无状态、可内容的点对点通信网络（如 IPFS）和具有状态的协商一致计算机（如以太坊）可以提供获得类似答案所需的部分解决方案。但是，至少有3个问题与上述实现有关。（A） 相关性的主观性质。（B） 难以将共识计算机扩展到超大的知识图。（C） 此类知识图中缺乏质量。他们容易受到各种表面攻击，如sybil攻击，以及相互作用的特工的自私行为。在本文中，我们定义了一个协议，用于 IPFS 对象之间相关性的可证明协商一致计算，该协议基于网络-Rank 的 Tendermint 共识，该共识在共识中使用 GPU 计算。由于风险证明共识无助于初始分销，因此我们概述了生态和高效分销游戏的设计。我们认为，协议的简约体系结构对于形成特定于域的知识共识计算机网络至关重要。由于我们的工作，一些以前从未存在过的申请将会出现。我们扩展本文档，并展望可能的功能和潜在应用。

**伟大的网络**

互联网的原始协议，例如：TCP/IP、DNS、URL 和 HTTP/S 使 Web 处于陈旧的位置，而到目前为止，它的位置就已位于此地。考虑到这些协议为网络的初始开发所产生的所有好处，以及它们，它们给表带来了重大障碍。全球化，作为网络的重要属性，自网络成立以来，一直面临真正的威胁。由于政府无处不在的干预，连接速度不断下降，而网络本身却在持续增长。后者将隐私问题视为对人权的生存威胁。

一个在开始时不明显的属性对互联网的日常使用变得很重要：因此，能够交换永久链接， 他们 [时间过去后不会中断](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN). 依靠一个一次一个ISP的架构，允许政府有效地审查数据包。这是每个关心我们孩子未来的工程师的传统网络堆栈的最后一滴。

其他属性虽然可能不那么重要，但非常可取：脱机和实时连接。普通互联网用户，虽然离线，仍然应该能够继续与他们已经持有的状态工作。获得连接后，他们应该能够与全局状态同步，并继续实时验证其状态的有效性。目前，这些属性在应用程序级别上提供。我们认为，这些属性应集成到较低级别的协议中。

出现 [全新的网络堆栈](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw) 为卓越的互联网创造了机会。社区称之为Web3。我们称之为伟大的网络。我们认为，各种类型的低级通信应该是不变的，几十年来不应改变，例如不可变的内容链接。它们似乎在消除传统协议堆栈的问题方面非常有希望。它们增加了更高的速度，并且提供了与新 Web 的更易于访问的连接。然而，正如它发生在任何概念，提供一些独特的 - 新的问题出现。一个这种关切是通用搜索。现有的通用搜索引擎是限制性的和集中的数据库，每个人都被迫信任。这些搜索引擎主要为基于 TCP/IP、DNS、URL 和 HTTP/S 的客户端-服务器体系结构而设计。Great Web 为基于新兴技术的搜索引擎带来了挑战和机会，并且专为这些目的而设计。令人惊讶的是，无权限的区块链架构允许以以前架构无法访问的方式构建通用搜索引擎。

## 关于对抗性示例问题

[搜索引擎的当前架构](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6) 是一个系统，一些实体处理所有狗屎。这种方法面临着一个具有挑战性的和一个独特的问题，这个问题尚未解决，即使由杰出的谷歌科学家：[对抗性示例问题](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9). 谷歌承认的问题是，很难从算法上推断某个样本是否是对抗性的。这是不体贴如何真棒教育技术本身是。加密经济方法可以改变游戏中的受益者。因此，这种方法将有效地消除可能的sybil攻击媒介。它消除了硬编码模型爬网和单个实体提取的必要性。相反，它给整个世界带来了这种力量。一个学习sybil耐，代理生成的模型，可能会导致数量级更多的预测结果。

## Cyber 协议

协议的核心是极简的，可以通过以下步骤来表达：

1. 基于定义的分布计算网络协议的起源
2. 定义 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
3. 使用 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
4. 检查签名的有效性
5. 检查 [带宽限制](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
6. 检查 CID 的有效性
7. 如果签名、带宽限制和 CID 都有效，请应用 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 和交易
8. 计算[cyber~排名](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberrank) 每轮为CID在 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)

本文档的其余部分讨论了拟议协议的理由和技术细节。

## 知识图

我们将知识图表示为内容地址之间定向链接的加权图形。Aka，内容识别器、CID、IPFS 哈希，或简单 - IPFS 链接。在本文档中，我们将使用上述术语作为同义词。

![img](https://github.com/serejandmyself/cyber/raw/master/images/knowledge-graph.png)

内容地址本质上是 Web3 链接。而不是使用不明确和可变的：

```
https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md
```

我们使用对象本身：

```
Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

通过使用内容地址构建我们获得的知识图 [急需的](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est) [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps) - [喜欢](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR) 搜索引擎所需的 p2p 协议的超能力：

- 网网面向未来
- 行星际可访问性
- 审查阻力
- 技术独立性

我们的知识图是由真棒大师生成的。大师们借助一个交易（一个网络链接）将自己添加到知识图中。因此，它们证明了其公开公钥的内容地址的私钥的存在。通过使用这些机制， [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 可以在知识图上实现主体和对象之间的可证明区分。

我们实施 [去-cyber](https://github.com/cybercongress/go-cyber) 基于 [宇宙-SDK](https://github.com/cosmos/cosmos-sdk) 身份和 [CIDv0/CIDv1](https://github.com/multiformats/cid#cidv0) 内容地址。

大师通过应用来形成知识图 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).

## Cyber链接

为了了解网络链接的功能，我们需要了解 URL 链接（也称为超链接）和 IPFS 链接之间的区别。URL 链接指向内容的位置，即 IPFS 链接是否指向内容本身。基于位置链接和内容链接的 Web 体系结构之间的差异是激进的，需要独特的方法。

Cyber链接 是一种在语义上链接两个内容地址或 IPFS 链接的方法：

```
.md 语法: [QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH](Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH)    
.dura 语法: QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH.Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

以上 cyber链接 意味着 [去-cyber](https://github.com/cybercongress/go-cyber) 在 [cyberc0n](https://etherscan.io/token/0x61B81103e716B611Fff8aF5A5Dc8f37C628efb1E) 引用宇宙白皮书。网络链接的概念是围绕任何p2p网络中通信格式的简单语义的约定：

![img](https://github.com/serejandmyself/cyber/raw/master/images/cyberlink.png)

我们看到，网络链接表示两个链接之间的链接。容易点！

网络链接是一种简单但强大的语义结构，用于构建宇宙的预测模型。这意味着，使用网络链接而不是超链接为我们提供了以前通用搜索引擎架构无法访问的超级大国。

网络链接可以扩展，即如果有两个或多个网络链接从一个主机中分离，则它们可以形成链接链，其中第一个网络链路中的第二个链接等于第二个网络链路中的第一个链接：

![img](https://github.com/serejandmyself/cyber/raw/master/images/linkchain.png)

如果代理扩展本机 IPFS 链接，具有语义上更丰富的内容，例如， [努力](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md) 链接，然后可以通过一种更自然的方法就特定程序的执行规则达成共识。

的 [去-cyber](https://github.com/cybercongress/go-cyber) 网络链接的实施可在 [.cyber](https://github.com/cybercongress/dot-cyber) 我们的实验 Web3 浏览器的应用程序 [cyb](https://cyb.ai/), 或是在 [cyber.页面](http://cyber.page/).

大师提交的网络链接存储在一个梅尔克树根据 [RFC-6962 标准](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). 这使得[相关性证明](https://github.com/serejandmyself/cyber/blob/master/cyber.md#proof-of-relevance).

![img](https://github.com/serejandmyself/cyber/raw/master/images/graph-tree.png)

使用网络链接，我们可以计算主题和对象的相关性。[知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). 但是我们需要奥利奇图 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer).

## 共识计算机的概念

共识计算机是从代理之间的交互中产生的抽象计算机。共识计算机在基本计算资源方面具有容量：内存和计算。要与代理进行交互，计算机需要带宽。理想的共识计算机是计算机，其中：

```
个人可以使用的所有计算和内存的总和
等于
共识计算机所有已验证的计算和内存的总和
```

我们知道：

```
计算验证 < (计算 + 计算验证)
```

因此，我们永远无法达到理想的共识计算机。CAP 定理和可伸缩性三角报为此语句提供了更多证据。

![img](https://github.com/serejandmyself/cyber/raw/master/images/consensus-computer.png)

然而，这个理论可以作为共识计算机的性能指标。经过6年对共识计算机的投资，我们逐渐认识到，[嫩明特](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) 共识在我们任务所需的冷静性与生产准备之间有足够的平衡。因此，我们决定实施 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 协议使用招标共识，它有非常接近的设置宇宙中心。的[去-cyber](https://github.com/cybercongress/go-cyber) 实现是一个64位Tendermint共识计算机，与64字节的字符串空间相关。这还不理想，至少为 1/146，因为我们有 146 个验证器，他们验证了生成[知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

我们必须将共识计算机的计算、存储和带宽供应绑定到对查询的最大化需求。计算和存储，在基本情况下 [相关机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 可根据带宽轻松预测。但是带宽需要限制机制。

## 相关性机器

我们将相关性计算机定义为转换 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 基于希望教导和研究的代理人的意愿， [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). 意志是由每个 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 主人会的。 代理询问越多 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph), 知识的价值就越大。根据这些预测，可以计算内容地址之间的相关性。相关性计算机通过查询和传递答案，为搜索机制提供简单的构造。

关联机的一个属性至关重要。它必须具有电感推理特性或遵循黑盒原理：

```
机器应该能够干扰预测，而不知道这些物体，`
除了谁，何时和什么是 cyber联系
```

如果我们假设[共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 必须包含有关链接对象的一些信息，那么此类模型的复杂性将难以预测地增长。因此，处理计算机对内存和计算的要求很高。由于内容处理符合黑盒原则的相关计算机，不需要存储数据。但是，仍然可以有效地运行在上面。内意义的推导 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 很贵。因此，这种设计可以依赖于假设盲。而不是扣除 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer),我们设计了一个系统，其中意味着提取被激励。这是由于大师要求 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 令牌来表达他们的意愿，基于哪个，相关性计算机可以计算排名。

在垃圾邮件保护系统的核心是一个假设，即写入操作只能由那些对关联机器的进化成功有既得利益的人执行。在 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 能够使用可能网络带宽的 1% 及其计算功能。一个简单的规则可以防止来自代理的滥用：一对内容识别器可能仅由地址链接一次。

![img](https://github.com/serejandmyself/cyber/raw/master/images/algo1.png)

只有两种方法可以改变账户的有效股份（主动投注+ 保税股份）：直接代币转账和粘结业务。

[Cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 使用非常简单的带宽模型。此模型的主要目标是将网络的日常增长减少到给定的常数。这样做是为了容纳英雄（验证者），能够预测未来对基础设施的任何投资。因此，在这里我们介绍"瓦特"或"W"。每个消息类型都有分配的 W 成本。常量"理想带宽"确定 W 值花费的"恢复窗口"。恢复期定义主机恢复带宽从 0 恢复到最大带宽的速度。主控形状的最大 W 与其有效赌注成正比，由以下公式决定：

```
代理MaxW = 有效风险 * 理想带宽
```

"AdjustPrice 周期"期间汇总了最新块中的"恢复期"期间花费 W 的金额。"支出带宽"/"理想带宽"比率称为小数准备金率。当网络使用率较低时，小数准备金率会调整消息成本，以便持有较低股份的主机进行更多交易。当资源需求增加时，小数准备金率将= 1，因此，增加消息成本，并限制长期周期的最终 tx 计数（W 回收将是 +然后 W 支出）。由于没有人使用他们所有拥有的带宽，我们可以在价格重新计算目标期间安全地使用高达 100 倍的分数储备。这种机制为创建提供了折扣 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks), 从而有效地最大化了对它的需求。您可以看到，建议的设计需要全带宽的需求，以便相关性变得有价值。

人类智力的组织方式，使一些没有相关和重要的记忆被遗忘随着时间的推移。这同样可以应用于相关计算机。相关机器可以实现 [积极的修剪策略](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb), 例如，修剪历史的形成[知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph), 或忘记不太相关的链接。

因此，实施的网络经济学 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)令牌不仅作为意愿表达和垃圾邮件保护机制，而且作为经济调节工具发挥作用，可以协调英雄的处理能力和对处理的市场需求。关联机的去网络实现基于一个非常直接的机制，称为：cyber~排名。

## cyber~排名。

使用 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 可能具有挑战性，因为共识计算机具有严重的资源限制。首先，我们必须问自己：为什么我们需要计算和存储链上的排名，而不是遵循与 [群](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj) or [真比特](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)?

当等级是在 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 可以轻松访问该等级的内容分布，并且可以轻松地 [生成可证明的应用程序](https://github.com/serejandmyself/cyber/blob/master/cyber.md#apps) 在那个排名之上。因此，我们决定遵循一个更宇宙的建筑。在下一节中，我们将介绍 [相关性证明](https://github.com/serejandmyself/cyber/blob/master/cyber.md#proof-of-relevance) 机制，允许网络在特定于域的帮助下进行扩展 [相关机器](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine). 由于 IBC 协议，这些工作同时进行。

最终， [相关机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 需要获得 （1） 确定性算法，该算法将允许计算连续追加网络上的排名，该算法本身可以扩展到类似[Google](https://google.com/). 此外，一个完美的算法（2）必须具有线性内存和计算复杂性。最重要的是，它必须有（3）最高可证明的预测能力，以存在相关 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).

后 [彻底的研究](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC), 我们发现不可能得到银弹。因此，我们决定找到一种更基本、防弹的方法，可以引导网络：[排名](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw) 拉里和谢尔盖曾经引导他们以前的网络。原始 PageRank 的关键问题是，它无法抵抗 sybil 攻击。但是，受令牌加权带宽模型限制的令牌加权 PageRank 不会继承天真的 PageRank 的关键问题，因为 - 它能够抵御 sybil 攻击。目前，我们将称之为网络-Rank，直到出现更合适的东西。以下算法应用于创世纪的实施：

![img](https://github.com/serejandmyself/cyber/raw/master/images/algo2.png)

据我们了解，排名机制将永远是一条红线。这就是为什么我们期望依赖链上治理工具，这些工具可以在给定时间定义最合适的机制。我们假设网络可以从一个算法切换到另一个算法，不仅基于主观意见，而是基于通过特定于域的"硬勺子"进行经济的 a/b 测试 [相关机器](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).

cyber~排名屏蔽了两个最重要的设计决策：（1） 它占了代理商当前的意图，（2） 它鼓励排名通货膨胀 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks). 第一个属性可确保网络排名不能被游戏使用。如果代理决定转移其 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 令牌从他们的帐户,  [相关机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 将调整所有 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 根据代理的当前意图与此帐户相关。反之亦然，如果代理转移[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 令牌到他们的帐户，所有[cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber链接) 从这个帐户提交将立即获得更多的相关性。第二个属性是必不可少的，以免在过去得到巩固。作为新的 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 不断添加，它们会按比例稀释现有链接的排名。此属性可防止出现新内容和更好的内容排名较低的情况，只是因为它最近提交了。我们期望这些决策为最近添加的内容启用推理质量，[知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

我们很想讨论买票的问题。买票是一种现象，并不是那么糟糕。买票的两难困境出现在投票影响系统分配通胀的系统中。例如， [Steem](http://ipfs.io/ipfs/QmepU77tqMAHHuiSASUvUnu8f8ENuPF2Kfs97WjLn8vAS3) 或任何基于法定状态的系统。对于使用零和游戏而不需要增加价值的对手来说，买票很容易获利。我们最初关于分散搜索的想法是基于这种方法。但是，我们拒绝了这个想法，删除了形成激励 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 到共识水平。在每个参与者必须为系统带来某种价值以影响预测模型的环境中，投票购买成为 NP 难题。因此，成为有利于系统。

目前实施的 [相关机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 使用 GPU 计算排名。机器可以在 64 字节 CID 空间内应答任何给定的搜索请求并提供有关结果。但是，构建特定于域的网络是不够的[相关机器](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine). [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 必须有能力证明彼此的相关性。

## 相关性证明

我们设计网络的假设是，在搜索方面，恶意行为等行为并不存在。这可以假定为在查找答案的意图中找不到恶意行为。这种方法大大减少了任何表面攻击。

```
排名是根据搜索某些内容（因此链接）以及因此影响预测模型的事实计算的
```

在量子力学中观察到一个很好的类比，观察本身会影响行为。这就是为什么我们没有要求这样的东西，如投反对票。通过这样做，我们将主观性从协议中删除，我们可以定义相关性证明。

![img](https://github.com/serejandmyself/cyber/raw/master/images/graph-tree.png)

每个新 CID 都会收到一个序列号。编号以零开始。然后为每个新 CID 增加一个。因此，我们可以将排名存储在一维数组中，其中索引是 CID 序列号。默克尔树计算基于[RFC-6962 标准](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). 使用 Merkle 树，我们可以有效地证明任何给定内容地址的排名。虽然相关性本质上是主观的，但我们有一个集体证据，证明某样东西在某一时刻与某个社区有关。

使用这种类型的证明任意两个 [IBC 兼容](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk) [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 可以证明一个相关性。这意味着特定于域[相关机器](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 可以蓬勃发展。

在共同的关联 [去-cyber](https://github.com/cybercongress/go-cyber) 实现，Merkle 树计算每轮，其根哈希承诺ABCI。

## 速度

我们需要即时确认时间，为用户提供传统 Web 应用程序的感觉。这是一个强大的体系结构要求，可塑造经济拓扑和可伸缩性。 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 协议。 建议的区块链设计基于[投标共识](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) 算法与146个验证器，有一个快速，5秒tx完成时间。平均确认时间接近 1 秒，使复杂的区块链交互对代理几乎不可见。

我们表示一个特定的 [去-cyber](https://github.com/cybercongress/go-cyber) 属性在速度排名计算上下文中.作为共识的一部分，它与回合中的事务验证并行发生。一轮是由利益相关者定义的协商一致变量。开始时，一轮设定为20个方块。实际上，这表明网络必须每 100 秒就对 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). 这意味着，每个 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 提交成为[知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 几乎瞬间，并在平均50秒内获得排名。在早期[Google](https://google.com/) 排名大约每周重新计算。我们相信，大网的大师会很高兴地观察到实时排名变化，但是，已经决定启动网络的假设，这个窗口就足够了。预计随着[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 协议每轮的速度将降低。这是由于英雄之间的竞争。我们知道某些机制可以使这个函数级级更快：

- 优化共识参数
- 排名计算的更好的并行化
-  [更好的时钟](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs) 在共识之前

## 可 伸缩 性

我们需要一个架构，它将允许我们扩展的想法，以这样的[Google](https://google.com/). 让我们假设，该节点实现，这是基于[宇宙-SDK](https://github.com/cosmos/cosmos-sdk) 每秒可处理 10k 个事务。这意味着，每天，至少864万大师将能够提交100 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 每个，并同时影响搜索结果。这足以验证野生的所有假设，但是，不足以说它将在目前互联网的规模工作。鉴于我们的团队进行的技术研究现状，我们可以放心地指出，不存在共识技术，从而能够将特定区块链扩展到所需的大小。因此，我们引入了特定于域的概念 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

![img](https://github.com/serejandmyself/cyber/raw/master/images/network.png)

可以通过分叉启动自己的特定于域的搜索引擎 [去-cyber](https://github.com/cybercongress/go-cyber), 专注于 [文本]公共知识。或者，只需插入 [去-cyber](https://github.com/cybercongress/go-cyber) 作为一个模块，进入一个现有的链，即宇宙中心。区块链间通信协议引入了在两者之间同步状态的并发机制 [相关机器](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine). 因此，在建议的搜索体系结构中，特定于域 [相关机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 将能够从常识中学习。正如常识可以从特定于域的 [相关机器](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).

## 布罗泽斯

我们渴望想象一下，建议的网络如何使用 Web3 浏览器运行。令我们失望的是，我们 [无法](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md) 找到一个Web3浏览器，可以展示建议的方法在行动的冷静。这就是为什么我们决定从头开始开发Web3浏览器的原因。[Cyb](https://cyb.ai/) is your friendly robot which has a sample [.cyber](https://cyber.page/) 与之互动的应用程序 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 协议.

![img](https://github.com/serejandmyself/cyber/raw/master/images/cyb.jpg)

作为交付的一个好例子，我们创建了 [cyber.页面](https://cyber.page/). 它允许英雄、大师和福音传道者通过 Web2 网关与协议进行交互。创建网络链接，将内容直接固定到IPFS，搜索大网络，参与网络治理等等。它还可以充当深入的资源管理器、钱包和口袋硬件钱包，如 Ledger 设备。

当前搜索代码段是丑陋的。但是，我们假设他们可以很容易地扩展使用 [IPLD](https://github.com/ipld/specs) 用于不同类型的内容。最终，他们可以变得比那些[Google](https://google.com/).

![img](https://github.com/serejandmyself/cyber/raw/master/images/architecture.png)

在拟议架构的实施过程中，我们至少意识到了3个关键优势 [Google](https://google.com/) 可能无法提供其传统方法：

- 搜索结果可以轻松地从任何 p2p 网络传递：例如 。cyber 可以播放视频
- 付款按钮可以直接嵌入到搜索代码段中。这意味着代理可以与搜索结果进行交互，例如，代理可以在 .cyber 中直接购买商品。这意味着电子商务可以公平地蓬勃发展，这要归功于可证明的转换归因
- 搜索代码段不必是静态的，但可以是交互式的。例如.网络可以提供您当前的钱包余额

## 部署

由于技术限制，我们必须使用 2 个令牌引导生态系统： [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 和 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)

- [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 是主权的原生代币 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 协议由Tendermint共识算法驱动。它有3个主要用途：（1） 提交共识，（2） 带宽限制提交 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks), （3）表达主对网络排名的计算意愿。
- [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) （发音为技术）是一种创造性的网络原型物质。 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 是以太坊ERC-20兼容令牌，具有效用价值，以控制网络基础（管理DAO的社区）和分销游戏中的ETH。 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 在创建作为阿拉贡组织的网络基金会期间发出。的创造力量 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 来自接收 1 的能力 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 每个 1 个令牌 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 令牌在网络拍卖结束之前授予。

这两个令牌都保持功能，并且由于它们本质上是非常不同的效用，它们将相互独立地跟踪值。

总体而言，部署过程具有以下结构：

1. cyber~国会部署链接游戏
2. 社区参与链接游戏
3. 社区验证并提出一个创世区块与链接游戏的结果
4. cyber~国会部署网络-基础和网络拍卖合同
5. 创世记后，社区参与网络拍卖。捐助者股份 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 要获取的令牌[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 令 牌
6. cyber~国会分发 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 代币在 cyber~拍卖
7. cyber~国会烧掉剩下的[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 和 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 初始分发过程结束时的令牌和报告

cyber~国会住在以里图姆作为一个 [阿拉贡 DAO](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330). 它还运行[2-of-3 网络网络中的多西格](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8). cyber~国会制定了 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 协议。在网络背景下，国会有两个角色：

1. To 部署并执行初始分发程序，这是不可能自动执行的。因为 ETH 和 ATOM 之间没有用于消息交换的无信任基础结构，cyber~国会在初始分发过程中引入了单点故障。我们决定发送 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 令牌到[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 投注者手动，因为我们认为，现在是启动我们创建的网络的正确时机。我们还认为，正在进行的拍卖对于初始分销过程至关重要。如果网络大会由于任何可能的原因未能履行其在分销方面的义务，我们希望社区能够分叉网络并分发 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 令牌，如承诺。希望每个操作的设计都是有条件和透明的。所有操作都将使用[网络网络中特殊用途的 2/3 多西格帐户](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j).
2. 支持成长 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 协议，直到社区接管以网络-基金会的形式发展。链接游戏期间 ATOM 中的捐赠将分发给[cyber~国会宇宙 2-3 多西格](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a). 所有被路由到网络-国会多西格的ATOM捐款将成为其财产。ATOM 捐赠的作用如下：由于 ATOM，我们希望在宇宙和网络生态系统的开发中确保网络大会的承诺。ATOM 捐赠将允许网络/国会使用获取奖励和达到可持续的流程，为持续的资金 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 协议无需转储两者 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 也不是 ATOM 令牌。

## CYB

风险证明系统无助于初始分发。我们认为，如果初始分布是有目的地设计，节能，证明和透明的，因此可访问，早期 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 将在质量和尺寸上有所提升。

网络协议的成因块包含 1 000 000 000 0000 CYB（一个 Petacyb 或 1 个 PCYB）令牌，细分如下：

- 750 000 000 000 CYB 代币为持有股份的人 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 令牌，直到网络拍卖结束（网络-大会参与者，ETH权力的游戏和网络拍卖的参与者）

- 150 000 000 000 000 CYB 链接游戏参与者的令牌

- 100 000 000 000 000 CYB 代币作为礼物给以提图姆，宇宙和乌尔比特社区

  ![img](https://github.com/serejandmyself/cyber/raw/master/images/CYB.svg?sanitize=true)

在创世纪之后，CYB 令牌只能由英雄基于拍摄和斜线参数创建。基本共识是，新创建的CYB代币由利益相关者使用。

目前不存在最多数量的 CYB 令牌。这是由于持续通货膨胀支付给网络的英雄。CYB 令牌使用 uint64 实现，因此创建额外的 CYB 令牌使得计算状态更改和排名的成本要高得多。我们期望在CYB代币完全初始分发和智能合约功能激活后，治理系统能够建立终身货币战略。通货膨胀的起始参数将通过链接游戏期间的治理来定义。

## THC

创建替代方法的目标 [Google-喜欢](https://google.com/) 结构需要不同群体的非凡努力。因此，我们决定成立网络基金作为基金，通过分散的引擎，如阿拉贡DAO进行管理。它由参与初始分发的代理负责 ETH 和管理。这种方法将允许保护本地平台令牌的过度市场倾销 - [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 在工作的头几年，从而保证稳定发展。此外，这允许使底层平台多样化，并在出现此类需求时将协议扩展到其他共识计算体系结构。

在选择捐款代币时，我们遵循了三个主要标准：1）最有流动性的，（2）最有前途的，这样一个社区就可以获得一个坚实的投资袋，即使与这样的巨头相比，也能具有竞争力。 [Google](https://google.com/), （3） 具有执行拍卖和最终组织的技术能力，而无需依赖任何第三方。唯一符合这些标准的系统是以里图姆，因此，捐赠的主要代币将是ETH。

创世纪之前，基金会已铸造750 000 000 000 THC （七百五十泰特hc） 分解如下：

- 600 000 000 000 000 THC 令牌分配给网络拍卖合同

- 150 000 000 000 000 THC 令牌分配给网络/大会合同

  ![img](https://github.com/serejandmyself/cyber/raw/master/images/THC.svg?sanitize=true)

网络基金会的所有决定都将根据 THC 投票结果执行。将应用以下参数：

- 支持： 51%
- 仲裁： 51%
- 投票期限： 500 小时

## 礼物

我们希望能够尽可能多地向尽可能多的代理评估建议的方法。但是，没有增加像KYC和/或卡普查这样的复杂性。这就是为什么我们选择赠送8% [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 创世纪到以天地的代币，1%到宇宙，1%到Urbit社区。以下规则适用于重现创世纪：

- 以地庭基础网络中的每个账户，至少有 1 个传出交易不是合同，并且持有 > 0.001 ETH 在块 8080808
- Cosmos 中心 3 中每个非零帐户，位于块 2000000
- 每个账户都包含星系（30%）、恒星（30%）或行星（40%）在块10677601根据对象的数量

此礼品的主要目的是让创世纪中的每个帐户能够至少制作 1[cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 在 24 小时内卸载网络。这就是为什么我们决定使分布曲线更均匀一些，并从根本上将其更改为二次曲线。因此，我们分发 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 在快照期间，与每个帐户余额的平方根成比例的标记。由于二次设计太容易玩，我们计算了分布式[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 在公众知道这一事实之前，建议的块的代币。我们不将二次规则应用于 Urbit 外星人。

## 链接游戏

在ATOM的宇宙霍勒游戏。参与者捐赠ATOM以换取CYB。捐赠的ATOM越多，CYB的价格就越高。游戏从每 1 GCYB 1 ATOM 开始。游戏已经结束，当146天已经过去了，因为起飞捐款开始，或者如果价格已经增加了5倍的起始价格。价格 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 起飞期间由以下功能定义：

f(c) = 40 * c + 1000

其中 f(c) 是 TCYB 价格在 ATOM 中，c 是起飞期间赢得的 TCYB 代币金额。

关键的想法是：起飞捐赠回合执行得越好，学科参与者将获得的报酬就越多。100 [TCYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 分配给起飞捐款的参与者和50[TCYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 分配给链接游戏学科的参与者。所有 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 保留从起飞的令牌，在游戏结束时分配给社区池。所有 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 保留的科目中的令牌分配给网络-国会。除了CYB代币外，链接游戏将测试EUL令牌分配给所有起飞捐赠者进行决赛。A [详细文件](https://cybercongress.ai/game-of-links/) 已经发布了游戏规则和游戏规则。

## Cyber~拍卖

ETH的以泰伦霍德勒的游戏。参与者捐赠ETH以换取THC。捐赠ETH越多，THC的价格就越高。游戏从价格开始，这是5倍的收盘价起飞在ETH。游戏已经结束，当888天已经过去了，因为它开始或如果价格增加了5倍的起始价格。在此阶段 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 令牌由网络/大会持续分发，基于[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 代币，直到拍卖结束。归属 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 令牌提供接收的能力 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 因此，以及网络基础内的表决权。价格[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 在网络拍卖期间，由以下功能定义：

g(t)= 1/30 * t * p + 5 * p

其中 g(t) 是ETH中的TTHC价格，t是在网络拍卖期间赢得的TTHC代币数量，p是一个CYB在收盘时刻转换为ETH的起飞价格。

起始价格旨在让起飞参与者在创世纪之前投资硬件和软件基础设施的风险提高 5 倍。网络拍卖为早期参与者提供了重要的激励。分发结束后，参与者将能够解锁其 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 代币，并根据需要使用它们，例如转让、交换等。通过拍卖，社区将有机会获得阿拉贡组织内所有捐赠的ETH。网络拍卖结束后，其余[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 网上拍卖合同必须可证明烧毁。以下规则适用于 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 下标记 [用于分发的多西格](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j):

- 网络-国会不会委托其股份，因此，它将继续被动的股份，直到它成为分配
- 网络拍卖结束后，所有剩余的 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 令牌必须可证明刻录

## 应用程序

我们假设建议的算法在默认情况下不能保证高质量的知识。就像新生儿一样，它需要获得知识才能进一步发展。协议本身只提供了一个简单的工具：创建 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 代理在两个内容地址之间放权。

可以通过智能合约和脱链应用程序来分析语义核心，行为因素，有关代理人兴趣的匿名数据以及其他确定搜索质量的工具，例如：[web3 浏览器](https://github.com/serejandmyself/cyber/blob/master/cyber.md#browzers), 分散的社交网络和内容平台。我们相信，这是社区和主人的利益，建立初始[知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 并维护它。因此，对于图形，提供最相关的搜索结果。

通常，我们区分三种类型的应用程序 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph):

- 共识应用程序。可以在 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 通过添加智能能力
- 链上应用。可以由 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 以换取天然气
- 链外应用。可以使用 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 作为执行环境中的输入

可以想象，以下应用列表整合了上述类别：

Web3 浏览器。在现实中，浏览器和搜索是密不可分的。很难想象一个基于Web2搜索的成熟的Web3浏览器的出现。目前，在区块链和分布式技术周围开发浏览器有好几项努力，其中包括烧杯、雾、勇敢和Metamask。他们都因试图将Web2嵌入到Web3中而受苦。我们的方法有点不同。我们认为 web2 是 Web3 的不安全子集。因此，我们开发了一个实验性的Web3浏览器，Cyb，展示 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 更好地回答查询并更快地交付内容的方法。

社交网络。社交网络并不太神秘。在任何社交网络内容是王道。因此，可证明排名是任何社交网络的基本组成部分。所有类型的社交网络都可以轻松构建在 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)。 也可以根据用户之间的相关性创建社交网络，这是当前网络无法实现的。

可编程语义。目前，在巨大的语义核心中最流行的关键字[Google](https://google.com/) 是应用的关键字，例如： [Youtube](https://youtube.com/), [Facebook](https://facebook.com/), [GitHub](https://github.com/), etc. 但是，这些成功应用的开发人员向 [Google](https://google.com/) 如何以更好的方式构建搜索结果。的 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 方法将这种功能重新赋予开发人员。开发人员现在能够定位特定的语义核心，并根据需要对其应用进行索引。

搜索操作。建议的设计支持区块链（和缠绕类似）资产相关活动。设计由 （1） 由创建者拥有的应用程序（2） 正确显示在搜索结果中，（3） 允许可处理的操作，以及 （4） 可证明的搜索查询转换属性，这微不足道。电子商务从来就不是那么容易。

非在线搜索。IPFS 使可以轻松地从没有全局互联网连接的环境中检索文档。 [去-cyber](https://github.com/cybercongress/go-cyber) 本身可以使用 IPFS 进行分发。这为无处不在的线下搜索创造了可能性！

命令工具。命令行工具可以依赖于搜索引擎的相关和结构化答案。实际上，以下 CLI 工具可以实现：

```
>  使用 100 GB 赚取网络收益

享受以下预测：
- 贴切安装文件币：            0.001   BTC p/ 月 p/ GB
- 贴切安装西亚德：            0.0007  BTC p/ 月 p/ GB
- 贴切安装 storjd：          0.0005 BTC p/ 月 p/ GB

根据最可取的预测，我决定尝试'我的去文件币 - 限制 107374182400`

Git 克隆 ...
建筑文件币
开始文件币
使用@xhipster种子创建钱包
您的地址是 ...
出价 ...
正在等待传入存储请求 ...
```

从CLI内部搜索工具将不可避免地为机器人创建一个极具竞争力的专用语义核心市场。

自主机器人。区块链技术能够创建能够自行管理数字资产的设备。

```
如果机器人可以存储、赚取、消费和投资 - 他们可以做你能做的一切
```

所需要的是一个简单，但强大的国家现实工具，能够找到特定的东西。 [去-cyber](https://github.com/cybercongress/go-cyber) 提供了一个简约的，但一个不断自我改进的数据源，为编程经济理性的机器人提供了必要的工具。根据 [最佳-10,000 英语单词](https://github.com/first20hours/google-10000-english) 英语中最流行的词是定义文章"the"，意思是指向特定项的指针。这一事实可以解释为：特定项目对我们最重要。因此，我们的本质是寻找独特的东西。因此，对独特事物的理解对于机器人也至关重要。

语言融合。程序员不应关心代理将使用的语言。我们不需要知道代理在哪个语言中执行搜索。整个 UTF-8 频谱都在工作。语义核心是开放的，因此应答查询的竞争可能会分布在不同的域特定区域。包括各种语言的语义内核。这种统一的方法为网络-巴哈萨创造了机会。自互联网诞生以来，我们观察到一个快速语言融合的过程。我们在整个星球上使用真正的全球词汇，独立于国籍、语言、种族、姓名或互联网连接。真正的全球语言的梦想很难实现，因为很难就什么意味着什么达成一致。然而，我们有工具使这个梦想成真。不难预测，一个词越短，其网络排名就越强大。按网络排名分类的符号、单词和短语的全局公开列表，以及由提供相应的链接[去-cyber](https://github.com/cybercongress/go-cyber) 可以成为每个人都能接受的真正全球语言出现的基础。最近 [科学进步](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1) 在机器翻译是惊人的，但毫无意义的人谁想要应用他们没有谷歌规模训练模型。拟议的网络排名正是提供这一点。

自我预测。  [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 可以连续构建 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 自己预测的存在[cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 并将这些预测应用到其状态。因此， [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 可以参与经济共识 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 协议。

通用预言。 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 可以将最相关的数据存储在键值存储中。其中键是 CID，并且值是实际内容的字节。这可以通过每轮做一个决定来实现，对于代理想要修剪的 CID 值以及他们希望应用的价值。基于 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)。 要计算实用程序度量，英雄检查 [知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph), 然后，重量的CID的大小和它的排名。紧急密钥值存储可用于写入 [共识计算机](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 只为代理，而不是代理。但是，值可以在程序中使用。

位置感知搜索。可以构造 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 与 [位置证明](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) 基于显着的现有协议，如 [泡沫](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG). 因此，如果 Web3 代理将挖掘三角剖分并附加[位置证明](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG)每个链接链。

预测市场链接相关性。我们可以使用[知识图](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 基于链路相关性的预测市场。一个应用程序，允许投注链接相关性，可以成为一个独特的来源，为方向的术语，以及，以及，并激励代理提交更多的链接。

私人网络链接。隐私是根本。虽然我们致力于隐私，实现私有 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 对于我们的团队来说，在创世纪中是不可行的。因此，由社区处理 WASM 程序，可以在协议之上执行。问题是根据 [cyber链接](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 由 Web3 大师提交，但没有透露：他们以前的请求或公钥。一般来说，零知识证明非常昂贵。我们认为，搜索的隐私应该是一个设计功能，但我们不确定我们是否知道如何在现阶段实现它。 [队列](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk) 像递归的咆哮和 [梦宝](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg) 从理论上讲，这种结构可以解决部分隐私问题。但是，它们是新的，未经测试，无论如何，与透明的替代方案相比，它们在计算方面的成本更高。

这当然不是所有可能的应用程序的过多列表，而是一个非常令人兴奋的应用程序。

## 结论

我们定义并实施了一项协议，用于在协商一致的计算机之间就相关性进行可证明的通信。该协议基于知识图的简单概念，这些知识图是由代理通过使用网络链接生成的。网络链接由共识计算机使用关联机的概念进行处理。网络共识计算机基于 CIDv0/CIDv1，以 Go-IPFS 和宇宙-SDK 为基础。IPFS在资源消耗方面提供了显著的好处。CID 作为主对象，其简单性强。对于每个 CID，网络排名由一个协商一致的计算机计算，没有一个故障点。网络+Rank 是 CYB 的令牌加权 PageRank，具有经济保护，免受 sybil 攻击和自私投票。每个圆的默克根的排名和图形树被发布。因此，每台计算机都可以向任何其他计算机证明给定 CID 的值的相关性。Sybil 电阻基于带宽限制。嵌入式程序执行能力提供了鼓舞人心的应用程序。启动的首要目标是索引点对点内容地址系统，无论是无状态的，例如：IPFS、Swarm、Sia、Git、BitTorrent 或有状态，例如：比特币、以非庭和其他区块链和纠结。网络链接的拟议语义提供了一个可靠的机制，通过共识的计算机本身预测对象之间的有意义的关系。关联计算机的源代码是开源的。共识计算机累积的每一点数据都可供任何人使用，如果一个人有资源来处理它。建议的软件实现的性能足以实现无缝交互。建议实现的可伸缩性足以索引当前存在的所有自身份验证数据，并可将其用于 Great Web 的数百万代理。区块链由超级智能管理，该智能在 Tendermint 共识算法下使用标准治理模块。尽管该系统提供了为传统搜索引擎提供替代方案的必要实用程序，但它并不仅限于此用例。该系统可扩展到许多应用，并使得设计经济合理的自有机器人成为可能，可以自主地理解它们周围的物体。

## 引用

1. [学术情境漂流](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN)
2. [全新堆栈](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw)
3. [搜索引擎信息检索在实践中](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6)
4. [对抗性示例研究的激励游戏](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9)
5. [分散搜索的想法](https://ipfs.io/ipfs/QmXNoGTWLQrcFRb66oS4HafpP1vcLKbVkJrQm4DVvihuoq)
6. [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps)
7. [DAT](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR)
8. [去-cyber](https://github.com/cybercongress/go-cyber)
9. [宇宙-sdk](https://github.com/cosmos/cosmos-sdk)
10. [CIDv1](https://github.com/multiformats/cid#cidv1)
11. [cyber.网页](http://cyber.page/)
12. [努力](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md)
13. [群](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj)
14. [真比特](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)
15. [预测的热力学](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb)
16. [页面排名](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw)
17. [RFC-6962](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG)
18. [IBC 协议](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk)
19. [嫩明特](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ)
20. [Web3 浏览器的比较](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md)
21. [Cyb](https://cyb.ai/)
22. [斯普林兰克](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC)
23. [在网络协议中运行验证器](https://cybercongress.ai/docs/go-cyber/run_validator/)
24. [前 10000 个英语单词](https://github.com/first20hours/google-10000-english)
25. [多语言神经机翻译](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1)
26. [泡沫](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG)
27. [队列](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk)
28. [温布尔姆](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg)
29. [特佐斯](https://ipfs.io/ipfs/QmdSQ1AGTizWjSRaVLJ8Bw9j1xi6CGLptNUcUodBwCkKNS)
30. [软件2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35)
31. [历史证明](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs)
32. [IPLD](https://github.com/ipld)
33. [网络〜大会组织](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330/)
34. [网络〜网络大会](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8)
35. [网络〜宇宙大会](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a)
36. [CYB分发的multisig](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j)
37. [.cyber](https://github.com/cybercongress/dot-cyber)

## 确认

1. @hleb-albau
2. @arturalbov
3. @jaekwon
4. @ebuchman
5. @npopeka
6. @belya
7. @serejandmyself
