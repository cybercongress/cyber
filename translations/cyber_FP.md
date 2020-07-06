# cyber: Pag-compute ng kaalaman ng Great Web

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/graph.png" />
</p>

## Abstract

Ang consensus ng computer ay pinapayagang mag-compute ng mga may kaugnayan na mga sagot nang walang mga kuro-kuro na mga tagapamagitan ng blackbox, tulad ng Google, Amazon o Facebook. Ang mga walang saysay, content-addressable peer-to-peer communication networks, tulad ng IPFS, at mga stateful consensus computer tulad ng Ethereum, ay maaaring magbigay ng bahagi lamang ng solusyon na kinakailangan upang makakuha ng mga parehong sagot. Gayunpaman, mayroong hindi bababa sa 3 mga problema na nauugnay sa nabanggit na mga pagpapatupad. (A) ang subjective na katangian ng kaugnayan. (B) kahirapan sa scaling consensus computer para sa over-sized knowledge graphs. (C) ang kakulangan ng kalidad sa mga tulad ng mga knowledge graphs. Sila ay madaling kapitan ng iba't ibang mga surface attacks, tulad ng sybil attacks, at ang makasariling pag-uugali ng mga nakikipag-ugnay na ahente. Sa dokumentong ito, tinukoy namin ang isang protocol para sa mapagkakatiwalaan na pagsasama ng computing na may kaugnayan, sa pagitan ng mga IPFS objects, na batay sa Tendermint na pinagkasunduan ng cyber~Rank, na kinakalkula gamit ang mga GPU sa pag sang-ayon. Bilang patunay na pagsang-ayon ng patakaran ay hindi makakatulong sa paunang pamamahagi, binabalangkas namin ang disenyo para sa mga laro ng ekolohiya at mahusay na pamamahagi. Naniniwala kami na ang isang minimalistic na arkitektura ng protocol ay kritikal para sa pagbuo ng isang network ng domain-specific knowledge consensus computers. Bilang isang resulta ng aming trabaho, ang ilang mga aplikasyon na hindi pa naganap nuon, ay lalabas na. Pinalawak namin ang dokumentong ito sa aming pangitain ng mga posibleng tampok at potensyal na aplikasyon.

## Ang Dakilang Web

Ang mga orihinal na protocol ng Internet, tulad ng: TCP / IP, DNS, URL at HTTP/S ay nagdala ng web sa isang stale point, kung saan ito matatagpuan hanggang ngayon. Isinasaalang-alang ang lahat ng mga benepisyo na ginawa ng mga protocol na ito para sa paunang pag-unlad ng web, kasama ang mga ito, nagdala sila ng mga makabuluhang obstacles sa talahanayan. Globality, ang pagiging isang vital property ng web ay nasa ilalim ng isang tunay na banta mula nang ito ay umpisahan. Ang bilis ng koneksyon ay nagpapanatili ng panghinaaalsa habang ang network mismo ay patuloy na lumalaki dahil sa maraming mga interbensyon ng gobyerno. Ang huli ay nagdudulot ng mga alalahanin sa privacy bilang isang umiiral na banta sa mga karapatang pantao.

Ang isang pag-aari na hindi maliwanag sa simula ay nagiging mahalaga sa pang-araw-araw na paggamit ng Internet: ang kakayahang makipagpalitan ng permanenteng mga link, sa gayon, [hindi sila masisira matapos ang oras na lumipas](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN). Ang pag-asa sa arkitektura nang paisa-isa ay pinapayagan ng ISP ang mga pamahalaan na epektibong magsumite ng mga packet. Ito ang huling pagbagsak sa tradisyonal na web-stack para sa bawat engineer na nababahala tungkol sa hinaharap.

Ang iba pang mga pag-aari, kahit na hindi gaanong kritikal, ay talagang kanais-nais: offline at real-time connection. Ang average Internet user, habang offline, ay dapat pa ring magkaroon ng kakayahang magpatuloy sa pagtatrabaho sa estado na hawak na nila. Matapos makuha ang isang koneksyon dapat silang mag-sync sa global state at magpatuloy upang mapatunayan ang pagiging totoo ng kanilang sariling estado real-time. Sa kasalukuyan, ang mga pag-aari na ito ay inaalok sa antas ng aplikasyon. Naniniwala kami na ang mga pag-aari na ito ay dapat isama sa mga mas mababang antas ng mga protocol.

Ang paglitaw ng [isang brand-new web-stack](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw) ay lumilikha ng isang pagkakataon para sa isang mahusay na Internet. Tinatawag ito ng web3 ng mga pamayanan. Tinatawag namin itong the Great Web. Naniniwala kami na ang iba't ibang uri ng mga komunikasyon sa mababang antas ay dapat na hindi mabago at hindi dapat baguhin sa loob ng mga dekada, hal. hindi mababago ang mga link sa nilalaman. Tila nangangako sila sa pag-alis ng mga problemang conventional protocol stack. Nagdaragdag sila ng higit na bilis at nagbibigay ng mas madaling ma-access na koneksyon sa bagong web. Gayunpaman, tulad ng nangyari sa anumang konsepto na nag-aalok ng something unique- lumitaw ang mga bagong problema. Ang isa sa gayong pagkabahala ay ang general-purpose search. Ang existing na general-purpose search engines ay mahigpit at sentralisadong database na ang lahat ay napipilitang magtiwala. Ang mga search engine ay partikular na idinisenyo para sa mga arkitektura ng client-server, batay sa TCP / IP, DNS, URL at HTTP/S. Ang Great Web ay lumilikha ng isang hamon at isang pagkakataon para sa isang search engine na batay sa mga umuusbong na teknolohiya at partikular na idinisenyo para sa mga layuning ito. Ito'y kahanga-hanga, ang walang pahintulot na arkitektura ng blockchain ay nagbibigay-daan sa pagbuo ng general-purpose search engine sa isang paraan na hindi naa-access sa mga nakaraang arkitektura.


## Sa mga Halimbawa ng mga problema ng kalaban

[Ang kasalukuyang arkitektura ng mga search engine](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6) ay isang sistema kung saan ang ilang mga entity ay nagpoproseso ng maling pamamaraan. Ang pamamaraang ito ay naghihirap mula sa isang mapaghamon at isang natatanging problema, na hindi pa malulutas, maging ng mga napakatalino na siyentipiko ng Google: ang mga halimbawa ng panlusob na problema. [the adversarial examples problem](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9). Ang problema na kinikilala ng Google, ay sa halip mahirap na algorithmically dahilan kung o isang partikular na sample ay magkasalungat. Ito ay hindi naaayon sa kung gaano kamangha-mangha ang teknolohiya sa pagtuturo sa sarili nito. Ang isang diskarte sa crypto-economical ay maaaring magbago ng mga benepisyaryo sa laro. Dahil dito, ang pamamaraang ito ay epektibong mag-alis ng mga posibleng mga vektor ng pag-atake ng sybil. Inaalis nito ang pangangailangan sa modelo ng hard-code na pag-crawl at nangangahulugang pagkuha ng isang nilalang. Sa halip, binibigyan nito ang kapangyarihang ito sa buong mundo. Ang isang pag-aaral na lumalaban sa sybil, agent-generated model, ay maaaring humantong sa mga order ng magnitude na higit na mahuhula na mga resulta.


## Cyber protocol

Sa core nito ang protocol ay napaka minimalistic at maaaring maipahayag gamit ang mga sumusunod na hakbang:

1.Sumite ang genesis ng cyber protocol batay sa tinukoy na pamamahagi.
2.Tukuyin ang estado ng [knowledge graph](#knowledge-graph)
3. Magtipon ng mga transaksyon gamit ang [consensus computer] (#the-notion-of-a-consensus-computer)
4.Suriin ang bisa ng mga lagda
5.Suriin ang [limitasyon ng bandwidth](#relevance-machine)
6.Suriin ang bisa ng mga CIDs
7.Kung ang mga lagda, ang limitasyon ng bandwidth at CIDs ay lahat ng may-bisa, mag-apply ng mga [cyberlink](#cyberlinks) at transaksyon
8.Kalkulahin ang mga mapagmataas ng [cyber/~Rank](#cyberrank) para sa bawat pag-ikot para sa mga CIDs sa [knowledge graph](#knowledge-graph)

Ang natitirang bahagi ng dokumentong ito ay tinatalakay ang makatwiran at ang mga teknikal na detalye ng iminungkahing protocol.

## Knowledge graph

Kinakatawan namin ang isang knowledge graph bilang isang weighted graph ng mga direktang link sa pagitan ng mga content addresses. Aka, mga pagkakakilanlan ng nilalaman, CID, IPFS hashes, o simpleng - mga link sa IPFS. Sa dokumentong ito, gagamitin namin ang mga term sa itaas bilang mga kasingkahulugan

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/knowledge-graph.png" />
</p>

Ang mga content addresses ay mahalagang web3 link. Sa halip na gamitin ang hindi maliwanag at pabago-bago:

`https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md`

Ginagamit namin ang bagay mismo:

`Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH`

Sa pamamagitan ng paggamit ng mga content addresses upang mabuo ang knowledge graph nakakakuha kami ng [labis na kinakailangang](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est) [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps) - [tulad](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR) ng mga superpower ng p2p protocol na nais para sa isang search engine:

- mesh-network future-proof
- pag-access sa interplanetary
- paglaban sa censorship
- teknolohiyang pagsasarili

Ang aming knowledge graph ay nabuo ng mga kamangha-manghang masters. Idinagdag ng mga masters ang kanilang sarili sa knowledge graph sa tulong ng isang solong transaksyon, isang cyberlink. Sa gayon, napatunayan nila ang pagkakaroon ng kanilang private keys para sa mga content addresses ng kanilang ipinahayag na mga Public keys. Sa pamamagitan ng paggamit ng mga mechanics na ito, ang [consensus computer](#the-notion-of-a-consensus-computer) ay maaaring makamit ang napatunayan na pagkakaiba sa pagitan ng mga paksa at mga bagay sa knowledge graph. 

Ang aming pagpapatupad ng [go-cyber](https://github.com/cybercongress/go-cyber) ay batay sa mga pagkakakilanlan ng [cosmos-SDK](https://github.com/cosmos/cosmos-sdk) at mga address ng nilalaman ng [CIDv0/CIDv1](https://github.com/multiformats/cid#cidv0 

Bumubuo ang mga masters graph ng kaalaman sa pamamagitan ng paglalapat ng mga [cyberlinks](#cyberlinks).


## Cyberlinks

Upang maunawaan kung paano gumagana ang mga cyberlink kailangan nating maunawaan ang pagkakaiba sa pagitan ng isang link sa URL (aka, isang hyperlink) at sa pagitan ng isang link sa IPFS. Ang isang link sa URL ay tumutukoy sa lokasyon ng nilalaman, maging isang link ng IPFS ang nilalaman mismo. Ang pagkakaiba sa pagitan ng web architectures batay sa mga location links at content links ay radikal at nangangailangan ng isang natatanging diskarte.

Ang Cyberlink ay isang diskarte upang maiugnay ang dalawang content addresses, o mga link sa IPFS, semantically:

````bash
.md syntax: [QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH](Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH)    
.dura syntax: QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH.Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
````

Ang nabanggit sa cyberlink ay nangangahulugan na ang pagtatanghal ng [go-cyber](https://github.com/cybercongress/go-cyber)sa panahon ng [cyberc0n](https://etherscan.io/token/0x61B81103e716B611Fff8aF5A5Dc8f37C628efb1E) ay tumutukoy sa Cosmos white paper. Ang konsepto ng mga cyberlink ay isang kombensyon sa paligid ng mga simpleng semantika ng isang format na pangkomunikasyon sa anumang p2p network:

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/cyberlink.png" />
</p>

Nakita namin na ang isang cyberlink ay kumakatawan sa isang link sa pagitan ng dalawang link. Napakadali!

Ang Cyberlink ay simple, ngunit napaka-powerful semantic construction para sa pagtatayo ng predictive model ng universe. Nangangahulugan ito na ang paggamit ng mga cyberlink sa halip ng mga hyperlink ay nagbibigay sa amin ng mga superpower na hindi naa-access sa mga nakaraang arkitektura ng mga search engine ng pangkalahatang-layunin.

Ang mga Cyberlink ay maaaring mapalawig, maaari silang bumuo ng mga linkchain kung mayroong dalawa o higit pang mga cyberlink subsist mula sa isang master, kung saan ang pangalawang link sa unang cyberlink ay katumbas ng unang link sa ikalawang cyberlink:

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/linkchain.png" />
</p>

Kung pinalawak ng mga ahente ang mga native IPFS links na may isang semantically mas mayamang, halimbawa, na may [dura](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md) links, kung gayon ang pagsang-ayon sa mga execution rules sa pamamagitan ng isang tiyak na programa ay maabot sa isang mas natural na pamamaraan.

Ang [go-cyber](https://github.com/cybercongress/go-cyber) implementation ng mga cyberlink ay available sa [.cyber](https://github.com/cybercongress/dot-cyber) app ng aming eksperimentong web3 browser cyb, at sa [cyber.page](http://cyber.page).

Ang mga cyberlink na isinumite ng mga masters ay naka-imbak sa isang merkle tree ayon sa [RFC-6962 standard](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). Pinapayagan nito ang pagpapatunay para sa [proof-of-relevance](#proof-of-relevance).

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/graph-tree.png" />
</p>

Gamit ang mga cyberlink, maaari nating kalkulahin ang kaugnayan ng mga paksa at mga bagay sa [knowledge graph](#knowledge-graph). Ngunit kailangan namin ng isang  [consensus computer](#the-notion-of-a-consensus-computer).

## Ang paniwala ng isang computer na pinagkasunduan

Ang isang consensus computer ay isang abstract na computing machine na lumitaw mula sa pakikipag-ugnayan sa pagitan ng mga ahente. Ang isang consensus computer ay may kakayahan sa mga tuntunin ng mga fundamental computing resources: memorya at pagkalkula. Upang makipag-ugnay sa mga ahente ang isang computer ay nangangailangan ng bandwidth. Ang isang perpektong consensus computer ay isang computer kung saan:

`the sum of all the computations and memory available to individuals`     
`is equal to`    
`the sum of all the verified computations and memory of the consensus computer`    


Alam natin na:

`verifications of computations < (computations + verifications of computations)`    

Samakatuwid, hindi namin makamit ang isang perpektong consensus computer. Ang CAP theorem at ang scalability trilemma ay nagdaragdag ng higit na katibayan sa pahayag na ito.

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/consensus-computer.png" />
</p>

Ngunit ang teoryang ito ay maaaring gumana bilang isang tagapagpahiwatig ng pagganap para sa isang consensus computer. Matapos ang 6 na taon ng pamumuhunan sa consensus computer, natanto namin na ang pinagkasunduan ng  [Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) ay may sapat na balanse sa pagitan na kinakailangan para sa aming gawain at kahandaan para sa paggawa nito. Samakatuwid, nagpasya kaming ipatupad ang [cyber](#cyber-protocol) gamit ang Tendermint consensus, na kung saan ay may napakalapit na mga setting sa Cosmos Hub. Ang pagpapatupad ng [go-cyber](https://github.com/cybercongress/go-cyber) ay isang 64-bit Tendermint consensus computer ng kaugnayan para sa 64-byte string-space. Hindi ito perpekto, hindi bababa sa 1/146, dahil mayroon kaming 146 na validator na nagpapatunay sa parehong mga pagkalkula na gumagawa ng [knowledge-graph](#knowledge-graph).

Dapat nating tiyakin ang pagkalkula, pag-iimbak at ang supply ng bandwidth ng consensus computer sa isang na-maximize na demand para sa mga query. Ang pagkalkula at pag-iimbak, kung sakaling ang isang basic [relevance machine](#relevance-machine) ay madaling mahulaan batay sa bandwidth. Ngunit ang bandwidth ay nangangailangan ng isang limiting mechanism.

## Relevance machine

Tinukoy namin ang relevance machine bilang isang makina na naglilipat ng estado ng isang [knowledge-graph](#knowledge-graph) batay sa kalooban ng mga ahente na nais magturo at pag-aralan ang [knowledge-graph](#knowledge-graph) na ito. Ang kalooban ay inaasahan ng bawat [cyberlinks](#cyberlinks) na ginagawa ng isang master. Kung mas maraming pang mga ahente ang nagtatanong sa [knowledge-graph](#knowledge-graph), mas nagiging higit ang kanilang kaalaman. Batay sa mga proyektong ito, ang pagkakaugnay sa pagitan ng content address ay maaaring makalkula. Ang relevance machine ay nagbibigay-daan sa isang simpleng konstruksyon para sa search mechanism sa pamamagitan ng pag-query at paghahatid ng mga sagot.

Ang isang pag-aari ng relevance machine ay mahalaga. Dapat itong magkaroon ng mga induktibong katangian ng pangangatuwiran o sundin ang prinsipyo ng blackbox:

`The machine should be able to interfere with predictions without any knowledge about the objects,`   
`except for who, when and what was cyberlinked`   

Kung ia-assume natin na ang [consensus computer](#the-notion-of-a-consensus-computer) ay dapat magkaroon ng ilang impormasyon tungkol sa mga linked objects, kung gayon ang pagiging kumplikado ng naturang modelo ay lalago nang hindi nahuhulaan. Samakatuwid ang mataas na mga kinakailangan ng computer sa pagproseso para sa memorya at pagkalkula. Salamat sa nilalaman ng pagtugon sa isang relevance machine na sumusunod sa prinsipyo ng blackbox, ay hindi kailangang mag-imbak ng data. Ngunit, maaari pa ring epektibong gumana sa tuktok nito. Ang pagbawas ng kahulugan sa loob ng [consensus computer](#the-notion-of-a-consensus-computer ay mahal. Samakatuwid, ang gayong disenyo ay maaaring depende sa assumption blindness. Sa halip na ibawas ang kahulugan sa loob ng [consensus computer](#the-notion-of-a-consensus-computer), nag-disenyo kami ng isang sistema kung saan ang kahulugan ng pagkuha ay hindi na-insentibo. Nakamit ito dahil sa mga masters na nangangailangan ng mga token ng [CYB](#cyb) upang ipahayag ang kanilang kalooban, batay sa kung saan, maaaring makalkula ang ranggo ng kaugnayan. 

Sa gitna ng sistema ng proteksyon ng spam ay isang palagay na ang mga operasyon ng pagsulat ay maaaring isakatuparan lamang ng mga mayroong isang vested na interes sa ebolusyon ng tagumpay ng relevance machine. Bawat 1% ng epektibong stake sa loob ng [consensus computer](#the-notion-of-a-consensus-computer) ay nagbibigay ng kakayahang magamit ang 1% ng mga bandwidth ng mga posibleng network at ang computing capabilities nito. Ang isang simpleng patakaran ay pumipigil sa pang-aabuso sa mga ahente: isang pares ng mga pagkakakilanlan ng nilalaman ay maaaring mai-cyberlink ng isang beses sa isang address.

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/algo1.png" />
</p>

Mayroong dalawang mga paraan lamang upang mabago ang epektibong stake (active stake + bonded stake) ng isang account: direct token transfers at bonding operations.

Gumagamit ang [Cyber](#cyber-protocol) ng isang napaka-simpleng modelo ng bandwidth. Ang pangunahing layunin ng modelong ito ay upang mabawasan ang pang-araw-araw na paglaki ng network sa naibigay palagi. Ginagawa ito upang mapaunlakan ang mga bayani (validators) na may kakayahang mag-forecast ng anumang pamumuhunan sa hinaharap sa imprastraktura. Kaya, narito ipinakilala namin ang 'watts' o 'W'. Ang bawat uri ng mensahe ay may itinalagang W cost. Ang palagiang 'DesirableBandwidth', ay tumutukoy sa kanais-nais na 'RecoveryWindow' na ginugol ng halaga ng W. Tinukoy ng recovery period kung gaano kabilis ang mababawi ng isang master ang kanilang bandwidth mula 0 pabalik sa max bandwidth. Ang isang master ay may pinakamataas na proporsyonal na W sa kanyang mabisang stake, na tinutukoy ng sumusunod na pormula:

`AgentMaxW = EffectiveStake * DesirableBandwidth`

Ang panahong 'AdjustPricePeriod' ay nagbubuo ng kung magkano ang ginugol sa W sa panahon ng 'RecoveryPeriod' sa pinakabagong block. Ang 'SpentBandwidth' / 'DesirableBandwidths' ratio ay tinatawag na fractional reserve ratio. Kapag ang network usage ay mababa, ang fractional reserve ratio ay nag-aayos ng gastos sa mensahe upang payagan ang mga masters na may mas mababang stake upang gumawa ng mas maraming mga transaksyon. Kapag ang demand para sa mga mapagkukunan ay nagdaragdag, ang fractional reserve ratio ay napupunta> 1, dahil dito, ang pagtaas ng gastos ng mensahe at paglilimita ng huling tx count para sa isang pangmatagalang panahon (ang pagbawi ng W ay <pagkatapos W paggastos). Dahil walang gumagamit ng lahat ng kanilang pagmamay-ari ng bandwidth, ito'y ligtas at maaaring gumamit ng hanggang sa 100x na fractional na reserba sa loob ng panahon ng target na recalculation target. Ang ganitong mga mechanics ay nagbibigay ng discount para sa paglikha ng [cyberlinking](#cyberlinks), sa gayon, epektibong na-maximize ang demand para dito. Maaari mong makita na ang iminungkahing disenyo ay nangangailangan ng demand para sa buong bandwidth para sa kaugnayan upang maging mahalaga.

Ang katalinuhan ng tao ay isinaayos sa isang paraan na walang nauugnay at walang-mahalagang mga alaala na nakalimutan sa paglipas ng panahon. Parehong maaaring mailapat sa relevance machine. Ang relevance machine ay maaaring magpatupad ng mga [aggressive pruning strategies](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb) tulad ng, ang pruning ng kasaysayan ng pagbuo ng [knowledge-graph](#knowledge-graph), o pagkalimot ng mga link na hindi gaanong nauugnay.

Bilang resulta, ang ipinatupad na cybernomics ng mga token ng [CYB](#cyb) ay nagsisilbi hindi lamang bilang mga mekanismo ng proteksyon ng pagpapahayag at proteksyon ng spam, kundi pati na rin, gumana bilang isang tool sa regulasyon sa ekonomiya na maaaring ihanay ang kapasidad sa pagproseso ng mga bayani at ang demand sa merkado para sa pagproseso. Ang go-cyber na pagpapatupad ng relevance machine ay batay sa isang straightforward mechanism, na tinatawag na: cyber~ Rank.


## cyber\~Rank

Ang pagraranggo gamit ang [consensus computer](#the-notion-of-a-consensus-computer) ay maaaring maging mahirap, dahil ang consensus computer ay may malubhang mga hadlang sa mapagkukunan. Una, dapat nating tanungin ang ating sarili: bakit kailangan nating makalkula at mag-imbak ng rank on-chain at hindi sundin ang parehong paraan tulad ng [Colony](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj)  o [Truebit](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)?

Kapag nakalkula ang ranggo sa loob ng isang [consensus computer](#the-notion-of-a-consensus-computer), ang isang tao ay madaling ma-access sa pamamahagi ng nilalaman ng ranggo na iyon at isang madaling paraan upang makabuo ng mga [kapaki-pakinabang na aplikasyon](#apps) sa tuktok ng ranggo na iyon. Samakatuwid, nagpasya kaming sundin ang mga cosmic architecture. Sa susunod na seksyon inilalarawan namin ang  [proof of relevance](#proof-of-relevance) mechanism, na nagpapahintulot sa network na masukat sa tulong ng domain-specific [relevance machines](#relevance-machine). Ang mga iyon ay nagtatrabaho nang sabay-sabay, salamat sa protocol ng IBC.

Sa kalaunan, ang [relevance machine](#relevance-machine) machine ay kailangang makakuha ng (1) isang deterministikong algorithm, na magbibigay-daan sa pagkalkula ng ranggo sa isang patuloy na appending network, na mismo, ay maaaring masukat sa mga order ng magnitude ng likes ng [Google](https://google.com). Bilang karagdagan, ang isang perpektong algorithm (2) ay dapat magkaroon ng linear memory at pagiging computational complexity. Pinakamahalaga, ito ay dapat magkaroon ng (3) ang pinakamataas na mapagkakatiwalaang mga kakayahan sa paghula para sa pagkakaroon ng mga may-katuturang mga [cyberlinks](#cyberlinks).

Matapos ang [masusing pananaliksik](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC), nalaman namin na imposible na makuha ang silver bullet. Samakatuwid, nagpasya kaming makahanap ng mas basic, bulletproof way, na maaaring mag-bootstrap sa network: ang [rank](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw) na ginamit nina Larry at Sergey upang i-bootstrap ang kanilang nakaraang network. Ang pangunahing problema sa orihinal na PageRank ay hindi ito lumalaban sa mga pag-atake ng sybil. Gayunpaman, ang isang token-weighted PageRank na kung saan ay limitado ng isang token-weighted bandwidth model ay hindi nagmana sa pangunahing problema ng walang muwang na PageRank, sapagkat - ito ay lumalaban sa pag-atake ng sybil. Sa ngayon, tatawagin natin ito sa cyber ~ Rank, hanggang sa isang bagay na mas angkop ang lalabas. Ang sumusunod na algorithm ay inilalapat sa pagpapatupad nito sa Genesis:

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/algo2.png" />
</p>

Naiintindihan namin na ang ranking mechanism ay palaging mananatiling isang red herring. Ito ang dahilan kung bakit inaasahan naming umaasa sa mga on-chain governance tools na maaaring tukuyin ang pinaka-angkop na mekanismo sa tamang oras. Ipagpalagay namin na ang network ay maaaring lumipat mula sa isang algorithm patungo sa isa pa, hindi lamang batay sa subjective na opinyon, ngunit sa halip na economical a/ b testing sa pamamagitan ng 'hard spooning' ng domain-specific [relevance machines](#relevance-machine).

cyber ~ Rank ay nagtatanggol ng dalawang mga pagpapasya sa disenyo na pinakamahalaga: (1) account nito ang kasalukuyang hangarin ng mga ahente, at (2) hinihikayat nito ang rank inflation ng mga [cyberlinks](#cyberlinks). Tinitiyak ng unang pag-aari na ang cyber ~ rank ay hindi maaaring maging laro. Kung nagpasya ang isang ahente na ilipat ang kanilang mga token ng [CYB](#cyb) sa kanilang account, aakma ang relevance machine sa lahat ng mga nauugnay na [cyberlinks](#cyberlinks) para sa account na ito sa bawat kasalukuyang hangarin ng ahente. Vice versa, kung ang isang ahente ay naglilipat ng mga token ng CYB sa kanilang account, ang lahat ng mga cyberlink na isinumite mula sa account na ito ay agad na makakakuha ng kaugnayan. Ang pangalawang pag-aari ay mahalaga upang hindi magaya sa nakaraan. Tulad ng mga bagong [cyberlinks](#cyberlinks) na patuloy na idinagdag, matutunaw nila ang rank ng mayroon nang mga link proporsyonal. Pinipigilan ng ari-arian na ito ang isang sitwasyon kung saan ang bago at mas mahusay na nilalaman ay may isang mas mababang ranggo dahil lamang ito ay isinumite kamakailan. Inaasahan namin na ang mga pagpapasyang ito ay paganahin ang isang kalidad ng pag-iinteres para sa kamakailang naidagdag na nilalaman sa mahabang buntot ng [knowledge graph](#knowledge-graph).

Gustung-gusto naming talakayin ang problema ng pagbili ng boto. Ang vote-buying bilang isang pangyayari ay hindi masama. Ang mga dilemmas na may pagbili ng boto ay lilitaw sa loob ng mga system kung saan nakakaapekto ang pagboto sa paglalaan ng mga system inflation na iyon. Halimbawa, ang [Steem](http://ipfs.io/ipfs/QmepU77tqMAHHuiSASUvUnu8f8ENuPF2Kfs97WjLn8vAS3) o anumang sistemang batay sa fiat-state. Ang pagbili ng pagboto ay maaaring madaling kumita para sa isang kalaban na gumagamit ng isang laro na zero-sum nang walang pangangailangan upang magdagdag ng halaga. Ang aming orihinal na ideya ng isang desentralisadong paghahanap ay batay sa pamamaraang ito. Ngunit, tinanggihan namin ang ideyang iyon, tinatanggal ang insentibo ng pagbuo ng [knowledge graph](#knowledge-graph) sa antas ng pinagkasunduan. Sa kapaligiran na kung saan ang bawat kalahok ay dapat magdala ng ilang halaga sa system upang maapektuhan ang mahuhulaan na modelo, ang pagbili ng boto ay nagiging matigas na problema sa NP. Samakatuwid, nagiging kapaki-pakinabang sa sistema.

Ang kasalukuyang pagpapatupad ng [relevance machine](#relevance-machine) ay gumagamit ng mga GPU upang makalkula ang ranggo. Ang machine ay makakasagot at maihatid ang may-katuturang mga resulta para sa anumang naibigay na kahilingan sa paghahanap sa isang 64-byte CID space. Gayunpaman, hindi sapat na magtayo ng isang network ng domain-specific [relevance machines](#relevance-machine). Ang mga [Consensus computers](#the-notion-of-a-consensus-computer) ay dapat magkaroon ng kakayahang patunayan ang kaugnayan sa isa't isa.


## Proof of relevance

Dinisenyo namin ang network sa ilalim ng pag-aakala na may kaugnayan sa paghahanap, tulad ng isang malicious behaviour, ay hindi umiiral. Maaari itong i-assume na walang nakakahamak na pag-uugali na matatagpuan sa hangarin na hanapin ang mga sagot. Ang pamamaraang ito ay makabuluhang binabawasan ang anumang pag-atake sa ibabaw.

````bash
Ranks are computed based on the fact that something was searched, thus linked, and as a result - affected the predictive model
````

Ang isang mahusay na pagkakatulad ay siniyasat sa quantum mechanics, kung saan ang pagmamasid mismo ay nakakaapekto sa pag-uugali. Ito ang dahilan kung bakit wala kaming kinakailangan para sa isang bagay tulad ng negatibong pagboto. Sa pamamagitan nito, tinanggal namin ang subjectivity sa labas ng protocol at maaari naming tukuyin ang proof of relevance. 

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/graph-tree.png" />
</p>

Ang bawat bagong CID ay tumatanggap ng isang numero ng pagkakasunud-sunod. Ang pagsunud-sunod ay nagsisimula sa zero. Pagkatapos ay nadagdagan ng isa para sa bawat bagong CID. Samakatuwid, maaari kaming mag-imbak ng ranggo sa isang one-dimensional na array, kung saan ang palatandaan ay ang mga numero ng pagkakasunud-sunod ng CID. Ang mga kalkulasyon ng Merkle tree ay batay sa pamantayang [RFC-6962 standard](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). Gamit ang Merkle trees, maaari nating epektibong patunayan ang ranggo para sa anumang naibigay na content address. Habang ang kaugnayan ay napapailalim pa rin sa likas na katangian, mayroon kaming isang kolektibong patunay na ang isang bagay ay nauugnay sa isang tiyak na pamayanan sa ano mang oras.

Gamit ang uri ng patunay na ito ang alinman sa dalawang [IBC compatible](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk) [consensus computers](#the-notion-of-a-consensus-computer) ay maaaring patunayan ang kaugnayan sa isa't isa. Nangangahulugan ito na ang domain-specific [relevance machines](#relevance-machine) ay maaaring umunlad.

Sa kaugnayan para sa isang pangkaraniwang pagpapatupad ng[go-cyber](https://github.com/cybercongress/go-cyber), ang Merkle tree ay kinakalkula sa bawat pag-ikot at ang pinanggalingan nito na nakatuon sa ABCI.

## Speed o Bilis

Nangangailangan kami ng instant confirmation time upang mabigyan o mapadama sa mga users ang conventional web-application. Ito ay isang powerful architectural requirement na humuhubog sa economical topology at sa scalability ng [cyber](#cyber-protocol) protocol. Ang ipinanukalang disenyo ng blockchain ay batay sa [Tendermint consensus](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) algorithm na may 146 na validator at may isang mabilis, 5 seconds tx finality time. Ang average na oras ng kumpirmasyon ay mas malapit sa 1 segundo at maaaring gumawa ng mga kumplikadong pakikipag-ugnayan sa blockchain na halos hindi nakikita ng mga ahente. 

Ipinapahiwatig namin ang isang partikular na pag-aari ng [go-cyber](https://github.com/cybercongress/go-cyber) sa context of speed - pagkalkula ng ranggo. Bilang isang bahagi ng pinagkasunduan, nangyayari ito kaayon sa pagpapatunay ng transaksyon sa loob ng mga pag-ikot. Ang isang round ay isang consensus variable na tinukoy ng mga stakeholder. Sa pagsisimula, ang isang round ay nakatakda sa 20 blocks. Samakatuwid, ipinapahiwatig nito na bawat 100 seconds ang network ay dapat sumang-ayon sa kasalukuyang ugat ng [knowledge graph](#knowledge-graph). Nangangahulugan ito na ang bawat isinumite ng [cyberlink](#cyberlinks) ay nagiging isang bahagi ng [knowledge graph](#knowledge-graph) agad at nakakakuha ng isang rank sa loob ng isang average period ng 50 seconds. Sa mga unang araw ng [Google](https://google.com) rank ay halos masinsinang nirere-compute every week. Naniniwala kami na ang mga masters ng Great Web ay malulugod na obserbahan na ang mga pagbabago sa ranggo sa real-time, ngunit, ay nagpasya na ilunsad ang network sa isang assumption na ang window na ito ay sapat. Inaasahan na sa pagbuo ng [cyber](#cyber-protocol) protocol ang pagbaba ng bilis ng bawat pag-ikot ay bababa. Ito ay dahil sa kompetisyon sa pagitan ng mga bayani. Alam namin ang ilang mga mekanismo upang gawing mas mabilis ang pagkakasunud-sunod ng function na ito ng mga magnitude:

- Pag-optimize ng mga consensus parameter
- Mas mahusay na parallelization ng ranggo ng pagkalkula
- Isang magandang [hakbang](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs) para sa consensus

## Scalability

Kailangan namin ng isang arkitektura na magpapahintulot sa amin na masukat ang ideya sa kahalagahan ng kagustuhan ng [Google](https://google.com). Ipagpalagay natin, na ang node implementation, na batay sa [Cosmos-SDK](https://github.com/cosmos/cosmos-sdk) ay maaaring magproseso ng 10k transactions bawat segundo. Ibig sabihin nito, na araw-araw, hindi bababa sa 8.64 milyong mga masters ay maaaring magsumite ng 100 [cyberlinks](#cyberlinks) bawat isa, at magkakasabay ang mga resulta ng paghahanap. Ito ay sapat na upang mapatunayan ang lahat ng mga assumptions ay mabangis, ngunit, hindi sapat upang sabihin na gagana ito sa kasalukuyang sukat ng Internet. Dahil sa kasalukuyang estado ng pananaliksik ng sining na ginawa ng aming koponan, ligtas naming maipahayag na walang consensus technology na umiiral, na magpapahintulot sa pagsukat ng isang partikular na blockchain sa laki na kailangan namin. Samakatuwid, ipinakilala namin ang konsepto ng domain-specific [knowledge graphs](#knowledge-graph). 

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/network.png" />
</p>

Ang isa ay maaaring maglunsad ng sariling domain-specific search engine sa pamamagitan ng forking [go-cyber](https://github.com/cybercongress/go-cyber), na nakatuon sa \textit {common public knowledge}. O kaya, simpleng ituro ang go-cyber bilang isang module sa isang umiiral na chain, e.i. Cosmos Hub. Ang protocol ng komunikasyon ng inter-blockchain ay nagpapakilala ng mga kasabay na mekanismo ng estado ng pag-sync sa pagitan ng [relevance machines](#relevance-machine). Samakatuwid, sa iminungkahing arkitektura ng paghahanap, ang domain-specific relevance machine ay maaaring malaman mula sa karaniwang kaalaman. Tulad ng common knowledge ay maaaring matuto mula sa mga domain-specific [relevance machines](#relevance-machine).

## Browzers

Nais naming isipin kung paano ang iminumungkahing network na gumagana sa isang web3 browser. Sa aming pagkabigo ay [hindi kami makahanap](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md) ng isang web3 browser na maaaring ipakita ang kahusayan ng iminungkahing diskarte sa aksyon. Ito ang dahilan kung bakit nagpasya kaming bumuo ng isang web3 browser mula sa simula. Ang [Cyb](https://cyb.ai) ay ang ating friendly robot na mayroong isang sample na. [.cyber](https://cyber.page) application para sa pakikipag-ugnay sa [cyber](#cyber-protocol) protocol.

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/cyb.jpg" />
</p>

Bilang isang mabuting halimbawa ng paghahatid, lumikha kami ng [cyber.page](https://cyber.page/). Pinapayagan nito ang mga bayani, masters at evangelists na makipag-ugnay sa protocol sa pamamagitan ng isang web2 gateway. Lumikha ng mga cyberlink, nilalaman ng pin nang direkta sa IPFS, i-search ang Great Web, lumahok sa pamamahala ng cyber at iba pa. Maaari rin itong kumilos bilang isang in-depth explorer, isang wallet at maaaring ibulsa ang hardware wallets, tulad ng Ledger devices. 

Ang mga kasalukuyang search snippet ay hindi kagandahan. Ngunit, ipinapalagay namin na madali silang mapalawak gamit ang [IPLD](https://github.com/ipld/specs) para sa iba't ibang uri ng nilalaman. Kalaunan, maaari silang maging mas kaakit-akit kaysa sa mga [Google](https://google.com).

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/architecture.png" />
</p>

Sa panahon ng pagpapatupad ng iminungkahing arkitektura, natanto namin ng hindi bababa sa 3 pangunahing mga benepisyo na maaaring hindi maihatid ng [Google](https://google.com) gamit ang conventional approach:

- ang mga resulta ng paghahanap ay madaling maihatid mula sa anumang p2p network: hal. Maaaring magplay ng video ang .cyber
- Ang payment buttons ay maaaring mai-embed papasok search snippet. Nangangahulugan ito na ang mga ahente ay maaaring makipag-ugnay sa mga search results, hal. ang mga ahente ay maaaring bumili ng isang item mula sa .cyber. Nangangahulugan ito na ang e-commerce ay maaaring umunlad ng patas ito'y pasasalamat sa isang provable conversion attribution. 
- Ang mga search snippet ay hindi kailangang maging static ngunit maaaring maging interactive. hal. Maaaring maihatid ng .cyber ang iyong kasalukuyang wallet balance.

## Deployment

Dahil sa mga limitasyong teknikal, kailangan nating i-bootstrap ang ekosistema gamit ang 2 token: [THC](#thc) at [CYB](#cyb)

- Ang [CYB](#cyb) ay ang katutubong tanda ng soberanong [cyber](#cyber-protocol) na pinalakas ng algorithm ng pinagkasunduang Tendermint. Ito ay may 3 pangunahing paggamit: (1) staking para sa consensus, (2) bandwidth na naglilimita sa pagsusumite ng mga [cyberlinks](#cyberlinks), at (3) pagpapahayag ng kalooban ng mga masters para sa pagkalkula ng cyber rank.

- Ang [THC](#thc) (pagbigkas bilang tech) ay isang malikhaing cyber proto substance. Ang [THC](#thc) bilang isang Ethereum ERC-20 compatible token na mayroong halaga ng utility sa anyo ng kontrol sa cyber Foundation (ang pamayanan na namamahala sa DAO) at ang ETH mula sa distribution game. Ang [THC](#thc) ay pinalabas sa paglikha ng cyber Foundation bilang isang samahan ng Aragon. Ang mga malikhaing kapangyarihan ng THC ay nagmula sa kakayahang makatanggap ng 1 CYB token bawat 1 [THC](#thc) token kapag na-vested bago matapos ang cyber Auction.

Ang parehong mga token ay mananatiling gumagana at susubaybayan nang nakapag-iisa ang halaga ng isa't isa dahil sa kanilang kakaibang utility sa pamamagitan ng likas na katangian.

Sa pangkalahatan, ang deployment process ay may sumusunod na istraktura:

1.Ang cyber Congress ang nagtataglay ng Game of Links
2.Ang pamayanan ay nakikilahok sa Game of Links
3. Ang pamayanan ay nagpapatunay at nagmumungkahi ng isang bloke ng Genesis na may mga resulta mula sa Game of Links
4.Ang cyber Congress ay nagdedeploy ng mga kontrata para sa cyber Foundation at cyber Auction
5.Ang pamayanan ay lumahok sa cyber Auction pagkatapos ng Genesis. Ang mga donors stake [THC](#thc) token upang makakuha ng mga token ng [CYB](#cyb)
6.Ang cyber Congress ay patuloy na namamahagi ng mga token ng CYB sa panahon ng cyber Auction
7. Sinusunog ng cyber Congress ang natitirang mga token ng [CYB](#cyb) at [THC](#thc) token at ito'y ibabalita sa pagtatapos ng paunang proseso ng pamamahagi

Nabubuhay ang cyber Congress sa Ethereum bilang isang [Aragon DAO](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330). Nagpapatakbo din ito ng [2-of-3 multisig in Cyber network](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8. Binuo ng cyber Congress  ang cyber protocol. Sa loob ng konteksto ng [cyber](#cyber-protocol), ang Congress ay may 2 tungkulin:

1. Upang mag-deploy at magsagawa ng paunang programa sa pamamahagi, na imposible maging awtomatiko. Dahil walang mapagkakatiwalaang imprastraktura para sa pagpapalit ng mensahe sa pagitan ng ETH at ATOM, ipinakilala ng cyber Congress ang isang punto ng pagkabigo sa paunang proseso ng pamamahagi. Napagpasyahan naming ipadala ang mga token ng [CYB](#cyb) sa mga staker ng [THC](#thc) dahil sa palagay namin na ngayon ang tamang oras upang ilunsad ang network na nilikha namin. Naniniwala rin kami na ang ongoing na auction ay mahalaga para sa paunang proseso ng pamamahagi. Kung ang cyber Congress ay hindi naghahatid ng mga obligasyon nito sa mga tuntunin ng pamamahagi dahil sa anumang posibleng mga kadahilanan, inaasahan namin na ang komunidad ay makakakuha ng network at ipamahagi ang mga token ng CYB tulad ng ipinangako. Inaasahan, ang bawat operasyon ay dinisenyo nang matibay at hayag. Ang lahat ng mga operasyon ay isasagawa gamit ang isang espesyal na [layunin 2-of-3 multisig account sa Cyber network](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j).

2. Suportahan ang paglaki ng [cyber](#cyber-protocol) protocol hanggang sa ang pamayanan ang pumalit  pagbuo sa anyo ng cyber ~ Foundation. Ang mga donasyon sa mga ATOM sa panahon ng Game of Link ay ibinahagi sa cyber ~ [cyber\~Congress Cosmos 2-of-3 multisig](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a). Ang lahat ng mga donasyong ATOM na naka-ruta sa cyber Congress multisig ay magiging pag-aari nito. Ang papel ng donasyon ng ATOM ay ang sumusunod: salamat sa ATOM nais naming ma-secure ang isang pangako para sa cyber Congress sa pagbuo ng parehong Cosmos at Cyber ecosystem. Pinahihintulutan ng mga donasyon ng ATOM ang cyber Congress na gumamit ng mga gantimpala ng staking at maabot ang isang napapanatiling daloy, para sa patuloy na pagpopondo ng cyber protocol nang walang pangangailangan na ibagsak ang mga token ng [CYB](#cyb) o ATOM.

## CYB

Ang mga sistema ng proof-of-stake ay hindi makakatulong sa paunang pamamahagi. Naniniwala kami na kung ang paunang pamamahagi ay idinisenyo nang may layunin, mabisang enerhiya, praktikal at malinaw, samakatuwid maa-access, ang unang [knowledge graph](#knowledge-graph) ay makakakuha ng kalidad at laki.

Ang genesis block ng cyber protocol ay naglalaman ng 1 000 000 000 000 000 CYB (isang petacyb o 1 PCYB) na mga token na pinaghiwa-hiwalay katulad ng sumusunod:

- 750 000 000 000 000 CYB tokens para sa mga nagtutuon ng [THC](#thc) tokens hanggang sa katapusan ng cyber Auction (mga kalahok ng cyber Congress, Game of Thrones sa ETH at cyber Auction)
- 150 000 000 000 000 CYB token para sa mga kalahok ng Game of Links
- 100 000 000 000 000 CYB token bilang isang regalo para sa mga pamayanan ng Ethereum, Cosmos at Urbit

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/CYB.svg" />
</p>

Matapos ang Genesis, ang mga token ng CYB ay maaari lamang malikha ng mga bayani batay sa mga parameter ng staking at slashing. Ang pangunahing pinagkasunduan ay ang mga bagong nilikha na mga token ng CYB ay nasa pagtatapon ng mga stakeholder.

Sa kasalukuyan ay walang ganoong bagay tulad ng isang maximum amount ng mga token ng CYB. Ito ay dahil sa patuloy na inflation na ibinayad sa mga bayani ng network. Ang CYB token ay ipinatupad gamit ang uint64, kaya ang paglikha ng karagdagang mga token ng CYB ay ginagawang makabuluhang mas mahal upang makalkula ang mga pagbabago at ranggo ng estado. Inaasahan namin para sa isang habang buhay na monetary strategy na maitatag ng sistema ng pamamahala pagkatapos ng kumpletong paunang pamamahagi ng mga token ng CYB at ang pag-activate ng pag-andar ng smart contracts. Ang mga panimulang parameter ng implasyon ay matutukoy sa pamamagitan ng pamamahala sa panahon ng Game of Links.

## THC

Ang layunin ng paglikha ng isang kahalili sa isang istraktura na tulad ng [Google-like](https://google.com) ay nangangailangan ng pambihirang pagsisikap mula sa iba't ibang mga grupo. Samakatuwid, nagpasya kaming mag-set up ng cyber Foundation bilang pondo, na pinamamahalaan sa pamamagitan ng isang desentralisadong engine tulad ng isang Aragon DAO. Sinisingil ito sa ETH at pinamamahalaan ng mga ahente na lumahok sa paunang pamamahagi. Ang pamamaraang ito ay magpapahintulot sa pangangalaga mula sa labis na paglalaglag ng merkado ng token ng katutubong platform - [CYB](#cyb) sa loob ng mga unang taon ng kanyang trabaho, at sa gayon, tinitiyak ang matatag na pag-unlad. Bilang karagdagan, pinapayagan nitong pag-iba-ibahin ang batayan ng platform at pahabain ang protocol sa iba pang mga consensus computing architectures, nararapat na lumitaw ang ganitong pangangailangan.

Habang pinipili ang token para sa mga donasyon, susundin natin ang tatlong pangunahing pamantayan: ang token ay dapat na (1) isa sa pinaka likido, (2) pinakapangako, kaya ang isang pamayanan ay makakatipid ng isang solidong investment bag upang maging mapagkumpitensya kahit na kung ihahambing sa naturang mga higante tulad ng [Google](https://google.com), at (3) may kakayahang teknikal na magsagawa ng auction at isang nagreresultang organisasyon, nang hindi umaasa sa anumang ikatlong partido. Ang nag-iisang sistema na tumutugma sa mga pamantayang ito ay ang Ethereum, samakatuwid, ang pangunahing token ng mga donasyon ay ETH.

Bago ang Genesis cyberFoundation ay nai-minted ang 750 000 000 000 000 THC (pitong daang limampu't terathc) na pinaghiwa-hiwalay katuad ng sumusunod:

- 600 000 000 000 000 THC tokens are allocated to the cyber\~Auction contract
- 150 000 000 000 000 THC tokens are allocated to the cyber\~Congress contract

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/THC.svg" />
</p>

Ang lahat ng mga desisyon ng cyber Foundation ay isasagawa batay sa mga resulta ng mga boto sa THC. Ang mga sumusunod na mga parameter ay ilalapat:

- Support: 51\%
- Quorum: 51\%
- Vote duration: 500 hours

## Gift

Nais naming bigyan ang kakayahang suriin ang iminungkahing diskarte sa maraming mga ahente hangga't maaari. Ngunit, nang walang pagdaragdag ng pagiging kumplikado tulad ng KYC at / o captcha. Iyon ang dahilan kung bakit pinili namin ang regalong 8% ng mga token ng [CYB](#cyb) sa Genesis para sa Ethereum, 1% sa Cosmos, at 1% sa mga komunidad ng Urbit. Ang mga sumusunod na patakaran ay inilalapat upang makalikha ang Genesis:

- Ang bawat account sa loob ng network ng pundasyon ng Ethereum, na may hindi bababa sa 1 papalabas na transaksyon na hindi isang kontrata, at may hawak na> 0.001 ETH sa block 8080808
- Ang bawat non-zero account sa loob ng Cosmos hub-3 sa block 2000000

- Ang bawat account na may hawak na galaxies (30%), stars (30%), o mga planeta (40%) at sa block 10677601 ayon sa bilang ng mga bagay

Ang pangunahing layunin ng regalong ito ay para sa bawat account sa Genesis upang makagawa ng hindi bababa sa 1 [cyberlink](#cyberlinks) sa loob ng 24 na oras habang ang network ay unloaded. Ito ang dahilan kung bakit nagpasya kaming gawing mas makurba nang kaunti pa ang distribusyon, at radikal na baguhin ito sa isang kuwadradong kurba. Samakatuwid, ipinamamahagi namin ang mga token ng [CYB](#cyb) na proporsyonal sa square root ng bawat balanse ng account sa panahon ng mga snapshot. Dahil ang isang disenyo ng kuwadratik ay napakadaling laruin, kinakalkula namin ang halaga ng ipinamamahaging mga token ng [CYB](#cyb) para sa iminungkahing mga bloke bago ang katotohanang ito ay makikilala sa publiko. Hindi namin inilalapat ang patakaran ng quadratic sa mga dayuhan ng Urbit.

## Game of Links

Isang laro para sa mga Cosmos hodler sa ATOM. Ang mga kalahok ay nagbibigay ng ATOM kapalit ng CYB. Ang mas maraming ATOM na naibigay, mas mataas ang presyo ng CYB. Ang laro ay nagsisimula mula sa 1 ATOM bawat 1 GCYB. Ang laro ay natatapos kapag ang alinman sa 146 days ay lumipas mula pa sa simula ng mga donasyon ng Takeoff, o kung ang presyo ay tumaas ng 5x mula sa panimulang presyo. Ang presyo ng CYB sa panahon ng Takeoff ay tinukoy ng mga sumusunod na function:

A game for Cosmos hodlers in ATOM. Participants donate ATOM in exchange for CYB. The more ATOM is donated, the higher the price of CYB. The game starts from 1 ATOM per 1 GCYB. The game is over when either 146 days have passed since the beginning of the Takeoff donations, or if the price has increased 5x from the starting price. The price of [CYB](#cyb) during the Takeoff is defined by the following function:

f(c) = 40 * c + 1000 

kung saan ang f (c) ay presyo ng TCYB sa ATOM, ang c ay halaga ng mga token ng TCYB na nanalo sa Takeoff.

Ang pangunahing ideya ay: ang mas mahusay na pag-ikot ng Takeoff donation round, mas maraming payout ang matatanggap ng mga kalahok sa mga disiplina. Ang 100 [TCYB](#cyb) ay inilalaan sa mga kalahok ng mga donasyon ng Takeoff at 50 [TCYB](#cyb) ang inilalaan para sa mga kalahok ng disiplina ng Game of Links. Ang lahat ng mga token ng CYB na nananatili mula sa Takeoff, ay inilalaan sa community  pool sa pagtatapos ng laro. Lahat ng mga token ng CYB na naiwan mula sa mga disiplina ay inilalaan sa cyber ~ Congress. Bilang karagdagan sa mga token ng CYB, ang Game of Link ay naglalaan ng pagsubok EUL token sa lahat ng mga donor ng Takeoff para sa pangwakas. Ang isang [detalyadong dokumento](https://cybercongress.ai/game-of-links/) ay nai-publish na may mga patakaran at probisyon para sa laro.

## Cyber\~Auction

Isang laro para sa Ethereum hodler sa ETH. Ang mga kalahok ay nagbibigay ng ETH kapalit ng THC. Ang mas maraming ETH ay naibigay, mas mataas ang presyo ng THC. Ang laro ay nagsisimula mula sa presyo na kung saan ay 5x closing price ng Takeoff sa ETH. Ang laro ay natapos kapag ang alinman sa 888 days ay lumipas mula nang umpisa o kung ang presyo ay tumaas ng 5x mula sa panimulang presyo. Sa panahong ito ang mga token ng CYB ay patuloy na ipinamamahagi ng cyber Congress, batay sa mga vested na token ng THC hanggang sa katapusan ng auction. Nagbibigay ang mga pinalalakas na token ng [THC](#thc) ng kakayahang makatanggap ng mga token ng [CYB](#cyb), at mga kapangyarihan sa pagboto sa loob ng cyber Foundation. Ang presyo ng [THC](#thc) sa panahon ng Cyber  ~Auction ay tinukoy ng mga sumusunod na function:

g(t)= 1/30 * t * p + 5 * p

kung saan ang g (t) ay presyo ng TTHC sa ETH, t ay halaga ng mga token ng TTHC noong cyber ~ Auction, p ang nagreresultang presyo ng Takeoff para sa isang CYB na na-convert sa ETH sa pagsasara ng sandali.

Ang panimulang presyo ay idinisenyo upang bigyan ang mga kalahok ng Takeoff ng 5x premium para sa kanilang panganib na mamuhunan sa mga imprastraktura ng hardware at software bago ang Genesis. Nagbibigay ang cyber Auction ng mga makabuluhang insentibo para sa mga unang kalahok. Matapos ang pagtatapos ng pamamahagi, mai-unlock ng mga kalahok ang kanilang mga token ng [THC](#thc) at gamitin ang mga ito ayon sa nais nila, e.i. transfer, exchange, atbp. Bilang isang resulta ng auction, ang komunidad ay magkakaroon ng access sa lahat ng naibigay na ETH sa loob ng samahan ng Aragon. Matapos ang pagtatapos ng cyber Auction, ang lahat ng natitirang [THC](#thc) sa cyber Auction contract ay dapat na masunog. Ang mga sumusunod na patakaran ay nalalapat sa mga token ng CYB sa ilalim ng [multisig](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j): para sa pamamahagi:

- Ang cyber Congress ay hindi iginawad ang stake, at bilang isang resulta, mananatili itong isang passive stake hanggang sa maipamahagi ito
- Pagkatapos ng cyber Auction, ang lahat ng natitirang mga token ng [CYB](#cyb) ay dapat na masunog 

## Apps

Ipinapalagay namin na ang iminungkahing algorithm ay hindi ginagarantiyahan ang mataas na kalidad na kaalaman sa pamamagitan ng default. Katulad ng isang bagong panganak, kailangang makakuha ng kaalaman upang umunlad pa. Nagbibigay ang protocol mismo ng isang simpleng tool: ang kakayahang lumikha ng isang [cyberlinks](#cyberlinks) na may stake agents sa pagitan ng dalawang content addresses. 

Ang pagtatasa ng pangunahing semantiko, behavioural factors, hindi kilalang data tungkol sa mga interes ng mga ahente at iba pang mga tool na matukoy ang kalidad ng paghahanap, maaaring makamit sa pamamagitan ng smart contracts at ng off-chain applications, tulad ng: [web3 browsers](#browzers), desentralisadong mga social network at mga platform ng nilalaman . Naniniwala kami, na ito ay para sa interes ng komunidad at mga masters na bumuo ng paunang [knowledge graph](#knowledge-graph) at mapanatili ito. Samakatuwid, para sa graph, upang magbigay ng mga pinaka-relevant search results.

Karaniwan, nakikilala namin ang tatlong uri ng mga aplikasyon para sa [knowledge graphs](#knowledge-graph):

- Consensus apps. Maaaring tumakbo sa pagpapasya ng [consensus computer](#the-notion-of-a-consensus-computer) sa pamamagitan ng pagdaragdag ng mga intelektwal na kakayahan
- On-chain apps. Maaaring patakbuhin ng [consensus computer](#the-notion-of-a-consensus-computer) kapalit ng gas
- Off-chain apps. Maaaring maipatupad sa pamamagitan ng paggamit ng [knowledge graph](#knowledge-graph) bilang isang input sa loob ng isang kapaligiran sa pagpapatupad

Ang sumusunod, maiisip, listahan ng mga app ay nagkukumpuni sa nabanggit na mga kategorya:

Web3 browsers. Sa katotohanan, ang browser at search ay hindi mapaghihiwalay. Mahirap isipin ang paglitaw ng isang full-blown web3 browser na batay sa web2 search. Sa kasalukuyan, maraming mga pagsisikap para sa pagbuo ng mga browser sa paligid ng mga blockchain at ipinamamahagi na tech. Kabilang sa mga ito ay Beaker, Mist, Brave, at Metamask. Lahat ng mga ito ay nagdurusa sa pagsubok na i-embed ang web2 sa web3. Ang aming diskarte ay medyo naiiba. Itinuturing namin ang web2 bilang isang hindi ligtas na subset para sa web3. Kaya nakabuo kami ng isang pang-eksperimentong browser ng web3, [cyber](#cyber-protocol), ipinakita ang diskarte sa cyber sa pagsagot sa mga query nang mas mahusay at mas mabilis na maihatid ang nilalaman.

Social networks. Ang mga social network ay hindi gaanong misteryoso. Sa anumang nilalaman ng social network ay ang hari. Samakatuwid, ang mapagkakatiwalaang pagraranggo ay ang pangunahing pagbuo ng bloke ng anumang social network. Ang lahat ng mga uri ng mga social network ay madaling maitayo sa tuktok ng isang [knowledge graph](#knowledge-graph). Ang cyber ay maaari ring lumikha ng mga social network batay sa kaugnayan sa pagitan ng mga users, na hindi makamit ang kasalukuyang network.

Programmable semantics. Sa kasalukuyan, ang pinakapopular na mga keyword sa napakalaking semantiko ng core ng [Google](https://google.com) ay mga keyword ng mga app tulad ng:[Youtube](https://youtube.com), [Facebook](https://facebook.com), [GitHub](https://github.com), atbp. Gayunpaman, ang mga nag-develop ng mga matagumpay na apps ay may limitadong kakayahang ipaliwanag sa [Google](https://google.com) kung paano istraktura ang mga resulta ng paghahanap sa isang mas mahusay na paraan. Ang diskarte ng [cyber](#cyber-protocol) ay nagbibigay ng kapangyarihan na ito pabalik sa mga developer. Nagagawa ng target ng mga nag-develop ang mga tukoy na semantics cores at i-index ang kanilang mga app ayon sa gusto nila.

Search actions. Ang iminungkahing disenyo ay nagbibigay-daan sa katutubong suporta para sa mga blockchain (at parehong tangle) na mga aktibidad na nauugnay sa aktibidad. Ito ay walang saysay sa disenyo ng mga application na (1) pagmamay-ari ng mga tagalikha, (2) ay lumilitaw nang tama sa mga resulta ng paghahanap at (3) pinapayagan ang isang maaaring ilipat, na may (4) magagawang katangian ng isang pag-convert para sa isang query sa paghahanap. Ang e-Commerce ay hindi naging madali para sa lahat.

Off-line search. Ginagawang posible ng IPFS na madaling makuha ang isang dokumento mula sa isang kapaligiran na walang koneksyon sa internet. Ang [go-cyber](https://github.com/cybercongress/go-cyber) mismo ay maaaring maipamahagi sa pamamagitan ng paggamit ng IPFS. Lumilikha ito ng posibilidad para sa, lahat, off-line search! 

Command tools. Ang mga tool sa command-line ay maaaring umasa sa mga nauugnay at nakabalangkas na mga sagot mula sa isang search engine. Kung tutuusin, ang sumusunod na tool sa CLI ay posibleng maipatupad:

````bash
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
````

Ang Search tools, mula sa loob ng CLI ay hindi maiiwasang lumikha ng isang lubos na mapagkumpitensya na merkado ng isang nakatuon na semantiko na core para sa mga robot.

Autonomous robots. Pinapayagan ng teknolohiyang blockchain ang paglikha ng mga devices na maaaring pamahalaan ang mga digital assets sa kanilang sarili.

`If a robot can store, earn, spend and invest - they can do everything you can do`

Ang kailangan ay simple, ngunit isang malakas na tool ng katotohanan ng estado na may kakayahang makahanap ng mga partikular na bagay. Ang [go-cyber](https://github.com/cybercongress/go-cyber) ay nag-aalok ng isang minimalistic, ngunit isang patuloy na pagpapabuti ng sarili na mapagkukunan ng data, na nagbibigay ng mga kinakailangang tool para sa mga pang-ekonomiyang makatwiran na mga robot. Ayon sa [nangungunang-10,000 English words](https://github.com/first20hours/google-10000-english) ang pinakapopular na salita sa wikang Ingles ay ang tinukoy na artikulong 'the', na nangangahulugang isang pointer sa isang partikular na item. Ang katotohanang ito ay maaaring ipaliwanag bilang mga sumusunod: ang mga partikular na item ay pinakamahalaga sa amin. Samakatuwid, ang likas na katangian sa amin ay upang makahanap ng mga natatanging bagay. Samakatuwid, ang pag-unawa sa mga natatanging bagay ay mahalaga din para sa mga robot.

Language convergence. Hindi dapat pakialam ng isang programista ang wika na gagamitin ng isang ahente. Hindi natin kailangang malaman kung aling wika ang isinasagawa ng ahente ng kanilang paghahanap. Ang buong spectrum ng UTF-8 ay gumagana. Ang semantic core ay bukas, kaya ang kumpetisyon para sa pagsagot sa mga query ay maaaring maipamahagi sa iba't ibang mga lugar na partikular sa domain. Kasama ang mga semantic cores para sa iba't ibang mga wika. Ang pinag-isang diskarte na ito ay lumilikha ng isang pagkakataon para sa cyber\~Bahasa. Mula pa sa madaling araw ng Internet, napapansin natin ang isang proseso ng mabilis na pagtaguyod ng wika. Ginagamit namin ang tunay na pandaigdigang mga salita sa buong planeta, nang nakapag-iisa ng nasyonalidad, wika, lahi, pangalan o koneksyon sa Internet. Ang pangarap ng isang tunay na pandaigdigang wika ay mahirap i-deploy sapagkat mahirap sumang-ayon sa kung ano ang ibig sabihin. Gayunpaman, mayroon kaming mga tool upang matupad ang pangarap na ito. Hindi mahirap mahulaan na mas maikli ang isang salita, mas malakas ang cyber~Rank nito. Ang pandaigdigan, magagamit na pampublikong listahan ng mga simbolo, salita, at parirala na pinagsunod-sunod ayon sa cyber\~Rank na may kaukulang link na ibinigay ng [go-cyber](https://github.com/cybercongress/go-cyber) ay maaaring maging pundasyon para sa paglitaw ng isang tunay na pandaigdigang wika na matatanggap ng lahat. Ang mga [kamakailang pang-agham](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1) na pagsulong sa pagsasalin ng makina ay nakamamangha ngunit walang kabuluhan sa mga nais mag-apply ng mga ito nang walang isang modelo na sinanay na Google. Ang iminungkahing cyber\~Rank ay nag-aalok ng hustong ito.

Self Prediction. Ang [consensus computer](#the-notion-of-a-consensus-computer) ay maaaring magpatuloy na bumuo ng [knowledge graph](#knowledge-graph) sa sarili nitong hinuhulaan ang pagkakaroon ng mga [cyberlinks](#cyberlinks) at inilalapat ang mga hula sa estado nito. Samakatuwid, ang [consensus computer](#the-notion-of-a-consensus-computer) ay maaaring lumahok sa pang-ekonomiyang pinagsama ng [cyber](#cyber-protocol)protocol.

Universal oracle. Ang [consensus computer](#the-notion-of-a-consensus-computer) ay maaaring mag-imbak ng mga pinaka may-katuturang data sa isang key-value storage. Kung saan ang susi ay isang CID at ang mga halaga ay mga byte ng aktwal na nilalaman. Ito ay maaaring makamit sa pamamagitan ng paggawa ng isang desisyon sa bawat pag-ikot, patungkol sa kung saan pinapahalagahan ng CID ang mga ahente na nais mag-aplay at kung anong halaga ang nais nilang ilapat. Batay sa utility measure ng mga content address sa loob ng [knowledge graph](#knowledge-graph). Upang makalkula ang panukalang magamit, sinusuri ng mga bayani ang pagkakaroon at ang laki ng nilalaman para sa mga nangungunang ranggo ng nilalaman sa loob ng [knowledge graph](#knowledge-graph) kung gayon, ang bigat sa laki ng mga CID at ranggo nito. Ang lumilitaw na imbakan ng key-value storage ay magagamit upang magsulat para sa [consensus computer](#the-notion-of-a-consensus-computer)  lamang at hindi para sa mga ahente. Ngunit, maaaring magamit ang mga halaga sa mga programa.

Location-aware search. Posible na bumuo ng mga [cyberlinks](#cyberlinks) with [Proof-of-Location](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) na may Proof-of-Location batay sa kamangha-manghang umiiral na mga protocol tulad ng [Foam](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG). Dahil dito, ang isang paghahanap na nakabatay sa lokasyon ay maaari ding maging kapani-paniwala, kung ang mga ahente ng web3 ay mag-mine ng triangulations at maglakip ng [proof-of-location](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) para sa bawat linked chain.

Prediction markets sa link relevance. Maaari naming ipatupad ang ideyang ito gamit ang pagraranggo ng [knowledge graph](#knowledge-graph) batay sa isang hula sa merkado sa kaugnayan ng link. Ang isang app na nagpapahintulot sa pagtaya sa kaugnayan ng link, ay maaaring maging isang natatanging mapagkukunan ng katotohanan para sa direksyon ng mga term, pati na rin, mag-udyok sa mga ahente na magsumite ng higit pang mga link.

Private cyberlinks. Ang pagkapribado ay napakahalaga. Habang nakatuon kami sa privacy, ang pagkamit ng pagpapatupad ng mga pribadong [cyberlinks](#cyberlinks) ay hindi magagawa para sa aming koponan hanggang sa Genesis. Samakatuwid, nasa komunidad na magtrabaho sa mga programa ng WASM, maaaring maisagawa sa tuktok ng protocol. Ang problema ay ang pagkalkula ng cyber ~ Rank, batay sa mga [cyberlinks](#cyberlinks) na isinumite ng isang web3-masters nang hindi inihayag ang alinman: ang kanilang nakaraang kahilingan o ang public keys. Ang mga patunay na kaalaman sa Zero, sa pangkalahatan, ay napakamahal. Naniniwala kami na ang privacy ng paghahanap ay dapat na isang tampok sa pamamagitan ng disenyo, ngunit hindi kami sigurado na alam namin kung paano ipatupad ito sa yugtong ito. Ang [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk) tulad ng recursive Snarks at [MimbleWimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg) na mga konstraksyon, sa teorya, ay maaaring malutas ang bahagi ng privacy concern. Ngunit, ang mga ito ay bago, hindi nasaksihan at gayon pa man, ay magiging mas mahal tungkol sa mga pagkalkula kaysa sa kanilang transparent na alternatibo.

Ito ay tiyak na hindi ang labis na listahan ng lahat ng mga posibleng aplikasyon, ngunit ito'y napaka-exciting.

## Conclusion

Natukoy namin at ipinatupad ang isang protocol para sa magagaling na komunikasyon, sa pagitan ng consensus computer sa kaugnayan. Ang protocol ay batay sa simpleng ideya ng knowledge graph, na nalilikha ng mga ahente sa pamamagitan ng paggamit ng mga cyberlink. Ang mga Cyberlink ay pinoproseso ng consensus computer gamit ang konsepto ng relevance machine. Ang cyber consensus computer ay batay sa CIDv0 / CIDv1 at gumagamit ng go-IPFS at Cosmos-SDK bilang isang pundasyon. Nagbibigay ang IPFS ng mga makabuluhang benepisyo sa pagkonsumo ng mapagkukunan. Ang CID bilang pangunahing mga bagay ay matatag sa kanilang pagiging simple. Para sa bawat CID, ang cyber ~ Rank ay kinukumpara ng consensus computer  nang walang punto ng pagkabigo. Ang Cyber   ~ Rank ay isang CYB token na may bigat na PageRank, na may proteksyon sa ekonomiya mula sa mga atake ng sybil at makasariling pagboto. Ang bawat pag-ikot ng Merkle root ng ranggo at graph trees ay nai-publish. Dahil dito, ang bawat computer ay maaaring patunayan sa anumang iba pang computer ang kaugnayan ng halaga para sa isang naibigay na CID. Ang resistensya ng Sybil ay batay sa paglilimita sa bandwidth. Ang naka-embed na kakayahan upang maisagawa ang mga programa ay nag-aalok ng inspiring applications. Ang panimulang pangunahing layunin ay ang pag-index ng mga sistema ng mga address ng nilalaman ng peer-to-peer, alinman sa walang bilang, tulad ng: IPFS, Swarm, Sia, Git, BitTorrent, o masigasig, tulad ng: Bitcoin, Ethereum at iba pang mga blockchain at tangles. Ang iminungkahing semantika ng cyberlinking ay nag-aalok ng isang matatag na mekanismo para sa paghula ng makabuluhang ugnayan sa pagitan ng mga bagay ng mismong consensus computer mismo. Ang source code ng relevance machine ay open-source. Ang bawat piraso ng data na naipon ng consensus computer ay magagamit para sa sinuman kung ang isa ay may mga mapagkukunan upang maproseso ito. Ang pagganap ng iminungkahing pagpapatupad ng software ay sapat na para sa walang maayos na pakikipag-ugnayan. Ang kakayahang sumukat ng iminungkahing pagpapatupad ay sapat na upang mai-index ang lahat ng mga napatunayang data na umiiral ngayon at maaaring ihatid ito sa milyon-milyong mga ahente ng Great Web. Ang blockchain ay pinamamahalaan ng isang Superintelligence, na gumagana sa ilalim ng Tendermint consensus algorithm na may pamantayang module ng pamamahala. Kahit na ang system ay nagbibigay ng kinakailangang utility upang mag-alok ng isang kahalili para sa isang conventional na search engine, hindi ito limitado lamang sa kasong ito. Ang system ay mapapalawak para sa maraming mga application at ginagawang posible upang mag-disenyo ng matipid, self-owned robots, na maaaring awtomatikong maunawaan ang mga bagay sa kanilang paligid.

## Mga Sanggunian

1. [Scholarly context adrift](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN)
2. [Brand-new stack](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw)
3. [Search engines information retrieval in practice](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6)
4. [Motivating game for adversarial example research](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9)
5. [An idea of a decentralized search](https://ipfs.io/ipfs/QmXNoGTWLQrcFRb66oS4HafpP1vcLKbVkJrQm4DVvihuoq)
6. [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps)
7. [DAT](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR)
8. [go-cyber](https://github.com/cybercongress/go-cyber)
9. [cosmos-sdk](https://github.com/cosmos/cosmos-sdk)
10. [CIDv1](https://github.com/multiformats/cid#cidv1)
11. [cyber.page](http://cyber.page)
12. [DURA](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md)
13. [Colony](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj)
14. [Truebit](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)
15. [Thermodynamics of predictions](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb)
16. [PageRank](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw)
17. [RFC-6962](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG)
18. [IBC protocol](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk)
19. [Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ)
20. [Comparison of web3 browsers](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md)
21. [Cyb](https://cyb.ai)
22. [SpringRank](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC)
23. [Run validator in cyber protocol](https://cybercongress.ai/docs/go-cyber/run_validator/)
24. [Top 10000 english words](https://github.com/first20hours/google-10000-english)
25. [Multilingual neural machine translation](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1)
26. [Foam](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG)
27. [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk)
28. [Mimblewimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg)
29. [Tezos](https://ipfs.io/ipfs/QmdSQ1AGTizWjSRaVLJ8Bw9j1xi6CGLptNUcUodBwCkKNS)
30. [Software 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35)
31. [Proof-of-history](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs)
32. [IPLD](https://github.com/ipld)
33. [cyber\~Congress organization](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330/)
34. [cyber~Congress in Cyber](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8)
35. [cyber~Congress in Cosmos](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a)
36. [multisig for CYB distribution](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j)
37. [.cyber](https://github.com/cybercongress/dot-cyber)

## Acknowledgements

1. @hleb-albau
2. @arturalbov
3. @jaekwon
4. @ebuchman
5. @npopeka
6. @belya
7. @serejandmyself


