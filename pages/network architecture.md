focus-flow superintelligence network — full architecture & design (aug 2025)

preface\
• this document consolidates our entire chat, restoring details you said were missing, and reformats everything for logseq: lower-case, no bold, and a hard line break after every bullet and paragraph.

vision and goals\
• earth-scale cybergraph with token-weighted focus (π) recomputed each block.\
• developer-friendly today via multiple vms; long-term, native focus-flow dominates compute.\
• sovereign data-availability inside the network, not outsourced.\
• portability first: pure-rust, webgpu kernels, browser light-clients.

principles\
• minimal deterministic base plane: focus-flow kernels, balances, ibc routing, one global commitment.\
• elastic application plane: several vms run as sandboxes, but all read and write the same shared state.\
• shared state over per-vm silos: interop by construction, single proof system, single da grid.\
• economics separated by function but settled in one bank.

focus-flow compute machine (ffcm)\
• purpose: turn edge deltas into a converged focus vector π that is committed on-chain.\
• memory model: flat u32 heap in 2 gb pages; word = 1 sub-bit | 5 tag | 18 label | 31 offset.\
• graph slice: dense f32 π vector mapped to gpu; edge deltas streamed as compact logs.\
• kernels (wgsl): apply, duplicate, distribute, succ\_switch, collapse, specialize (jit).\
• dispatcher: 64-entry tag-pair table → 7 opcodes, constant-buffer lookup, unknown pairs fall back to collapse.\
• block pipeline: load edge deltas → scatter (build redex queue) → dispatch until queue empty or iteration cap → push-sum gather until ε < 1e-6 → write π slice and graph\_root.\
• jit specialization: track hot 3-op motifs, auto-emit fused wgsl kernel, cache pipeline for next block.\
• sharding: murmur64(cid) → shard id; validators own disjoint shards; cross-shard edges buffered and forwarded.\
• convergence guard: spectral gap estimate per shard; hard cap 2048 iterations; proposer penalty if not converged.\
• cpu fallback for tiny shards; webgpu light mode lowers workgroup sizes and ε thresholds.\
• performance expectations: desktop rtx 3060 \~25 gb/s effective rewrite (≈10⁸ edges update in \~1.2 s); mac m2 \~6 gb/s; browser webgpu \~0.5 gb/s on m2.

hvm lineage and minimized rule-set\
• hvm2 vs hvm3: hvm3 makes dup and sup explicit, uses affine variables with global substitutions, and specializes interactions by type.\
• ffcm meta-rules mapped to hvm3: apply, duplicate, distribute, succ, switch, collapse, specialize.\
• benefit: optimal sharing and small dispatch surface ideal for gpu.

query and reasoning layer\
• dual approach.\
• logic layer: datalog and prolog for integrity rules, incremental views, and provable queries.\
• graph algebra: gql-style patterns and iterative operators (random walk, pagerank, label propagation) compiled to scatter and gather kernels.\
• cross-calls allowed: a datalog rule may invoke a graph operator and cache results as relations.

state and storage model\
• one shared key-space with three logical areas (prefixes), one global sparse-merkle root.\
• /graph: edges, π slices, analytics indexes.\
• /token: storage of balances\
• /kv: properties, orders, validator metadata, governance params, large blobs by cid.\
• physical back-ends chosen for portability.\
• native: redb single-writer b-tree, pure-rust.\
• browser: indexeddb via idb-wasm.\
• fallback: sled for native where useful.\
• single commit path: all module deltas merge into one redb transaction per block; root updated incrementally over changed keys.\
• optional multiple physical files for tuning (graph focus bin, bank db, kv db) while preserving one logical commitment and proof.\
• concurrency rules: vms run in a scheduler; each maintains a write-set; scheduler merges deltas deterministically; single commit produces the global root.

sovereign data-availability (internal da)\
• internal blob-grid per block with reed–solomon rs(2k,k) row parity and a namespaced merkle tree (nmt) root committed in the header.\
• one da namespace is enough, but shares are lexicographically ordered by top-level prefix for locality.\
• validators sample random shares; failure rejects block.\
• iroh transports blob shares; share ids = hash(namespace || row || col || height).\
• persistence policy: keep hot graph shares locally; pin long term in iroh; balances small so keep all; kv shares best-effort with a pin bounty market.\
• code footprint for da: about 1.5 k loc (codec, nmt, producer, sampler, pin-market).

networking and consensus\
• iroh for gossip, blobs, and da shares; no c or c++ tool-chain.\
• consensus default: avalanche snowman adapter; later back-ends pluggable.\
• ibc router in-process with capability keys; cross-vm calls are zero-fee ibc packets delivered in the same block.

multi-vm strategy without per-vm stores\
• execution plane hosts evm, move, wasm (lean cosmwasm), and bpf adapters.\
• all vms use the same shared state (prefix-scoped views under /vm//...), not per-vm roots.\
• cross-vm calls go through in-process ibc channels; proofs and ordering are captured by the scheduler.\
• failure containment via namespaces and capability keys, not via separate trees.

system modules: tokens, trading, names\
• token: balances, transfers, staking; lives under /bank.\
• dex: minimal amm or order-book encoded as graph + kv; orders as particles, mutable fields in kv.\
• name: cid ↔ short-name registry; under /kv/name.\
• economics: graph edges burn weight; kv blobs pay blob-credits; single gas token for fees and staking.

portability stance\
• rust everywhere; wgpu kernels for vulkan, metal, dx12, webgpu.\
• redb native, sled fallback, idb in browser; all hidden behind a shard-store trait.\
• wasm light client compiles the same crates; webgpu kernels reused.\
• rust + webgpu typically within 1.3–2× of cuda, acceptable for adoption; optional cuda fast-path later if needed.

code structure and size\
• core ffcm (cpu + wgpu host + kernels) ≈ 4 k loc.\
• shared store facade (redb, sled, idb) ≈ 0.7 k.\
• sovereign da (codec, nmt, sampler, pin market) ≈ 1.5 k.\
• multi-vm adapters (evm, move, wasm, bpf) ≈ 2.4 k.\
• contracts + cli + grpc and http api ≈ 3.0 k.\
• p2p + consensus adapter ≈ 2.5 k.\
• observability + tests + benches ≈ 11 k.\
• total human-written now ≈ 25 k loc, with natural growth toward 50–100 k as features mature.

rollout plan\
• phase 0: ffcm cpu path and tests; flat heap and whnf parity.\
• phase 1: wgsl kernels for apply, duplicate, distribute, collapse; dispatcher; gpu parity.\
• phase 2: push-sum gather, convergence checks, shard scheduler.\
• phase 3: sovereign da producer and sampler wired through iroh.\
• phase 4: shared store facade; bank and name modules; first vm adapter.\
• phase 5: dex, second vm, ibc router; browser light client.\
• phase 6: jit specialize, telemetry, soak tests; optional cuda fast-path.

trade-offs resolved\
• hvm3 semantics kept, rule surface minimized for gpu dispatch.\
• one global root across a shared key-space for maximum interop.\
• sovereign da mandatory; no external dependency.\
• multiple vms allowed, but all read and write the same shared state; cross-vm via ibc.\
• three logical stores for tuning, yet one commitment and one proof scheme.

open questions\
• final consensus selection and block-time constraints for π updates.\
• on-chain proof flavor per vm (fraud vs zk) and base-plane verification cost.\
• exact scheduling and ordering for cross-vm dependencies under load.\
• archival policy for very old graph shards and blob-retention economics.

developer enablement\
• feasibility: solo with llm pairing in 6–8 weeks for ffcm mvp; 3–4 months for a networked mvp.\
• learning path: rustlings → learn wgpu compute → ffcm cpu → wgsl kernels → sovereign da.

summary\
• a compact, portable, sovereign network where focus-flow computation is first-class, data stays available, and developers can build today across familiar vms without fragmenting state.
