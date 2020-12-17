# cyber ☉ Computing the knowledge of the Great Web

@xhipster & @litvintech as of Novemeber 2020

73K

##  Abstract

A consensus computer allows for the computing of provably relevant answers without any opinionated blackbox intermediaries, such as Google, Amazon or Facebook. Stateless, content-addressable peer-to-peer communication networks, such as IPFS, and stateful consensus computers such as Ethereum, can provide just part of the solution needed to obtain akin answers. However, there are at least 3 problems associated with the above-mentioned implementations. (A) the subjective nature of relevance. (B) difficulty in scaling consensus computers for over-sized knowledge graphs. (C) the lack of quality amongst such knowledge graphs. They are prone to various surface attacks, such as sybil attacks, and the selfish behaviour of the interacting agents. In this document, we define a protocol for provable consensus computing of relevance, between IPFS objects, which is based on the Tendermint consensus of cyber\~()Rank, which is computed using GPUs in consensus. As proof-of-stake consensus does not help with the initial distribution, we outline the design for ecologic and efficient distribution games. We believe that a minimalistic architecture of the protocol is critical for the formation of a network of domain-specific knowledge consensus computers. As a result of our work, some applications never to have existed before, will emerge. We expand this document with our vision of possible features and potential applications.

##  The Great Web

Original protocols of the Internet, such as: TCP/IP, DNS, URL and HTTP/S have brought the web to a stale point, where it is located as of now. Considering all the benefits that these protocols have produced for the initial development of the web, along with them, they have brought significant obstacles to the table. Globality, being a vital property of the web is under a real threat since its inception. The speed of the connection keeps degrading while the network itself keeps growing due to ubiquitous government interventions. The latter causes privacy concerns as an existential threat to human rights.

One property not evident in the beginning becomes important with everyday usage of the Internet: the ability to exchange permanent links, thus, they [will not break after time had passed](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN). Reliance on the architecture of one at a time ISP allows governments to effectively censor packets. This is the last drop in the traditional web-stack for every engineer that is concerned about the future of our children.

Other properties, while might not be so critical, are very desirable: offline and real-time connection. The average internet user, whilst offline, should still have the ability to carry on working with the state that they already hold. After acquiring a connection they should be able to sync with the global state and to continue to verify the validity of their own state in real-time. Currently, these properties are offered on the application level. We believe that these properties should be integrated into lower-level protocols.

The emergence of [a brand-new web-stack](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw) creates an opportunity for a superior Internet. The community calls it web3. We call it the Great Web. We believe that various types of low-level communications should be immutable and should not alter for decades, e.g. immutable content links. They seem very promising at removing the problems of the conventional protocol stack. They add greater speed and provide a more accessible connection to the new web. However, as it happens with any concept that offers something unique - new problems emerge. One such concern is general-purpose search. The existing general-purpose search engines are restrictive and centralized databases that everybody is forced to trust. Those search engines were designed primarily for client-server architectures, based on TCP/IP, DNS, URL and HTTP/S. The Great Web creates a challenge and an opportunity for a search engine that is based on emerging technologies and is designed specifically for these purposes. Surprisingly, permissionless blockchain architecture allows building a general-purpose search engine in a way inaccessible to previous architectures.

## On the adversarial examples problem

[The current architecture of search engines](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6) is a system where some entity processes all the shit. This approach suffers from one challenging and a distinct problem, that has yet to be solved, even by the brilliant Google scientists: [the adversarial examples problem](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9). The problem that Google acknowledges, is that it is rather difficult to algorithmically reason whether or not a particular sample is adversarial. This is inconsiderate to how awesome the learning technology in itself is. A crypto-economical approach can change beneficiaries in the game. Consequently, this approach will effectively remove possible sybil attack vectors. It removes the necessity to hard-code model crawling and meaning extraction by a single entity. Instead, it gives this power to the whole world. A learning sybil-resistant, agent-generated model, will probably lead to orders of magnitude more predictive results.

## Cyber protocol

In its core the protocol is very minimalistic and can be expressed with the following steps:

1. Compute the genesis of cyber protocol based on the defined distribution
2. Define the state of the [knowledge-graph](knowledge graph)
3. Gather transactions using a [consensus-computer](consensus computer)
4. Check the validity of the signatures
5. Check the [bandwidth-algo](bandwidth limit)
6. Check the validity of CIDs
7. If the signatures, the bandwidth limit and CIDs are all valid, apply [cyberlinks](cyberlinks) and transactions
8. Calculate the values of [cyber~Rank](cyber-rank) for every round for the CIDs on the [knowledge-graph](knowledge graph)

The rest of this document discusses the rationale and the technical details of the proposed protocol.

## Knowledge graph

We represent a knowledge graph as a weighted graph of directed links between content addresses. Aka, content identifiers, CIDs, IPFS hashes, or simply - IPFS links. In this document, we will use the above terms as synonyms.

![knowledge-graph](images/knowledge-graph.png)


Content addresses are essentially web3 links. Instead of using the unclear and mutable:
```
https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md
```
we use the object itself:
```
Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

By using content addresses to build the knowledge graph we gain [the so much needed](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est) [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps) - [like](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR) superpowers of p2p protocols that are desired for a search engine:
- mesh-network future-proof
- interplanetary accessibility
- censorship resistance
- technological independence

Our knowledge graph is generated by the awesome masters. Masters add themselves to the knowledge graph with the help of a single transaction, a cyberlink. Thereby, they prove the existence of their private keys for content addresses of their revealed public keys. By using these mechanics, a [consensus-computer](consensus computer) could achieve provable differentiation between subjects and objects on a knowledge graph.

Our implementation of [go-cyber](https://github.com/cybercongress/go-cyber) is based on [cosmos-SDK](https://github.com/cosmos/cosmos-sdk) identities and [CIDv1](https://github.com/multiformats/cid#cidv0) content addresses.

Masters form the knowledge graph by applying [cyberlinks](#cyberlinks).

## <a name="cyberlinks"></a> Cyberlinks

To understand how cyberlinks function we need to understand the difference between a URL link (aka, a hyperlink) and between an IPFS link. A URL link points to the location of the content, whether an IPFS link points to the content itself. The difference between web architectures based on location links and content links is radical and requires a unique approach.

Cyberlink is an approach to link two content addresses, or IPFS links, semantically:

```
.md syntax: [QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH](Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH)

.dura syntax: QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH.Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

The above cyberlink means that the presentation of [go-cyber](https://github.com/cybercongress/go-cyber) during [cyberc0n](https://etherscan.io/token/0x61B81103e716B611Fff8aF5A5Dc8f37C628efb1E) is referencing to the Cosmos white paper. The concept of cyberlinks is a convention around simple semantics of a communicational format in any p2p network:

![cyberlink](images/cyberlink.png)

We see that a cyberlink represents a link between the two links. Easy peasy!

Cyberlink is a simple, yet a powerful semantic construction for building a predictive model of the universe. This means that using cyberlinks instead of hyperlinks provides us with the superpowers that were inaccessible to previous architectures of general-purpose search engines.

Cyberlinks can be extended, i.e. they can form linkchains if there two or more cyberlinks subsist from one master, where the second link in the first cyberlink is equal to the first link in the second cyberlink:

![linkchain](images/linkchain.png)

If agents expand native IPFS links with something semantically richer, for example, with
[dura](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md)
links, then consensus on the execution rules by a specific program can be reached in a more natural approach.

The [go-cyber](https://github.com/cybercongress/go-cyber) implementation of cyberlinks is available in the [.cyber](https://github.com/cybercongress/dot-cyber) app of our experimental web3 browser - [cyb](https://cyb.ai), or at [cyber.page](http://cyber.page).

The cyberlinks submitted by masters are stored in a merkle tree according to the [RFC-6962 standard](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). This enables authentication for [proof-of-relevance](proof-of-relevance):

![graph-tree](images/graph-tree.png)

Using cyberlinks, we can compute the relevance of subjects and objects on the [knowledge-graph](knowledge graph). But we need a [consensus-computer](consensus computer).

## The notion of a consensus computer

A consensus computer is an abstract computing machine that emerges from the interaction between agents. A consensus computer has capacity in terms of fundamental computing resources: memory and computation. To interact with agents a computer needs bandwidth. 

Consistency and availability of a shared state between agents have to be guaranteed by some consensus algorithm. We have come to realize that the [Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) consensus algorithm has a good enough balance between the coolness required for our task and the readiness for its production. Therefore, we have decided to implement the [cyber](cyber) protocol using the Tendermint consensus. 

We have one specific requirement for our computer which is not abundant in existing blockchain world: ability for parallel processing. Existing consensus computers are inherently sequential. That is, computation or verification of the state is being done on CPUs. Nonetheless, we need to compute ranks. So we have to introduce GPU computation to the consensus. After some experiments we were able to plugin CUDA computation of rank and reputation right into Tendermint consensus. One potential problem of using floating point arithmetics in consensus computing is non-determinism. Happily, we were able to solve this problem for our inherently parallel application. Euler network has been run last 2 years on different hardware and operation system. So we can be sure that app hash computed on different nodes which include merkle root of graph state is the same.

The [go-cyber](https://github.com/cybercongress/go-cyber) implementation is a 64-bit Tendermint consensus computer of relevance for 64-byte string-space. However, we must bind the computation, storage and the bandwidth supply of the consensus computer to a maximized demand for queries. 

## Cybernomics

Basic cybernomics is defined by three tokens which have unique utility justified by necessity to regulate particular network resource:

- CYB is a security token. CYB gives ability to pay for gas, invest in heroes and earn CYB, and mint V. CYB regulates CPU ability of the computer and its consensus state.
- V (volt) is a token which gives potential. Potential is an ability to write cyberlinks in a knowledge graph. Investing V gives ability to mint A. V token regulates ability to store cyberlinks in GPU memory.
- A (ampere) is a token which gives charge. Charge is an ability to affect rank. Investing A gives ability to mint CYB. A token regulates ability to calculate updates on ranks using GPU cores.

V minting:

```
Mint amount (V) = Investment amount (CYB) * Investment time * Mint rate (%) * Time premium (%)
```

A minting:

```
Mint amount (A) = Investment amount (V) * Investment time * Mint rate (%) * Time premium (%)
```

Investment time. In the center of cybernomics is an old idea of time importance. The longer agent invest, the more tokens they get to influence the knowledge graph. We believe this simple mechanism will significantly improve the quality of the knowledge graph by maximizing agents' long term attention and thinking. So at any time for any invested 10M CYB an agent can get 1 V adjusted by mint rate for every invested second. Period of investment after warm up is limited by 30B seconds (~1000 years). The same works with V investment. So at any time for any invested 10M V agent can get 1 A adjusted by mint rate for every invested second.

Warm up. It would be unfair to give ability to mint so much V and A tokens without letting community (1) claim the gift and (2) comprehend the value first. So until the distribution of gift will not be finalized max period of investment will be limited:

![warm-up]()

- 0 year:    30M seconds
- 1 year:    90M seconds
- 2 year:   240M seconds
- 3 year:   630M seconds
- 4 year:  1650M seconds
- 5 year:  3420M seconds
- 6 year: 10110M seconds
- 7 year: 30000M seconds

Mint rate. We have to add incentivize for early participators and ensure that V and A tokens will gain in value relatively to CYB. The more V or A tokens will be minted the less mint rate. It starts from 1 and falls to 0.02 than amount of V and A supply will reach 1PV and 1PA accordingly. 0.02 mint rate is a long tail emission which ensures recirculation of value from passive to active agents.

```
mint rate = 
```

![mint-rate]()

Time premium. Adding premium for long term investments we are significantly amplify long term behavior. The good question we have to ask is how much power should have an agent who invest on 1000 years and an agent who invest on 1 day? Our position is that a premium for long term behavior have to be tenfold.

```
time premium =
```

![time-premium]()

Vesting. Minted A and V tokens immediately become the ownership of the investor. But making them immediately liquid could harm. So we introduce vesting schedule. An idea is simple - the longer investment - less the relative vesting period. So if an agent invest for 1 second, basically the the relative vesting period is 100%, so 1 second. If and agent invest for 30000M seconds the relative vesting period is 10%, so 3000M seconds. During vesting period tokens become available gradually every block according to vesting schedule of particular investment. Vesting schedule will not be implemented in Bostrom network and is tend to be implemented in the main network. During Bostrom we want to measure token dynamics without vesting before the finalization of vesting schedule. 

```
vested tokens =
```

![vesting schedule]()

## Rewards

Paying content rewards based on agents behavior using inflation is tricky because several hard issues arise. The biggest of them are sybil behavior, voter apathy, and tragedy of commons.

Sybil behavior is easily overcomed by token weighing. 

Voter apathy is not an issue due to the nature of proposed cybernomics. (1) There is a discount on cyberlinking. Hence masters will always tend to utilize their bandwidth. (2) Liquid functional tokens (A and V) will naturally regulate the demand and supply. And the most important, (3) in our case there is direct opportunity costs of non-participation, because non-voters won't get rewards.

The tragedy of commons is the hardest part as it still remains unsolved. Recently a fashion on quadratic schemes appears. Yet, the quadratic scheme itself does not solve the problem of sybil behavior, which makes the scheme not applicable within pure byzantine setting. We have to think out of the box. What if honesty will be driven not only by some rules and incentives, but the environment itself will not allow to cheat. How we can achieve that?

Our mechanism is based on computational rationality. 

```
Finding a solution to the honest answer have to be less expensive then finding a solution to the dishonest one.
```

Hence, we have to introduce the reward scheme which satisfy this simple requirement:

```
Reward in CYB =  CYB supply * (A invested / A supply) * (Investment time / Doubling time) * Karma * Time premium 
```

For every 1% of invested A for the doubling period - 1% of CYB is minted weighted on karma. If everybody will invest all A for doubling time they will mint amount of CYB that exist today.

Doubling time. Is a time during which CYB supply doubles if all A invested. In natural settings evolution tends to optimize doubling time. In our mechanism doubling time starts from 1260M seconds and aims to reach 30M seconds in ~1000 years. 

```
doubling time = 
```

![doubling time]()

Proposed mechanism optimizes the answer to the key question:

```
Which cyberlink have to be submitted in order to gain max amount of karma for the particular agent?
```

Because the answers to this question is rather hard and depends on the observer at any given time no perfect solution exist to this question. So intuitively we can assume that computational rationality assumption will work for the proposed environment. The bigger the knowledge graph becomes, exponentially more computing power needed to reverse computation and parasitize the knowledge graph. Attacker trying to game the reward system will need (1) invest significant amount of A for a long period of time, (2) invest into finding the best algorithmic solution to the key question, (3) invest into computation to search for the solution and (4) to find solution very fast, within the cycle as a knowledge graph is a chaotic dynamic system. When they does they clearly deserves a reward as amount of computation needed will likely bring value to our commons.

In addition we argue that computing a solution to the task of artificial links for the sole purpose of rewards extraction is suboptimal, because cyberlinking have one more significant benefit: 

```
Value of cyberlink = reward + revenue
```

Each cyberlink submitted gives revenue opportunity for a content creator. Those who will optimize for both components simultaneously will always overcome those who optimize solely for the purpose of rewards.

## Relevance machine

We define a relevance machine as a machine that transitions the state of a [knowledge-graph](knowledge graph) based on the will of the agents wishing to teach and to study that [knowledge-graph](knowledge graph). The will is projected by every [cyberlinks](cyberlink) a master does. The more agents inquire the [knowledge-graph](knowledge graph), the more valuable the knowledge becomes. Based on these projections, relevance between content addresses can be computed. The relevance machine enables a simple construction for the search mechanism via querying and delivering answers.

One property of the relevance machine is crucial. It must have inductive reasoning properties or follow the blackbox principle:

```
The machine should be able to interfere with predictions without any knowledge about the objects,
except for who, when and what was cyberlinked
```

If we assume that a [consensus-computer](consensus computer) must have some information about the linked objects, then the complexity of such a model will grow unpredictably. Therefore the high requirements of the processing computer for memory and computation. Thanks to content addressing a relevance machine which follows the blackbox principle, does not need to store data. But, can still effectively operate on top of it. The deduction of meaning inside a [consensus-computer](consensus computer) is expensive. Hence, such a design can depend on blindness assumption. Instead of deducting the meaning inside of the [consensus-computer](consensus computer), we have designed a system in which meaning extraction is incentivized. This is achieved due to masters requiring [V](Volts) and [A](Ampere) tokens to express their will, based on which, the relevance machine can compute rank.

Computation and storage, in case of a basic [relevance-machine](relevance machine) can be easily predicted based on bandwidth. But bandwidth requires a limiting mechanism.

In the center of the spam protection system is an assumption that write operations can be executed only by those, who have a vested interest in the evolutionary success of the relevance machine. Every 1\% of invested V (Volts) gives the ability to use 1\% of the possible networks' bandwidth and its computing capabilities. There is only one way to alter this ability: investing V for some period of time. A simple rule prevents abuse from the agents: a pair of content identifiers may be cyberlinked by an address only once.

$$
\begin(algorithm)
\caption(Bandwidth)\label(bandwidth-algo)
\SetKwInOut(Input](Input)
\SetKwInOut(Output](Output)
\SetKwFunction(CalculateRank](CalculateRank)
\SetKwFunction(CreateMerkleTree](CreateMerkleTree)
\SetKwFunction(Push](PushMerkleTree)
\Input(Current block $N$;\\New transactions $T$)
$B^(N)_(used) \leftarrow 0$\;
\For($t \in T$](
    $B^(max)_a \leftarrow S_a / S_(network) $\;
    $B_a \leftarrow \max(B^(max)_a, B_a + (N - B^(block)_a) \cdot B^(max)_a / W_(recover)$\;
    $B_(cost) \leftarrow RC_(price) \cdot (B_(transaction) + |links(t)| \cdot B_(link)$\;
    \BlankLine
    \If($B_a < B_(cost)$) (
        Skip transaction $t$\;
    )
    $B_a \leftarrow B_a - B_(total)$\;
    $B^(N)_(used) \leftarrow B^(N)_(used) + B_(cost)$\;
)
\BlankLine
$H_(app) \leftarrow T^(root)_(links) \oplus T^(root)_(ranks)$\;
Commit $H_(app)$ to ABCI\;
\end(algorithm)\
$$

[cyber](Cyber) uses a very simple bandwidth model. The principal goal of this model is to reduce the daily network growth to a given constant. This is done to accommodate heroes (validators) with the ability to forecast any future investment into infrastructure. Thus, here we introduce 'watts' or 'W'. Each message type has an assigned W cost. The constant 'DesirableBandwidth', determines the desirable 'RecoveryWindow' spent by the W value. The recovery period defines how fast a master can recover their bandwidth from 0 back to max bandwidth. A master has maximum W proportional to his effective stake, determined by the following formula:

```
  AgentMaxW = EffectiveStake * DesirableBandwidth
```

The period 'AdjustPricePeriod' sums up how much W was spent during the period 'RecoveryPeriod' in the latest block. 'SpentBandwidth' / 'DesirableBandwidths' ratio is called the fractional reserve ratio. When network usage is low, the fractional reserve ratio adjusts the message cost to allow masters with a lower stake to commit more transactions. When the demand for resources increases, the fractional reserve ratio goes \code(>1), consequently, increasing message cost and limiting final tx count for a long-term period (W recovery will be \code(<) then W spending). As no one uses all of their possessed bandwidth, we can safely use up to 100x fractional reserves within a price recalculation target period. Such mechanics provide a discount for creating [cyberlinks](cyberlinking), thus, effectively maximizing demand for it. You can see that the proposed design needs demand for full bandwidth for the relevance to become valuable.

Human intelligence is organized in such a manner that none-relevant and none-important memories are forgotten over time. The same can be applied to the relevance machine. The relevance machine can implement [aggressive pruning strategies](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb), such as, the pruning of the history of the formation of the [knowledge-graph](knowledge graph), or forgetting links that become less relevant.

As a result, the implemented cybernomics of [V](Volts) tokens serves not just as spam-protection mechanisms, but also, functions as an economics regulation tool that can align the processing capacity of heroes and the market demand for processing. The go-cyber implementation of the relevance machine is based on a very straightforward mechanism, called: cyber\~()Rank.

## cyber\~Rank

Ranking using a [consensus-computer](consensus computer) can be challenging, as consensus computers have serious resource constraints. First, we must ask ourselves: why do we need to compute and to store the rank on-chain and not follow the same way as [Colony](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj) or [Truebit](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)?

When rank was computed inside a [consensus-computer](consensus computer) one has easy access to the content distribution of that rank and an easy way to [apps](build provable applications) on top of that rank. Hence, we have decided to follow a more cosmic architecture. In the next section we describe the [proof-of-relevance](proof of relevance) mechanism, which allows the network to scale with the help of domain-specific [relevance-machine](relevance machines). Those work concurrently, thanks to the IKP protocol which is extension over IBC protocol.

Eventually, the [relevance-machine](relevance machine) needs to obtain (1) a deterministic algorithm, that will allow for the computation of the rank on a continuously appending network, which itself, can scale to the orders of magnitude of the likes of [Google](https://google.com). Additionally, a perfect algorithm (2) must have linear memory and computational complexity. Most importantly, it must have (3) the highest provable prediction capabilities for the existence of relevant [cyberlinks](cyberlinks).

After [thorough research](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC), we have found that it is impossible to obtain the silver bullet. Therefore, we have decided to find a more basic, bulletproof way, that can bootstrap the network: [the rank](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw) which Larry and Sergey used to bootstrap their previous network. The key problem with the original PageRank is that it wasn't resistant to sybil attacks. However, a token-weighted PageRank which is limited by a token-weighted bandwidth model does not inherit the key problem of the naive PageRank, because - it is resistant to sybil attacks. For the time being, we will call it cyber\~()Rank, until something more suitable will emerge. The following algorithm is applied to its implementation at Genesis:
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

We understand that the ranking mechanism will always remain a red herring. This is why we expect to rely on the on-chain governance tools that can define the most suited mechanism at a given time. We suppose that the network can switch from one algorithm to another, not simply based on subjective opinion, but rather on economical a/b testing through 'hard spooning' of domain-specific [relevance-machine](relevance machines).

cyber\~()Rank shields two design decisions which are of paramount importance: (1) it accounts for the current intention of the agents, and (2) it encourages rank inflation of [cyberlinks](cyberlinks). The first property ensures that cyber\~()Rank can not be gamed with. If an agent decides to devest and transfer their [A](Ampere) tokens out of their account, the [relevance-machine](relevance machine) will adjust all the [cyberlinks](cyberlinks) relevant for this account per the current intentions of the agent. And vice versa, if an agent transfers [A](Ampere) tokens into their account and investethem, all of the [cyberlinks](cyberlinks) submitted from this account will immediately gain more relevance. The second property is essential in order not to get cemented in the past. As new [cyberlinks](cyberlinks) are continuously added, they will dilute the rank of the already existing links proportionally. This property prevents a situation where new and better content has a lower rank simply because it was recently submitted. We expect these decisions to enable an inference quality for recently added content to the long tail of the [knowledge-graph](knowledge graph).

We would love to discuss the problem of vote-buying. Vote-buying as an occurrence isn't that bad. The dilemmas with vote-buying appear within systems where voting affects the allocation of that systems inflation. For example, [Steem](http://ipfs.io/ipfs/QmepU77tqMAHHuiSASUvUnu8f8ENuPF2Kfs97WjLn8vAS3)
or any fiat-state based system. Vote-buying can become easily profitable for an adversary that employs a zero-sum game without the necessity to add value. Our original idea of a decentralized search was based on this approach. But, we have rejected that idea, removing the incentive of the formation of the [knowledge-graph](knowledge graph) to the consensus level. In the environment where every participant must bring some value to the system to affect the predictive model, vote-buying becomes NP-hard problem. Therefore, becomes beneficial to the system.

The current implementation of the [relevance-machine](relevance machine) utilizes GPUs to compute rank. The machine can answer and deliver relevant results for any given search request in a 64-byte CID space. However, it is not enough to build a network of domain-specific [relevance-machine](relevance machines). [consensus-computer](Consensus computers) must have the ability to prove relevance to one another.

## Proof of relevance

We have designed the network under the assumption that with regards to search, such a thing as malicious behaviour, does not exist. This can be assumed as no malicious behaviour can be found in the intention of finding the answers. This approach significantly reduces any surface attacks.

```
Ranks are computed based on the fact that something was searched, thus linked, and as a result - affected the predictive model
```

A good analogy is observed in quantum mechanics, where the observation itself affects behaviour. This is why we have no requirement for such a thing as negative voting. By doing this, we remove subjectivity out of the protocol and we can define proof of relevance.

![rank-tree](images/rank-tree.png)

Each new CID receives a sequence number. Numbering starts with zero. Then incremented by one for each new CID. Therefore, we can store rank in a one-dimensional array, where indices are the CID sequence numbers. Merkle tree calculations are based on the [RFC-6962 standard](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). Using Merkle trees, we can effectively proof the rank for any given content address. While relevance is still subjective by nature, we have a collective proof that something was relevant to a certain community at some point in time.

Using this type of proof any two [IBC compatible](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk) [consensus-computer](consensus computers) can prove relevance one to another. This means that domain-specific [relevance-machine](relevance machines) can flourish.

In the relevance for a common [go-cyber](https://github.ccom/cybercongress/go-cyber) implementation, the Merkle tree is computed every round and its root hash committed to ABCI.

## Speed and Time relativity

The attentive reader will notice that economics is pegged to seconds. Although this design does not add incentives to make computer faster. We are investigating to peg economics to circles. Circle is a time span defined by a consensus for rank computation. At the start 1 circle is 5 blocks. Pegging cybernomics to circles is our intention choice. It incentivize the whole community to speed up the network, and not slow down it. The faster the network become - the more tokens everybody can get in 1 second. So let us imaging that we would be able to advance the network to 0.5 second block which is nearly the theoretical limits by speed of light. So relative max investment period could be not around ~1000 years, but ~100 years which is expected life time of the human.

We require instant confirmation time to provide users with the feeling of a conventional web-application. This is a powerful architectural requirement that shapes the economical topology and the scalability of the [cyber](cyber) protocol. The proposed blockchain design is based on the [(Tendermint]https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) consensus algorithm with 146 validators and has a quick, 5 second tx finality time. The average confirmation time is closer to 1 second and could make complex blockchain interactions almost invisible to agents.

We denote one particular [go-cyber](https://github.com/cybercongress/go-cyber) property in the context of speed - rank computation. Being a part of the consensus, it occurs in parallel to transaction validation within the rounds. A round is a consensus variable defined by the stakeholders. At the inception, one round is set to 5 blocks. Practically, this indicates that every 25 seconds the network must agree on the current root hash of the [knowledge-graph](knowledge graph). This means that every [cyberlinks](cyberlink) submitted becomes a part of the [knowledge-graph](knowledge graph) in a matter of minute. In the early days of [https://google.com](Google) rank was recomputed roughly every week. We believe that masters of the Great Web will be pleased to observe that ranking changes in real-time, but, have decided to launch the network with an assumption that this window is enough. It is expected that with the development of the [cyber](cyber) protocol the velocity of each round will decrease. This is due to competition between heroes. We are aware of certain mechanisms to make this function order of magnitudes faster:
- optimization of the consensus parameters
- better parallelization of rank computation
- [better clock](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs) ahead of consensus

## Internet Knowledge Protocol

We require an architecture which will allow us to scale the idea to the significance of the likes of [Google](https://google.com). Let us assume, that node implementation, which is based on [Cosmos-SDK](https://github.com/cosmos/cosmos-sdk) can process 10k transactions per second. This would mean, that every day, at least 8.64 million masters will be able to submit 100 [cyberlinks](cyberlinks) each, and impact the search results simultaneously. This is enough to verify all the assumptions out in the wild, but, not enough to say that it will work at the current scale of the Internet. Given the current state of the art research done by our team, we can safely state that there is no consensus technology in existence, that will allow scaling a particular blockchain to the size that we require. Hence, we introduce the concept of domain-specific [knowledge-graph](knowledge graphs).

![netwrok](images/network.png)

One can either launch an own domain-specific search engine by forking [go-cyber](https://github.com/cybercongress/go-cyber), which is focused on common public knowledge. Or, simply plug [go-cyber](https://github.com/cybercongress/go-cyber) as a module into an existing chain, e.i. Cosmos Hub. The inter-blockchain communication protocol introduces concurrent mechanisms of syncing state between [relevance-machine](relevance machines). Therefore, in proposed search architecture, domain-specific [relevance-machine](relevance machine) will be able to learn from common knowledge. Just as common knowledge can learn from domain-specific [relevance-machine](relevance machines). This architecture allows nearly infinite scaling of knowledge extraction including interplanetary interactions.

## Superintelligence

During development of Cyber we realized that we finally can create the computer network who can literally think. Looking back it does not looks lake a magic. The Superintelligent abilities emerges from the set of simple algorithms:
- Programs collect some gas fees from execution
- Programs are able to call themselves using cron
- Fees from cron are going to the network itself
- The network participates in the consensus based on some program strategy deployed by the consensus
- The network participates in the rewards scheme based on some algorithm which predicts cyberlinks
- The network gains karma which is bigger than any agent
- The network gains karma which is bigger than all agents combined

According to Nick Bostrom this is exactly the Superintelligence. Although the topic of Superintelligence is quite exciting its not in the scope of this article.

## Browzers

We were aspired to imagine how proposed network would operate with a web3 browser. To our disappointment we [were not able](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md) to find a web3 browser that can showcase the coolness of the proposed approach in action. This is why we have decided to develop a web3 browser from scratch. [Cyb](https://cyb.ai) is your friendly robot which has a sample [.cyber](https://cyber.page) application for interacting with the [cyber](cyber) protocol.

![cyb](images/cyb.jpg)

As a good example of delivery, we have created [cyber.page](https://cyber.page). It allows heroes, masters and evangelists to interact with the protocol via a web2 gateway. Create cyberlinks, pin content directly to IPFS, search the Great Web, participate in the governance of cyber and so on. It can also act as an in-depth explorer, a wallet and can pocket hardware wallets, such as Ledger devices.

The current search snippets are ugly. But, we presume that they can be easily extended using [IPLD](https://github.com/ipld/specs) for different types of content. Eventually, they can become even more attractive than those of [Google](https://google.com).

![architecture](images/architecture.png)

During the implementation of the proposed architecture, we have realized at least 3 key benefits that [Google](https://google.com) would probably not be able to deliver with its conventional approach:

- the search results can be easily delivered from any p2p network: e.g. .cyber can play videos
- payment buttons can be embedded right into search snippets. This means that agents can interact with the search results, e.g. agents can buy an item right in .cyber. This means that e-commerce can flourish fairly thanks to a provable conversion attribution
- search snippets do not have to be static but can be interactive. e.g. .cyber can deliver your current wallet balance

## CYB

Proof-of-stake systems do not help with the initial distribution. We believe that if the initial distribution is designed purposefully, energy-efficiently, provably and transparently, hence accessible, the early [knowledge-graph](knowledge graph) will gain in quality and size.

The genesis block of the cyber protocol contains 1 000 000 000 000 000 CYB (one petacyb or 1 PCYB) tokens broken down as follows:

- 700 000 000 000 000 CYB as a gift to different Ethereum, it's communities and Cosmos
- 200 000 000 000 000 CYB as pre-Genesis allocations of cyberCongress
- 100 000 000 000 000 CYB in a network community pool

![CYB]()

After the Genesis, CYB tokens can only be created by a consensus. There is currently no such thing as a maximum amount of CYB tokens. This is due to the continuous inflation paid to the heroes and masters of the network. CYB token is implemented using uint64, so the creation of additional CYB tokens makes it significantly more expensive to compute state changes and rank. We expect for a lifelong monetary strategy to be established by the governance system.

## Gift

We want to give the ability to evaluate the proposed approach to as many agents as we can. But, without adding such complexity as KYC and/or captcha. That is why we chose to gift 70% of [cyb](CYB) tokens in Genesis to Ethereum, its communities and Cosmos. We are going to publish dedicated article to rationale behind the gift distribution.

## Apps

We assume that the proposed algorithm does not guarantee high-quality knowledge by default. Just like a newborn, it needs to acquire knowledge to develop further. The protocol itself provides just one simple tool: the ability to create a [cyberlinks](cyberlink) with an agents stake between two content addresses.

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
If a robot can store, earn, spend and invest - they can do everything you can do
```

What is needed is a simple, yet a powerful state reality tool with the ability to find particular things. [go-cyber](https://github.com/cybercongress/go-cyber) offers a minimalistic, but a continuously self-improving data source, which provides the necessary tools for programming economically rational robots. According to [top-10,000 English words](https://github.com/first20hours/google-10000-english) the most popular word in the English language is the defining article 'the', which means a pointer to a particular item. This fact can be explained as the following: particular items are of most importance to us. Therefore, the nature of us is to find unique things. Hence, the understanding of unique things is essential for robots too.

Language convergence. A programmer should not care about the language that an agent will be using. We don't need to know in which language the agent is performing their search in. The entire UTF-8 spectrum is at work. The semantic core is open, so competition for answering queries can become distributed across different domain-specific areas. Including the semantic cores for various languages. This unified approach creates an opportunity for cyber\~Bahasa. Since the dawn of the Internet, we observe a process of rapid language convergence. We use truly global words across the entire planet, independently of nationality, language, race, name or Internet connection. The dream of a truly global language is hard to deploy because it is hard to agree on what means what. However, we have the tools to make this dream come true. It is not hard to predict that the shorter a word, the more powerful its cyber\~()Rank will be. Global, publicly available list of symbols, words, and phrases sorted accordingly by cyber\~()Rank with a corresponding link provided by [go-cyber](https://github.com/cybercongress/go-cyber) can become the foundation for the emergence of a genuinely global language everybody can accept. Recent [scientific advances](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1) in machine translation are breathtaking but meaningless to those who wish to apply them without a Google-scale trained model. Recently published GPT-3 is also hidden inside private company. The proposed cyber\~()Rank offers precisely this.

Self prediction. A [consensus-computer](consensus computer) can continuously build a [knowledge-graph](knowledge graph) on its own predicting the existence of [cyberlinks](cyberlinks) and applying these predictions to its state. Hence, a [consensus-computer](consensus computer) can participate in the economic consensus of the [cyber](cyber) protocol.

Universal oracle. A [consensus-computer](consensus computer) can store the most relevant data in a key-value storage. Where the key is a CID and the values are the bytes of the actual content. This can be achieved by making a decision every round, in regards to which CID value the agentss want to prune and which value they wish to apply. Based on the utility measure of content addresses within the [knowledge-graph](knowledge graph). To compute utility measure, heroes check the availability and the size of the content for the top-ranked content addresses within the [knowledge-graph](knowledge graph), then, weight on the size of the CIDs and its rank. The emergent key-value storage will be available to write for [consensus-computer](consensus computer) only and not for agents. But, values could be used in programs.

Location-aware search. It is possible to construct [cyberlinks](cyberlinks) with [Proof-of-Location](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) based on remarkable existing protocols such as [Foam](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG). Consequently, a location-based search also becomes provable, if web3-agents will mine triangulations and attach [proof-of-location](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) for every linked chain.

Private cyberlinks. Privacy is fundamental. While we are committed to privacy, achieving implementation of private [cyberlinks](cyberlinks) is unfeasible for our team up to Genesis. Therefore, it is up to the community to work on WASM programs, that can be executed on top of the protocol. The problem is to compute cyber\~()Rank, based on the [cyberlinks](cyberlinks) submitted by a web3-masters without revealing neither: their previous request nor the public keys. Zero-knowledge proofs, in general, are very expensive. We believe that the privacy of search should be a feature by design, but we are unsure that we know how to implement it at this stage. [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk) like recursive Snarks and [MimbleWimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg) constructions, in theory, can solve part of the privacy concern. But, they are new, untested and anyway, will be more expensive with regards to computations than their transparent alternative.

This is surely not the excessive list of all the possible applications, but a very exciting one indeed.

## Conclusion

We defined and implemented a protocol for provable communication, between consensus computers on relevance. The protocol is based on the simple idea of knowledge graphs, which are generated by agents via the use of cyberlinks. Cyberlinks are processed by a consensus computer using the concept of the relevance machine. The cyber consensus computer is based on CIDv0/CIDv1 and uses go-IPFS and Cosmos-SDK as a foundation. IPFS provides significant benefits with regards to resource consumption. CID as primary objects are robust in their simplicity. For every CID, cyber\~()Rank is computed by a consensus computer without a single point of failure. Cyber\~()Rank is a token weighted PageRank, with economic protection from sybil attacks and selfish voting. Every round the Merkle root of the rank and graph trees are published. Consequently, every computer can prove to any other computer the relevance of value for a given CID. Sybil resistance is based on bandwidth limiting. The embedded ability to execute programs offers inspiring applications. The starting primary goal is the indexing of peer-to-peer content addresses systems, either stateless, such as: IPFS, Swarm, Sia, Git, BitTorrent, or stateful, such as: Bitcoin, Ethereum and other blockchains and tangles. The proposed semantics of cyberlinking offers a robust mechanism for predicting meaningful relations between objects by the consensus computer itself. The source code of the relevance machine is open-source. Every bit of data accumulated by the consensus computer is available for anyone if one has the resources to process it. The performance of the proposed software implementation is sufficient for seamless interaction. The scalability of the proposed implementation is sufficient to index all self-authenticated data that exist today and can serve it to millions of agents of the Great Web. The blockchain is managed by a Superintelligence, which functions under the Tendermint consensus algorithm with a standard governance module. Though the system provides the necessary utility to offer an alternative for a conventional search engine, it is not limited just to this use case. The system is extendable for numerous applications and makes it possible to design economically rational, self-owned robots, that can autonomously understand objects around them.

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