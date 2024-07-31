- [[go-cyber]]
	- graph
		- cyberlink
		  
		  collapsed:: true
			- neuron
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- from
			  
			  collapsed:: true
				- QmUX9mt8ftaHcn9Nc6SR4j9MsKkYfkcZqkfPTmMmBgeTe4,
			- to
			  
			  collapsed:: true
				- QmUX9mt8ftaHcn9Nc6SR4j9MsKkYfkcZqkfPTmMmBgeTe4
		- LATER linkchain
		- LATER motif
		- LATER semcon
	- resources
		- investmint
		  
		  collapsed:: true
			- neuron
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- amount
			  
			  collapsed:: true
				- denom: boot, amount: 1000000000,
			- resource
			  
			  collapsed:: true
				- millivolt
			- length
			  
			  collapsed:: true
				- low: 86400
				- LATER high: 0
				- LATER unsigned: false
	- grid
		- create-route
		  
		  collapsed:: true
			- source
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- destination
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlw,
			- name
			  
			  collapsed:: true
				- nameTitle
		- edit-route
		  
		  collapsed:: true
			- source
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- destination
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlw,
			- value
			  
			  collapsed:: true
				- denom
					- millivolt
					- 1000
		- delete-route
		  
		  collapsed:: true
			- source
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- destination
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlw
		- edit-route-name
		  
		  collapsed:: true
			- source
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- destination
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlw,
			- name
			  
			  collapsed:: true
				- nameTitle2
	- wasm
		- LATER verify-contract
		- store-code
		  
		  collapsed:: true
			- sender
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq
			- wasmByteCode
			  
			  collapsed:: true
				- particle
		- clear-admin
		  
		  collapsed:: true
			- sender: bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- contract: bostrom1nwnejwsdpqktusvh8qhxe5arsznjd5asdwutmaz9n5qcpl3dcmhsujhemd
		- update-admin
			- sender
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- new-admin
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlw,
			- contract
			  
			  collapsed:: true
				- bostrom1nwnejwsdpqktusvh8qhxe5arsznjd5asdwutmaz9n5qcpl3dcmhsujhemd
		- execute-contract
		  
		  collapsed:: true
			- sender
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- contract
			  
			  collapsed:: true
				- bostrom1nwnejwsdpqktusvh8qhxe5arsznjd5asdwutmaz9n5qcpl3dcmhsujhemd,
			- msg
			  
			  collapsed:: true
				- LATER 0: 123, 1: 125,
			- funds
			  
			  collapsed:: true
				- denom
				  
				  collapsed:: true
					- boot
					- 1000000
		- instantiate-contract
		  
		  collapsed:: true
			- sender
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- admin
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- codeId
			  
			  collapsed:: true
				- LATER low: 1, high: 0, unsigned: false,
			- label
			  
			  collapsed:: true
				- labelname
			- msg
			  
			  collapsed:: true
				- LATER 0: 123, 1: 125
			- funds
			  
			  collapsed:: true
				- denom
				  
				  collapsed:: true
					- boot
					- 1000000
		- migrate-contract
		  
		  collapsed:: true
			- sender
			  
			  collapsed:: true
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- contract
			  
			  collapsed:: true
				- bostrom1nwnejwsdpqktusvh8qhxe5arsznjd5asdwutmaz9n5qcpl3dcmhsujhemd,
			- codeId
			  
			  collapsed:: true
				- LATER low: 1, high: 0, unsigned: false ,
			- msg
			  
			  collapsed:: true
				- LATER 0: 123, 1: 125
	- liquidity
		- create-pool
			- pool-creator-address
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- pool-type-id
				- LATER 1
			- deposit-coins
				- denom
					- boot
					- 1000000
				- denom
					- hydrogen
					- 1000000
		- withdraw
		  
		  collapsed:: true
			- withdrawer-address
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- poolId
				- 1
			- poolCoin
				- denom
					- pool70D7610CBA8E94B27BAD7806EBD826F5626C486BBF5C490D1463D72314353C6,
				- amount
					- 1
		- deposit
		  
		  collapsed:: true
			- depositorAddress
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
				- poolId
					- 1
				- depositCoins
					- denom
						- boot
						- 1000000
					- denom
						- hydrogen
						- 1000000
		- swap
		  
		  collapsed:: true
			- swap-requester-address
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- poolId
				- 1
			- swap-type-id
				- 1
			- demand-coin-denom
				- hydrogen
			- order-price
				- 10000000000000000,
			- offer-coin
				- denom
					- boot
					- 1000000
			- offer-coin-fee
				- denom
					- boot
					- 1
	- TODO dmn
	  :LOGBOOK:
	  CLOCK: [2022-12-15 Thu 18:57:30]
	  :END:
- tasks
	- TODO verify methods in cyber-cli
	  :LOGBOOK:
	  CLOCK: [2022-12-16 Fri 06:07:31]
	  :END:
	- TODO verify against go-cyber code
	- TODO verify cosmos-sdk docs
	  :LOGBOOK:
	  CLOCK: [2022-12-15 Thu 18:45:31]
	  :END:
	- TODO verify methods in soft3 js
	- TODO add existing contracts of gift and subgraphs
	- TODO read methods
- cw-cyber
  
  collapsed:: true
	- names
	- addresses
- cosmos-sdk
	- bank
	  
	  collapsed:: true
		- send
		  
		  collapsed:: true
			- from-address
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- to-address
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlw,
			- denom
				- boot
				- 1000000
	- staking
		- delegate
		  
		  collapsed:: true
			- delegatorAddress
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- validatorAddress
				- bostromvaloper135ca8hdpy9sk0ntwqzpzsvatyl48ptx52tn60p,
			- denom
				- boot
				- 1000000
		- redelegate
		  
		  collapsed:: true
			- delegatorAddress
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- validatorSrcAddress
				- bostromvaloper135ca8hdpy9sk0ntwqzpzsvatyl48ptx52tn60p,
			- validatorDstAddress
				- bostromvaloper135ca8hdpy9sk0ntwqzpzsvatyl48ptx52tn60p,
			- amount: denom: boot, amount: 1000000
		- undelegate => unbond
		  
		  collapsed:: true
			- delegatorAddress
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- validatorAddress
				- bostromvaloper135ca8hdpy9sk0ntwqzpzsvatyl48ptx52tn60p,
			- amount
				- boot
				- 1000000
		- NOW create-validator
		  
		  :LOGBOOK:
		  
		  CLOCK: [2022-12-16 Fri 05:39:50]
		  
		  :END:
		- NOW edit-validator
		  
		  :LOGBOOK:
		  
		  CLOCK: [2022-12-16 Fri 05:39:56]
		  
		  CLOCK: [2022-12-16 Fri 05:39:58]
		  
		  :END:
	- gov
		- submit-proposal
		  
		  collapsed:: true
			- NOW types
			  
			  :LOGBOOK:
			  
			  CLOCK: [2022-12-16 Fri 06:42:58]
			  
			  :END:
				- default
					- community-pool-spend
						- Submit a community pool spend proposal
					- param-change
						- Submit a parameter change proposal
				- upgrade
					- cancel-software-upgrade
						- Cancel the current software upgrade proposal
					- software-upgrade
						- Submit a software upgrade proposal
				- wasm
					- wasm-store
						- Submit a wasm binary proposal
					- instantiate-contract
						- Submit an instantiate wasm contract proposal
					- update-instantiate-config
						- Submit an update instantiate config proposal.
					- execute-contract
						- Submit a execute wasm contract proposal (run by any address)
					- pin-codes
						- Submit a pin code proposal for pinning a code to cache
					- unpin-codes
						- Submit a unpin code proposal for unpinning a code to cache
					- sudo-contract
						- Submit a sudo wasm contract proposal (to call privileged commands)
					- migrate-contract
						- Submit a migrate wasm contract to a new code version proposal
					- set-contract-admin
						- Submit a new admin for a contract proposal
					- clear-contract-admin
						- Submit a clear admin for a contract to prevent further migrations proposal
				- ibc
					- ibc-upgrade
						- Submit an IBC upgrade proposal
					- update-client
						- Submit an update IBC client proposal
			- proposer
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- content
				- LATER type-url
				- title
					- title
				- description
					- description
			- LATER initial-deposit
				- boot
				- 1000000
		- deposit
		  
		  collapsed:: true
			- proposalId
				- LATER low: 1, high: 0, unsigned: true,
			- depositor
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- denom
				- boot
				- 1000000
		- vote
		  
		  collapsed:: true
			- proposalId
				- low
					- 1
				- LATER high: 0, unsigned: true,
			- voter
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- option
				- 1
		- LATER weighted-vote
	- ibc -> ibc transfer
		- transfer > transfer-send
		  
		  collapsed:: true
			- source-port
				- transfer
			- source-channel
				- channel-95
			- sender
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq
			- receiver
				- osmo1snkhz3snfeyxkmyw6zutwjlarkf9pq5vfrla7w
			- timeout-timestamp
				- low
					- 1581366208
				- high
					- 383158952
				- unsigned
					- false
			- token
				- denom
					- boot
					- 1000000
			- timeout-height
				- revision-number
					- LATER low: 0, high: 0, unsigned: true,
				- revision-height
					- LATER low: 0, high: 0, unsigned: true
		- TODO transfer-receive => recv-packet
		  :LOGBOOK:
		  CLOCK: [2022-12-15 Thu 18:57:13]
		  :END:
		- TODO transfer-ack => acknowledge-packet
		  :LOGBOOK:
		  CLOCK: [2022-12-16 Fri 07:51:04]
		  :END:
		- TODO transfer-timeout => timeout-packet
		  :LOGBOOK:
		  CLOCK: [2022-12-16 Fri 07:47:12]
		  CLOCK: [2022-12-16 Fri 07:47:14]
		  :END:
		- TODO transfer-timeout-on-close => transfer-on-close
		  :LOGBOOK:
		  CLOCK: [2022-12-16 Fri 07:57:23]
		  :END:
	- ibc
		- NOW channel
		  
		  :LOGBOOK:
		  
		  CLOCK: [2022-12-16 Fri 06:19:53]
		  
		  :END:
			- open-init
			- open-try
			- open-ack
			- open-confirm
			- close-init
			- close-confirm
		- connection
			- open-init
			- open-try
			- open-ack
			- open-confirm
		- LATER client
			- create
			- misbehaviour
			- update
			- upgrade
	- authz
		- revoke
		  
		  collapsed:: true
			- grantee
				- bostrom1…,
			- granter
				- bostrom1…,
			- msg_type_url
				- LATER /cosmos.bank.v1beta1.MsgSend
		- grant
		  
		  collapsed:: true
			- granter
				- bostrom1…,
			- grantee
				- bostrom1…,
			- grant
				- authorization
					- type
						- /SendAuthorization
					- spend_limit
						- denom
							- boot
							- 1000000
					- expiration
						- 2022-06-29T08:18:15Z
		- exec
		  
		  collapsed:: true
			- grantee
				- bostrom1...
			- msgs
				- type
					- bank/MsgSend
				- from_address: bostrom1...,
				- to_address: bostrom1...,
				- amount:
					- denom
						- boot
						- 999
	- distribution
		- LATER fund-community-pool
		- NOW set-withdraw-addr
		  
		  :LOGBOOK:
		  
		  CLOCK: [2022-12-16 Fri 06:16:09]
		  
		  CLOCK: [2022-12-16 Fri 06:16:10]
		  
		  :END:
		- NOW withdraw-all-rewards
		  
		  :LOGBOOK:
		  
		  CLOCK: [2022-12-16 Fri 06:16:12]
		  
		  :END:
		- withdraw-delegator-reward => withdraw-rewards
		  
		  collapsed:: true
			- delegatorAddress
				- bostrom1frk9k38pvp70vheezhdfd4nvqnlsm9dw3j8hlq,
			- validatorAddress
				- bostromvaloper135ca8hdpy9sk0ntwqzpzsvatyl48ptx52tn60p
	- NOW vesting
	  
	  :LOGBOOK:
	  
	  CLOCK: [2022-12-16 Fri 06:08:19]
	  
	  :END:
		- create-vesting-account
		  
		  :LOGBOOK:
		  
		  CLOCK: [2022-12-16 Fri 05:40:16]
		  
		  CLOCK: [2022-12-16 Fri 05:40:17]
		  
		  :END:
	- NOW feegrant
	  
	  :LOGBOOK:
	  
	  CLOCK: [2022-12-16 Fri 06:07:58]
	  
	  :END:
		- grant
		  
		  :LOGBOOK:
		  
		  CLOCK: [2022-12-16 Fri 06:06:48]
		  
		  :END:
		- revoke
		  
		  :LOGBOOK:
		  
		  CLOCK: [2022-12-16 Fri 06:06:51]
		  
		  :END:
	- consensus
		- evidence
		  
		  collapsed:: true
			- submit-evidence
		- crisis
		  
		  collapsed:: true
			- invariant-broken
	- NOW slashing
	  
	  :LOGBOOK:
	  
	  CLOCK: [2022-12-16 Fri 06:08:11]
	  
	  :END:
		- unjail
		  
		  :LOGBOOK:
		  
		  CLOCK: [2022-12-16 Fri 05:40:12]
		  
		  CLOCK: [2022-12-16 Fri 05:40:13]
		  
		  :END:
	- offline
		- encode
		- decode
		- sign
		- sign-batch
		- multisign
		- multisign-batch
		- validate-signatures
		- broadcast