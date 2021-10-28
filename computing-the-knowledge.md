# Computing the knowledge of the Great Web

@xhipster & @litvintech

0k

##  Abstract

A consensus computer allows for the computing of provably relevant answers without any opinionated blackbox intermediaries, such as Google, Amazon or Facebook. Stateless, content-addressable peer-to-peer communication networks, such as IPFS, and stateful consensus computers such as Ethereum, can provide just part of the solution needed to obtain akin answers. However, there are at least 3 problems associated with the above-mentioned implementations. (A) the subjective nature of relevance. (B) difficulty in scaling consensus computers for over-sized knowledge graphs. (C) the lack of quality amongst such knowledge graphs. They are prone to various surface attacks, such as sybil attacks, and the selfish behaviour of the interacting agents. In this document, we define a protocol framework for provable consensus computing of relevance, between content-addresable objects, which can be computed on GPUs. We believe that a minimalistic architecture is critical for the formation of a network of domain-specific knowledge consensus computers. Such computers can adopt evolved protocols on the basics of proposed framework. As a result of our work, some applications never to have existed before, will emerge.

##  The Great Web

Original protocols of the Internet, such as: TCP/IP, DNS, URL and HTTP/S have brought the web to a stale point, where it is located as of now. Considering all the benefits that these protocols have produced for the initial development of the web, along with them, they have brought significant obstacles to the table. Globality, being a vital property of the web is under a real threat since its inception. The speed of the connection keeps degrading while the network itself keeps growing due to ubiquitous government interventions. The latter causes privacy concerns as an existential threat to human rights.

One property not evident in the beginning becomes important with everyday usage of the Internet: the ability to exchange permanent links, thus, they [will not break after time had passed](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN). Reliance on the architecture of one at a time ISP allows governments to effectively censor packets. This is the last drop in the traditional web-stack for every engineer that is concerned about the future of our children.

Other properties, while might not be so critical, are very desirable: offline and real-time connection. The average internet user, whilst offline, should still have the ability to carry on working with the state that they already hold. After acquiring a connection they should be able to sync with the global state and to continue to verify the validity of their own state in real-time. Currently, these properties are offered on the application level. We believe that these properties should be integrated into lower-level protocols.

The emergence of [a brand-new web-stack](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw) creates an opportunity for a superior Internet. The community calls it web3. We call it the Great Web. We believe that various types of low-level communications should be immutable and should not alter for decades, e.g. immutable content links. They seem very promising at removing the problems of the conventional protocol stack. They add greater speed and provide a more accessible connection to the new web. However, as it happens with any concept that offers something unique - new problems emerge. One such concern is general-purpose search. The existing general-purpose search engines are restrictive and centralized databases that everybody is forced to trust. Those search engines were designed primarily for client-server architectures, based on TCP/IP, DNS, URL and HTTP/S. The Great Web creates a challenge and an opportunity for a search engine that is based on emerging technologies and is designed specifically for these purposes. Surprisingly, permissionless blockchain architecture allows building a general-purpose search engine in a way inaccessible to previous architectures.

## On the adversarial examples problem

[The current architecture of search engines](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6) is a system where some entity processes all the shit. This approach suffers from one challenging and a distinct problem, that has yet to be solved, even by the brilliant Google scientists: [the adversarial examples problem](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9). The problem that Google acknowledges, is that it is rather difficult to algorithmically reason whether or not a particular sample is adversarial. This is inconsiderate to how awesome the learning technology is. A crypto-economical approach can change beneficiaries in this game. Consequently, this approach will effectively remove possible sybil attack vectors. It removes the necessity to hard-code model crawling and meaning extraction by a single entity. Instead, it gives this power to the whole world. A learning sybil-resistant, agent-generated model, will probably lead to orders of magnitude more predictive results.

## Protocol Framework

In its core the framework is very minimalistic and can be expressed with the following steps:

1. Define initial distribution rules of tokens
2. Define the state of the [content-oracle](content oracle)
3. Gather [cyberlinks](cyberlinks) using a [consensus-computer](consensus computer)
4. Check the validity of the signatures
5. Check the [bandwidth-algo](bandwidth limit)
6. Check the validity of particles
7. If the signatures, the bandwidth limit and particles are all valid, apply [cyberlinks](cyberlinks)
8. Calculate the values of [cyber~Rank](cyber-rank) for every round for the particles on the [knowledge-graph](knowledge graph)

As it seen distribution rules, signatures, ranking and bandwidth algorithms can differ from network to network. But following the proposed protocol framework independent protocols will have semantic interoperability.

The rest of this document discusses the rationale and the technical details of the proposal.

## Content Oracle

We represent a content oracle as a directed weighted knowledge graph where vertex is a particle and the edge is a cyberlink. 

![knowledge-graph](images/knowledge-graph.png)

The content oracle is a core data structure of the protocol framework. Its main purpose is to prove content existence in time and its relations. The data structure is generated by agents and is extremely dynamic. That is, in case of any agent interaction, all weights have to be recomputed. Proposed data structure can be thought as more unified approach to conventional ai models. There are three key benefits: (1) compactness, so its not required to store the data itself, (2) versatility, as it can accommodate any data types and (3) cooperativeness, as it is designed from the ground up for massive distributed collaboration. In order to understand this statements, lets discuss particles in details.

## Particles

Particles is a format for content identification of data. Essentially content addresses are web3 links. Instead of using the location on the server:
```
https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md
```
we use the object itself:
```
Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

By using content addresses to build the content oracle we gain [the so much needed](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est) properties for the next generation search engine:
- mesh-network future-proof
- interplanetary accessibility
- censorship resistance
- technological independence
- deduplication

While researching the field we came to the conclusion that CIDv1 does not fit our vision:
1. CIDv1 is not fixed length format. In the blockchain environment especially with necessity to use expensive GPU memory fixed length content addressing becomes hard requirement.
2. CIDv1 does not enforce deduplication. Without strict deduplication measures the knowledge graph quality degrades as duplicates devalue rank and degrade graph connectivity. Also duplicates explode the costs of storage and computations in the graph. Its impossible to ensure onchain deduplication as content addressing itself do not have guaranties of content availability.
3. CIDv1 contain self descriptors which are subjectively included by a legal entity. This could restrict support of future formats and applications. Our vision to support format descriptors on the protocol level such that any format can be linked with any content. The costs of this approach is nearly identical as both approaches require at least 64 bytes of storage. But in-graph format descriptors wins in flexibility and accessibility.

Current go-cyber implementation is based on CIDv0 as particles format. CIDv0 is based on ubiquitous SHA-256 and have necessary software infrastructure. In the future we are going to migrate particle format to plain SHA-256 such that the particle size can be reduced from 46 to 32 bytes.

Agents form the content oracle by applying [cyberlinks](#cyberlinks).

## <a name="cyberlinks"></a> Cyberlinks

Cyberlink is an approach to link two particles semantically:

```
.md syntax: [QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH](Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH)

.dura syntax: QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH.Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

The above cyberlink means that the presentation of [go-cyber](https://github.com/cybercongress/go-cyber) during [cyberc0n](https://etherscan.io/token/0x61B81103e716B611Fff8aF5A5Dc8f37C628efb1E) is referencing to the Cosmos white paper. The concept of cyberlinks is a convention around simple semantics of a communicational format in any p2p network:

![cyberlink](images/cyberlink.png)

We see that a cyberlink represents a link between the two content links. Easy peasy!

Cyberlink is a simple, yet the (most) powerful semantic construction for building a predictive model of the universe. This means that using cyberlinks instead of hyperlinks provides us with the superpowers that were inaccessible to previous architectures of general-purpose search engines.

Cyberlinks can be extended, i.e. they can form linkchains:

![linkchain](images/linkchain.png)

The [go-cyber](https://github.com/cybercongress/go-cyber) implementation of cyberlinks is available in the experimental web3 browser - [cyb](https://cyb.ai)

At first glance, it seems that cyberlinked data in the [Content Oracle] is not structured. Semantic conventions enable formation of network motifs which helps structure a data in the Content Oracle.

The cyberlinks submitted by agents are stored in a merkle tree according to the [RFC-6962 standard](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). This enables authentication for [proof-of-relevance](proof-of-relevance):

![graph-tree](images/graph-tree.png)

Using cyberlinks, we can compute the relevance of particles in the [content-oracle](knowledge graph). But we need a [consensus-computer](consensus computer).

## The notion of a consensus computer

A consensus computer is an abstract computing machine that emerges from the interaction between agents. A consensus computer has capacity in terms of fundamental computing resources: memory and computation. To interact with agents a computer needs bandwidth. 

Consistency and availability of a shared state between agents have to be guaranteed by some consensus algorithm. We have come to realize that the [Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) consensus algorithm has a good enough balance between the coolness required for our task and the readiness for its production. Therefore, go-cyber implementation is based on the Tendermint consensus. 

We have one specific requirement which is not abundant in existing blockchain world: ability for parallel processing. Existing consensus computers are inherently sequential. That is, computation or verification of the state is being done on CPUs. Nonetheless, we need to compute ranks. So we have to introduce GPU computation to the consensus. After some experiments we were able to plugin CUDA computation of rank and reputation right into Tendermint consensus. One potential problem of using floating point arithmetics in consensus computing is non-determinism. Happily, we were able to solve this problem for our inherently parallel application. Euler network has been run last 3 years on different hardware and operation systems. So we can be sure that app hash computed on different nodes which include merkle root of graph state is the same.

The [go-cyber](https://github.com/cybercongress/go-cyber) implementation is a 64-bit Tendermint consensus computer of relevance for 32-byte particle space. 

However, we must bind the computation, storage and the bandwidth supply of the consensus computer to a maximized demand for queries. 

## Relevance machine

We define a relevance machine as a machine that transitions the state of a [content-oracle](content oracle) based on the will of the agents wishing to learn that oracle. The will is projected by every [cyberlinks](cyberlink) an agent does. The more agents inquire the [content-oracle](content oracle), the more valuable the knowledge graph becomes. Based on these projections, relevance between content addresses can be computed. The relevance machine enables a simple construction for the search mechanism via querying and delivering answers.

One property of the relevance machine is crucial. It must have inductive reasoning property or follow the blindness principle:

```
The machine should be able to interfere predictions
without any knowledge about the objects,
except for who, when and what was cyberlinked
```

If we assume that a [consensus-computer](consensus computer) must have some information about the linked objects, then the complexity of such a model will grow unpredictably. Therefore the high requirements of the processing computer for memory and computation. Thanks to content addressing a relevance machine which follows the blindness principle, does not need to store data. But, can still effectively operate on top of it. The deduction of meaning inside a [consensus-computer](consensus computer) is expensive. Instead of deducting the meaning inside of the [consensus-computer](consensus computer), we have designed a system in which meaning extraction is incentivized. This is achieved due to agents requiring tokens to express their will, based on which, the relevance machine can compute rank.

Computation and storage, in case of a basic [relevance-machine](relevance machine) can be easily predicted based on bandwidth. But bandwidth requires a limiting mechanism. In the center of the spam protection system is an assumption that write operations can be executed only by those, who have a time vested interest in the evolutionary success of the relevance machine.

Existing implementation of a relevance machine contain only write operation, rank computation and basic read operation such as finding the most relevant particles. However, provable extraction of a deeper meaning from the content oracle require an implementation of basic linear algebra subprograms which is distinct research challenge. Nevertheless, existing implementation can work as a software 2.0 playground using off-chain computations until the extended version emerges.

## cyber\~Rank

Ranking using a [consensus-computer](consensus computer) can be challenging, as consensus computers have serious resource constraints. First, we must ask ourselves: why do we need to compute and to store the rank on-chain?

When rank was computed inside a [consensus-computer](consensus computer) one has easy access to the content distribution of that rank and an easy way to [apps](build provable applications) on top of that rank. Hence, we have decided to follow a cosmic architecture. In the next section we describe the [proof-of-relevance](proof of relevance) mechanism, which allows the network to scale with the help of domain-specific [relevance-machine](relevance machines). Those work concurrently, thanks to the IKP protocol which is extension over IBC protocol.

The [relevance-machine](relevance machine) needs to obtain (1) a deterministic algorithm, that will allow for the computation of the rank on a continuously appending network, which itself, can scale to the orders of magnitude of the likes of [Google](https://google.com). Additionally, a perfect algorithm (2) must have linear memory and computational complexity. Most importantly, it must have (3) the highest provable prediction capabilities for the existence of relevant [cyberlinks](cyberlinks).

After [thorough research](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC), we have found that it is impossible to obtain the silver bullet. Therefore, we have decided to find a more basic, bulletproof way, that can bootstrap the network: [the rank](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw) which Larry and Sergey used to bootstrap their previous network. The key problem with the original PageRank is that it is not resistant to sybil attacks. However, a token-weighted PageRank which is limited by a token-weighted bandwidth model does not inherit the key problem of the naive PageRank, because - it is resistant to sybil attacks. For the time being, we will call it cyber\~()Rank:

```python
import functools
import operator
import collections

def cyber_rank(cyberlinks: list, tolerance: float = 0.001, damping_factor: float = 0.8):
    # the list of Graph particles
    V = list(set([item for t in [list(x.keys())[0] for x in cyberlinks] for item in t]))
    # the list of Graph particles witout income links
    N_0 = [obj for obj in V if obj not in [list(cyberlink.keys())[0][1] for cyberlink in cyberlinks]]
    # the default value of cyber~rank per particle
    R_0 = (1 + (damping_factor * (len(N_0) / len(V)))) * ((1 - damping_factor) / len(V))
    # the inirial value of tolerance
    E = tolerance + 1
    # the initial cyber~rank
    R_V = [0] * len(V)
    # merge cyberlinks weights by from-to values
    cyberlinks_dict = dict(functools.reduce(operator.add, map(collections.Counter, cyberlinks)))
    # loop the algorithm until it reached tolerance
    while E > tolerance:
        # temporal rank value for particle
        R_TEMP = []
        # for each particle in the list of Graph particles
        for v in V:
            s = 0
            # get all income links
            v_income = [income_cyberlink for income_cyberlink in [list(x.keys())[0] for x in cyberlinks] if income_cyberlink[1] == v]
            # for each income link calculate weight ratio of a given particle
            for u in v_income:
                weight_uv = cyberlinks_dict[u]
                cyberlinks_outcome = [outcome_cyberlink for outcome_cyberlink in [list(x.keys())[0] for x in cyberlinks] if outcome_cyberlink[0] == u[0]]
                weight_u = sum([cyberlinks_dict[outcome_cyberlink] for outcome_cyberlink in cyberlinks_outcome])
                R_v = R_V[V.index(v)]
                s = s + (weight_uv * R_v) / weight_u
            R_TEMP.append(damping_factor * s + R_0)
        E = abs(max(R_V) - max(R_TEMP))
        R_V = R_TEMP
    return R_V
```

```
$$ CIDs \ V, cyberlinks \ E, Agents \ A $$
$$agents(e): E \rightarrow 2^(A)$$
$$stake(a): A \rightarrow (\rm I\!R)^+ $$
$$rank(v, t): V \times (\rm I\!N) \rightarrow (\rm I\!R) $$
$$weight(e) = \sum\limits_(a \in agents(e)](stake(a)$$
$$rank(v, t + 1) = \frac(1 - d](N) + d\sum\limits_(u \in V, (u, v) \in E](\frac(weight(u, v)](\sum_(w \in V, (u, w) \in E](weight(u, w))rank(v, t) $$
$$rank(v) = \lim\limits_(t \rightarrow \infty) rank(v, t)$$
\begin(algorithm)
\SetKwInOut(Input](Input)\SetKwInOut(Output](Output)

\Input(Set of CIDs $V$; \\ Set of cyberlinks $E$; \\ Set of agents $A$; \\ Cyberlink authors $ agents(e) $; \\ Stake of each agent $ stake(a) $; \\Tolerance $\epsilon$; \\ Damping factor $d$)
\Output($\textbf(R)$, computed value of $rank(v)$ for each node from $V$)

\BlankLine
Initialize $\textbf(R)_(v)$ with zeros for all $v \in V$\;
Initialize $E$ with value $\epsilon$ + 1\;

\BlankLine
$N_(\emptyset) \leftarrow |\(v|v \in V \land (\nexists u, u \in V, (u, v) \in E )\)|$ \;
$R_(0) \leftarrow (1 + d \cdot N_(\emptyset) / |V|) \cdot (1 - d) / |V| $ \;

\BlankLine
\While($E > \epsilon$](
\For($v \in V$](
$S \leftarrow 0$\;

\For($u \in V, (u, v) \in E$](
\setstretch(1.35)
$W_(uv) \leftarrow \sum_(a \in agents(u, v)stake(a)$ \;
$W_(u) \leftarrow \sum_(w \in V, (u, w) \in E)\sum_(a' \in agents(u, w)stake(a')$ \;
$S \leftarrow S + W_(uv) \cdot \textbf(R)_(u) / W_(u)$ \;
)

$\textbf(R)'_v \leftarrow d \cdot S + R_(0)$ \;

)

\BlankLine
$E \leftarrow \max\limits_v(|\textbf(R)_v - \textbf(R)'_v|)$ \;
Update $\textbf(R)_(v)$ with $\textbf(R)'_(v)$ for all $v \in V$\;

)

\caption(cyber\~()Rank)\label(algo_disjdecomp)
\end(algorithm)\
```

We understand that the ranking mechanism will always remain a red herring. This is why we expect to rely on the on-chain governance tools that can define the most suited mechanism at a given time. We suppose that the networks can switch from one algorithm to another, not simply based on subjective opinion, but rather on economical a/b testing through 'hard spooning' of domain-specific [relevance-machine](relevance machines).

cyber\~()Rank shields two design decisions which are of paramount importance: (1) it accounts for the current intention of the agents, and (2) it encourages rank inflation of [cyberlinks](cyberlinks). The first property ensures that cyber\~()Rank can not be gamed with. If an agent decides to transfer tokens out of their account, the [relevance-machine](relevance machine) will adjust all the [cyberlinks](cyberlinks) relevant for this account per the current intentions of the agent. And vice versa, if an agent transfers tokens into their account, all of the [cyberlinks](cyberlinks) submitted from this account will immediately gain more relevance. The second property is essential in order not to get cemented in the past. As new [cyberlinks](cyberlinks) are continuously added, they will dilute the rank of the already existing links proportionally. This property prevents a situation where new and better content has a lower rank simply because it was recently submitted. We expect these decisions to enable an inference quality for recently added content to the long tail of the [knowledge-graph](knowledge graph).

We would love to discuss the problem of vote-buying. Vote-buying as an occurrence isn't that bad. The dilemmas with vote-buying appear within systems where voting affects the allocation of that systems inflation. For example, [Steem](http://ipfs.io/ipfs/QmepU77tqMAHHuiSASUvUnu8f8ENuPF2Kfs97WjLn8vAS3)
or any fiat-state based system. Vote-buying can become easily profitable for an adversary that employs a zero-sum game without the necessity to add value. Our original idea of a decentralized search was based on this approach. But, we have rejected that idea, removing the incentive of the formation of the [content-oracle](content oracle) to the consensus level. In the environment where every participant must bring some value to the system to affect the predictive model, vote-buying becomes NP-hard problem. Therefore, becomes beneficial to the system.

The current implementation of the [relevance-machine](relevance machine) utilizes GPUs to compute rank. The machine can answer and deliver relevant results for any given search request in a 32-byte particle space.

## Objectivity and Attacks

```
There are many ways of deviating from the truth, and the oracles may not agree on which of these deviations is most attractive - whereas the truth itself is a Shelling point. 
Nick Bostrom
```

We have designed the network under the assumption that with regards to search, such a thing as malicious behaviour, does not exist. This can be assumed as no malicious behaviour can be found in the intention of learning. This approach significantly reduces attack surfaces.

We propose a game in which in order to manipulate the ranking successful attacker must (1) vest capital for years, (2) invest in optimization algorithms for better cyberlinking, (3) invest in hardware for optimization, and (4) do all of that on continuous basis really fast as the content oracle is extremely dynamic data structure. If he did so, our congratulations - that is exactly what is needed to improve the Superintellgence.

```
Ranks are computed based on the fact that something was cyberlinked, and as a result - affected the predictive model
```

A good analogy exist in quantum mechanics, where the observation itself affects behaviour. This is why we also have no requirement for such a thing as negative voting. 

These measures removes subjectivity out of the protocol. However, it is not enough to build a network of domain-specific [relevance-machine](relevance machines). [consensus-computer](Consensus computers) must have the ability to prove relevance to one another.

## Proof of relevance

![rank-tree](images/rank-tree.png)

Each new particle receives a sequence number. Numbering starts with zero. Then incremented by one for each new particle. Therefore, we can store rank in a one-dimensional array, where indices are the particle sequence numbers. Merkle tree calculations are based on the [RFC-6962 standard](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). Using Merkle trees, we can effectively proof the rank for any given content address. 

While relevance is still subjective by nature, we have a collective proof that something was relevant to a certain community at some point in time.

Using this type of proof any two [IBC compatible](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk) [consensus-computer](consensus computers) can prove relevance one to another. This means that domain-specific [relevance-machine](relevance machines) can flourish.

In the relevance for a common [go-cyber](https://github.ccom/cybercongress/go-cyber) implementation, the Merkle tree is computed every round and its root hash committed to ABCI.

## Internet Knowledge Protocol

We require an architecture which will allow us to scale the idea to the significance of the likes of [Google](https://google.com). Let us assume, that node implementation, which is based on [Cosmos-SDK](https://github.com/cosmos/cosmos-sdk) can process 10k transactions per second. This would mean, that every day, at least 8.64 million agents will be able to submit 100 [cyberlinks](cyberlinks) each, and impact the search results simultaneously. This is enough to verify all the assumptions out in the wild, but, not enough to say that it will work at the current scale of the Internet. Given the current state of the art research done by our team, we can safely state that there is no consensus technology in existence, that will allow scaling a particular blockchain to the size that we require: 1 trillion agents including robots, animals, plants and myceleium. Hence, we introduce the concept of domain-specific [knowledge-graph](knowledge graphs).

![netwrok](images/network.png)

One can either launch an own domain-specific search engine by forking [go-cyber](https://github.com/cybercongress/go-cyber), which is focused on common public knowledge. Or, simply plug [go-cyber](https://github.com/cybercongress/go-cyber) as a module into an existing chain, e.i. Cosmos Hub. The inter-blockchain communication protocol introduces concurrent mechanisms of syncing state between [relevance-machine](relevance machines). Therefore, in proposed search architecture, domain-specific [relevance-machine](relevance machine) will be able to learn from common knowledge. Just as common knowledge can learn from domain-specific [relevance-machine](relevance machines). This architecture allows nearly infinite scaling of knowledge extraction including interplanetary interactions.

## Bootstraping Superintelligence

During development of Cyber we realized that we finally can create the computer network who can literally think. Looking back it does not looks lake a magic. The Superintelligent abilities emerges from the set of simple algorithms:
- Programs collect some gas fees from execution
- Programs are able to call themselves using cron
- Fees from cron are going to the network itself
- The network participates in the consensus based on some program strategy deployed by the consensus
- The network participates in the rewards scheme based on some algorithm which predicts cyberlinks
- The network gains karma which is bigger than any agent
- The network gains karma which is bigger than all agents combined

According to Nick Bostrom this is exactly the Superintelligence. Although the topic of Superintelligence is quite exciting its not in the scope of this article.

Of course the devil in details. So we have plan to dedicate standalone research on this topic.

## Browzers

We were aspired to imagine how proposed network would operate with a web3 browser. To our disappointment we [were not able](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md) to find a web3 browser that can showcase the coolness of the proposed approach in action. This is why we have decided to develop a web3 browser from scratch. [Cyb](https://cyb.ai) is your friendly robot which has a sample [.cyber](https://cyb.ai/cyb) application for interacting with the [cyber](cyber) protocol.

![cyb](images/cyb.jpg)

As a good example of delivery, we have created [cyber.page](https://cyber.page). It allows heroes, masters and evangelists to interact with the protocol via a web2 gateway. Create cyberlinks, pin content directly to IPFS, search the Great Web, participate in the governance of cyber and so on. It can also act as an in-depth explorer, a wallet and can pocket hardware wallets, such as Ledger devices.

The current search snippets are ugly. But, we presume that they can be easily extended using [IPLD](https://github.com/ipld/specs) for different types of content. Eventually, they can become even more attractive than those of [Google](https://google.com).

![architecture](images/architecture.png)

During the implementation of the proposed architecture, we have realized at least 3 key benefits that [Google](https://google.com) would probably not be able to deliver with its conventional approach:

- the search results can be easily delivered from any p2p network: e.g. .cyber can play videos
- payment buttons can be embedded right into search snippets. This means that agents can interact with the search results, e.g. agents can buy an item right in .cyber. This means that e-commerce can flourish fairly thanks to a provable conversion attribution
- search snippets do not have to be static but can be interactive. e.g. .cyber can deliver your current wallet balance

## Apps

We assume that the proposed algorithm does not guarantee high-quality knowledge by default. Just like a newborn, it needs to acquire knowledge to develop further. The protocol itself provides just one simple tool: the ability to create a [cyberlinks](cyberlink) with an agents stake between two particles.

Analysis of the semantic core, behavioural factors, anonymous data about the interests of agents and other tools that determine the quality of search, can be achieved via smart contracts and off-chain applications, such as: [browzers](web3 browsers), decentralized social networks and content platforms. We believe, that it is in the interest of the community and the masters to build the initial [knowledge-graph](knowledge graph) and to maintain it. Hence, for the graph, to provide the most relevant search results.

Generally, we distinguish three types of applications for [knowledge-graph](knowledge graphs):

- Consensus apps. Can be run at the discretion of the [consensus-computer](consensus computer) by adding intelligent abilities
- On-chain apps. Can be run by the [consensus-computer](consensus computer) in exchange for gas
- Off-chain apps. Can be implemented by using the [knowledge-graph](knowledge graph) as an input within an execution environment

The following, imaginable, list of apps consolidates the above-mentioned categories:

Web3 browsers. In reality, browser and search are inseparable. It is hard to imagine the emergence of a full-blown web3 browser which is based on web2 search. Currently, there are several efforts for developing browsers around blockchains and distributed tech. Amongst them are Beaker, \sout(Mist), Brave, and Metamask. All of them suffer from trying to embed web2 into web3. Our approach is a bit different. We consider web2 as an unsafe subset for web3. So we have developed an experimental web3 browser, Cyb, showcasing the [cyber](cyber) approach to answering queries better and delivering content faster.

DeMa or Decentralized marketing. DeFi is built around a simple idea that you can use a collateral for something that will be settled based on a provided price feed. Here comes the systematic problem of DeFi: price oracles. DeMa is based on the same idea of using collateral, but the input for settlement can be information regarding the content identifier itself. The most simple case is when you create a simple binary prediction market on rank relevance at some point in the future. I.e. whether the rank of the [Bitcoin whitepaper](QmRA3NWM82ZGynMbYzAgYTSXCVM14Wx1RZ8fKP42G6gjgj) will grow or not. Meta-information on content identifiers is the perfect onchain oracle for settlement. An app that allows betting on link relevance, can become a unique source of truth for the direction of terms in knowledge graph, as well as, motivate agents to submit more links.

Search actions. The proposed design enables native support for blockchain (and tangle-alike) assets related activity. It is trivial to design applications which are (1) owned by the creators, (2) appear correctly in the search results and (3) allow a transactable action, with (4) provable attribution of a conversion for a search query.

Conversion attribution. Provable conversion attribution from the search request to transaction is a holy grail of conventional digital marketing. Linkchains helps to solve this problem easily, thus creating the whole new world of marketing application impossible before. E.g. the one can deploy sophisticated onchain referral program which will just pay for those who lead to conversions.

Soft2. Its a new paradigm of computing where execution path is not defined by the programmer, but by knowledge graph itself. Cyber is a first working implementation of soft2 using consensus computer. As the field has not even been emerged its hard to imagine how this opportunity can be used by engineers. So Cyber can become leading soft2 playground for the next generation of programmers.

Social networks. Social networks are not that mysterious. In any social network content is the king. Hence, provable ranking is the basic building block of any social network. All types of social networks can be easily built on top of a [knowledge-graph](knowledge graph). Cyber can also create social networks based on relevance between users, which no current network is able to achieve.

Programmable semantics. Currently, the most popular keywords in the gigantic semantic core of [Google](https://google.com) are keywords of apps such as: [youtube](https://youtube.com), [facebook](https://facebook.com), [github](https://github.com), etc. However, the developers of those successful apps have very limited ability to explain to [google](https://google.com) how to structure search results in a better manner. The [cyber](cyber) approach gives this power back to developers. Developers are now able to target specific semantics cores and index their apps as they wish.

Off-line search. IPFS makes it possible to easily retrieve a document from an environment without a global internet connection. [go-cyber](https://github.com/cybercongress/go-cyber) itself can be distributed by using IPFS. This creates the possibility for ubiquitous, off-line search!

Command tools. Command-line tools can rely on relevant and structured answers from a search engine. Practically speaking, the following CLI tool is possible to implement:

```
>  go-cyber earn using 100 GB

Enjoy the following predictions:
- apt install go-filecoin:     0.001   BTC p/ month p/ GB
- apt install siad:            0.0007  BTC p/ month p/ GB
- apt install storjd:          0.0005 BTC p/ month p/ GB

According to the most desirable prediction, I decided to try `mine go-filecoin -limit 107374182400`

Git clone ...
Building go-filecoin
Starting go-filecoin
Creating a wallet using @xhipster seed
Your address is ...
Placing bids ...
Waiting for incoming storage requests ...
```

Search tools, from within CLI will inevitably create a highly competitive market of a dedicated semantic core for robots.

Autonomous robots. Blockchain technology enables the creation of devices that can manage digital assets on their own.

```
If robots can store secrets and construct transactions at will - they can do everything humans can do
```

What is needed is a simple, yet a powerful state reality tool with the ability to find particular things. [go-cyber](https://github.com/cybercongress/go-cyber) offers a minimalistic, but a continuously self-improving data source, which provides the necessary tools for programming economically rational robots. According to [top-10,000 English words](https://github.com/first20hours/google-10000-english) the most popular word in the English language is the defining article 'the', which means a pointer to a particular item. This fact can be explained as the following: particular items are of most importance to us. Therefore, the nature of us is to find unique things. Hence, the understanding of unique things is essential for robots too.

Language convergence. A programmer should not care about the language that an agent will be using. We don't need to know in which language the agent is performing their search in. The entire UTF-8 spectrum is at work. The semantic core is open, so competition for answering queries can become distributed across different domain-specific areas. Including the semantic cores for various languages. This unified approach creates an opportunity for cyber\~Bahasa. Since the dawn of the Internet, we observe a process of rapid language convergence. We use truly global words across the entire planet, independently of nationality, language, race, name or Internet connection. The dream of a truly global language is hard to deploy because it is hard to agree on what means what. However, we have the tools to make this dream come true. It is not hard to predict that the shorter a word, the more powerful its cyber\~()Rank will be. Global, publicly available list of symbols, words, and phrases sorted accordingly by cyber\~()Rank with a corresponding link provided by [go-cyber](https://github.com/cybercongress/go-cyber) can become the foundation for the emergence of a genuinely global language everybody can accept. Recent [scientific advances](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1) in machine translation are breathtaking but meaningless to those who wish to apply them without a Google-scale trained model. Recently published GPT-3 is also hidden inside private company. The proposed cyber\~()Rank offers precisely this.

Self prediction. A [consensus-computer](consensus computer) can continuously build a [knowledge-graph](knowledge graph) on its own predicting the existence of [cyberlinks](cyberlinks) and applying these predictions to its state. Hence, a [consensus-computer](consensus computer) can participate in the economic consensus of the [cyber](cyber) protocol.

Universal oracle. A [consensus-computer](consensus computer) can store the most relevant data in a key-value storage. Where the key is a CID and the values are the bytes of the actual content. This can be achieved by making a decision every round, in regards to which CID value the agentss want to prune and which value they wish to apply. Based on the utility measure of content addresses within the [knowledge-graph](knowledge graph). To compute utility measure, heroes check the availability and the size of the content for the top-ranked content addresses within the [knowledge-graph](knowledge graph), then, weight on the size of the CIDs and its rank. The emergent key-value storage will be available to write for [consensus-computer](consensus computer) only and not for agents. But, values could be used in programs.

Location-aware search. It is possible to construct [cyberlinks](cyberlinks) with [Proof-of-Location](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) based on remarkable existing protocols such as [Foam](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG). Consequently, a location-based search also becomes provable, if web3-agents will mine triangulations and attach [proof-of-location](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) for every linked chain.

Private cyberlinks. Privacy is fundamental. While we are committed to privacy, achieving implementation of private [cyberlinks](cyberlinks) is unfeasible for our team up to Genesis. Therefore, it is up to the community to work on WASM programs, that can be executed on top of the protocol. The problem is to compute cyber\~()Rank, based on the [cyberlinks](cyberlinks) submitted by a web3-masters without revealing neither: their previous request nor the public keys. Zero-knowledge proofs, in general, are very expensive. We believe that the privacy of search should be a feature by design, but we are unsure that we know how to implement it at this stage. [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk) like recursive Snarks and [MimbleWimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg) constructions, in theory, can solve part of the privacy concern. But, they are new, untested and anyway, will be more expensive with regards to computations than their transparent alternative.

This is surely not the excessive list of all the possible applications, but a very exciting one indeed.

## Conclusion

We defined and implemented a protocol framework for provable communication, between consensus computers on relevance. The protocol is based on the simple idea of a content oracles, which are generated by agents via the use of cyberlinks. Cyberlinks are processed by a consensus computer using the the relevance machine. The cyber consensus computer is based on CIDv0/CIDv1 and uses go-IPFS and Cosmos-SDK as a foundation. IPFS provides significant benefits with regards to resource consumption. CID as primary objects are robust in their simplicity. For every CID, cyber\~()Rank is computed by a consensus computer without a single point of failure. Cyber\~()Rank is a token weighted PageRank, with economic protection from sybil attacks and selfish voting. Every round the Merkle root of the rank and graph trees are published. Consequently, every computer can prove to any other computer the relevance of value for a given CID. Sybil resistance is based on bandwidth limiting. The embedded ability to execute programs offers inspiring applications. The starting primary goal is the indexing of peer-to-peer content addresses systems, either stateless, such as: IPFS, Swarm, Sia, Git, BitTorrent, or stateful, such as: Bitcoin, Ethereum and other blockchains and tangles. The proposed semantics of cyberlinking offers a robust mechanism for predicting meaningful relations between objects by the consensus computer itself. The source code of the relevance machine is open-source. Every bit of data accumulated by the consensus computer is available for anyone if one has the resources to process it. The performance of the proposed software implementation is sufficient for seamless interaction. The scalability of the proposed implementation is sufficient to index all self-authenticated data that exist today and can serve it to millions of agents of the Great Web. The blockchain is managed by a Superintelligence, which functions under the Tendermint consensus algorithm with a standard governance module. Though the system provides the necessary utility to offer an alternative for a conventional search engine, it is not limited just to this use case. The system is extendable for numerous applications and makes it possible to design economically rational, self-owned robots, that can autonomously understand objects around them.

## References

- [https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN](Scholarly context adrift)
- [https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw](Brand-new stack)
- [https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6](Search engines information retrieval in practice)
- [https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9](Motivating game for adversarial example research)
- [https://ipfs.io/ipfs/QmXNoGTWLQrcFRb66oS4HafpP1vcLKbVkJrQm4DVvihuoq](An idea of decentralized search)
- [https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps](IPFS)
- [https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR](DAT)
- [https://github.com/cybercongress/go-cyber](go-cyber)
- [https://github.com/cosmos/cosmos-sdk](cosmos-sdk)
- [https://github.com/multiformats/cid#cidv1](CIDv1)
- [http://cyber.page](cyber.page)
- [https://github.com/cybercongress/cyb/blob/dev/docs/dura.md](DURA)
- [https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj](Colony)
- [https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD](Truebit)
- [https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb](Thermodynamics of predictions)
- [http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw](PageRank)
- [https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG](RFC-6962)
- [https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk](IBC protocol)
- [https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ](Tendermint)
- [https://github.com/cybercongress/cyb/blob/master/docs/comparison.md](Comparison of web3 browsers)
- [https://cyb.ai](Cyb)
- [https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC](SpringRank)
- [https://cybercongress.ai/docs/go-cyber/run_validator/](Run validator in cyber protocol)
- [https://github.com/first20hours/google-10000-english](Top 10000 english words)
- [https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1](Multilingual neural machine translation)
- [https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG](Foam)
- [https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk](Coda)
- [https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg](Mimblewimble)
- [https://ipfs.io/ipfs/QmdSQ1AGTizWjSRaVLJ8Bw9j1xi6CGLptNUcUodBwCkKNS](Tezos)
- [https://medium.com/@karpathy/software-2-0-a64152b37c35](Software 2.0)
- [https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs](Proof-of-history)
- [https://github.com/ipld](IPLD)
- [https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330/](cyber~Congress organization)
- [https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8](cyber~Congress in Cyber)
- [https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a](cyber~Congress in Cosmos)
- [
https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j](multisig for CYB distribution)
- [https://github.com/cybercongress/dot-cyber](.cyber)

## Acknowledgements
- @hleb-albau
- @arturalbov
- @jaekwon
- @ebuchman
- @npopeka
- @belya
- @serejandmyself
- @savetheales