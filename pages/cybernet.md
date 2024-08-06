icon:: 🍄
tags:: cyber

- experimental [[learning incentives]] layer for [[cyber]] using [[cosmwasm]] [[progs]]
- effort to incentivize [[soft3]] learning
- [cybernet](https://github.com/cybercongress/cybernet): subtensor is ported from [[substrate]] palets to [[cosmwasm]] programs
- it is inspired by [[yuma]] algorithm of [bittensor](https://cyb.ai/oracle/ask/QmUwHh7mKJhVMfnnNuDLeDfkUoknHu9FH9bZiS65MaHL72)
- advanced security due to decoupling of layers
	- [[bostrom]] [[tendermint]] [[consensus]] as consensus layer
	- [[cosmos-sdk]] with [[cosmwasm]] as sequential computation layer
	- [[cyber-sdk]] as parallel computation layer
- cybernet spawns family of projects
	- [[cybertensor]]: bittensor cli is ported to cosmwasm endpoints
	- [templates](https://github.com/cybercongress/cybertensor-subnet-template) ported to work with cybernet and [[cybertensor]]
	- protocol is mostly remained untouched for maximum compatibility
	- [[cybverver]] and art created for easier adoption
- whats is different in comparison with bittensor
	- deploy you whole new network and token: the network is just [[contract instance]]
	- manage your network using manual ux weights in [tech preview app](https://spacepussy.ai/cybernet/subnets/0)
	- maximize rewards with the help of [[cybergraph]]
	- extend subnets using [[cosmwasm]] programs
	- deploy your [[daodao]] instance for subnet management
	- participate in vibrant [[ibc]] ecosystem
	- trade earning on permissionless [[warp dex]]
	- enjoy security and speed of [[tendermint]] [[consensus]]
	- and more
- protocol extension: subnetwork is about learning particle's subgraph
- technical preview of webapp for exploring and setting weights: [spacepussy.ai/cybernet](https://spacepussy.ai/cybernet)
- TODO [[daodao]] integration
- TODO enrich original [docs](https://docs.spacepussy.ai/) of the project