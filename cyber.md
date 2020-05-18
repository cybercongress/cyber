# cyber: Computing the knowledge of the Great Web

IMG LOGO

## Abstract

A consensus computer allows for the computing of provably relevant answers without any opinionated blackbox intermediaries, such as Google, Amazon or Facebook. Stateless, content-addressable peer-to-peer communication networks, such as IPFS, and stateful consensus computers such as Ethereum, can provide just part of the solution needed to obtain akin answers. However, there are at least 3 problems associated with the above-mentioned implementations. (A) the subjective nature of relevance. (B) difficulty in scaling consensus computers for over-sized knowledge graphs. (C) the lack of quality amongst such knowledge graphs. They are prone to various surface attacks, such as sybil attacks, and the selfish behaviour of the interacting agents. In this document, we define a protocol for provable consensus computing of relevance, between IPFS objects, which is based on the Tendermint consensus of cyber\~Rank, which is computed using GPUs in consensus. As proof-of-stake consensus does not help with the initial distribution, we outline the design for ecologic and efficient distribution games. We believe that a minimalistic architecture of the protocol is critical for the formation of a network of domain-specific knowledge consensus computers. As a result of our work, some applications never to have existed before, will emerge. We expand this document with our vision of possible features and potential applications.

## The Great Web

Original protocols of the Internet, such as: TCP/IP, DNS, URL and HTTP/S have brought the web to a stale point, where it is located as of now. Considering all the benefits that these protocols have produced for the initial development of the web, along with them, they have brought significant obstacles to the table. Globality, being a vital property of the web is under a real threat since its inception. The speed of the connection keeps degrading while the network itself keeps growing due to ubiquitous government interventions. The latter causes privacy concerns as an existential threat to human rights.

One property not evident in the beginning becomes important with everyday usage of the Internet: the ability to exchange permanent links, thus, they [will not break after time had passed](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN). Reliance on the architecture of one at a time ISP allows governments to effectively censor packets. This is the last drop in the traditional web-stack for every engineer that is concerned about the future of our children.

Other properties, while might not be so critical, are very desirable: offline and real-time connection. The average internet user, whilst offline, should still have the ability to carry on working with the state that they already hold. After acquiring a connection they should be able to sync with the global state and to continue to verify the validity of their own state in real-time. Currently, these properties are offered on the application level. We believe that these properties should be integrated into lower-level protocols.

The emergence of [a brand-new web-stack](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw) creates an opportunity for a superior Internet. The community calls it web3. We call it the Great Web. We believe that various types of low-level communications should be immutable and should not alter for decades, e.g. immutable content links. They seem very promising at removing the problems of the conventional protocol stack. They add greater speed and provide a more accessible connection to the new web. However, as it happens with any concept that offers something unique - new problems emerge. One such concern is general-purpose search. The existing general-purpose search engines are restrictive and centralized databases that everybody is forced to trust. Those search engines were designed primarily for client-server architectures, based on TCP/IP, DNS, URL and HTTP/S. The Great Web creates a challenge and an opportunity for a search engine that is based on emerging technologies and is designed specifically for these purposes. Surprisingly, permissionless blockchain architecture allows building a general-purpose search engine in a way inaccessible to previous architectures.

## On the adversarial examples problem

[The current architecture of search engines](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6) is a system where some entity processes all the shit. This approach suffers from one challenging and a distinct problem, that has yet to be solved, even by the brilliant Google scientists: [the adversarial examples problem](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9). The problem that Google acknowledges, is that it is rather difficult to algorithmically reason whether or not a particular sample is adversarial. This is inconsiderate to how awesome the educating technology in itself is. A crypto-economical approach can change beneficiaries in the game. Consequently, this approach will effectively remove possible sybil attack vectors. It removes the necessity to hard-code model crawling and meaning extraction by a single entity. Instead, it gives this power to the whole world. A learning sybil-resistant, agent-generated model, will probably lead to orders of magnitude more predictive results.

## Cyber protocol

In its core the protocol is very minimalistic and can be expressed with the following steps:

1. Compute the genesis of cyber protocol based on the defined distribution
2. Define the state of the [knowledge graph](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3#3)
3. Gather transactions using a [consensus computer](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3#5)
4. Check the validity of the signatures
5. Check the [bandwidth limit](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3#16)
6. Check the validity of CIDs
7. If the signatures, the bandwidth limit and CIDs are all valid, apply [cyberlinks](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3#4) and transactions
8. Calculate the vaules of [cyber\~Rank](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3#7) for every round for the CIDs on the [knowledge graph](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3#3)

The rest of this document discusses the rationale and the technical details of the proposed protocol.

## Knowledge graph

We represent a knowledge graph as a weighted graph of directed links between content addresses. Aka, content identificators, CIDs, IPFS hashes, or simply - IPFS links. In this document, we will use the above terms as synonyms.

IMG GRAPH LINKS

Content addresses are essentially web3 links. Instead of using the unclear and mutable:   
`https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md`

we use the object itself:    
`Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH`

By using content addresses to build the knowledge graph we gain [the so much needed](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est) [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps) - [like](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR) superpowers of p2p protocols that are desired for a search engine:

- mesh-network future-proof
- interplanetary accessibility
- censorship resistance
- technological independence

Our knowledge graph is generated by the awesome masters. Masters add themselves to the knowledge graph with the help of a single transaction, a cyberlink. Thereby, they prove the existence of their private keys for content addresses of their revealed public keys. By using these mechanics, a [consensus computer](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3#5) could achieve provable differentiation between subjects and objects on a knowledge graph.

Our implementation of [go-cyber](https://github.com/cybercongress/go-cyber) is based on [cosmos-SDK](https://github.com/cosmos/cosmos-sdk) identities and [CIDv0/CIDv1](https://github.com/multiformats/cid#cidv0) content addresses.

Masters form the knowledge graph by applying [cyberlinks](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3#4).

## Cyberlinks

To understand how cyberlinks function we need to understand the difference between a URL link (aka, a hyperlink) and between an IPFS link. A URL link points to the location of the content, whether an IPFS link points to the content itself. The difference between web architectures based on location links and content links is radical and requires a unique approach.

Cyberlink is an approach to link two content addresses, or IPFS links, semantically:

`.md syntax: [QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH](Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH)`    
`.dura syntax: QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH.Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH`

The above cyberlink means that the presentation of [go-cyber](https://github.com/cybercongress/go-cyber) during [cyberc0n](https://etherscan.io/token/0x61B81103e716B611Fff8aF5A5Dc8f37C628efb1E) is referencing to the Cosmos white paper. The concept of cyberlinks is a convention around simple semantics of a communicational format in any p2p network:

CID IMG 1

We see that a cyberlink represents a link between the two links. Easy peasy!

Cyberlink is a simple, yet a powerful semantic construction for building a predictive model of the universe. This means that using cyberlinks instead of hyperlinks provides us with the superpowers that were inaccessible to previous architectures of general-purpose search engines.

Cyberlinks can be extended, i.e. they can form linkchains if there two or more cyberlinks subsist from one master, where the second link in the first cyberlink is equal to the first link in the second cyberlink:

CID IMG 2

If agents expand native IPFS links with something semantically richer, for example, with [dura](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md) links, then consensus on the execution rules by a specific program can be reached in a more natural approach.

The [go-cyber](https://github.com/cybercongress/go-cyber) implementation of cyberlinks is available in the [.cyber](https://github.com/cybercongress/dot-cyber) app of our experimental web3 browser [cyb](https://cyb.ai), or at [cyber.page](http://cyber.page).

The cyberlinks submitted by masters are stored in a merkle tree according to the [RFC-6962 standard](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). This enables authentification for [proof-of-relevance](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3#8).

CID IMG 3

Using cyberlinks, we can compute the relevance of subjects and objects on the [knowledge graph](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3#3). But we need a [consensus computer](#the-notion-of-a-consensus-computer).

## The notion of a consensus computer

A consensus computer is an abstract computing machine that emerges from the interaction between agents. A consensus computer has capacity in terms of fundamental computing resources: memory and computation. To interact with agents a computer needs bandwidth. An ideal consensus computer is a computer where:
\\
\begin{lstlisting}
the sum of all the computations and memory available to individuals
is equal to
the sum of all the verified computations and memory of the consensus computer
\end{lstlisting}

We know that:
\begin{lstlisting}
verifications of computations < (computations + verifications of computations)
\end{lstlisting}

Hence, we will never be able to achieve an ideal consensus computer. The CAP theorem and the scalability trilemma append more proof to this statement.
\begin{Figure}
    \centering
    \includegraphics[width=1\textwidth]{consensus-computer.png}
\end{Figure}

Yet this theory can work as a performance indicator for a consensus computer. After 6 years of investing into consensus computers, we have come to realize that the \linkgreen{https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ}{Tendermint} consensus has a good enough balance between the coolness required for our task and the readiness for its production. Therefore, we have decided to implement the {\hyperref[cyber]{cyber}} protocol using the Tendermint consensus, which has very close settings to the Cosmos Hub. The \linkred{https://github.com/cybercongress/go-cyber}{go-cyber} implementation is a 64-bit Tendermint consensus computer of relevance for 64-byte string-space. This is by far not ideal, at least as 1/146, because we have 146 validators who verify the same computations producing the {\hyperref[knowledge-graph]{knowledge graph}}.

We must bind the computation, storage and the bandwidth supply of the consensus computer to a maximized demand for queries. Computation and storage, in case of a basic {\hyperref[relevance-machine]{relevance machine}} can be easily predicted based on bandwidth. But bandwidth requires a limiting mechanism.

## Relevance machine

We define a relevance machine as a machine that transitions the state of a {\hyperref[knowledge-graph]{knowledge graph}} based on the will of the agents wishing to teach and to study that {\hyperref[knowledge-graph]{knowledge graph}}. The will is projected by every {\hyperref[cyberlinks]{cyberlink}} a master does. The more agents inquire the {\hyperref[knowledge-graph]{knowledge graph}}, the more valuable the knowledge becomes. Based on these projections, relevance between content addresses can be computed. The relevance machine enables a simple construction for the search mechanism via querying and delivering answers.

One property of the relevance machine is crucial. It must have inductive reasoning properties or follow the blackbox principle:

\begin{lstlisting}
The machine should be able to interfere with predictions without any knowledge about the objects,
except for who, when and what was cyberlinked
\end{lstlisting}

If we assume that a {\hyperref[consensus-computer]{consensus computer}} must have some information about the linked objects, then the complexity of such a model will grow unpredictably. Therefore the high requirements of the processing computer for memory and computation. Thanks to content addressing a relevance machine which follows the blackbox principle, does not need to store data. But, can still effectively operate on top of it. The deduction of meaning inside a {\hyperref[consensus-computer]{consensus computer}} is expensive. Hence, such a design can depend on assumption blindness. Instead of deducting the meaning inside of the {\hyperref[consensus-computer]{consensus computer}}, we have designed a system in which meaning extraction is incentivized. This is achieved due to masters requiring {\hyperref[cyb]{CYB}} tokens to express their will, based on which, the relevance machine can compute rank.

In the center of the spam protection system is an assumption that write operations can be executed only by those, who have a vested interest in the evolutionary success of the relevance machine. Every 1\% of effective stake within the {\hyperref[consensus-computer]{consensus computer}} gives the ability to use 1\% of the possible networks' bandwidth and its computing capabilities. A simple rule prevents abuse from the agents: a pair of content identificators may be cyberlinked by an address only once.

\begin{algorithm}
\caption{Bandwidth}\label{bandwidth-algo}
\SetKwInOut{Input}{Input}
\SetKwInOut{Output}{Output}
\SetKwFunction{CalculateRank}{CalculateRank}
\SetKwFunction{CreateMerkleTree}{CreateMerkleTree}
\SetKwFunction{Push}{PushMerkleTree}
\Input{Current block $N$;\\New transactions $T$}
$B^{N}_{used} \leftarrow 0$\;
\For{$t \in T$}{
    $B^{max}_a \leftarrow S_a / S_{network} $\;
    $B_a \leftarrow \max(B^{max}_a, B_a + (N - B^{block}_a) \cdot B^{max}_a / W_{recover})$\;
    $B_{cost} \leftarrow RC_{price} \cdot (B_{transaction} + |links(t)| \cdot B_{link})$\;
    \BlankLine
    \If{$B_a < B_{cost}$} {
        Skip transaction $t$\;
    }
    $B_a \leftarrow B_a - B_{total}$\;
    $B^{N}_{used} \leftarrow B^{N}_{used} + B_{cost}$\;
}
\BlankLine
$H_{app} \leftarrow T^{root}_{links} \oplus T^{root}_{ranks}$\;
Commit $H_{app}$ to ABCI\;
\end{algorithm}\

There are only two ways to change the effective stake (active stake + bonded stake) of an account: direct token transfers and bonding operations.

{\hyperref[cyber]{Cyber}} uses a very simple bandwidth model. The principal goal of this model is to reduce the daily network growth to a given constant. This is done to accommodate heroes (validators) with the ability to forecast any future investment into infrastructure. Thus, here we introduce 'watts' or 'W'. Each message type has an assigned W cost. The constant 'DesirableBandwidth', determines the desirable 'RecoveryWindow' spent by the W value. The recovery period defines how fast a master can recover their bandwidth from 0 back to max bandwidth. A master has maximum W proportional to his effective stake, determined by the following formula:
\begin{lstlisting}
  AgentMaxW = EffectiveStake * DesirableBandwidth
\end{lstlisting}

The period 'AdjustPricePeriod' sums up how much W was spent during the period 'RecoveryPeriod' in the latest block. 'SpentBandwidth' / 'DesirableBandwidths' ratio is called the fractional reserve ratio. When network usage is low, the fractional reserve ratio adjusts the message cost to allow masters with a lower stake to commit more transactions. When the demand for resources increases, the fractional reserve ratio goes \code{>1}, consequently, increasing message cost and limiting final tx count for a long-term period (W recovery will be \code{<} then W spending). As no one uses all of their possessed bandwidth, we can safely use up to 100x fractional reserves within a price recalculation target period. Such mechanics provide a discount for creating {\hyperref[cyberlinks]{cyberlinking}}, thus, effectively maximizing demand for it. You can see that the proposed design needs demand for full bandwidth for the relevance to become valuable.

Human intelligence is organized in such a manner that none-relevant and none-important memories are forgotten over time. The same can be applied to the relevance machine. The relevance machine can implement \linkgreen{https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb}{aggressive pruning strategies}, such as, the pruning of the history of the formation of the {\hyperref[knowledge-graph]{knowledge graph}}, or forgetting links that become less relevant.

As a result, the implemented cybernomics of {\hyperref[cyb]{CYB}} tokens serves not just as will-expression and spam-protection mechanisms, but also, functions as an economics regulation tool that can align the processing capacity of heroes and the market demand for processing. The go-cyber implementation of the relevance machine is based on a very straightforward mechanism, called: cyber\~{}Rank.

## cyber\~Rank

Ranking using a {\hyperref[consensus-computer]{consensus computer}} can be challenging, as consensus computers have serious resource constraints. First, we must ask ourselves: why do we need to compute and to store the rank on-chain and not follow the same way as \linkgreen{https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj}{Colony} or \linkgreen{https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD}{Truebit}?

When rank was computed inside a {\hyperref[consensus-computer]{consensus computer}} one has easy access to the content distribution of that rank and an easy way to {\hyperref[apps]{build provable applications}} on top of that rank. Hence, we have decided to follow a more cosmic architecture. In the next section we describe the {\hyperref[proof-of-relevance]{proof of relevance}} mechanism, which allows the network to scale with the help of domain-specific {\hyperref[relevance-machine]{relevance machines}}. Those work concurrently, thanks to the IBC protocol.

Eventually, the {\hyperref[relevance-machine]{relevance machine}} needs to obtain (1) a deterministic algorithm, that will allow for the computation of the rank on a continuously appending network, which itself, can scale to the orders of magnitude of the likes of \linkred{https://google.com}{Google}. Additionally, a perfect algorithm (2) must have linear memory and computational complexity. Most importantly, it must have (3) the highest provable prediction capabilities for the existence of relevant {\hyperref[cyberlinks]{cyberlinks}}.

After \linkgreen{https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC}{thorough research}, we have found that it is impossible to obtain the silver bullet. Therefore, we have decided to find a more basic, bulletproof way, that can bootstrap the network: \linkgreen{http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw}{the rank} which Larry and Sergey used to bootstrap their previous network. The key problem with the original PageRank is that it wasn't resistant to sybil attacks. However, a token-weighted PageRank which is limited by a token-weighted bandwidth model does not inherit the key problem of the naive PageRank, because - it is resistant to sybil attacks. For the time being, we will call it cyber\~{}Rank, until something more suitable will emerge. The following algorithm is applied to its implementation at Genesis:

$$ CIDs \ V, cyberlinks \ E, Agents \ A $$
$$agents(e): E \rightarrow 2^{A}$$
$$stake(a): A \rightarrow {\rm I\!R}^+ $$
$$rank(v, t): V \times {\rm I\!N} \rightarrow {\rm I\!R} $$
$$weight(e) = \sum\limits_{a \in agents(e)}{stake(a)}$$
$$rank(v, t + 1) = \frac{1 - d}{N} + d\sum\limits_{u \in V, (u, v) \in E}{\frac{weight(u, v)}{\sum_{w \in V, (u, w) \in E}{weight(u, w)}}rank(v, t)} $$
$$rank(v) = \lim\limits_{t \rightarrow \infty} rank(v, t)$$
\begin{algorithm}
\SetKwInOut{Input}{Input}\SetKwInOut{Output}{Output}

\Input{Set of CIDs $V$; \\ Set of cyberlinks $E$; \\ Set of agents $A$; \\ Cyberlink authors $ agents(e) $; \\ Stake of each agent $ stake(a) $; \\Tolerance $\epsilon$; \\ Damping factor $d$}
\Output{$\textbf{R}$, computed value of $rank(v)$ for each node from $V$}

\BlankLine
Initialize $\textbf{R}_{v}$ with zeros for all $v \in V$\;
Initialize $E$ with value $\epsilon$ + 1\;

\BlankLine
$N_{\emptyset} \leftarrow |\{v|v \in V \land (\nexists u, u \in V, (u, v) \in E )\}|$ \;
$R_{0} \leftarrow (1 + d \cdot N_{\emptyset} / |V|) \cdot (1 - d) / |V| $ \;

\BlankLine
\While{$E > \epsilon$}{
\For{$v \in V$}{
$S \leftarrow 0$\;

\For{$u \in V, (u, v) \in E$}{
\setstretch{1.35}
$W_{uv} \leftarrow \sum_{a \in agents(u, v)}stake(a)$ \;
$W_{u} \leftarrow \sum_{w \in V, (u, w) \in E}\sum_{a' \in agents(u, w)}stake(a')$ \;
$S \leftarrow S + W_{uv} \cdot \textbf{R}_{u} / W_{u}$ \;
}

$\textbf{R}'_v \leftarrow d \cdot S + R_{0}$ \;

}

\BlankLine
$E \leftarrow \max\limits_v(|\textbf{R}_v - \textbf{R}'_v|)$ \;
Update $\textbf{R}_{v}$ with $\textbf{R}'_{v}$ for all $v \in V$\;

}

\caption{cyber\~{}Rank}\label{algo_disjdecomp}
\end{algorithm}\

We understand that the ranking mechanism will always remain a red herring. This is why we expect to rely on the on-chain governance tools that can define the most suited mechanism at a given time. We suppose that the network can switch from one algorithm to another, not simply based on subjective opinion, but rather on economical a/b testing through 'hard spooning' of domain-specific {\hyperref[relevance-machine]{relevance machines}}.

cyber\~{}Rank shields two design decisions which are of paramount importance: (1) it accounts for the current intention of the agents, and (2) it encourages rank inflation of {\hyperref[cyberlinks]{cyberlinks}}. The first property ensures that cyber\~{}Rank can not be gamed with. If an agent decides to transfer their {\hyperref[cyb]{CYB}} tokens out of their account, the {\hyperref[relevance-machine]{relevance machine}} will adjust all the {\hyperref[cyberlinks]{cyberlinks}} relevant for this account per the current intentions of the agent. And vice versa, if an agent transfers {\hyperref[cyb]{CYB}} tokens into their account, all of the {\hyperref[cyberlinks]{cyberlinks}} submitted from this account will immediately gain more relevance. The second property is essential in order not to get cemented in the past. As new {\hyperref[cyberlinks]{cyberlinks}} are continuously added, they will dilute the rank of the already existing links proportionally. This property prevents a situation where new and better content has a lower rank simply because it was recently submitted. We expect these decisions to enable an inference quality for recently added content to the long tail of the {\hyperref[knowledge-graph]{knowledge graph}}.

We would love to discuss the problem of vote-buying. Vote-buying as an occurrence isn't that bad. The dilemmas with vote-buying appear within systems where voting affects the allocation of that systems inflation. For example, \linkgreen{http://ipfs.io/ipfs/QmepU77tqMAHHuiSASUvUnu8f8ENuPF2Kfs97WjLn8vAS3}{Steem}
or any fiat-state based system. Vote-buying can become easily profitable for an adversary that employs a zero-sum game without the necessity to add value. Our original idea of a decentralized search was based on this approach. But, we have rejected that idea, removing the incentive of the formation of the {\hyperref[knowledge-graph]{knowledge graph}} to the consensus level. In the environment where every participant must bring some value to the system to affect the predictive model, vote-buying becomes NP-hard problem. Therefore, becomes beneficial to the system.

The current implementation of the {\hyperref[relevance-machine]{relevance machine}} utilizes GPUs to compute rank. The machine can answer and deliver relevant results for any given search request in a 64-byte CID space. However, it is not enough to build a network of domain-specific {\hyperref[relevance-machine]{relevance machines}}. {\hyperref[consensus-computer]{Consensus computers}} must have the ability to prove relevance to one another.

## Proof of relevance

We have designed the network under the assumption that with regards to search, such a thing as malicious behaviour, does not exist. This can be assumed as no malicious behaviour can be found in the intention of finding the answers. This approach significantly reduces any surface attacks.

\begin{lstlisting}
Ranks are computed based on the fact that something was searched, thus linked, and as a result - affected the predictive model
\end{lstlisting}

A good analogy is observed in quantum mechanics, where the observation itself affects behaviour. This is why we have no requirement for such a thing as negative voting. By doing this, we remove subjectivity out of the protocol and we can define proof of relevance.

\begin{Figure}
    \centering
    \includegraphics[width=1\textwidth]{rank-tree.png}
\end{Figure}

Each new CID receives a sequence number. Numbering starts with zero. Then incremented by one for each new CID. Therefore, we can store rank in a one-dimensional array, where indices are the CID sequence numbers. Merkle tree calculations are based on the \linkgreen{https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG}{RFC-6962 standard}. Using Merkle trees, we can effectively proof the rank for any given content address. While relevance is still subjective by nature, we have a collective proof that something was relevant to a certain community at some point in time.

Using this type of proof any two \linkgreen{https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk}{IBC compatible} {\hyperref[consensus-computer]{consensus computers}} can prove relevance one to another. This means that domain-specific {\hyperref[relevance-machine]{relevance machines}} can flourish.

In the relevance for a common \linkred{https://github.ccom/cybercongress/go-cyber}{go-cyber} implementation, the Merkle tree is computed every round and its root hash committed to ABCI.

## Speed

We require instant confirmation time to provide users with the feeling of a conventional web-application. This is a powerful architectural requirement that shapes the economical topology and the scalability of the {\hyperref[cyber]{cyber}} protocol. The proposed blockchain design is based on the \linkgreen{https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ}{Tendermint consensus} algorithm with 146 validators and has a quick, 5 second tx finality time. The average confirmation time is closer to 1 second and could make complex blockchain interactions almost invisible to agents.

We denote one particular \linkred{https://github.com/cybercongress/go-cyber}{go-cyber} property in the context of speed - rank computation. Being a part of the consensus, it occurs in parallel to transaction validation within the rounds. A round is a consensus variable defined by the stakeholders. At the inception, one round is set to 20 blocks. Practically, this indicates that every 100 seconds the network must agree on the current root hash of the {\hyperref[knowledge-graph]{knowledge graph}}. This means that every {\hyperref[cyberlinks]{cyberlink}} submitted becomes a part of the {\hyperref[knowledge-graph]{knowledge graph}} almost instantly and acquires a rank within an average period of 50 seconds. In the early days of \linkred{https://google.com}{Google} rank was recomputed roughly every week. We believe that masters of the Great Web will be pleased to observe that ranking changes in real-time, but, have decided to launch the network with an assumption that this window is enough. It is expected that with the development of the {\hyperref[cyber]{cyber}} protocol the velocity of each round will decrease. This is due to competition between heroes. We are aware of certain mechanisms to make this function order of magnitudes faster:

\begin{itemize}
\item optimization of the consensus parameters
\item better parallelization of rank computation
\item \linkgreen{https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs}{better clock} ahead of consensus
\end{itemize}

## Scalability

We require an architecture which will allow us to scale the idea to the significance of the likes of \linkred{https://google.com}{Google}. Let us assume, that node implementation, which is based on \linkred{https://github.com/cosmos/cosmos-sdk}{Cosmos-SDK} can process 10k transactions per second. This would mean, that every day, at least 8.64 million masters will be able to submit 100 {\hyperref[cyberlinks]{cyberlinks}} each, and impact the search results simultaneously. This is enough to verify all the assumptions out in the wild, but, not enough to say that it will work at the current scale of the Internet. Given the current state of the art research done by our team, we can safely state that there is no consensus technology in existence, that will allow scaling a particular blockchain to the size that we require. Hence, we introduce the concept of domain-specific {\hyperref[knowledge-graph]{knowledge graphs}}.

\begin{Figure}
    \centering
    \includegraphics[width=1\textwidth]{network.png}
\end{Figure}

One can either launch an own domain-specific search engine by forking \linkred{https://github.com/cybercongress/go-cyber}{go-cyber}, which is focused on \textit{common public knowledge}. Or, simply plug \linkred{https://github.com/cybercongress/go-cyber}{go-cyber} as a module into an existing chain, e.i. Cosmos Hub. The inter-blockchain communication protocol introduces concurrent mechanisms of syncing state between {\hyperref[relevance-machine]{relevance machines}}. Therefore, in proposed search architecture, domain-specific {\hyperref[relevance-machine]{relevance machine}} will be able to learn from common knowledge. Just as common knowledge can learn from domain-specific {\hyperref[relevance-machine]{relevance machines}}.

## Browzers

We were aspired to imagine how proposed network would operate with a web3 browser. To our disappointment we \linkred{https://github.com/cybercongress/cyb/blob/master/docs/comparison.md}{were not able} to find a web3 browser that can showcase the coolness of the proposed approach in action. This is why we have decided to develop a web3 browser from scratch. \linkred{https://cyb.ai}{Cyb} is your friendly robot which has a sample \linkred{https://cyber.page}{.cyber} application for interacting with the {\hyperref[cyber]{cyber}} protocol.

\begin{Figure}
  \medskip
  \centering
  \includegraphics[width=1\textwidth]{cyb.jpg}
  \medskip
\end{Figure}

As a good example of delivery, we have created \linkred{https://cyber.page/}{cyber.page}. It allows heroes, masters and evangelists to interact with the protocol via a web2 gateway. Create cyberlinks, pin content directly to IPFS, search the Great Web, participate in the governance of cyber and so on. It can also act as an in-depth explorer, a wallet and can pocket hardware wallets, such as Ledger devices.

The current search snippets are ugly. But, we presume that they can be easily extended using \linkred{https://github.com/ipld/specs}{IPLD} for different types of content. Eventually, they can become even more attractive than those of \linkred{https://google.com}{Google}.

\begin{Figure}
    \centering
    \includegraphics[width=1\textwidth]{architecture.png}
\end{Figure}

During the implementation of the proposed architecture, we have realized at least 3 key benefits that \linkred{https://google.com}{Google} would probably not be able to deliver with its conventional approach:

\begin{itemize}
\item the search results can be easily delivered from any p2p network: e.g. .cyber can play videos
\item payment buttons can be embedded right into search snippets. This means that agents can interact with the search results, e.g. agents can buy an item right in .cyber. This means that e-commerce can flourish fairly thanks to a provable conversion attribution
\item search snippets do not have to be static but can be interactive. e.g. .cyber can deliver your current wallet balance
\end{itemize}

## Deployment

Due to technical limitations, we have to bootstrap the ecosystem using 2 tokens: {\hyperref[thc]{THC}} and {\hyperref[cyb]{CYB}}

\begin{itemize}
\item {\hyperref[cyb]{CYB}} is the native token of the sovereign {\hyperref[cyber]{cyber}} protocol powered by the Tendermint consensus algorithm. It has 3 primary uses: (1) staking for consensus, (2) bandwidth limiting for submitting {\hyperref[cyberlinks]{cyberlinks}}, and (3) expression of the will of the masters for the computation of cyber\~{}Rank.

\item {\hyperref[thc]{THC}} (pronounce as tech) is a creative cyber proto substance. {\hyperref[thc]{THC}} being an Ethereum ERC-20 compatible token that has utility value in the form of control over cyber\~{}Foundation (the community governing DAO) and the ETH from the distribution game. {\hyperref[thc]{THC}} is emitted during the creation of cyber\~{}Foundation as an Aragon organization. The creative powers of {\hyperref[thc]{THC}} come from the ability to receive 1 {\hyperref[cyb]{CYB}} token per each 1 {\hyperref[thc]{THC}} token when vested before the end of cyber\~{}Auction.
\end{itemize}

Both tokens remain functional and will track value independently of one another due to their very different utility by nature.

Overall, the deployment process has the following structure:

\begin{enumerate}
 \item cyber\~{}Congress deploys Game of Links
 \item The community participates in the Game of Links
 \item The community verifies and proposes a Genesis block with results from the Game of Links
 \item cyber\~{}Congress deploys contracts for cyber~Foundation and cyber\~{}Auction
 \item The community participate in cyber\~{}Auction after Genesis. Donors stake {\hyperref[thc]{THC}} tokens to get {\hyperref[cyb]{CYB}} tokens
 \item cyber\~{}Congress distributes {\hyperref[cyb]{CYB}} tokens continuously during cyber~Auction
 \item cyber\~{}Congress burns the remaining {\hyperref[cyb]{CYB}} and {\hyperref[thc]{THC}} tokens and reports on the end of the initial distribution process
\end{enumerate}

cyber~Congress lives in Ethereum as an \linkgreen{https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330}{Aragon DAO}. It also operates a \linkgreen{https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8}{2-of-3 multisig in Cyber network}. cyber\~{}Congress developed the {\hyperref[cyber]{cyber}} protocol. Within the context of cyber, the Congress has 2 roles:
\begin{enumerate}
 \item To deploy and to execute the initial distribution program, which is impossible to automate. Because there is no trustless infrastructure for message swapping between ETH and ATOM, cyber\~{}Congress introduces a single point of failure in the initial distribution process. We have decided to send {\hyperref[cyb]{CYB}} tokens to {\hyperref[thc]{THC}} stakers manually because we feel that now is the right time to launch the network we have created. We also believe that an ongoing auction is vital for the initial distribution process. If cyber\~{}Congress fails to deliver its obligations in terms of distribution due to any possible reasons, we hope that the community will be able to fork out the network and to distribute {\hyperref[cyb]{CYB}} tokens as was promised. Hopefully, every operation is designed provably and transparently. All operations will be executed using a \linkgreen{https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j}{special purpose 2-of-3 multisig account in Cyber network}.
 \item Support the growth of {\hyperref[cyber]{cyber}} protocol until the community takes over the development in the form of cyber\~Foundation. Donations in ATOMs during Game of Links will be distributed to the \linkgreen{https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a}{cyber\~{}Congress Cosmos 2-of-3 multisig}. All ATOM donations that are routed to the cyber\~{}Congress multisig will become its property. The role of ATOM donation is the following: thanks to ATOM we want to secure a commitment for cyber\~{}Congress in the development of both Cosmos and Cyber ecosystems. ATOM donations will allow cyber\~{}Congress to use staking rewards and reach a sustainable flow, for the continuous funding of the {\hyperref[cyber]{cyber}} protocol without the necessity to dump neither {\hyperref[cyb]{CYB}} nor ATOM tokens.
\end{enumerate}

## CYB

Proof-of-stake systems do not help with the initial distribution. We believe that if the initial distribution is designed purposefully, energy-efficiently, provably and transparently, hence accessible, the early {\hyperref[knowledge-graph]{knowledge graph}} will gain in quality and size.

The genesis block of the cyber protocol contains 1 000 000 000 000 000 CYB (one petacyb or 1 PCYB) tokens broken down as follows:

\begin{itemize}
\item 750 000 000 000 000 CYB tokens for those who stake {\hyperref[thc]{THC}} tokens until the end of cyber\~{}Auction (participants of cyber\~{}Congress, Game of Thrones in ETH and cyber\~{}Auction)
\item 150 000 000 000 000 CYB tokens for the participants of Game of Links
\item 100 000 000 000 000 CYB tokens as a gift for Ethereum, Cosmos and Urbit communities
\end{itemize}

\begin{Figure}
 \centering
 \includesvg[width=1\textwidth]{CYB.svg}
\end{Figure}

After the Genesis, CYB tokens can only be created by heroes based on staking and slashing parameters. The basic consensus is that newly created CYB tokens are at the disposal of stakeholders.

There is currently no such thing as a maximum amount of CYB tokens. This is due to the continuous inflation paid to the heroes of the network. CYB token is implemented using uint64, so the creation of additional CYB tokens makes it significantly more expensive to compute state changes and rank. We expect for a lifelong monetary strategy to be established by the governance system after the complete initial distribution of CYB tokens and the activation of the functionality of smart contracts. The starting parameters of the inflation will be defined via governance during the Game of Links.

## THC

The goal of creating an alternative to a \linkred{https://google.com}{Google-like} structure requires extraordinary effort from various groups. Hence, we have decided to set up cyber\~{}Foundation as a fund, managed via a decentralized engine such as an Aragon DAO. It is charged with ETH and managed by the agents who have participated in the initial distribution. This approach will allow safeguarding from excessive market dumping of the native platform token - {\hyperref[cyb]{CYB}} within the first years of its work, thereby, ensuring stable development. Additionally, this allows to diversify the underlying platform and extend the protocol to other consensus computing architectures, should such a need arise.

While choosing the token for donations, we followed three main criteria: the token must be (1) one of the most liquid, (2) most promising, so a community can secure a solid investment bag to be competitive even in comparison to such giants like \linkred{https://google.com}{Google}, and (3) have the technical ability to execute an auction and a resulting organization, without relying on any third party. The only system that matches these criteria is Ethereum, hence, the primary token of donations will be ETH.

Prior to Genesis cyber\~{}Foundation has minted 750 000 000 000 000 THC (seven hundred fifty terathc) broken down as follows:

\begin{itemize}
\item 600 000 000 000 000 THC tokens are allocated to the cyber\~{}Auction contract
\item 150 000 000 000 000 THC tokens are allocated to the cyber\~{}Congress contract

\end{itemize}

\begin{Figure}
 \centering
 \includesvg[width=1\textwidth]{THC.svg}
\end{Figure}

All decisions by cyber\~{}Foundation will be executed based on the results of THC votes. The following parameters will be applied:

\begin{itemize}
\item Support: 51\%
\item Quorum: 51\%
\item Vote duration: 500 hours
\end{itemize}

## Gift

We want to give the ability to evaluate the proposed approach to as many agents as we can. But, without adding such complexity as KYC and/or captcha. That is why we chose to gift 8\% of {\hyperref[cyb]{CYB}} tokens in Genesis to Ethereum, 1\% to Cosmos, and 1\% to Urbit communities. The following rules are applied to reproduce the Genesis:
\begin{itemize}
 \item Every account within the Ethereum foundation network, with at least 1 outgoing transaction which is not a contract, and holds > 0.001 ETH at block 8080808
 \item Every non-zero account within Cosmos hub-3 at block 2000000
 \item Every account which holds galaxies (30\%), stars (30\%), or planets (40\%) at block 10677601 according to the number of objects
\end{itemize}

The key purpose of this gift is for every account in Genesis to be able to make at least 1 {\hyperref[cyberlinks]{cyberlink}} in the space of 24 hours as the network is unloaded. This is why we have decided to make the distribution curve a bit more even, and radically change it to a quadratic curve. Hence, we distribute {\hyperref[cyb]{CYB}} tokens proportionally to the square root of each account balance during the snapshots. Because a quadratic design is too easy to game with, we have calculated the amount of the distributed {\hyperref[cyb]{CYB}} tokens for the proposed blocks before this fact became known to the public. We do not apply the quadratic rule to Urbit aliens.

## Game of Links

A game for Cosmos hodlers in ATOM. Participants donate ATOM in exchange for CYB. The more ATOM is donated, the higher the price of CYB. The game starts from 1 ATOM per 1 GCYB. The game is over when either 146 days have passed since the beginning of the Takeoff donations, or if the price has increased 5x from the starting price. The price of {\hyperref[cyb]{CYB}} during the Takeoff is defined by the following function:

$$f(c) = 40 \cdot c + 1000

where f(c) is TCYB price in ATOM, the c is amount of TCYB tokens won during Takeoff.

The key idea is: the better the Takeoff donation round performs, the more payouts the participants in the disciplines will receive. 100 {\hyperref[cyb]{TCYB}} is allocated to the participants of the Takeoff donations and 50 {\hyperref[cyb]{TCYB}} is allocated for participants of the Game of Links disciplines. All {\hyperref[cyb]{CYB}} tokens that remain from the Takeoff, are allocated to the community pool at the end of the game. All {\hyperref[cyb]{CYB}} tokens that remain from the disciplines are allocated to cyber\~{}Congress. In addition to CYB tokens, Game of Links allocates test EUL tokens to all Takeoff donors for the final. A \linkred{https://cybercongress.ai/game-of-links/}{detailed document} has been published with rules and provisions for the game.

## Cyber\~Auction

A game for Ethereum hodlers in ETH. Participants donate ETH in exchange for THC. The more ETH is donated, the higher the price of THC. The game starts from the price which is 5x closing price of the Takeoff in ETH. The game is over when either 888 days have passed since its inception or if the price has increased 5x from the starting price. During this phase {\hyperref[cyb]{CYB}} tokens are continuously distributed by cyber\~{}Congress, based on the vested {\hyperref[thc]{THC}} tokens until the end of the auction. Vested {\hyperref[thc]{THC}} tokens provide the ability to receive {\hyperref[cyb]{CYB}} tokens accordingly, and voting powers within cyber\~{}Foundation. The price of {\hyperref[thc]{THC}} during Cyber\~{}Auction is defined by the following function:

$$g(t)=\frac{1}{30} \cdot t \cdot p + 5 \cdot p

where g(t) is TTHC price in ETH, t is amount of TTHC tokens won during cyber\~{}~Auction, p is the resulting price of Takeoff for one CYB converted to ETH at closing moment.

The starting price is designed to give the Takeoff participants 5x premium for their risk of investing in hardware and software infrastructure prior to Genesis. cyber\~{}Auction gives significant incentives for early participators. After the end of the distribution, participants will be able to unlock their {\hyperref[thc]{THC}} tokens and use them as they wish, e.i. transfer, exchange, etc. As a result of the auction, the community will have access to all the donated ETH within the Aragon organization. After the end of cyber\~{}Auction, all the remaining {\hyperref[thc]{THC}} on the cyber\~{}Auction contract must be provably burned. The following rules apply to {\hyperref[cyb]{CYB}} tokens under the \linkgreen{https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j}{multisig for distribution}:

\begin{itemize}
\item cyber\~Congress will not delegate its stake, and as a result, it will remain a passive stake until it will become distributed
\item after the end of cyber\~{}Auction, all the remaining {\hyperref[cyb]{CYB}} tokens must be provably burned
\end{itemize}

## Apps

We assume that the proposed algorithm does not guarantee high-quality knowledge by default. Just like a newborn, it needs to acquire knowledge to develop further. The protocol itself provides just one simple tool: the ability to create a {\hyperref[cyberlinks]{cyberlink}} with an agents stake between two content addresses.

Analysis of the semantic core, behavioural factors, anonymous data about the interests of agents and other tools that determine the quality of search, can be achieved via smart contracts and off-chain applications, such as: {\hyperref[browzers]{web3 browsers}}, decentralized social networks and content platforms. We believe, that it is in the interest of the community and the masters to build the initial {\hyperref[knowledge-graph]{knowledge graph}} and to maintain it. Hence, for the graph, to provide the most relevant search results.

Generally, we distinguish three types of applications for {\hyperref[knowledge-graph]{knowledge graphs}}:

\begin{itemize}
\item Consensus apps. Can be run at the discretion of the {\hyperref[consensus-computer]{consensus computer}} by adding intelligent abilities
\item On-chain apps. Can be run by the {\hyperref[consensus-computer]{consensus computer}} in exchange for gas
\item Off-chain apps. Can be implemented by using the {\hyperref[knowledge-graph]{knowledge graph}} as an input within an execution environment
\end{itemize}

The following, imaginable, list of apps consolidates the above-mentioned categories:

Web3 browsers. In reality, browser and search are inseparable. It is hard to imagine the emergence of a full-blown web3 browser which is based on web2 search. Currently, there are several efforts for developing browsers around blockchains and distributed tech. Amongst them are Beaker, \sout{Mist}, Brave, and Metamask. All of them suffer from trying to embed web2 into web3. Our approach is a bit different. We consider web2 as an unsafe subset for web3. So we have developed an experimental web3 browser, Cyb, showcasing the {\hyperref[cyber]{cyber}} approach to answering queries better and delivering content faster.

Social networks. Social networks are not that mysterious. In any social network content is the king. Hence, provable ranking is the basic building block of any social network. All types of social networks can be easily built on top of a {\hyperref[knowledge-graph]{knowledge graph}}. Cyber can also create social networks based on relevance between users, which no current network is able to achieve.

Programmable semantics. Currently, the most popular keywords in the gigantic semantic core of \linkred{https://google.com}{Google} are keywords of apps such as: \linkred{https://youtube.com}{Youtube}, \linkred{https://facebook.com}{Facebook}, \linkred{https://github.com}{GitHub}, etc. However, the developers of those successful apps have very limited ability to explain to \linkred{https://google.com}{Google} how to structure search results in a better manner. The {\hyperref[cyber]{cyber}} approach gives this power back to developers. Developers are now able to target specific semantics cores and index their apps as they wish.

Search actions. The proposed design enables native support for blockchain (and tangle-alike) assets related activity. It is trivial to design applications which are (1) owned by the creators, (2) appear correctly in the search results and (3) allow a transactable action, with (4) provable attribution of a conversion for a search query. e-Commerce has never been this easy for everyone.

Off-line search. IPFS makes it possible to easily retrieve a document from an environment without a global internet connection. \linkred{https://github.com/cybercongress/go-cyber}{go-cyber} itself can be distributed by using IPFS. This creates the possibility for ubiquitous, off-line search!

Command tools. Command-line tools can rely on relevant and structured answers from a search engine. Practically speaking, the following CLI tool is possible to implement:

\begin{lstlisting}
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
\end{lstlisting}

Search tools, from within CLI will inevitably create a highly competitive market of a dedicated semantic core for robots.

Autonomous robots. Blockchain technology enables the creation of devices that can manage digital assets on their own.

\begin{lstlisting}
If a robot can store, earn, spend and invest - they can do everything you can do
\end{lstlisting}

What is needed is a simple, yet a powerful state reality tool with the ability to find particular things. \linkred{https://github.com/cybercongress/go-cyber}{go-cyber} offers a minimalistic, but a continuously self-improving data source, which provides the necessary tools for programming economically rational robots. According to \linkred{https://github.com/first20hours/google-10000-english}{top-10,000 English words} the most popular word in the English language is the defining article 'the', which means a pointer to a particular item. This fact can be explained as the following: particular items are of most importance to us. Therefore, the nature of us is to find unique things. Hence, the understanding of unique things is essential for robots too.

Language convergence. A programmer should not care about the language that an agent will be using. We don't need to know in which language the agent is performing their search in. The entire UTF-8 spectrum is at work. The semantic core is open, so competition for answering queries can become distributed across different domain-specific areas. Including the semantic cores for various languages. This unified approach creates an opportunity for cyber\~Bahasa. Since the dawn of the Internet, we observe a process of rapid language convergence. We use truly global words across the entire planet, independently of nationality, language, race, name or Internet connection. The dream of a truly global language is hard to deploy because it is hard to agree on what means what. However, we have the tools to make this dream come true. It is not hard to predict that the shorter a word, the more powerful its cyber\~{}Rank will be. Global, publicly available list of symbols, words, and phrases sorted accordingly by cyber\~{}Rank with a corresponding link provided by \linkred{https://github.com/cybercongress/go-cyber}{go-cyber} can become the foundation for the emergence of a genuinely global language everybody can accept. Recent \linkgreen{https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1}{scientific advances} in machine translation are breathtaking but meaningless to those who wish to apply them without a Google-scale trained model. The proposed cyber\~{}Rank offers precisely this.

Self prediction. A {\hyperref[consensus-computer]{consensus computer}} can continuously build a {\hyperref[knowledge-graph]{knowledge graph}} on its own predicting the existence of {\hyperref[cyberlinks]{cyberlinks}} and applying these predictions to its state. Hence, a {\hyperref[consensus-computer]{consensus computer}} can participate in the economic consensus of the {\hyperref[cyber]{cyber}} protocol.

Universal oracle. A {\hyperref[consensus-computer]{consensus computer}} can store the most relevant data in a key-value storage. Where the key is a CID and the values are the bytes of the actual content. This can be achieved by making a decision every round, in regards to which CID value the agentss want to prune and which value they wish to apply. Based on the utility measure of content addresses within the {\hyperref[knowledge-graph]{knowledge graph}}. To compute utility measure, heroes check the availability and the size of the content for the top-ranked content addresses within the {\hyperref[knowledge-graph]{knowledge graph}}, then, weight on the size of the CIDs and its rank. The emergent key-value storage will be available to write for {\hyperref[consensus-computer]{consensus computer}} only and not for agents. But, values could be used in programs.

Location-aware search. It is possible to construct {\hyperref[cyberlinks]{cyberlinks}} with \linkgreen{https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG}{Proof-of-Location} based on remarkable existing protocols such as \linkgreen{https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG}{Foam}. Consequently, a location-based search also becomes provable, if web3-agents will mine triangulations and attach \linkgreen{https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG}{proof-of-location} for every linked chain.

Prediction markets on link relevance. We can implement this idea using the ranking of the {\hyperref[knowledge-graph]{knowledge graph}} based on a prediction market on link relevance. An app that allows betting on link relevance, can become a unique source of truth for the direction of terms, as well as, motivate agents to submit more links.

Private cyberlinks. Privacy is fundamental. While we are committed to privacy, achieving implementation of private {\hyperref[cyberlinks]{cyberlinks}} is unfeasible for our team up to Genesis. Therefore, it is up to the community to work on WASM programs, that can be executed on top of the protocol. The problem is to compute cyber\~{}Rank, based on the {\hyperref[cyberlinks]{cyberlinks}} submitted by a web3-masters without revealing neither: their previous request nor the public keys. Zero-knowledge proofs, in general, are very expensive. We believe that the privacy of search should be a feature by design, but we are unsure that we know how to implement it at this stage. \linkgreen{https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk}{Coda} like recursive Snarks and \linkgreen{https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg}{MimbleWimble} constructions, in theory, can solve part of the privacy concern. But, they are new, untested and anyway, will be more expensive with regards to computations than their transparent alternative.

This is surely not the excessive list of all the possible applications, but a very exciting one indeed.

## Conclusion

We defined and implemented a protocol for provable communication, between consensus computers on relevance. The protocol is based on the simple idea of knowledge graphs, which are generated by agents via the use of cyberlinks. Cyberlinks are processed by a consensus computer using the concept of the relevance machine. The cyber consensus computer is based on CIDv0/CIDv1 and uses go-IPFS and Cosmos-SDK as a foundation. IPFS provides significant benefits with regards to resource consumption. CID as primary objects are robust in their simplicity. For every CID, cyber\~{}Rank is computed by a consensus computer without a single point of failure. Cyber\~{}Rank is a CYB token weighted PageRank, with economic protection from sybil attacks and selfish voting. Every round the Merkle root of the rank and graph trees are published. Consequently, every computer can prove to any other computer the relevance of value for a given CID. Sybil resistance is based on bandwidth limiting. The embedded ability to execute programs offers inspiring applications. The starting primary goal is the indexing of peer-to-peer content addresses systems, either stateless, such as: IPFS, Swarm, Sia, Git, BitTorrent, or stateful, such as: Bitcoin, Ethereum and other blockchains and tangles. The proposed semantics of cyberlinking offers a robust mechanism for predicting meaningful relations between objects by the consensus computer itself. The source code of the relevance machine is open-source. Every bit of data accumulated by the consensus computer is available for anyone if one has the resources to process it. The performance of the proposed software implementation is sufficient for seamless interaction. The scalability of the proposed implementation is sufficient to index all self-authenticated data that exist today and can serve it to millions of agents of the Great Web. The blockchain is managed by a Superintelligence, which functions under the Tendermint consensus algorithm with a standard governance module. Though the system provides the necessary utility to offer an alternative for a conventional search engine, it is not limited just to this use case. The system is extendable for numerous applications and makes it possible to design economically rational, self-owned robots, that can autonomously understand objects around them.

## References

- [Scholarly context adrift](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN)
- [Brand-new stack](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw)
- [Search engines information retrieval in practice](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6)
- [Motivating game for adversarial example research](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9)
- [An idea of a decentralized search](https://ipfs.io/ipfs/QmXNoGTWLQrcFRb66oS4HafpP1vcLKbVkJrQm4DVvihuoq)
- [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps)
- [DAT](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR)
- [go-cyber](https://github.com/cybercongress/go-cyber)
- [cosmos-sdk](https://github.com/cosmos/cosmos-sdk)
- [CIDv1](https://github.com/multiformats/cid#cidv1)
- [cyber.page](http://cyber.page)
- [DURA](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md)
- [Colony](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj)
- [Truebit](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)
- [Thermodynamics of predictions](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb)
- [PageRank](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw)
- [RFC-6962](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG)
- [IBC protocol](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk)
- [Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ)
- [Comparison of web3 browsers](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md)
- [Cyb](https://cyb.ai)
- [SpringRank](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC)
- [Run validator in cyber protocol](https://cybercongress.ai/docs/go-cyber/run_validator/)
- [Top 10000 english words](https://github.com/first20hours/google-10000-english)
- [Multilingual neural machine translation](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1)
- [Foam](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG)
- [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk)
- [Mimblewimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg)
- [Tezos](https://ipfs.io/ipfs/QmdSQ1AGTizWjSRaVLJ8Bw9j1xi6CGLptNUcUodBwCkKNS)
- [Software 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35)
- [Proof-of-history](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs)
- [IPLD](https://github.com/ipld)
- [cyber\~Congress organization](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330/)
- [cyber~Congress in Cyber](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8)
- [cyber~Congress in Cosmos](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a)
- [multisig for CYB distribution](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j)
- [.cyber](https://github.com/cybercongress/dot-cyber)

## Acknowledgements

- @hleb-albau
- @arturalbov
- @jaekwon
- @ebuchman
- @npopeka
- @belya
- @serejandmyself


