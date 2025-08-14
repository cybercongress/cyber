title
focus flow: realistic complexity vs connectivity of the cybergraph

summary
this note derives realistic memory and compute complexity for focus flow as a function of cybergraph size and connectivity. the punchline: per-iteration cost is o(v + e) = o(v · c), where v is particles (nodes), e is cyberlinks (directed edges), and c = e/v is average out-degree. total cost multiplies this by the iterations to convergence, which depends on the spectral gap (λ) and target accuracy (ε). in practice, you get near-o(v) only when c stays bounded (sparse graphs), storage is compressed, and communication is well-partitioned.  

notation
v = number of particles (nodes)
e = number of cyberlinks (directed edges)
c = e / v = average out-degree (connectivity)
λ = spectral gap of the transition matrix p (mixing rate)
ε = target l1 error to stationary focus distribution
b = branching factor within a local horizon (for localized updates)
h = locality horizon (number of hops) for localized focus flow
p = number of workers/devices (in distributed execution)

model assumptions
1) focus flow update is a markovian step on a token-weighted graph: π^{t+1} = normalize(w · (t ⊙ π^t))  
2) storage maintains particles, edges, edge weights, and (optionally) per-node token/state vectors  
3) implementations may be synchronous (power iteration), asynchronous (push/pull random walks), or localized (bounded horizon)  

per-iteration complexity
memory (working set)
• node state: o(v)  
• edge list + weights + indices: o(e)  
• optional token/stake vectors and buffers: o(v)  
• total: o(v + e) = o(v · (1 + c))  

compute (one global iteration)
• touch each edge once for message passing / accumulation: o(e)  
• light per-node normalization and activation: o(v)  
• total: o(e + v) = o(v · (1 + c))  

iterations to convergence
• for power iteration on an ergodic chain, iterations k ≈ o((1/λ) · log(1/ε))  
• total work ≈ o((v + e) · (1/λ) · log(1/ε))  
interpretation: denser graphs often have larger λ (faster mixing) but higher per-iteration cost; sparser graphs have smaller cost per step but may need more steps. there is a regime where moderate c maximizes time-to-ε.  

connectivity regimes and scaling
1) sparse (c = o(1) or bounded constant)
   • e ≈ c · v  
   • memory per iter: o(v)  
   • compute per iter: o(v)  
   • total: o(v · (log(1/ε)/λ))  
   • achievable with degree caps, pruning, sparsification, or local attention windows  

2) small-world / semi-sparse (c = o(log v))
   • e ≈ v log v  
   • memory per iter: o(v log v)  
   • compute per iter: o(v log v)  
   • total: o(v log v · (log(1/ε)/λ))  

3) densifying power-law (c ~ v^α, 0 < α < 1)
   • e ≈ v^{1+α}  
   • memory per iter: o(v^{1+α})  
   • compute per iter: o(v^{1+α})  
   • total: o(v^{1+α} · (log(1/ε)/λ))  

4) dense (c ~ v)
   • e ≈ v^2  
   • memory per iter: o(v^2)  
   • compute per iter: o(v^2)  
   • total: o(v^2 · (log(1/ε)/λ))  

localized focus flow (bounded horizon)
idea: approximate global focus by propagating probability mass within an h-hop neighborhood per step.  
• per-node work ≈ o(b^h) with b the average branching factor inside the active subgraph  
• global pass ≈ o(v · b^h), memory ≈ o(v · b^h) if expansions are materialized  
• with degree caps b ≤ b_max, complexity becomes o(v · b_max^h)  
• quality/ε depends on how much stationary mass lies outside the local horizon; hierarchy or teleportation can correct bias  

monte carlo focus (random-walk sampling)
• launch m walkers per node (or per active node) for t steps  
• compute ≈ o(m · v · t) with t tied to mixing time ~ o((1/λ) · log(1/ε))  
• memory can be o(v) if edges are streamed from disk and visits are counted in compact sketches  
• good for streaming graphs and massive v when exact power iteration is too costly  

communication and parallelism
• 1d edge-partitioned message passing per iter: comm ≈ o(edge_cuts)  
• in practice: comm_time ≈ α · msgs + β · bytes, where msgs ∝ partitions and bytes ∝ cut edges  
• graph partitioning to minimize cuts while balancing o(e/p) work per worker is critical  
• pipeline across levels (gpu for edge ops, cpu for normalization, nvme for streaming) to hide latency  

storage layout and constants
• csr/csc sparse matrices: near-optimal scans over edges  
• mixed precision for weights/focus: halve bandwidth, minimal accuracy loss in late iterations  
• compressed integer indices and delta-encoding for adjacency cut memory by 1.5–3×  

practical knobs to stay near-linear
• cap degree: enforce c ≤ c_max via pruning or reweighting  
• sparsify adaptively: drop edges with low long-run contribution (trust-region pruning)  
• hierarchical coarsening: solve on coarse graph, prolongate, then refine (multigrid-style)  
• restart/teleportation: improves λ without densifying topology  
• warm starts: reuse π from previous timestep to cut iterations  

numerical swags (illustrative)
assume λ_eff and constants absorbed into a factor k_ε = (log(1/ε)/λ_eff).  

• v = 1e6, c = 6 (sparse)
  - e = 6e6  
  - memory per iter ~ o(7e6) entries  
  - compute per iter ~ o(7e6) ops-equivalent  
  - total ~ o(7e6 · k_ε)  

• v = 1e8, c = 12 (semi-sparse)
  - e = 1.2e9  
  - memory per iter ~ o(1.2e9)  
  - compute per iter ~ o(1.2e9)  
  - total ~ o(1.2e9 · k_ε)  

• v = 1e10, c = v^{0.25} ≈ 100 (densifying)
  - e ≈ 1e12  
  - memory/compute per iter ~ o(1e12)  
  - total ~ o(1e12 · k_ε)  

takeaways
1) strict o(v) per-iteration is only realistic when connectivity is bounded (c = o(1)) and layouts are sparse  
2) total runtime is dominated by (v + e) times the mixing factor log(1/ε)/λ  
3) you can trade density for mixing: increase λ via teleportation, hierarchy, or degree caps instead of raw edges  
4) localized and monte carlo variants let you control constants and memory by limiting horizon or samples  
5) in decentralized deployments, communication and partitioning dominate — design for minimal edge cuts and steady streaming  

appendix: mapping to transformer intuition
• focus flow with capped c and h resembles sliding-window + sparse global tokens  
• teleportation ≈ global tokens or cls-like anchors improving mixing without quadratic blowup  
• hierarchy ≈ multi-scale attention layers that refine coarse focus  

open questions
• optimal sparsification policy that maximizes λ per edge budget  
• error bounds for localized focus vs global stationary distribution under degree caps  
• best-in-class partitioners and pipelines for billion-edge cybergraphs on commodity clusters  

