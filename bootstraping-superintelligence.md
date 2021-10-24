
## Cybernomics

Basic cybernomics is defined by three tokens which have unique utility justified by necessity to regulate particular network resource:

- CYB is a security token. CYB gives ability to pay for gas, invest in heroes and earn CYB. CYB regulates CPU ability of the computer and its consensus state.
- sCYB or staked CYB. sCYB gives ability to mint resource tokens as like V (volt) and A (ampere).
- V is a token which gives potential. Potential is an ability to write cyberlinks in a knowledge graph. Investing V gives ability to mint A. V token regulates ability to store cyberlinks in GPU memory.
- A is a token which gives charge. Charge is an ability to affect rank. Investing A gives ability to mint CYB. A token regulates ability to calculate updates on ranks using GPU cores.

Resource token minting:

```python
def mint_resource_token(
                        hydrogen: int, 
                        investmint_time: int, 
                        base_vesting_resource: int = 10_000_000_000, 
                        base_vesting_time: int = 86400,
                        max_vesting_time: int = 604800):
    # hydrogen is a fuel token for resources minting
    # investment time is a time token locked
    if investmint_time > max_vesting_time:
        print('Impossible to lock tokens longer than max vesting time')
        return 0
    return int(hydrogen / base_vesting_resource) * (investmint_time / base_vesting_time)
```

V minting:

```
Mint amount (V) = Investment amount (sCYB) / Base token amount * Time premium
```

A minting:

```
Mint amount (A) = Investment amount (sCYB) / Base token amount * Time premium
```

where Base token amount is a consensus parameter. It is defined as a minimum amount of investment tokens that necessary for minting one resource token for Base vesting time**,
Time premium is an additional multiplier for agents who vested longer than Base vesting time**

```
Time premium = Investment time / Base investment time
```

> Investment time should be <= Max investmint time. Max investmint time parameter is hardcoded currently, but will have developed as network function.

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


## Speed and Time relativity

The attentive reader will notice that economics is pegged to seconds. Although this design does not add incentives to make computer faster. We are investigating to peg economics to circles. Circle is a time span defined by a consensus for rank computation. At the start 1 circle is 5 blocks. Pegging cybernomics to circles is our intention choice. It incentivize the whole community to speed up the network, and not slow down it. The faster the network become - the more tokens everybody can get in 1 second. So let us imaging that we would be able to advance the network to 0.5 second block which is nearly the theoretical limits by speed of light. So relative max investment period could be not around ~1000 years, but ~100 years which is expected life time of the human.


## CYB

Proof-of-stake systems do not help with the initial distribution. We believe that if the initial distribution is designed purposefully, energy-efficiently, provably and transparently, hence accessible, the early [knowledge-graph](knowledge graph) will gain in quality and size.

The genesis block of the cyber protocol contains 1 000 000 000 000 000 CYB (one petacyb or 1 PCYB) tokens broken down as follows:

- 700 000 000 000 000 CYB as a gift to different Ethereum, it's communities and Cosmos
- 200 000 000 000 000 CYB as pre-Genesis allocations of cyberCongress
- 100 000 000 000 000 CYB in a network community pool

![CYB]()

After the Genesis, CYB tokens can only be created by a consensus. There is currently no such thing as a maximum amount of CYB tokens. This is due to the continuous inflation paid to the heroes and masters of the network. CYB token is implemented using uint64, so the creation of additional CYB tokens makes it significantly more expensive to compute state changes and rank. We expect for a lifelong monetary strategy to be established by the governance system.

Every 1\% of invested V (Volts) gives the ability to use 1\% of the possible networks' bandwidth and its computing capabilities. There is only one way to alter this ability: investing V for some period of time. A simple rule prevents abuse from the agents: a pair of content identifiers may be cyberlinked by an address only once.

## Speed

We require instant confirmation time to provide users with the feeling of a conventional web-application. This is a powerful architectural requirement that shapes the economical topology and the scalability of the [cyber](cyber) protocol. The proposed blockchain design is based on the [(Tendermint]https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) consensus algorithm with 146 validators and has a quick, 5 second tx finality time. The average confirmation time is closer to 1 second and could make complex blockchain interactions almost invisible to agents.

We denote one particular [go-cyber](https://github.com/cybercongress/go-cyber) property in the context of speed - rank computation. Being a part of the consensus, it occurs in parallel to transaction validation within the rounds. A round is a consensus variable defined by the stakeholders. At the inception, one round is set to 5 blocks. Practically, this indicates that every 25 seconds the network must agree on the current root hash of the [knowledge-graph](knowledge graph). This means that every [cyberlinks](cyberlink) submitted becomes a part of the [knowledge-graph](knowledge graph) in a matter of minute. In the early days of [https://google.com](Google) rank was recomputed roughly every week. We believe that masters of the Great Web will be pleased to observe that ranking changes in real-time, but, have decided to launch the network with an assumption that this window is enough. It is expected that with the development of the [cyber](cyber) protocol the velocity of each round will decrease. This is due to competition between heroes. We are aware of certain mechanisms to make this function order of magnitudes faster:
- optimization of the consensus parameters
- better parallelization of rank computation
- [better clock](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs) ahead of consensus

We want to give the ability to evaluate the proposed approach to as many agents as we can. But, without adding such complexity as KYC and/or captcha. That is why we chose to gift 70% of [cyb](CYB) tokens in Genesis to Ethereum, its communities and Cosmos. We are going to publish dedicated article to rationale behind the gift distribution.