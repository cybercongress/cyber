# cyber: Computação do conhecimento da Grande Web

![img](https://github.com/serejandmyself/cyber/raw/master/images/graph.png)

## Resumo

Um computador de consenso permite a computação de respostas comprovadamente relevantes sem quaisquer intermediários de blackbox opinados, como Google, Amazon ou Facebook. As redes de comunicação par-a-par apátridas, como as IPFS e os computadores de consenso imponentes, como o Ethereum, podem fornecer apenas uma parte da solução necessária para obter respostas semelhantes. No entanto, existem pelo menos 3 problemas associados às referidas implementações. a A natureza subjetiva de relevância. (B) dificuldade em escalonar computadores de consenso para gráficos de conhecimento sofisticados. c A falta de qualidade entre esses gráficos de conhecimento. São propensos a vários ataques à superfície, como ataques de síbil, e o comportamento egoísta dos agentes que interagem. Neste documento, definimos um protocolo para computação de consenso comprovada de relevância, entre objetos IPFS, que se baseia no consenso tendermint do cyber~Rank, que é calculado usando GPUs em consenso. Como o consenso de prova de participação não ajuda na distribuição inicial, delineamos o design para jogos de distribuição ecológica e eficiente. Acreditamos que uma arquitetura minimalista do protocolo é fundamental para a formação de uma rede de computadores de conhecimento específicos de domínio. Como resultado do nosso trabalho, algumas aplicações que nunca existiram antes, surgirão. Expandimos este documento com a nossa visão de possíveis funcionalidades e potenciais aplicações.

## A Grande Teia

Os protocolos originais da Internet, tais como: TCP/IP, DNS, URL e HTTP/S trouxeram a web para um ponto velho, onde está localizada a partir de agora. Tendo em conta todos os benefícios que estes protocolos produziram para o desenvolvimento inicial da web, juntamente com eles, trouxeram obstáculos significativos à mesa. Globalidade, sendo uma propriedade vital da web está sob uma ameaça real desde a sua criação. A velocidade da ligação continua a degradar-se enquanto a própria rede continua a crescer devido a intervenções governamentais ubíquas. Este último causa preocupações de privacidade como uma ameaça existencial aos direitos humanos.

Uma propriedade não evidente no início torna-se importante com o uso diário da Internet: a capacidade de trocar ligações permanentes, assim, [não vai quebrar após o tempo tinha passado](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN). A confiança na arquitetura de um de cada vez o ISP permite que os governos censuram efetivamente os pacotes. Esta é a última gota na tradicional web-stack para cada engenheiro que está preocupado com o futuro das nossas crianças.

Outras propriedades, embora possam não ser tão críticas, são muito desejáveis: ligação offline e em tempo real. O utilizador médio da Internet, embora offline, ainda deve ter a capacidade de continuar a trabalhar com o estado que já detém. Após adquirirem uma ligação, devem poder sincronizar-se com o Estado global e continuar a verificar a validade do seu próprio Estado em tempo real. Atualmente, estas propriedades são oferecidas ao nível da aplicação. Acreditamos que estas propriedades devem ser integradas em protocolos de nível inferior.

O aparecimento de [uma nova web-stack](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw) cria uma oportunidade para uma Internet superior. A comunidade chama-lhe web3. Chamamos-lhe a Grande Teia. Consideramos que vários tipos de comunicações de baixo nível devem ser imutáveis e não devem ser alterados durante décadas, por exemplo, ligações de conteúdo imutáveis. Parecem muito promissores na remoção dos problemas da pilha de protocolos convencionais. Eles adicionam maior velocidade e fornecem uma ligação mais acessível à nova web. No entanto, como acontece com qualquer conceito que ofereça algo único - surgem novos problemas. Uma dessas preocupações é a procura de propósito geral. Os motores de busca de uso geral existentes são bases de dados restritivas e centralizadas em que todos são obrigados a confiar. Estes motores de busca foram concebidos principalmente para arquiteturas de servidores de clientes, com base em TCP/IP, DNS, URL e HTTP/S. A Great Web cria um desafio e uma oportunidade para um motor de busca que se baseia em tecnologias emergentes e é projetado especificamente para estes fins. Surpreendentemente, a arquitetura blockchain sem permissão permite construir um motor de pesquisa de propósito geral de uma forma inacessível às arquiteturas anteriores.

## Sobre o problema dos exemplos contraditórios

[A arquitetura atual dos motores de busca](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6) é um sistema onde alguma entidade processa toda a merda. Esta abordagem sofre de um desafio e de um problema distinto, que ainda tem de ser resolvido, mesmo pelos brilhantes cientistas do Google: [o problema dos exemplos adversos](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9). O problema que o Google reconhece é que é bastante difícil raciocinar algoritmos se uma determinada amostra é ou não adversária. Isto é imprudente de como a tecnologia educativa em si é incrível. Uma abordagem criptoeconômica pode mudar os beneficiários no jogo. Consequentemente, esta abordagem removerá eficazmente possíveis vetores de ataque de síbil. Elimina a necessidade de rastejar e de extração de um único modelo de código rígido por uma única entidade. Em vez disso, dá este poder a todo o mundo. Um modelo de aprendizagem resistente a sybil, gerado por agentes, provavelmente levará a ordens de magnitude mais preditivas.

## Cyber  protocolo

No seu cerne, o protocolo é muito minimalista e pode ser expresso com os seguintes passos:

1. Calcular a génese do protocolo cibernético com base na distribuição definida
2. Definir o estado do [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
3. Recolher transações usando um [consensus computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
4. Verifique a validade das assinaturas
5. Verifique o [limite de largura de banda](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
6. Verifique a validade dos CIDs
7. Se as assinaturas, o limite de largura de banda e os CIDs forem todos válidos, aplicar [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) e transações
8. Calcular os vânulos de [cyber~Rank](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberrank) para cada rodada para os CIDs no [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)

O resto deste documento discute a lógica e os pormenores técnicos do protocolo proposto.

## Gráfico de conhecimento

Representamos um gráfico de conhecimento como um gráfico ponderado de ligações direcionadas entre endereços de conteúdo. Aka, identificadores de conteúdo, CIDs, hashes IPFS, ou simplesmente - ligações IPFS. Neste documento, usaremos os termos acima referidos como sinónimos.

![img](https://github.com/serejandmyself/cyber/raw/master/images/knowledge-graph.png)

Os endereços de conteúdo são essencialmente links web3. Em vez de usar o pouco claro e mutável:

```
https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md
```

Usamos o objeto em si:

```
Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

Ao usar endereços de conteúdo para construir o gráfico de conhecimento que ganhamos [o tão necessário](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est) [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps) - [like](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR) superpoderes de protocolos p2p que são desejados para um motor de busca:

- rede de malha à prova de futuro
- acessibilidade interplanetária
- resistência à censura
- independência tecnológica

O nosso gráfico de conhecimento é gerado pelos mestres incríveis. Os mestres adicionam-se ao gráfico de conhecimento com a ajuda de uma única transação, uma ligação cibernética. Assim, provam a existência das suas chaves privadas para endereços de conteúdo das suas chaves públicas reveladas. Usando estes mecânicos, um [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) poderia alcançar uma diferenciação comprovada entre sujeitos e objetos num gráfico de conhecimento.

A nossa implementação de [go-cyber](https://github.com/cybercongress/go-cyber) baseia-se em [cosmos-SDK](https://github.com/cosmos/cosmos-sdk) identidades e [CIDv0/CIDv1](https://github.com/multiformats/cid#cidv0) endereços de conteúdo.

Os mestres formam o gráfico de conhecimento aplicando [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).

## Cyberlinks

Para entender como as ligações cibernéticas funcionam, precisamos entender a diferença entre uma ligação URL (aka, uma hiperligação) e entre uma ligação IPFS. Uma ligação URL aponta para a localização do conteúdo, quer uma ligação IPFS aponte para o conteúdo em si. A diferença entre arquiteturas web baseadas em links de localização e links de conteúdo é radical e requer uma abordagem única.

Cyberlink é uma abordagem para ligar dois endereços de conteúdo, ou ligações IPFS, semântica:

```
.md syntax: [QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH](Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH)    
.dura syntax: QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH.Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

A ciberlige acima significa que a apresentação de [go-cyber](https://github.com/cybercongress/go-cyber) durante [cyberc0n](https://etherscan.io/token/0x61B81103e716B611Fff8aF5A5Dc8f37C628efb1E) está a referir-se ao livro branco do Cosmos. O conceito de cyberlinks é uma convenção em torno da semântica simples de um formato comunicacional em qualquer rede p2p:

![img](https://github.com/serejandmyself/cyber/raw/master/images/cyberlink.png)

Vemos que uma ligação cibernética representa uma ligação entre as duas ligações. Fácil de ervilhas!

Cyberlink é uma construção simples, mas uma poderosa construção semântica para construir um modelo preditivo do universo. Isto significa que o uso de ligações cibernéticas em vez de hiperligações fornece-nos as superpotências que eram inacessíveis às arquiteturas anteriores dos motores de busca de fins gerais.

Os cyberlinks podem ser estendidos, ou seja, podem formar correntes de ligação se houver dois ou mais ciberligações subsistem de um mestre, onde a segunda ligação na primeira ligação é igual à primeira ligação no segundo cyberlink:

![img](https://github.com/serejandmyself/cyber/raw/master/images/linkchain.png)

Se os agentes expandirem as ligações nativas do IPFS com algo semânticamente mais rico, por exemplo, com [dura](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md)links, em seguida, o consenso sobre as regras de execução por um programa específico pode ser alcançado numa abordagem mais natural.

O [go-cyber)](https://github.com/cybercongress/go-cyber) implementação de links cibernéticos está disponível no [.cyber](https://github.com/cybercongress/dot-cyber) app do nosso navegador web3 experimental [cyb](https://cyb.ai/), ou em [cyber.página](http://cyber.page/).

The cyberlinks submetidos por mestres são armazenados em uma árvore merkle de acordo com o [RFC-6962 padrão](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). Isto permite a authentificação para [prova de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#proof-of-relevance).

![img](https://github.com/serejandmyself/cyber/raw/master/images/graph-tree.png)

Usando ciberlinks, podemos calcular a relevância de sujeitos e objetos no [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). Mas precisamos de um [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer).

## A noção de um computador de consenso

Um computador de consenso é uma máquina de computação abstrata que emerge da interação entre agentes. Um computador de consenso tem capacidade em termos de recursos de computação fundamentais: memória e computação. Para interagir com agentes, um computador precisa de largura de banda. Um computador de consenso ideal é um computador onde:

```
the sum of all the computations and memory available to individuals`
`is equal to`
`the sum of all the verified computations and memory of the consensus computer
```

Sabemos que:

```
verifications of computations < (computations + verifications of computations)
```

Assim, nunca seremos capazes de alcançar um computador de consenso ideal. O teorema da PAC e o trilema de escalae adquir mais provas a esta afirmação.

![img](https://github.com/serejandmyself/cyber/raw/master/images/consensus-computer.png)

No entanto, esta teoria pode funcionar como um indicador de desempenho para um computador de consenso. Depois de 6 anos a investir em computadores de consenso, chegamos a perceber que o [Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) o consenso tem um bom equilíbrio entre a frieza necessária para a nossa tarefa e a prontidão para a sua produção. Portanto, decidimos implementar o [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) protocolo usando o consenso Tendermint, que tem configurações muito próximas para o Cosmos Hub. O [go-cyber](https://github.com/cybercongress/go-cyber) implementação é um computador de consenso tendermint de 64 bits de relevância para o espaço de cordas de 64 byte. Isto não é de longe o ideal, pelo menos como 1/146, porque temos 146 validadores que verificam os mesmos cálculos que produzem o [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

Temos de vincular a computação, o armazenamento e a oferta de largura de banda do computador de consenso a uma procura máxima de consultas. Computação e armazenamento, em caso de uma base [máquina de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) pode ser facilmente previsto com base na largura de banda. Mas a largura de banda requer um mecanismo de limitação.

## Máquina de relevância

Definimos uma máquina de relevância como uma máquina que faz a transição do estado de um [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) com base na vontade dos agentes que desejam ensinar e estudar que [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). The will is projected by every [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) um mestre faz. Quanto mais agentes perguntar o [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph), quanto mais valioso o conhecimento se torna. Com base nestas projeções, a relevância entre endereços de conteúdo pode ser calculada. A máquina de relevância permite uma construção simples para o mecanismo de pesquisa através de consultas e respostas de entrega.

Uma propriedade da máquina de relevância é crucial. Deve ter propriedades de raciocínio indutivo ou seguir o princípio blackbox:

```
The machine should be able to interfere with predictions without any knowledge about the objects,`
`except for who, when and what was cyberlinked
```

Se assumirmos que um [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) deve ter alguma informação sobre os objetos ligados, então a complexidade de tal modelo crescerá imprevisivelmente. Portanto, os elevados requisitos do computador de processamento para memória e cálculo. Graças ao conteúdo que aborda uma máquina de relevância que segue o princípio blackbox, não precisa de armazenar dados. Mas ainda pode operar eficazmente em cima dele. A dedução do significado dentro de um [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) é caro. Assim, tal design pode depender da cegueira suposição. Em vez de deduzir o significado dentro do [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer), concebemos um sistema em que a extração é incentivada. Isto é conseguido devido aos mestres que exigem [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas para expressar a sua vontade, com base na qual, a máquina de relevância pode calcular a classificação.

No centro do sistema de proteção de spam está um pressuposto de que as operações de escrita só podem ser executadas por aqueles, que têm um interesse investido no sucesso evolutivo da máquina de relevância. Cada 1% de participação efetiva dentro do [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) dá a capacidade de usar 1% da largura de banda das redes possíveis e as suas capacidades de computação. Uma regra simples impede o abuso dos agentes: um par de identificadores de conteúdo pode ser cyberlinked por um endereço apenas uma vez.

![img](https://github.com/serejandmyself/cyber/raw/master/images/algo1.png)

Existem apenas duas formas de alterar a participação efetiva (participação ativa + participação obrigacionista) de uma conta: transferências diretas de fichas e operações de caução.

[Cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) usa um modelo de largura de banda muito simples. O principal objetivo deste modelo é reduzir o crescimento diário da rede para uma determinada constante. Isto é feito para acomodar heróis (validadores) com a capacidade de prever qualquer investimento futuro em infraestruturas. Assim, aqui introduzimos 'watts' ou 'W'. Cada tipo de mensagem tem um custo W atribuído. A constante 'Unidade de Desejável', determina o desejável 'RecoveryWindow' gasto pelo valor W. O período de recuperação define a rapidez com que um mestre pode recuperar a largura de banda de 0 para a largura de banda máxima. Um mestre tem um W máximo proporcional à sua participação efetiva, determinada pela seguinte fórmula:

```
AgentMaxW = EffectiveStake * DesirableBandwidth
```

O período 'AdjustPricePeriod' resume quanto W foi gasto durante o período 'RecoveryPeriod' no último bloco. O rácio 'SpentBandwidth' / 'DesirableBandwidths' é denominado o rácio de reserva fracionária. Quando o uso da rede é baixo, o rácio de reserva fracionária ajusta o custo da mensagem para permitir que os mestres com uma participação mais baixa cometam mais transações. Quando a procura de recursos aumenta, o rácio de reserva fracionária vai > 1, consequentemente, aumentando o custo da mensagem e limitando a contagem final de tx para um período de longo prazo (a recuperação W será < então gastos W). Como ninguém usa toda a largura de banda possuída, podemos usar com segurança até 100x reservas fracionadas dentro de um período de recálculo de preços. Tais mecânicas fornecem um desconto para criar [cyberlinking](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks), assim, efetivamente maximizando a procura por ela. Pode ver que o design proposto necessita de uma procura de largura de banda completa para que a relevância se torne valiosa.

A inteligência humana é organizada de tal forma que memórias não relevantes e nenhumas importantes são esquecidas ao longo do tempo. O mesmo pode ser aplicado à máquina de relevância. A máquina de relevância pode implementar [estratégias de poda agressivas](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb), como, a poda da história da formação do [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph), ou esquecendo ligações que se tornam menos relevantes.

Como resultado, a cibermómica implementada de [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) Os tokens servem não só como mecanismos de expressão de vontade e de proteção de spam, mas também funciona como uma ferramenta de regulação da economia que pode alinhar a capacidade de processamento dos heróis e a procura de processamento no mercado. A implementação cibernética da máquina de relevância baseia-se num mecanismo muito simples, chamado: cyber~Rank.

## cyber~Rank

Ranking usando um [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) pode ser um desafio, uma vez que os computadores de consenso têm sérias restrições de recursos. Em primeiro lugar, temos de nos perguntar: por que precisamos calcular e armazenar o posto em cadeia e não seguir o mesmo caminho que [Colony](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj) ou [Truebit](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)?

Quando a classificação foi calculada dentro de um [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) um tem fácil acesso à distribuição de conteúdo de que o rank e uma maneira fácil de [construir aplicações comprovadas](https://github.com/serejandmyself/cyber/blob/master/cyber.md#apps) no topo da classificação. Por isso, decidimos seguir uma arquitetura mais cósmica. Na secção seguinte descrevemos o [prova de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#proof-of-relevance) mecanismo, que permite que a rede se dimensione com a ajuda de domínio específico [máquinas de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine). Estes funcionam simultaneamente, graças ao protocolo da IBC.

Eventualmente, o [máquina de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) precisa de obter (1) um algoritmo determinístico, que permita a computação do posto numa rede continuamente aping, que por si só, pode escalar para as ordens de magnitude dos gostos de [Google](https://google.com/). Além disso, um algoritmo perfeito (2) deve ter memória linear e complexidade computacional. Mais importante ainda, deve ter (3) as maiores capacidades de previsão comprovadas para a existência de relevantes [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).

Depois de [pesquisa minuciosa](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC), descobrimos que é impossível obter a bala de prata. Por isso, decidimos encontrar uma forma mais básica e à prova de bala, que pode arrancar a rede: [the rank](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw) que Larry e Sergey usavam para arrancar a sua rede anterior. O problema principal com o PageRank original é que não era resistente a ataques de síbil. No entanto, um PageRank ponderado por token, que é limitado por um modelo de largura de banda ponderado por símbolos, não herda o problema chave do ingénuo PageRank, porque - é resistente a ataques de sybil. Por enquanto, vamos chamá-lo de cyber~Rank, até que algo mais adequado surja. O seguinte algoritmo é aplicado à sua implementação na Génesis:

![img](https://github.com/serejandmyself/cyber/raw/master/images/algo2.png)

Entendemos que o mecanismo de classificação continuará a ser sempre um arenque vermelho. É por isso que esperamos confiar nos instrumentos de governação em cadeia que podem definir o mecanismo mais adequado num dado momento. Supomos que a rede pode mudar de um algoritmo para outro, não apenas com base em opinião subjetiva, mas sim em testes económicos a/b através de "colher dura" de domínio específico [máquinas de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).

cyber~Rank protege duas decisões de design que são de extrema importância: (1) ele explica a intenção atual dos agentes, e (2) incentiva a inflação de classificação de [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks). A primeira propriedade garante que o cyber~Rank não pode ser brincado. Se um agente decidir transferir a sua [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas fora da sua conta, o [máquinas de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) vai ajustar todos os [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) relevante para esta conta de acordo com as intenções atuais do agente. E vice-versa, se um agente transferir [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas na sua conta, todos os [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) submetida a partir desta conta ganhará imediatamente mais relevância. A segunda propriedade é essencial para não se cimentar no passado. Como novo [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) são continuamente adicionados, eles vão diluir a classificação dos links já existentes proporcionalmente. Esta propriedade previne uma situação em que o conteúdo novo e melhor tem um posto mais baixo simplesmente porque foi recentemente submetido. Esperamos que estas decisões permitam uma qualidade de inferência para conteúdo recentemente adicionado à longa cauda do [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

Gostaríamos de discutir o problema da compra de votos. Comprar votos como ocorrência não é assim tão mau. Os dilemas com a compra de votos aparecem nos sistemas em que a votação afeta a atribuição da inflação desse sistema. Por exemplo [Steem](http://ipfs.io/ipfs/QmepU77tqMAHHuiSASUvUnu8f8ENuPF2Kfs97WjLn8vAS3) ou qualquer sistema baseado em estado fiat. A compra de votos pode tornar-se facilmente rentável para um adversário que emprega um jogo de soma zero sem a necessidade de acrescentar valor. A nossa ideia original de uma busca descentralizada baseou-se nesta abordagem. Mas, nós rejeitamos essa ideia, removendo o incentivo da formação do [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) ao nível de consenso. No ambiente em que cada participante deve trazer algum valor ao sistema para afetar o modelo preditivo, a compra de votos torna-se um problema difícil de NP. Portanto, torna-se benéfico para o sistema.

A implementação atual do [máquinas de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) utiliza GPUs para calcular o rank. A máquina pode atender e entregar resultados relevantes para qualquer pedido de pesquisa num espaço CID de 64 bytes. No entanto, não é suficiente construir uma rede de domínio específico [máquinas de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine). [Computadores de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) deve ter a capacidade de provar relevância uns aos outros.

## Prova de relevância

Concebemos a rede sob o pressuposto de que, no que diz respeito à procura, tal como comportamentos maliciosos, não existe. Isto pode ser assumido como nenhum comportamento malicioso pode ser encontrado na intenção de encontrar as respostas. Esta abordagem reduz significativamente quaisquer ataques à superfície.

```
Ranks are computed based on the fact that something was searched, thus linked, and as a result - affected the predictive model
```

Uma boa analogia é observada na mecânica quântica, onde a observação em si afeta o comportamento. É por isso que não temos qualquer exigência para uma votação negativa. Ao fazê-lo, removemos a subjetividade do protocolo e podemos definir provas de relevância.

![img](https://github.com/serejandmyself/cyber/raw/master/images/graph-tree.png)

Cada novo CID recebe um número de sequência. A numeragem começa com zero. Em seguida, incrementado por um para cada novo CID. Portanto, podemos armazenar a classificação numa matriz unidimensional, onde os índices são os números de sequência cid. Os cálculos da árvore merkle são baseados na [RFC-6962 standard](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). Usando árvores Merkle, podemos efetivamente provar a classificação para qualquer endereço de conteúdo dado. Embora a relevância ainda seja subjetiva por natureza, temos uma prova coletiva de que algo era relevante para uma determinada comunidade em algum momento.

Usando este tipo de prova qualquer dois [IBC compatível](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk) [computadores de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) pode provar a relevância um para o outro. Isto significa que o domínio específico [relevance machines](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) pode florescer.

Na relevância para um comum [go-cyber](https://github.com/cybercongress/go-cyber) implementação, a árvore Merkle é calculada a cada rodada e seu haxixe raiz comprometido com o ABCI.

## Rapidez

Exigimos tempo de confirmação instantânea para fornecer aos utilizadores a sensação de uma aplicação web convencional. Esta é uma poderosa exigência arquitetônica que molda a topologia económica e a escalabilidade do [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) protocolo. O design de blockchain proposto baseia-se na [Tconsenso endermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) algoritmo com 146 validadores e tem um tempo de finalidade rápido de 5 segundos tx. O tempo médio de confirmação está mais próximo de 1 segundo e pode tornar interações complexas de blockchain quase invisíveis para os agentes.

Nós denotamos um particular [go-cyber](https://github.com/cybercongress/go-cyber) propriedade no contexto da velocidade - computação de classificação. Fazendo parte do consenso, ocorre paralelamente à validação de transações dentro das rondas. Uma ronda é uma variável de consenso definida pelas partes interessadas. No início, uma rodada está definida para 20 quarteirões. Praticamente, isto indica que a cada 100 segundos a rede deve concordar com o haxixe raiz atual do [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). Isto significa que cada [cyberlink](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)  submetida torna-se uma parte do  [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) quase instantaneamente e adquire uma classificação dentro de um período médio de 50 segundos. Nos primeiros dias de [Google](https://google.com/) posto foi recomputação aproximadamente todas as semanas. Acreditamos que os mestres da Grande Web terão o prazer de observar que as mudanças de classificação em tempo real, mas. Espera-se que com o desenvolvimento do [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) protocolo a velocidade de cada rodada diminuirá. Isto deve-se à competição entre heróis. Estamos cientes de certos mecanismos para tornar esta ordem de função de magnitudes mais rápida:

- otimização dos parâmetros de consenso
- melhor paralelização da computação de classificação
- um [relógio melhor](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs) à frente do consenso

## Escalabilidade

Exigimos uma arquitetura que nos permita escalar a ideia para o significado dos gostos de [Google](https://google.com/). Vamos supor, que a implementação do nó, que é baseado em [Cosmos-SDK](https://github.com/cosmos/cosmos-sdk) pode processar transações de 10 k por segundo. Isto significaria que todos os dias, pelo menos 8,64 milhões de mestres poderão submeter 100 [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) cada um, e impactar os resultados da pesquisa simultaneamente. Isto é suficiente para verificar todos os pressupostos na natureza, mas não o suficiente para dizer que funcionará à escala atual da Internet. Dada a investigação de estado atual da arte feita pela nossa equipa, podemos afirmar com segurança que não existe tecnologia de consenso, que permitirá escalar uma determinada blockchain para o tamanho que exigimos. Assim, introduzimos o conceito de domínio específico [gráficos de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

![network.png](https://github.com/serejandmyself/cyber/blob/master/images/network.png?raw=true)

Pode-se lançar um próprio motor de pesquisa específico de domínio, falsificando [go-cyber](https://github.com/cybercongress/go-cyber), que está focado em textit{conhecimento público comum}. Ou simplesmente ligar [go-cyber](https://github.com/cybercongress/go-cyber) como um módulo numa cadeia existente, e.i. Cosmos Hub. O protocolo de comunicação inter-blockchain introduz mecanismos simultâneos de sincronização entre [máquina de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine). Portanto, na arquitetura de pesquisa proposta, específica de domínio [máquina de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) será capaz de aprender com o conhecimento comum. Assim como o conhecimento comum pode aprender com o domínio específico [máquina de relevância](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).

## Browzers

Estávamos aspirados a imaginar como a rede proposta funcionaria com um navegador web3. Para a nossa desilusão nós [não foram capazes](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md) para encontrar um navegador web3 que possa mostrar a frieza da abordagem proposta em ação. É por isso que decidimos desenvolver um navegador web3 de raiz. [Cyb](https://cyb.ai/) é o seu robô amigável que tem uma amostra [.cyber](https://cyber.page/) pedido de interação com o [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) protocolo.

![img](https://github.com/serejandmyself/cyber/raw/master/images/cyb.jpg)

Como um bom exemplo de entrega, criamos [cyber.page](https://cyber.page/). Permite que heróis, mestres e evangelistas interajam com o protocolo através de uma porta web2. Crie ciberligões, pin conteúdo diretamente para O IPFS, procure na Grande Web, participe na governação do ciberliguar e assim por diante. Também pode funcionar como um explorador aprofundado, uma carteira e pode embolsar carteiras de hardware, como dispositivos Ledger.

Os cortes de pesquisa atuais são feios. Mas, presumimos que podem ser facilmente estendidas usando [IPLD](https://github.com/ipld/specs) para diferentes tipos de conteúdo. Eventualmente, podem tornar-se ainda mais atraentes do que os de [Google](https://google.com/).

![img](https://github.com/serejandmyself/cyber/raw/master/images/architecture.png)

Durante a implementação da arquitetura proposta, percebemos pelo menos 3 benefícios fundamentais que [Google](https://google.com/) provavelmente não seria capaz de cumprir com a sua abordagem convencional:

- os resultados da pesquisa podem ser facilmente entregues a partir de qualquer rede p2p: por exemplo, .cyber pode reproduzir vídeos
- botões de pagamento podem ser incorporados em snippets de pesquisa. Isto significa que os agentes podem interagir com os resultados da pesquisa, por exemplo, os agentes podem comprar um item em .cyber. Isto significa que o e-commerce pode florescer bastante graças a uma atribuição de conversão comprovada
- os snippets de pesquisa não têm que ser estáticos, mas podem ser interativos. por exemplo, .cyber pode entregar o seu saldo atual da carteira

## desenvolvimento

Devido a limitações técnicas, temos de arrancar o ecossistema usando 2 fichas: [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) e [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)

- [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) é o símbolo nativo do soberano [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) protocolo alimentado pelo algoritmo de consenso Tendermint. Tem 3 utilizações primárias: (1) aposta para consenso, (2) largura de banda limitada para apresentação [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks), e (3) expressão da vontade dos mestres para a computação do cyber~Rank.
- [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) (pronuncia-se como tecnologia) é uma substância criativa de proto-substância cibernética. [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) sendo um token compatível com Ethereum ERC-20 que tem valor de utilidade sob a forma de controlo sobre a Cyber~Foundation (a comunidade que rege o DAO) e o ETH do jogo de distribuição. [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) é emitida durante a criação da Cyber~Foundation como uma organização Aragão. Os poderes criativos de [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) vêm da capacidade de receber 1 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) símbolo por cada 1 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) símbolo quando investido antes do fim do cyber~Leilão.

Ambos os tokens permanecem funcionais e acompanharão o valor independentemente uns dos outros devido à sua utilidade muito diferente por natureza.

Globalmente, o processo de implantação tem a seguinte estrutura:

1. cyber~Congresso implementa Jogo de Links
2. A comunidade participa no Jogo das Ligações
3. A comunidade verifica e propõe um bloco Génesis com resultados do Jogo de Links
4. cyber~Congresso implementa contratos para cyber~Foundation e cyber~Leilão
5. A comunidade participa no cyber~Leilão depois de Génesis. Participação de doadores [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) fichas para obter [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas
6. cyber~Congresso distribui [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas continuamente durante cyber~Leilão
7. cyber~Congresso queima o restante [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) e [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) fichas e relatórios sobre o fim do processo de distribuição inicial

cyber~Congresso vive em Ethereum como um [Aragon DAO](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330). Também opera um [2-of-3 multisig in Cyber network](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8). cyber~Congresso desenvolveu o [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) protocolo. No contexto da cibersegurança, o Congresso tem 2 funções:

1. Para implementar e executar o programa de distribuição inicial, que é impossível de automatizar. Como não há infraestruturas de confiança para a troca de mensagens entre o ETH e o ATOM, o Cyber~Congress introduz um único ponto de falha no processo de distribuição inicial. Decidimos enviar [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas para [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) aposta manualmente porque sentimos que agora é o momento certo para lançar a rede que criamos. Acreditamos também que um leilão em curso é vital para o processo de distribuição inicial. Se o Cyber~Congresso não cumprir as suas obrigações em termos de distribuição devido a eventuais razões, esperamos que a comunidade seja capaz de despalá-lo e distribuir [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas como foi prometido. Esperemos que cada operação seja projetada com prova e transparência. Todas as operações serão executadas usando um [propósito especial 2-de-3 conta multisig na rede Cyber](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j).
2. Apoiar o crescimento de [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) protocolo até que a comunidade assuma o desenvolvimento sob a forma de Cyber~Foundation. Doações em ATOMs durante o Jogo de Links serão distribuídos [cyber~Congress Cosmos 2-de-3 multisig](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a). Todas as doações do ATOM que são encaminhadas para o cyber~Congresso multisig tornar-se-ão a sua propriedade. O papel da doação da ATOM é o seguinte: graças à ATOM queremos garantir um compromisso para o Cyber~Congresso no desenvolvimento dos ecossistemas Cosmos e Cyber. As doações da ATOM permitirão que o Cyber~Congresso use recompensas de estafilocos e atinja um fluxo sustentável, para o financiamento contínuo do [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) protocolo sem a necessidade de despejar ou [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) nem fichas ATOM.

## CYB

Os sistemas de prova de participação não ajudam na distribuição inicial. Acreditamos que se a distribuição inicial for projetada de forma propositada, eficiente em termos energéticos, comprovadamente e transparente, portanto acessível, o mais cedo [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) vai ganhar em qualidade e tamanho.

O bloco de génese do protocolo cibernético contém 1 000 000 000 000 000 cyb (um petacyb ou 1 PCYB) que se avariam da seguinte forma:

- 750 000 000 000 000 Tokens CYB para aqueles que apostam [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) tokens até o final do cyber~Leilão (participantes do Cyber~Congress, Game of Thrones in ETH e cyber~Auction)
- 150 000 000 000 000 Tokens CYB para os participantes do Jogo das Ligações
- 100 000 000 000 000 Tokens CYB como um presente para as comunidades Ethereum, Cosmos e Urbit

![img](https://github.com/serejandmyself/cyber/raw/master/images/CYB.svg?sanitize=true)

Após o Génesis, os tokens CYB só podem ser criados por heróis baseados em parâmetros de estaca e corte. O consenso fundamental é que os tokens CYB recém-criados estão à disposição das partes interessadas.

Atualmente, não existe tal quantidade de fichas CYB. Isto deve-se à inflação contínua paga aos heróis da rede. O token CYB é implementado usando uint64, por isso a criação de tokens CYB adicionais torna significativamente mais caro calcular as mudanças de estado e classificar. Esperamos que uma estratégia monetária ao longo da vida seja estabelecida pelo sistema de governação após a distribuição inicial completa dos tokens CYB e a ativação da funcionalidade dos contratos inteligentes. Os parâmetros iniciais da inflação serão definidos através da governação durante o Jogo de Links.

## THC

O objetivo de criar uma alternativa a um [Google-like](https://google.com/) estrutura requer esforço extraordinário de vários grupos. Por isso, decidimos criar a Cyber~Foundation como um fundo, gerido através de um motor descentralizado, como um DAO Aragão. É cotado com a ETH e gerido pelos agentes que participaram na distribuição inicial. Esta abordagem permitirá salvaguardar o dumping excessivo do mercado do token da plataforma nativa - [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) nos primeiros anos do seu trabalho, garantindo assim um desenvolvimento estável. Além disso, isto permite diversificar a plataforma subjacente e alargar o protocolo a outras arquiteturas de computação de consenso, caso surja tal necessidade.

Ao escolher o símbolo para doações, seguimos três critérios principais: o símbolo deve ser (1) um dos mais líquidos, (2) mais promissores, para que uma comunidade possa garantir um saco de investimento sólido para ser competitivo mesmo em comparação com tais gigantes como [Google](https://google.com/), e (3) têm a capacidade técnica de executar um leilão e uma organização resultante, sem depender de terceiros. O único sistema que corresponde a estes critérios é o Ethereum, portanto, o principal sinal de doações será o ETH.

Antes de Genesis cyber~Fundação tem cunhado 750 000 000 000 000 THC (700 terathc) dividido da seguinte forma:

- 600 000 000 000 000 As fichas thc são atribuídas ao contrato cyber~Leilão
- 150 000 000 000 000 THC tokens são atribuídos ao contrato cyber~Congresso

![img](https://github.com/serejandmyself/cyber/raw/master/images/THC.svg?sanitize=true)

Todas as decisões da Cyber~Foundation serão executadas com base nos resultados dos votos do THC. Serão aplicados os seguintes parâmetros:

- Suporte: 51%
- Quórum: 51%
- Duração do voto: 500 horas

## Gift

Queremos dar a capacidade de avaliar a abordagem proposta para o maior número possível de agentes. Mas, sem acrescentar tal complexidade como KYC e/ou captcha. É por isso que escolhemos dar 8% dos [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas em Gênesis a Ethereum, 1% para Cosmos, e 1% para as comunidades Urbit. Aplicam-se as seguintes regras para reproduzir o Génesis:

- Todas as contas da rede de fundações Ethereum, com pelo menos 1 transação de saída que não é um contrato, e detém > 0,001 ETH no bloco 8080808
- Cada conta não-zero dentro do cosmos hub-3 no bloco 2000000
- Cada conta que detém galáxias (30%), estrelas (30%), ou planetas (40%) no bloco 10677601 de acordo com o número de objetos

O principal propósito deste presente é que cada conta em Gênesis possa fazer pelo menos 1 [cyberlink](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) no espaço de 24 horas à medida que a rede é descarregada. É por isso que decidimos tornar a curva de distribuição um pouco mais equilibrada, e mudá-la radicalmente para uma curva quadrática. Assim, distribuímos [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas proporcionalmente para a raiz quadrada de cada saldo da conta durante os instantâneos. Como um design quadrático é muito fácil de jogar com, calculamos a quantidade do distribuído [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) símbolos para os blocos propostos antes que este facto se tornasse conhecido do público. Não aplicamos a regra quadrática aos alienígenas de Urbit.

## Jogo de Links

Um jogo para os hodlers cosmos no ATOM. Os participantes doam o ATOM em troca do CYB. Quanto mais ATOM for doado, maior o preço da CYB. O jogo começa a partir de 1 ATOM por 1 GCYB. O jogo acaba quando ou 146 dias se passaram desde o início das doações de descolagem, ou se o preço aumentou 5x em relação ao preço inicial. O preço de [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) durante a descolagem é definida pela seguinte função:

f(c) = 40 * c + 1000

nos casos em que f(c) seja o preço do TCYB no ATOM, a quantidade c é de fichas TCYB ganhas durante a descolagem.

A ideia chave é: quanto melhor for a ronda de doações de descolagem, mais pagamentos os participantes nas disciplinas receberão. 100 [TCYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) é atribuído aos participantes das doações de descolagem e 50 [TCYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) é atribuído aos participantes das disciplinas de Jogo de Links. Todos os [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) Tokens que restam da Descolagem, são atribuídos à piscina comunitária no final do jogo. Todos os [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) Tokens que permanecem das disciplinas são atribuídos ao Cyber~Congresso. Para além dos tokens CYB, o Game of Links atribui fichas de teste eul a todos os dadores de descolagem para a final. A [documento detalhado](https://cybercongress.ai/game-of-links/) foi publicado com regras e disposições para o jogo.

## Cyber~Leilão

Um jogo para os hodlers Ethereum na ETH. Os participantes doam ETH em troca de THC. Quanto mais ETH for doado, maior o preço do THC. O jogo parte do preço que é 5x preço de fecho da descolagem na ETH. O jogo acaba quando ou 888 dias se passaram desde o seu início ou se o preço aumentou 5x em relação ao preço inicial. Durante esta fase [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) tokens são continuamente distribuídos pelo cyber~Congresso, com base no investido [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) fichas até o final do leilão. Investido [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) fichas fornecem a capacidade de receber [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) símbolos em conformidade, e poderes de voto dentro da Cyber~Foundation. O preço de [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) durante o Cyber~Auction é definido pela seguinte função:

g(t)= 1/30 * t * p + 5 * p

onde g(t) é o preço TTHC em ETH, t é a quantidade de fichas TTHC ganhas durante o cyber~Leilão, p é o preço resultante de descolagem para um CYB convertido para ETH no momento de encerramento.

O preço inicial é projetado para dar aos participantes da Descolagem 5x premium pelo seu risco de investir em infraestruturas de hardware e software antes de Génesis. cyber~Leilão dá incentivos significativos para os primeiros participantes. Após o fim da distribuição, os participantes serão capazes de desbloquear a sua [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) fichas e usá-las como quiserem, por que transferir, trocar, etc. Como resultado do leilão, a comunidade terá acesso a toda a ETH doada dentro da organização Aragão. Após o fim do cyber~Leilão, todos os restantes [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) sobre o contrato cyber~Leilão deve ser provavelmente queimado. As seguintes regras aplicam-se a [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas sob o [multisig para distribuição](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j):

- cyber~Congresso não vai delegar a sua participação, e como resultado, permanecerá uma participação passiva até que seja distribuído
- após o fim do cyber~Leilão, todos os restantes [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) fichas devem ser comprovadamente queimados

## Apps

Assumimos que o algoritmo proposto não garante conhecimentos de alta qualidade por defeito. Tal como um recém-nascido, precisa de adquirir conhecimento para se desenvolver ainda mais. O protocolo em si fornece apenas uma ferramenta simples: a capacidade de criar um [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) com uma participação de agentes entre dois endereços de conteúdo.

A análise do núcleo semântico, os fatores comportamentais, os dados anónimos sobre os interesses dos agentes e outras ferramentas que determinam a qualidade da pesquisa, podem ser alcançados através de contratos inteligentes e aplicações off-chain, tais como: [navegadores web3](https://github.com/serejandmyself/cyber/blob/master/cyber.md#browzers), redes sociais descentralizadas e plataformas de conteúdo. Acreditamos, que é do interesse da comunidade e dos mestres construir a inicial [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) e mantê-lo. Daí, para o gráfico, fornecer os resultados de pesquisa mais relevantes.

Geralmente, distinguimos três tipos de aplicações para [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph):

- Aplicativos de consenso. Pode ser executado à discrição do [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) adicionando habilidades inteligentes
- Aplicativos em cadeia. Pode ser dirigido pelo [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) em troca de gás
- Aplicativos fora da cadeia. Pode ser implementado usando o [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) como uma entrada dentro de um ambiente de execução

A seguinte lista de aplicações, imaginável, consolida as categorias acima mencionadas:

Navegadores Web3. Na realidade, o navegador e a pesquisa são inseparáveis. É difícil imaginar o surgimento de um navegador web3 completo que é baseado na pesquisa web2. Atualmente, existem vários esforços para desenvolver navegadores em torno de blockchains e tecnologia distribuída. Todos sofrem de tentar incorporar web2 na web3. A nossa abordagem é um pouco diferente. Consideramos a web2 como um subconjunto inseguro para a web3. Então desenvolvemos um navegador web3 experimental, Cyb, mostrando o [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) abordagem para responder melhor perguntas e entregar conteúdo mais rapidamente.

Redes sociais. As redes sociais não são assim tão misteriosas. Em qualquer conteúdo da rede social está o rei. Assim, o ranking comprovado é o bloco básico de construção de qualquer rede social. Todos os tipos de redes sociais podem ser facilmente construídos em cima de um [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). A Cyber também pode criar redes sociais com base na relevância entre os utilizadores, que nenhuma rede atual é capaz de alcançar.

Semântica programável. Atualmente, as palavras-chave mais populares no gigantesco núcleo semântico de [Google](https://google.com/) são palavras-chave de apps como: [Youtube](https://youtube.com/), [Facebook](https://facebook.com/), [GitHub](https://github.com/), etc. No entanto, os desenvolvedores dessas aplicações bem sucedidas têm capacidade muito limitada de explicar [Google](https://google.com/) como estruturar a pesquisa resulta de uma forma melhor. O [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) abordagem devolve este poder aos desenvolvedores. Os desenvolvedores são agora capazes de direcionar núcleos de semântica específicos e indexar as suas aplicações como quiserem.

Ações de pesquisa. O design proposto permite o apoio nativo para a atividade relacionada com blockchain (e emaranhados). É trivial conceber aplicações que são (1) propriedade dos criadores, (2) aparecem corretamente nos resultados da pesquisa e (3) permitem uma ação transacionável, com (4) atribuição comprovada de uma conversão para uma consulta de pesquisa. o e-Commerce nunca foi tão fácil para todos.

Procura fora da linha. O IPFS permite facilmente recuperar um documento de um ambiente sem uma ligação global à Internet. [go-cyber](https://github.com/cybercongress/go-cyber) em si pode ser distribuído através do IPFS. Isto cria a possibilidade de uma pesquisa ubíqua e off-line!

Ferramentas de comando. As ferramentas de linha de comando podem contar com respostas relevantes e estruturadas a partir de um motor de busca. Na prática, é possível implementar a seguinte ferramenta CLI:

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

Ferramentas de pesquisa, a partir de dentro do CLI criarão inevitavelmente um mercado altamente competitivo de um núcleo semântico dedicado para robôs.

Robôs autónomos. A tecnologia Blockchain permite a criação de dispositivos que possam gerir ativos digitais por si só

```
If a robot can store, earn, spend and invest - they can do everything you can do
```

O que é necessário é uma ferramenta simples, mas uma poderosa ferramenta de realidade do Estado com a capacidade de encontrar coisas particulares. [go-cyber](https://github.com/cybercongress/go-cyber) oferece uma fonte de dados minimalista, mas continuamente auto-aperfeiçoante, que fornece as ferramentas necessárias para a programação de robôs economicamente racionais. De acordo com [top-10,000 English words](https://github.com/first20hours/google-10000-english) a palavra mais popular na língua inglesa é o artigo definitivo 'o', que significa um ponteiro para um determinado item. Este facto pode ser explicado como o seguinte: os itens específicos são da maior importância para nós. Portanto, a natureza de nós é encontrar coisas únicas. Assim, a compreensão de coisas únicas é essencial para os robôs também.

Convergência linguística. Um programador não deve preocupar-se com a linguagem que um agente vai usar. Não precisamos de saber em que língua o agente está a fazer a sua busca. Todo o espectro UTF-8 está a funcionar. O núcleo semântico está aberto, pelo que a concorrência para responder a consultas pode ser distribuída por diferentes áreas específicas do domínio. Incluindo os núcleos semânticos para várias línguas. Esta abordagem unificada cria uma oportunidade para cyber~Bahasa. Desde o início da Internet, observamos um processo de rápida convergência linguística. Usamos palavras verdadeiramente globais em todo o planeta, independentemente da nacionalidade, língua, raça, nome ou ligação à Internet. O sonho de uma linguagem verdadeiramente global é difícil de implementar porque é difícil chegar a acordo sobre o que significa. No entanto, temos as ferramentas para realizar este sonho. Não é difícil prever que quanto mais curta uma palavra, mais poderosa será a sua cyber~Rank. Lista global, publicamente disponível de símbolos, palavras e frases ordenadas em conformidade por cyber~Rank com um link correspondente fornecido por [go-cyber](https://github.com/cybercongress/go-cyber) pode tornar-se a base para o surgimento de uma linguagem genuinamente global que todos podem aceitar. Recente [avanços científicos](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1) na tradução automática são de tirar o fôlego, mas sem sentido para aqueles que desejam aplicá-los sem um modelo treinado à escala Google. O cyber~Rank proposto oferece precisamente este.

Auto-previsão. A [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) pode construir continuamente um [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) por si só, prevendo a existência de [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) e aplicando estas previsões ao seu estado. Daí, um [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) pode participar no consenso económico do [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) protocolo.

Universal oracle. A [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) pode armazenar os dados mais relevantes num armazenamento de valor chave. Onde a chave é um CID e os valores são os bytes do conteúdo real. Isto pode ser conseguido através da tomada de uma decisão em cada ronda, no que diz respeito à qual os cid valorizam os agentes que pretendem podar e que valor pretendem aplicar. Com base na medida de utilidade dos endereços de conteúdo dentro [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). Para calcular a medida de utilidade, os heróis verificam a disponibilidade e o tamanho do conteúdo para os endereços de conteúdo mais bem classificados dentro [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph), em seguida, peso no tamanho dos CIDs e sua classificação. O armazenamento de valor-chave emergente estará disponível para escrever para [computador de consenso](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) apenas e não para os agentes. Mas os valores podem ser usados em programas.

Procura no local. É possível construir [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) com [Prova de localização](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) com base em protocolos notáveis existentes, tais como [Foam](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG). Consequentemente, uma pesquisa baseada em localização também se torna comprovada, se os agentes web3 minarem triangulações e anexarem [Prova de localização](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) para cada cadeia ligada.

Mercados de previsão sobre relevância de ligação. Podemos implementar esta ideia usando o ranking do [gráfico de conhecimento](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) com base num mercado de previsão sobre a relevância das ligações. Uma aplicação que permite apostar na relevância do link, pode tornar-se uma fonte única de verdade para a direção dos termos, bem como motivar os agentes a submeter mais links.

Cyberlinks privados. A privacidade é fundamental. Enquanto estamos comprometidos com a privacidade, alcançar a implementação de privado [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) é inviável para a nossa equipa até Génesis. Portanto, cabe à comunidade trabalhar em programas WASM, que podem ser executados em cima do protocolo. O problema é calcular cyber~Rank, com base no [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) submetida por um web3-masters sem revelar nem: o seu pedido anterior nem as chaves públicas. As provas de conhecimento zero, em geral, são muito caras. Acreditamos que a privacidade da pesquisa deve ser uma característica por design, mas não temos certeza de que sabemos implementá-la nesta fase. [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk) como Snarks recursivos e [MimbleWimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg) construções, em teoria, podem resolver parte da preocupação de privacidade. Mas, são novos, não testados e, de qualquer forma, serão mais caros no que diz respeito aos cálculos do que à sua alternativa transparente.

Esta não é certamente a lista excessiva de todas as aplicações possíveis, mas uma muito emocionante, na verdade,.

## Conclusão

Definimos e implementamos um protocolo de comunicação comprovada, entre computadores de consenso sobre relevância. O protocolo baseia-se na simples ideia de gráficos de conhecimento, que são gerados por agentes através do uso de botões cibernéticos. Os cyberlinks são processados por um computador de consenso utilizando o conceito da máquina de relevância. O computador de consenso cibernético baseia-se no CIDv0/CIDv1 e utiliza o go-IPFS e o Cosmos-SDK como base. O IPFS proporciona benefícios significativos no que diz respeito ao consumo de recursos. CID como objetos primários são robustos na sua simplicidade. Para cada CID, cyber~Rank é calculado por um computador de consenso sem um único ponto de falha. Cyber~Rank é um PageRank ponderado por cyb, com proteção económica contra ataques de síbil e voto egoísta. Todas as voltas da raiz merkle do posto e das árvores de gráfico são publicadas. Consequentemente, cada computador pode provar a qualquer outro computador a relevância de valor para um dado CID. A resistência ao sybil baseia-se na limitação da largura de banda. A capacidade incorporada de executar programas oferece aplicações inspiradoras. O objetivo inicial principal é a indexação de sistemas de endereços de conteúdo peer-to-peer, seja apátrida, tais como: IPFS, Swarm, Sia, Git, BitTorrent, ou stateful, tais como: Bitcoin, Ethereum e outros blockchains e emaranhados. A semântica proposta de ciberligação oferece um mecanismo robusto para prever relações significativas entre objetos pelo próprio computador de consenso. O código-fonte da máquina de relevância é de código aberto. Cada bit de dados acumulados pelo computador de consenso está disponível para qualquer pessoa se tiver os recursos para processá-lo. O desempenho da implementação do software proposto é suficiente para uma interação perfeita. A escalabilidade da implementação proposta é suficiente para indexar todos os dados auto-autenticados que existem hoje e podem servi-lo a milhões de agentes da Grande Web. A blockchain é gerida por uma Superinteligência, que funciona sob o algoritmo de consenso Tendermint com um módulo de governação padrão. Embora o sistema forneça o utilitário necessário para oferecer uma alternativa para um motor de busca convencional, não se limita apenas a este caso de utilização. O sistema é extensível para inúmeras aplicações e permite conceber robôs economicamente racionais e auto-próprios, que possam compreender autonomamente objetos à sua volta.

## Referências

1. [Contexto académico à deriva](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN)
2. [ Pilha nova em folha ](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw)
3. [Recuperação de informação dos motores de busca na prática](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6)
4. [Jogo motivador para pesquisa de exemplo adversário](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9)
5. [Uma ideia de uma pesquisa descentralizada](https://ipfs.io/ipfs/QmXNoGTWLQrcFRb66oS4HafpP1vcLKbVkJrQm4DVvihuoq)
6. [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps)
7. [DAT](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR)
8. [go-cyber](https://github.com/cybercongress/go-cyber)
9. [cosmos-sdk](https://github.com/cosmos/cosmos-sdk)
10. [CIDv1](https://github.com/multiformats/cid#cidv1)
11. [cyber.página](http://cyber.page/)
12. [DURA](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md)
13. [Colony](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj)
14. [Truebit](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)
15. [Termodinâmica das previsões](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb)
16. [PageRank](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw)
17. [RFC-6962](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG)
18. [IBC protocolo](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk)
19. [Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ)
20. [Comparação de navegadores web3](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md)
21. [Cyb](https://cyb.ai/)
22. [SpringRank](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC)
23. [Executar validador no protocolo cibernético](https://cybercongress.ai/docs/go-cyber/run_validator/)
24. [Top 10000 palavras em inglês](https://github.com/first20hours/google-10000-english)
25. [Tradução multilíngue da máquina neural](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1)
26. [Foam](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG)
27. [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk)
28. [Mimblewimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg)
29. [Tezos](https://ipfs.io/ipfs/QmdSQ1AGTizWjSRaVLJ8Bw9j1xi6CGLptNUcUodBwCkKNS)
30. [Software 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35)
31. [Proof-of-history](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs)
32. [IPLD](https://github.com/ipld)
33. [ciber~Organização do Congresso](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330/)
34. [cyber~Congresso em Cyber](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8)
35. [cyber~Congresso em Cosmos](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a)
36. [multisig para distribuição CYB](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j)
37. [.cyber](https://github.com/cybercongress/dot-cyber)

## Reconhecimentos

1. @hleb-albau
2. @arturalbov
3. @jaekwon
4. @ebuchman
5. @npopeka
6. @belya
7. @serejandmyself

