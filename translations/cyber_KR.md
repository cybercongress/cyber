#                                       cyber:   위대한 웹에 대한 지식 컴퓨팅



![img](https://github.com/serejandmyself/cyber/raw/master/images/graph.png)

## 추상

합의 컴퓨터는 구글, 아마존 이나 페이스 북과 같은 어떤 의견 블랙 박스 중개인없이 입증 관련 답변의 컴퓨팅을 할 수 있습니다. IPFS와 같은 상태 비수기, 콘텐츠 주소 지정 가능한 피어 투 피어 통신 네트워크 및 이더리움과 같은 상태 관리 합의 컴퓨터는 유사한 답변을 얻는 데 필요한 솔루션의 일부만 제공할 수 있습니다. 그러나 위에서 언급한 구현과 관련된 3개 이상의 문제가 있습니다. (A) 관련성의 주관적인 특성. (B) 대규모 지식 그래프에 대한 합의 컴퓨터의 확장에 어려움. (C) 이러한 지식 그래프 사이에 품질의 부족. 그들은 다양한 표면 공격하는 경향이있다, 이러한 sybil 공격, 상호 작용 에이전트의 이기적인 행동. 이 문서에서는 IPFS 개체 간의 관련성에 대한 입증 가능한 합의 컴퓨팅 프로토콜을 정의하며, 이는 합의에 따라 GPU를 사용하여 계산되는 사이버~랭크의 Tendermint 합의를 기반으로 합니다. 지분 증명 합의는 초기 배포에 도움이되지 않기 때문에, 우리는 생태학적이고 효율적인 유통 게임의 디자인을 간략하게 설명합니다. 우리는 프로토콜의 최소한의 아키텍처가 도메인 별 지식 합의 컴퓨터의 네트워크의 형성에 중요하다고 생각합니다. 우리의 작업의 결과로, 이전에 존재하지 않았던 일부 응용 프로그램이 등장할 것입니다. 우리는 가능한 기능과 잠재적 인 응용 프로그램에 대한 비전으로이 문서를 확장합니다.

## 위대한 웹

TCP/IP, DNS, URL 및 HTTP/S와 같은 인터넷의 원래 프로토콜은 웹을 현재 위치하는 오래된 지점으로 가져왔습니다. 이러한 프로토콜이 웹의 초기 개발을 위해 생성한 모든 이점을 고려할 때, 이러한 프로토콜은 이러한 프로토콜과 함께 테이블에 상당한 장애물을 가져왔습니다. 글로벌성, 웹의 중요한 속성인 것은 처음부터 실제 위협을 받고있다. 유비쿼터스 정부의 개입으로 인해 네트워크 자체가 계속 증가하는 동안 연결 속도가 저하됩니다. 후자는 인권에 대한 실존적 위협으로 개인 정보 보호 문제를 야기한다.

처음에 분명하지 않은 하나의 속성은 인터넷의 일상적인 사용과 함께 중요해진다 : 영구 링크를 교환 할 수있는 능력, 따라서, 그들은 [시간이 경과 한 후 휴식하지 않습니다](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN). ISP는 한 번에 하나씩 아키텍처에 의존하여 정부가 패킷을 효과적으로 검열할 수 있도록 합니다. 이것은 우리 아이들의 미래에 대해 우려하는 모든 엔지니어를위한 전통적인 웹 스택의 마지막 하락입니다.

ISP는 한 번에 하나씩 아키텍처에 의존하여 정부가 패킷을 효과적으로 검열할 수 있도록 합니다. 이것은 우리 아이들의 미래에 대해 우려하는 모든 엔지니어를위한 전통적인 웹 스택의 마지막 하락입니다.

의 출현 [새로운 웹 스택](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw) 우수한 인터넷을 위한 기회를 창출합니다. 커뮤니티는 이를 web3이라고 부릅니다. 우리는 그것을 위대한 웹이라고 부릅니다. 우리는 다양한 유형의 저수준 통신이 불변이어야 하며 수십 년 동안 변경할 수 없는 콘텐츠 링크와 같은 변경해서는 안 된다고 생각합니다. 그들은 기존의 프로토콜 스택의 문제를 제거하는 데 매우 유망한 것처럼 보입니다. 그들은 더 큰 속도를 추가하고 새로운 웹에 더 접근 가능한 연결을 제공합니다. 그러나 독특한 무언가를 제공하는 개념으로 발생함에 따라 새로운 문제가 발생합니다. 이러한 관심사 중 하나는 범용 검색입니다. 기존의 범용 검색 엔진은 모든 사람이 신뢰해야 하는 제한적이고 중앙 집중식 데이터베이스입니다. 이러한 검색 엔진은 주로 TCP/IP, DNS, URL 및 HTTP/S를 기반으로 클라이언트-서버 아키텍처를 위해 설계되었습니다. Great Web은 새로운 기술을 기반으로 하고 이러한 목적을 위해 특별히 설계된 검색 엔진에 도전과 기회를 제공합니다. 놀랍게도, 허가없는 블록 체인 아키텍처는 이전 건축가가 접근 할 수없는 방식으로 범용 검색 엔진을 구축 할 수 있습니다.es.

## 적대적인 예의 문제

[검색 엔진의 현재 아키텍처](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6) 는 일부 엔터티가 모든 똥을 처리하는 시스템입니다. 이 접근 방식은 뛰어난 Google 과학자들조차도 아직 해결되지 않은 하나의 도전과 뚜렷한 문제로 고통받고 있습니다. [적대적인 예 문제](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9). Google이 인정하는 문제는 특정 샘플이 적대적인지 여부를 알고리즘적으로 추론하기가 다소 어렵다는 것입니다. 이것은 그 자체로 교육 기술이 얼마나 멋진에 사려 깊다. 암호화 폐 경제적 접근 방식은 게임의 수혜자를 바꿀 수 있습니다. 따라서 이 접근 방식은 가능한 sybil 공격 벡터를 효과적으로 제거합니다. 단일 엔터티에 의한 하드 코드 모델 크롤링 및 의미 추출에 대한 필요성을 제거합니다. 대신, 그것은 전 세계에이 힘을 제공합니다. 학습 sybil 저항, 에이전트 생성 모델, 아마 더 많은 예측 결과의 크기의 순서로 이어질 것입니다.

## 사이버 프로토콜

핵심 프로토콜은 매우 최소하며 다음 단계로 표현할 수 있습니다.

1. 정의된 분포를 기반으로 사이버 프로토콜의 기원계산
2. 의 상태를 정의합니다. [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
3. 다음을 사용하여 트랜잭션을 수집합니다. [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
4. 서명의 유효성 확인
5. 확인 을 통해 [대역폭 제한](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
6. CID의 유효성 확인
7. 서명, 대역폭 제한 및 CID가 모두 유효한 경우 [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 및 거래
8. 의 가치를 계산[cyber~순위](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberrank) CID의 모든 라운드에 대해 지식 그래프  [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)

이 문서의 나머지 부분에서는 제안된 프로토콜의 근거와 기술적 세부 사항에 대해 설명합니다.

## 지식 그래프

지식 그래프는 콘텐츠 주소 간의 지시링크에 대한 가중치 그래프로 표시됩니다. 일명, 콘텐츠 식별자, CID, IPFS 해시, 또는 단순히 - IPFS 링크. 이 문서에서는 위의 용어를 동의어로 사용합니다.

![img](https://github.com/serejandmyself/cyber/raw/master/images/knowledge-graph.png)

콘텐츠 주소는 기본적으로 web3 링크입니다. 불분명하고 가변성 인 사용 대신 :

```
https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md
```

우리는 객체 자체를 사용합니다.

```
Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

콘텐츠 주소를 사용하여 지식 그래프를 작성함으로써 [너무 많이 필요](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est) [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps) - [처럼](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR) 검색 엔진에 대 한 원하는 p2p 프로토콜의 초강대국:

- 메쉬 네트워크 미래 지향적
- 행성 간 접근성
- 검열 저항
- 기술적 독립성

우리의 지식 그래프는 멋진 주인에 의해 생성됩니다. 마스터는 단일 트랜잭션, 사이버 링크의 도움으로 지식 그래프에 자신을 추가합니다. 따라서 공개된 공개 키의 콘텐츠 주소에 대한 개인 키가 있음을 증명합니다. 이러한 메커니즘을 사용하여 [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 지식 그래프에서 주제와 개체 간의 가능한 차별화를 달성할 수 있습니다.

우리의 구현은 [go-cyber](https://github.com/cybercongress/go-cyber) 를 기반으로 합니다. [cosmos-SDK](https://github.com/cosmos/cosmos-sdk)정체성  [CIDv0/CIDv1](https://github.com/multiformats/cid#cidv0) 콘텐츠 주소.

마스터는 적용하여 지식 그래프를 형성합니다. [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).

## Cyberlinks

사이버 링크가 어떻게 작동하는지 이해하려면 URL 링크 (일명 하이퍼 링크)와 IPFS 링크 간의 차이점을 이해해야합니다. URL 링크는 IPFS 링크가 콘텐츠 자체를 가리키는지 여부에 관계없이 콘텐츠의 위치를 가리킵니다. 위치 링크와 콘텐츠 링크를 기반으로 하는 웹 아키텍처의 차이는 급진적이며 고유한 접근 방식이 필요합니다.

사이버 링크는 두 개의 콘텐츠 주소 또는 IPFS 링크를 의미적으로 연결하는 접근 방식입니다.

```
.md syntax: [QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH](Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH)    
.dura syntax: QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH.Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

위의 사이버 링크는 [go-cyber](https://github.com/cybercongress/go-cyber) 동안 [cyberc0n](https://etherscan.io/token/0x61B81103e716B611Fff8aF5A5Dc8f37C628efb1E) 코스모스 백서를 참조하고 있습니다. 사이버 링크의 개념은 모든 p2p 네트워크에서 통신 형식의 간단한 의미 론에 관한 규칙입니다.

![img](https://github.com/serejandmyself/cyber/raw/master/images/cyberlink.png)

우리는 사이버 링크가 두 링크 사이의 링크를 나타내는 것을 볼 수 있습니다. 쉬운 쉬운!

사이버 링크는 우주의 예측 모델을 구축하기위한 간단하면서도 강력한 의미 체계 구조입니다. 즉, 하이퍼링크 대신 사이버 링크를 사용하면 범용 검색 엔진의 이전 아키텍처에 액세스할 수 없었던 초능력을 사용할 수 있습니다.

사이버 링크는 확장 될 수 있습니다., 즉 그들은 두 개 이상의 사이버 링크 는 하나의 마스터에서 subsist 경우 링크 체인을 형성할 수 있습니다., 첫 번째 사이버 링크의 두 번째 링크는 두 번째 사이버 링크의 첫 번째 링크와 동일:

![img](https://github.com/serejandmyself/cyber/raw/master/images/linkchain.png)

에이전트가 기본 IPFS 링크를 의미상으로 더 풍부한 것으로 확장하는 경우(예: [경막](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md) 링크, 다음 특정 프로그램에 의해 실행 규칙에 대 한 합의에 도달 할 수 있습니다 보다 자연 스러운 접근.

그만큼 [go-cyber](https://github.com/cybercongress/go-cyber) 사이버 링크의 구현은 [.cyber](https://github.com/cybercongress/dot-cyber) 우리의 실험 웹3 브라우저의 응용 프로그램 [cyb](https://cyb.ai/), 또는 [cyber.page](http://cyber.page/).

마스터가 제출한 사이버 링크는 [RFC-6962 표준](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). 이를 통해 [관련성 증명](https://github.com/serejandmyself/cyber/blob/master/cyber.md#proof-of-relevance).

![img](https://github.com/serejandmyself/cyber/raw/master/images/graph-tree.png)

사이버 링크를 사용하여, 우리는 주제와 개체의 관련성을 계산할 수 있습니다. [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). 그러나 우리는 [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer).

## 합의 컴퓨터의 개념

합의 컴퓨터는 에이전트 간의 상호 작용에서 나오는 추상 컴퓨팅 컴퓨터입니다. 컨센서스 컴퓨터는 메모리와 계산이라는 기본적인 컴퓨팅 리소스의 용량을 가지고 있습니다. 에이전트와 상호 작용하려면 컴퓨터가 대역폭이 필요합니다. 이상적인 합의 컴퓨터는 다음과 같은 컴퓨터입니다.

```
the sum of all the computations and memory available to individuals`
`is equal to`
`the sum of all the verified computations and memory of the consensus computer
```

우리는 그것을 알고 :

```
verifications of computations < (computations + verifications of computations)
```

따라서, 우리는 이상적인 합의 컴퓨터를 달성 할 수 없을 것입니다. CAP 정리와 확장성 trilemma는 이 진술에 더 많은 증거를 추가합니다.

![img](https://github.com/serejandmyself/cyber/raw/master/images/consensus-computer.png)

그러나이 이론은 합의 컴퓨터에 대한 성능 지표로 작동 할 수 있습니다. 컨센서스 컴퓨터에 투자한 지 6년이 지난 지금, 우리는 [Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) 합의는 우리의 작업에 필요한 차가움과 생산 준비 사이의 충분한 균형을 가지고있다. 따라서, 우리는 구현하기로 결정했습니다 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 코스모스 허브에 매우 가까운 설정을 가지고 Tendermint 합의를 사용하여 프로토콜. Tthe [go-cyber](https://github.com/cybercongress/go-cyber) 구현은 64바이트 문자열 공간에 대한 관련성의 64비트 Tendermint 합의 컴퓨터입니다. 이것은 적어도 1/146으로, 우리는 생산 동일한 계산을 확인 146 유효성 검사기를 가지고 있기 때문에, 지금까지 이상적이지 않다 [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

합의 컴퓨터의 계산, 저장 및 대역폭 공급을 쿼리에 대한 최대수요에 결합해야 합니다. 계산 및 스토리지( 기본 [관련성 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 대역폭을 기반으로 쉽게 예측할 수 있습니다. 그러나 대역폭에는 제한 메커니즘이 필요합니다..

## 관련성 기계 

우리는 우리를 정의한 관련성을 기계 기계로 전환되는 상태의 [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 가르치고 자하는 대리인의 뜻에 따라 [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). 의지는 모든 사람에 의해 예상됩니다 [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 마스터가 수행합니다. 에이전트가 많을수록 [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph), 지식이 더 가치있게 됩니다. 이러한 예측을 기반으로 콘텐츠 주소 간의 관련성을 계산할 수 있습니다. 관련성 머신을 사용하면 쿼리 및 답변을 전달하여 검색 메커니즘을 간단하게 구성할 수 있습니다.

관련성 기계의 한 속성은 매우 중요합니다. 유도 추론 속성이 있거나 블랙 박스 원칙을 따라야합니다.

```
The machine should be able to interfere with predictions without any knowledge about the objects,`
`except for who, when and what was cyberlinked
```

우리가 가정하는 경우 [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 연결된 개체에 대한 몇 가지 정보가 있어야 하며 이러한 모델의 복잡성은 예측할 수 없게 증가합니다. 따라서 메모리 및 계산을 위한 프로세싱 컴퓨터의 높은 요구 사항. 블랙박스 원칙을 따르는 관련성 머신을 다루는 콘텐츠 덕분에 데이터를 저장할 필요가 없습니다. 그러나, 여전히 효과적으로 그 위에 작동 할 수 있습니다. 내부의 의미의 공제는 [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 비싸다. 따라서 이러한 디자인은 가정 실명에 따라 달라질 수 있습니다. 내부의 의미를 공제하는 대신 [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer), 우리는 추출이 인센티브를 제공하는 시스템을 설계했습니다. 이는 마스터가 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 토큰은 관련성 기계가 순위를 계산할 수 있는 에 따라 자신의 의지를 표현할 수 있습니다.

스팸 방지 시스템의 중심에는 관련 기계의 진화적 성공에 기득권을 가진 사람들만 쓰기 작업을 실행할 수 있다는 가정이 있습니다. 유효 지분의 1%마다 [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 가능한 네트워크 대역폭과 컴퓨팅 기능의 1%를 사용할 수 있습니다. 간단한 규칙은 에이전트의 남용을 방지합니다: 한 쌍의 콘텐츠 식별자는 한 번만 주소로 사이버 링크될 수 있습니다.

![img](https://github.com/serejandmyself/cyber/raw/master/images/algo1.png)

계좌의 유효 지분 (활성 지분 + 채권)을 변경하는 방법은 다이렉트 토큰 이체와 본딩 운영의 두 가지뿐입니다.

[Cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 매우 간단한 대역폭 모델을 사용합니다. 이 모델의 주요 목표는 일일 네트워크 증가를 지정된 상수로 줄이는 것입니다. 이는 인프라에 대한 향후 투자를 예측할 수 있는 영웅(유효성 검사기)을 수용하기 위한 것입니다. 따라서 여기에서는 '와트' 또는 'W'를 소개합니다. 각 메시지 유형에는 할당된 W 비용이 있습니다. 상수 '바람직한 대역폭'은 W 값에 의해 소비되는 바람직한 '복구 창'을 결정합니다. 복구 기간은 마스터가 대역폭을 0에서 최대 대역폭으로 복구할 수 있는 속도입니다. 마스터는 다음 공식에 의해 결정되는 자신의 유효 지분에 최대 W 비례를 가합니다:

```
AgentMaxW = EffectiveStake * DesirableBandwidth
```

'adjustPricePeriodPeriod' 기간은 최신 블록의 '복구 기간' 기간 동안 W가 소비된 금액을 요약합니다. '소비 대역폭' / '바람직한 대역폭' 비율을 소수 예비 비라고 합니다. 네트워크 사용량이 적으면 소수 준비 비율이 메시지 비용을 조정하여 베팅 금액이 낮은 마스터가 더 많은 트랜잭션을 커밋할 수 있도록 합니다. 리소스에 대한 수요가 증가하면 소수 준비 비율이 1로 되므로 메시지 비용이 증가하고 장기 기간 동안 최종 tx 수를 제한합니다(W 복구는 <다음 W 지출이 됩니다). 아무도 소유한 대역폭을 모두 사용하지 않아서 가격 재계산 목표 기간 내에 최대 100배의 분수 보유를 안전하게 사용할 수 있습니다. 이러한 메커니즘은 만들기에 대한 할인을 제공합니다. [cyberlinking](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks), 따라서, 효과적으로 그것에 대한 수요를 극대화. 제안된 설계에는 관련성이 가치 있게 되기 위해 전체 대역폭에 대한 수요가 필요하다는 것을 알 수 있습니다.

인간의 지능은 시간이 지남에 따라 아무도 관련이 없고 중요한 기억이 잊혀지는 방식으로 조직됩니다. 관련성 컴퓨터에도 동일하게 적용할 수 있습니다. 관련성 기계는 [적극적인 가지 치기 전략](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb), 예를 들어, 형성의 역사의 가지 치기 [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph), 관련성이 떨어지는 링크를 잊어버리는 경우.

그 결과, 구현된 사이버 노믹스는 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 토큰은 의지 표현 및 스팸 방지 메커니즘뿐만 아니라 영웅의 처리 능력과 처리에 대한 시장 수요를 조정할 수있는 경제 규제 도구의 역할을합니다. 관련성 머신의 사이버 사이버 구현은 사이버 직급이라는 매우 간단한 메커니즘을 기반으로합니다.

## cyber~순위

를 사용한 순위 [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 합의 된 컴퓨터는 심각한 리소스 제약 조건을 가지고 있기 때문에 어려울 수 있습니다. 첫째, 우리는 왜 계산하고 체인에 순위를 저장하고 같은 방식으로 수행하지 해야합니까? [Colony](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj) or [Truebit](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)?

랭크가 내부에서 계산된 경우 [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 하나는 해당 순위의 콘텐츠 배포에 쉽게 액세스 할 수 있으며, [입증 가능한 응용 프로그램 빌드](https://github.com/serejandmyself/cyber/blob/master/cyber.md#apps) 그 순위의 상단에. 따라서, 우리는 더 우주 건축을 따르기로 결정했습니다. 다음 섹션에서는 [관련성 증명](https://github.com/serejandmyself/cyber/blob/master/cyber.md#proof-of-relevance) 도메인별 네트워크를 통해 확장할 수 있습니다. [관련성 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine). IBC 프로토콜 덕분에 동시에 작업할 수 있습니다..

결국, [관련성 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) (1) 결정적 알고리즘을 구해야 하며, 이는 지속적으로 인더해하는 네트워크에서 순위를 계산할 수 있게 해주며, 그 자체가 [Google](https://google.com/). 또한 완벽한 알고리즘(2)에는 선형 메모리와 계산 복잡성이 있어야 합니다. 가장 중요한 것은( 3) 관련 존재에 대한 가장 높은 예측 능력이 있어야 한다는 것입니다. [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).

후[철저한 조사 ](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC), 우리는 은총알을 얻는 것이 불가능하다는 것을 발견했습니다. 따라서, 우리는 네트워크를 부트 스트랩 할 수있는 보다 기본적인 방탄 방법을 찾기로 결정했습니다 : [순위](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw) 래리와 세르게이는 이전 네트워크를 부트스트랩하는 데 사용했습니다. 원래 PageRank의 주요 문제는 sybil 공격에 저항하지 않았다는 것입니다. 그러나 토큰 가중 대역폭 모델에 의해 제한되는 토큰 가중 PageRank는 순진한 PageRank의 주요 문제를 상속하지 않습니다. 당분간, 우리는 더 적합한 무언가가 나타날 때까지, 그것을 사이버 ~ 랭크라고 합니다. 다음 알고리즘은 제네시스의 구현에 적용됩니다.

![img](https://github.com/serejandmyself/cyber/raw/master/images/algo2.png)

우리는 순위 메커니즘은 항상 빨간색 청어 남아 있음을 이해합니다. 이것이 우리가 주어진 시간에 가장 적합한 메커니즘을 정의할 수 있는 온체인 거버넌스 도구에 의존할 것으로 예상되는 이유입니다. 우리는 네트워크가 단순히 주관적인 의견에 기초한 것이 아니라 도메인별 '하드 스푼'을 통해 경제적인 a/b 테스트에 따라 하나의 알고리즘에서 다른 알고리즘으로 전환할 수 있다고 가정합니다. [관련성 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).

cyber~Rank는 가장 중요한 두 가지 설계 결정을 보호합니다: (1) 에이전트의 현재 의도를 설명하며, (2) 순위 인플레이션을 장려합니다. [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks). 첫 번째 속성은 사이버 ~ 순위와 함께 게임 할 수 없습니다 보장합니다. 에이전트가 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 토큰은 계정에서 나오며, [관련성 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) will adjust all the [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 에이전트의 현재 의도에 따라 이 계정과 관련이 있습니다. 에이전트가 전송하는 경우 그 반대의 경우도 마찬가지입니다. [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 토큰을 자신의 계정으로, 모든 [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 이 계정에서 제출하면 즉시 더 많은 관련성을 얻을 수 있습니다. 두 번째 속성은 과거에 시멘트얻을하지 않기 위해 필수적이다. 새로운 [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 지속적으로 추가되며, 기존 링크의 순위를 비례적으로 희석시됩니다. 이 속성은 새롭고 더 나은 콘텐츠가 최근에 제출되었기 때문에 순위가 낮은 상황을 방지합니다. 우리는 이러한 결정이 최근 추가 된 콘텐츠에 대한 추론 품질을 가능하게 할 것으로 기대합니다. [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

우리는 투표 구매의 문제를 논의하고 싶습니다. 투표 를 발생으로 구매하는 것은 그렇게 나쁘지 않습니다. 투표 구매의 딜레마는 투표가 해당 시스템 인플레이션의 할당에 영향을 미치는 시스템 내에서 나타납니다. 예를 들어 [Steem](http://ipfs.io/ipfs/QmepU77tqMAHHuiSASUvUnu8f8ENuPF2Kfs97WjLn8vAS3) 또는 피아트 상태 기반 시스템. 투표 구매는 가치를 추가할 필요 없이 제로섬 게임을 사용하는 적에게 쉽게 수익을 낼 수 있습니다. 분산 된 검색에 대한 우리의 원래 아이디어는이 접근 방식을 기반으로했습니다. 그러나, 우리는 그 아이디어를 거부했다, 의 형성의 인센티브를 제거 [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 합의 수준으로. 모든 참가자가 예측 모델에 영향을 미치기 위해 시스템에 어떤 가치를 가져와야하는 환경에서 투표 구매는 NP 하드 문제가됩니다. 따라서 시스템에 유익합니다.

의 현재 구현 [관련 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) GPU를 활용하여 순위를 계산합니다. 기계는 64바이트 CID 공간에서 주어진 검색 요청에 대한 관련 결과에 응답하고 제공할 수 있습니다. 그러나 도메인별 네트워크를 구축하는 것만으로는 충분하지 않습니다. [관련 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine). [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 서로 의관련성을 입증할 수 있는 능력이 있어야 합니다.

## 관련성 증명

검색과 관련하여 악의적 인 행동과 같은 것은 존재하지 않는다는 가정하에 네트워크를 설계했습니다. 답을 찾을 의도로 악의적 인 행동을 찾을 수 없기 때문에 가정 할 수 있습니다. 이 접근 방식은 모든 표면 공격을 크게 줄입니다.

```
Ranks are computed based on the fact that something was searched, thus linked, and as a result - affected the predictive model
```

관찰 자체가 행동에 영향을 미치는 양자 역학에서 좋은 비유가 관찰됩니다. 그렇기 때문에 우리는 부정적인 투표와 같은 것에 대한 요구 사항이 없습니다. 이렇게 하면 프로토콜에서 주관성을 제거하고 관련성 증명을 정의할 수 있습니다.

![img](https://github.com/serejandmyself/cyber/raw/master/images/graph-tree.png)

각 새 CID는 시퀀스 번호를 받습니다. 번호 매기기는 0으로 시작합니다. 그런 다음 각 새 CID에 대해 하나씩 증가합니다. 따라서 인덱스가 CID 시퀀스 번호인 1차원 배열에 순위를 저장할 수 있습니다. 머클 트리 계산은 [RFC-6962 표준](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). Merkle 나무를 사용하여 특정 콘텐츠 주소의 순위를 효과적으로 증명 할 수 있습니다. 관련성은 여전히 본질적으로 주관적이지만, 우리는 어떤 시점에서 특정 커뮤니티와 관련이 있다는 집단적 증거를 가지고 있습니다.

이 유형의 증거를 사용하여 두 가지 [IBC 호환](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk) [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 서로 관련성을 증명할 수 있습니다. 즉, 도메인별 [관련성 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 번창할 수 있습니다.

공통의 관련성에서 [go-cyber](https://github.com/cybercongress/go-cyber) Merkle 트리는 매 라운드마다 계산되며 ABCI에 전념하는 루트 해시입니다.

## 속도

우리는 기존의 웹 응용 프로그램의 느낌을 사용자에게 제공하기 위해 즉각적인 확인 시간이 필요합니다. 이것은 경제적인 토폴로지와 확장성을 형성하는 강력한 아키텍처 요구 사항입니다. [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 프로토콜. 제안된 블록체인 디자인은 [텐더민트 컨센서스](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) 146 개의 유효성 검사기가있는 알고리즘과 빠른 5 초 tx 최종 시간을 가있습니다. 평균 확인 시간은 1 초에 가까울 수 있으며 복잡한 블록 체인 상호 작용이 에이전트에게 거의 보이지 않게 될 수 있습니다.

우리는 하나의 특정한 것을 나타냅니다 [go-cyber](https://github.com/cybercongress/go-cyber) 속도의 맥락에서 속성 - 순위 계산. 합의의 일부이기 때문에 라운드 내의 트랜잭션 유효성 검사와 병렬로 발생합니다. 라운드는 이해 관계자가 정의한 합의 변수입니다. 시작 시 한 라운드는 20 블록으로 설정됩니다. 실질적으로, 이것은 네트워크가 100초마다 네트워크의 현재 루트 해시에 동의해야 함을 나타냅니다. [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). This means that every [cyberlink](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 제출된 제출물의 일부가 됩니다. [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 50초 의 평균 기간 내에 랭크를 획득할 수 있습니다. 초기에 [Google](https://google.com/) 계급은 대략 매주 재계산되었습니다. 우리는 위대한 웹의 주인은 실시간으로 순위 변화를 관찰하는 것을 기쁘게 생각하지만,이 창이 충분하다는 가정하에 네트워크를 시작하기로 결정했습니다. 의 발전과 함께 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 프로토콜은 각 라운드의 속도가 감소합니다. 이것은 영웅 들 간의 경쟁 때문입니다. 우리는 이 함수 순서를 더 빠르게 만들기 위한 특정 메커니즘을 알고 있습니다.

- 합의 매개 변수의 최적화
- 순위 계산의 더 나은 병렬화
- a [더 나은 시계](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs) 합의에 앞서

## 확장성

우리는 우리가 같은 의 중요성에 아이디어를 확장 할 수 있도록 아키텍처가 필요합니다 [Google](https://google.com/). 우리가 가정하자, 그 노드 구현, 이는 기반 [코스모스-SDK](https://github.com/cosmos/cosmos-sdk) 초당 10k 트랜잭션을 처리할 수 있습니다. 즉, 매일 적어도 864만 명의 마스터가 100명의 마스터를 제출할 수 있습니다. [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 검색 결과에 동시에 영향을 미칩니다. 이것은 야생에서 밖으로 모든 가정을 확인 하기에 충분 한, 하지만, 그것은 인터넷의 현재 규모에서 작동 하는 말을 충분 하지. 우리 팀에 의해 수행 된 예술 연구의 현재 상태를 감안할 때, 우리는 안전하게 우리가 필요로하는 크기로 특정 블록 체인을 확장 할 수 있도록, 존재에 합의 기술이 없다는 것을 명시 할 수 있습니다. 따라서 도메인별 개념을 소개합니다. [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

![img](https://github.com/serejandmyself/cyber/raw/master/images/network.png)

하나는 forking하여 자신의 도메인 별 검색 엔진을 시작할 수 있습니다. [go-cyber](https://github.com/cybercongress/go-cyber), textit{공용 지식}에 중점을 둔다. 또는 플러그를 꽂기만 하면 됩니다. [go-cyber](https://github.com/cybercongress/go-cyber) 기존 체인, 즉 코스모스 허브에 모듈로. 블록 체인 간 통신 프로토콜은 사이의 상태를 동기화하는 동시 메커니즘을 도입합니다. [관련성 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine). 따라서 제안된 검색 아키텍처에서 도메인별 [관련성 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 상식에서 배울 수 있을 것입니다. 도메인별에서 배울 수 있는 일반적인 지식과 마찬가지로 [관련성 기계](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).

## 브라우저

우리는 제안 된 네트워크가 web3 브라우저로 어떻게 작동하는지 상상하고 싶었습니다. 우리의 실망에 우리는 [할 수 없습니다.](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md) 웹3 브라우저를 찾아 제안된 접근 방식의 시원함을 보여줄 수 있습니다. 우리가 처음부터 웹3 브라우저를 개발하기로 결정한 이유입니다. [Cyb](https://cyb.ai/) 견본이 있는 당신의 친절한 로봇입니다 [.cyber](https://cyber.page/) 와 상호 작용하기 위한 응용 프로그램 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 프로토콜.

![img](https://github.com/serejandmyself/cyber/raw/master/images/cyb.jpg)

배달의 좋은 예로, 우리는 [cyber.page](https://cyber.page/). 그것은 영웅, 마스터 와 전도사 웹 2 게이트웨이를 통해 프로토콜과 상호 작용할 수 있습니다. 사이버 링크를 만들고, 콘텐츠를 IPFS에 직접 고정하고, 그레이트 웹을 검색하고, 사이버 거버넌스에 참여하는 등의 방식으로 콘텐츠를 생성합니다. 또한 심층 탐색기, 지갑 및 원장 장치와 같은 하드웨어 지갑을 포켓 할 수 있습니다.

현재 검색 스니펫은 못생겼습니다. 그러나, 우리는 그들이 쉽게 사용하여 확장 할 수 있다고 가정 [IPLD](https://github.com/ipld/specs) 콘텐츠 유형에 대해 결국, 그들은 의 경우보다 훨씬 더 매력적으로 될 수 있습니다. [Google](https://google.com/).

![img](https://github.com/serejandmyself/cyber/raw/master/images/architecture.png)제안된 아키텍처를 구현하는 동안, 우리는 적어도 3가지 주요 이점을 실현했습니다. [Google](https://google.com/) 아마도 기존의 접근 방식으로는 제공 할 수 없을 것입니다.

- 검색 결과는 모든 p2p 네트워크에서 쉽게 전달 될 수있다 : 예를 들어 .cyber는 비디오를 재생할 수 있습니다

- 지불 버튼은 바로 검색 조각에 포함 될 수있다. 즉, 에이전트는 .cyber에서 바로 항목을 구매할 수 있는 등 검색 결과와 상호 작용할 수 있습니다. 즉, 전자 상거래는 입증 가능한 전환 어트리뷰션덕분에 상당히 번창할 수 있습니다.

- 검색 스니펫은 정적 일 필요는 없지만 대화형일 수 있습니다. 예를 들어 .cyber는 현재 지갑 잔액을 제공할 수 있습니다.

  ## 전개

  기술적 한계로 인해 2 개의 토큰을 사용하여 생태계를 부트 스트랩해야합니다. [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 및 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)

  - [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 는 주권자의 기본 토큰입니다. [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 텐더민트 합의 알고리즘에 의해 구동되는 프로토콜. 그것은 3 기본 용도가 있습니다 : (1) 합의에 대한 스킹, (2) 제출을위한 대역폭 제한 [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks), (3) 사이버 ~ 랭크의 계산을위한 주인의 의지의 표현.
  - [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) (기술로 발음) 창조적 인 사이버 프로토 물질이다. [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 사이버 ~ 재단 (DAO를 지배하는 지역 사회) 및 유통 게임에서 ETH에 대한 제어의 형태로 유틸리티 가치를 가지고 이더리움 ERC-20 호환 토큰인. [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 아라곤 조직으로 사이버 ~ 재단의 창조 중에 방출된다. 의 창조적 인 힘 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 1을 받을 수 있는 능력에서 나온 것입니다. [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 각 1개당 토큰 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 사이버 ~ 경매가 끝나기 전에 기득권을 부여할 때 토큰을 표시합니다.

  두 토큰은 여전히 기능적이며 본질적으로 매우 다른 유틸리티로 인해 서로 독립적으로 값을 추적합니다.

  전반적으로 배포 프로세스에는 다음과 같은 구조가 있습니다.

  1. 사이버 ~ 의회는 링크의 게임을 배포
  2. 커뮤니티는 링크의 게임에 참여
  3. 커뮤니티는 링크 의 게임 결과와 함께 창세기 블록을 확인하고 제안합니다.
  4. 사이버 ~의회, 사이버 ~ 재단 및 사이버 ~ 경매에 대한 계약을 배포
  5. 커뮤니티는 창세기 이후 사이버~경매에 참여합니다. 기부자 스테이크 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 얻을 토큰 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 토큰
  6. 사이버 ~ 의회 배포 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 사이버 ~ 경매 동안 지속적으로 토큰
  7. 사이버 ~ 의회는 나머지를 태워 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 및 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 토큰 및 초기 배포 프로세스 종료에 대한 보고서

  사이버 ~ 의회는 이더리움에 살고 [Aragon DAO](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330). 또한 작동[2-of-3 사이버 네트워크의 멀티시그](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8). 사이버~의회가 개발한 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 프로토콜. 사이버의 맥락에서, 의회는 2 역할이 있다:

  1. 자동화가 불가능한 초기 배포 프로그램을 배포하고 실행합니다. ETH와 ATOM 간에 메시지 교환을 위한 신뢰할 수 없는 인프라가 없기 때문에 사이버~의회는 초기 배포 프로세스에서 단일 실패 지점을 소개합니다. 우리는 보내기로 결정했습니다 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 토큰을 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 우리가 지금 우리가 만든 네트워크를 시작하는 적절한 시기라고 생각하기 때문에 수동으로 수작업으로. 또한 초기 배포 프로세스에는 지속적인 경매가 필수적이라고 생각합니다. 사이버 ~의회가 가능한 사유로 인해 배포 측면에서 의무를 이행하지 못하는 경우, 우리는 지역 사회가 네트워크를 포크하고 배포 할 수 있기를 바랍니다. [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 약속된 대로 토큰을 표시합니다. 바라건대, 모든 작업은 입증되고 투명하게 설계되었습니다. 모든 작업은 [사이버 네트워크의 특수 목적 2-3 멀티 시그 계정](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j).
  2. 의 성장을 지원 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 커뮤니티가 사이버 ~ 재단의 형태로 개발을 인수 할 때까지 프로토콜. 링크 게임 중 ATOM의 기부금은 [사이버 ~ 의회 코스모스 2-의 3 멀티 시그](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a). 사이버 ~ 의회 멀티 시그에 라우팅되는 모든 ATOM 기부금은 재산이 될 것입니다. ATOM 기부의 역할은 다음과 다: ATOM 덕분에 우리는 코스모스와 사이버 생태계의 개발에 사이버 ~ 의회에 대한 약속을 확보하고자. ATOM 기부는 사이버 ~ 의회가 스케일 보상을 사용하고 지속 가능한 흐름에 도달 할 수 있도록 할 것입니다, 지속적인 자금 조달을위해 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 어느 쪽도 덤프 할 필요없이 프로토콜 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 도 ATOM 토큰.

  ## CYB

  지분 증명 시스템은 초기 배포에 도움이 되지 않습니다. 우리는 초기 분포가 의도적으로, 에너지 효율적이며, 입증가능하고 투명하게 설계되어, 따라서 접근이 가능하다고 믿습니다. [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 품질과 크기에서 얻을 것이다.

  사이버 프로토콜의 제네시스 블록에는 다음과 같이 세분화된 1 000 000 000 000 000 CYB(1페타시브 또는 1 PCYB) 토큰이 포함되어 있습니다.

  - 지분 사람들을위한 750 000 000 000 000  CYB 토큰 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 사이버 ~ 경매의 끝까지 토큰 (사이버 ~ 의회, ETH의 왕좌의 게임 및 사이버 ~ 경매의 참가자)

  - 150 000 000 000 000  링크 게임 참가자를 위한 CYB 토큰

  - 100 000 000 000 000 CYB 토큰은 이더리움, 코스모스 및 Urbit 커뮤니티를 위한 선물로

    ![img](https://github.com/serejandmyself/cyber/raw/master/images/CYB.svg?sanitize=true)

창세기 이후 CYB 토큰은 점령 및 슬래시 매개 변수에 따라 영웅만 만들 수 있습니다. 기본 합의는 새로 생성 된 CYB 토큰이 이해 관계자의 처분에 있다는 것입니다.

현재 최대 CYB 토큰 양과 같은 것은 없습니다. 이것은 네트워크의 영웅들에게 지급되는 지속적인 인플레이션 때문입니다. CYB 토큰은 uint64를 사용하여 구현되므로 CYB 토큰을 추가로 만들면 상태 변경 및 순위를 계산하는 데 훨씬 더 비용이 많이 듭니다. 우리는 CYB 토큰의 완전한 초기 배포 및 스마트 계약의 기능 활성화 후 거버넌스 시스템에 의해 평생 통화 전략이 수립 될 것으로 기대합니다. 인플레이션의 시작 매개 변수는 링크 의 게임 동안 거버넌스를 통해 정의됩니다.

## THC

에 대한 대안을 만드는 목표 [Google-like](https://google.com/) 구조는 다양한 그룹의 특별한 노력이 필요합니다. 따라서 우리는 아라곤 DAO와 같은 분산 된 엔진을 통해 관리되는 사이버 ~ 재단을 기금으로 설립하기로 결정했습니다. 그것은 ETH로 청구되고 초기 배포에 참여한 에이전트에 의해 관리됩니다. 이 접근 방식은 네이티브 플랫폼 토큰의 과도한 시장 투기로부터 보호 할 수 있습니다. - [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 이에 따라 1년 이내에 안정적인 개발을 보장할 수 있습니다. 또한 이러한 요구가 발생할 경우 기본 플랫폼을 다양화하고 프로토콜을 다른 합의 컴퓨팅 아키텍처로 확장할 수 있습니다.

기부에 대한 토큰을 선택하는 동안, 우리는 세 가지 주요 기준을 따랐다 : 토큰은 (1) 가장 유동적인 중 하나, (2) 가장 유망한 것이므로 지역 사회는 그러한 거인과 비교하여 경쟁력을 갖출 수있는 견고한 투자 가방을 확보 할 수 있습니다. [Google](https://google.com/), (3) 제3자에 의존하지 않고 경매 및 결과 조직을 실행할 수 있는 기술적 능력을 가진다. 이러한 기준과 일치하는 유일한 시스템은 이더리움이므로 기부의 기본 토큰은 ETH입니다.

제네시스 사이버 ~ 재단은 다음과 같이 세분화 750 000 000 000 000  THC (칠백 오십 테라스크)를 채굴했다 :

- 600 000 000 000 000  THC 토큰은 사이버 ~ 경매 계약에 할당됩니다

- 150 000 000 000 000 THC 토큰은 사이버 ~ 의회 계약에 할당됩니다

  ![img](https://github.com/serejandmyself/cyber/raw/master/images/THC.svg?sanitize=true)

사이버 ~재단의 모든 결정은 THC 투표 결과에 따라 실행됩니다. 다음 매개 변수가 적용됩니다.

- 지원: 51%
- 정원회: 51%
- 투표 시간: 500시간

## Gift

우리는 가능한 한 많은 에이전트에 대한 제안 된 접근 방식을 평가 할 수있는 기능을 제공하고자합니다. 그러나 KYC 및 / 또는 captcha와 같은 복잡성을 추가하지 않고. 그래서 우리는 8%의 선물을 선택했습니다. [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 창세기에서 이더리움으로, 코스모스에 1%, 우르빗 커뮤니티에 1%를 제공합니다. 창세기를 재현하기 위해 다음 규칙이 적용됩니다.

- 이더리움 재단 네트워크 내의 모든 계정( 계약이 아닌 최소 1개의 발적 거래) 및 블록 8080808에 0.001 ETH보유

- 블록 2000000에서 코스모스 허브-3 내의 모든 0이 아닌 계정

- 은하(30%), 별(30%), 행성(40%)을 보유한 모든 계정 개체 수에 따라 블록 10677601에서

  

이 선물의 주요 목적은 창세기의 모든 계정이 적어도 1개의 [cyberlink](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 네트워크가 언로드될 때 24시간 의 공간에 있습니다. 그래서 분포 곡선을 좀 더 균등하게 만들고 근본적으로 이차 곡선으로 변경하기로 결정했습니다. 따라서, 우리는 배포 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 스냅샷 중에 각 계정 잔액의 제곱근에 비례하여 토큰을 생성합니다. 이차 디자인으로 게임이 너무 쉽기 때문에, 우리는 분산의 양을 계산했습니다 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 이 사실이 대중에게 알려지기 전에 제안 된 블록에 대한 토큰. 우리는 Urbit 외계인에 이차 규칙을 적용하지 않습니다.

## 링크의 게임

ATOM에서 코스모스 호들러를위한 게임. 참가자들은 CYB에 대한 대가로 ATOM을 기부합니다. ATOM이 더 많이 기부될수록 CYB의 가격이 높아지게 됩니다. 이 게임은 1 GCYB 당 1 ATOM에서 시작합니다. 이 게임은 이륙 기부금이 시작된 지 146일이 지났거나 가격이 시작 가격보다 5배 상승한 경우 끝났습니다. 의 가격은 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 이륙 하는 동안 다음 함수에 의해 정의 됩니다.

f(c) = 40 * c + 1000

여기서 f(c)는 ATOM의 TCYB 가격이며, c는 이륙 시 획득한 TCYB 토큰의 양입니다.

핵심 아이디어는 테이크 오프 기부 라운드가 더 잘 수행 될수록 분야의 참가자가 더 많은 지불금을 받게됩니다. 100 [TCYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 핵심 아이디어는 테이크 오프 기부 라운드가 더 잘 수행 될수록 분야의 참가자가 더 많은 지불금을 받게됩니다. 100 ... [TCYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 링크 게임 분야의 참가자에게 할당됩니다. 모든 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 토큰은 게임이 끝날 때 커뮤니티 풀에 할당됩니다. 모든 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) tokens that remain from the disciplines are 사이버 ~ 의회에 할당. CYB 토큰 외에도, 링크의 게임은 결승전에 대한 모든 테이크 오프 기증자에게 테스트 EUL 토큰을 할당합니다. A. [자세한 문서](https://cybercongress.ai/game-of-links/) 게임에 대한 규칙과 조항이 게시되었습니다.

## Cyber~경매

ETH에서 이더리움 호들러를위한 게임. 참가자는 THC에 대한 대가로 ETH를 기부합니다. 더 많은 ETH가 기부될수록 THC의 가격이 높아지게 됩니다. 이 게임은 ETH에서 이륙의 5 배 종가인 가격에서 시작합니다. 게임이 시작된 지 888일이 지났거나 가격이 시작 가격보다 5배 증가한 경우 게임이 끝났습니다. 이 단계에서 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 토큰은 지속적으로 사이버 ~ 의회에 의해 배포됩니다, 기득권을 기반으로 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 경매가 끝날 때까지 토큰을 판매합니다. 권리가 주어진 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 토큰은 토큰을 받을 수 있는 기능을 제공합니다. [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 이에 따라 사이버~재단 내에서 의결권을 행사할 수 있습니다. 의 가격은 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 사이버 ~ 경매 중 다음 기능에 의해 정의됩니다 :

g(t)= 1/30 * t * p + 5 * p

여기서 g(t)는 ETH의 TTHC 가격이며, t는 사이버~경매에서 획득한 TTHC 토큰의 양이며, p는 마감 순간에 ETH로 변환된 CYB 1개에 대한 이륙의 결과 가격입니다.

시작 가격은 제네시스 이전에 하드웨어 및 소프트웨어 인프라에 투자할 위험에 대해 테이크오프 참가자에게 5배의 프리미엄을 제공하도록 설계되었습니다. 사이버 ~경매는 초기 참여자들에게 상당한 인센티브를 제공합니다. 배포가 끝나면 참가자는 배포를 잠금 해제할 수 있습니다. [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 양도, 교환 등 원하는 대로 사용할 수 있습니다. 경매의 결과로, 지역 사회는 아라곤 조직 내에서 기부 된 모든 ETH에 액세스 할 수 있습니다. 사이버 ~ 경매가 끝나면 나머지 모든 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 사이버 ~ 경매 계약은 입증 연소해야합니다. 다음 규칙은 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 토큰은 [배포용 멀티시그](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j):

- 사이버 - 의회는 지분을 위임하지 않을 것이며, 그 결과, 그것은 분산 될 때까지 소극적 인 지분으로 남아있을 것입니다.
- 사이버 ~ 경매의 끝 후, 나머지 모든 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 토큰은 반드시 연소되어야 합니다.

## Apps

제안된 알고리즘이 기본적으로 고품질 지식을 보장하지는 않는다고 가정합니다. 신생아처럼, 더 발전하기 위해 지식을 습득해야합니다. 프로토콜 자체는 하나의 간단한 도구만 을 제공합니다. [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 두 콘텐츠 주소 사이에 에이전트 지분.

검색 품질을 결정하는 에이전트 및 기타 도구의 관심사에 대한 의미 론적 핵심, 행동 요인, 익명 데이터 분석은 다음과 같은 스마트 계약 및 오프 체인 응용 프로그램을 통해 달성 할 수 있습니다. [웹3 브라우저](https://github.com/serejandmyself/cyber/blob/master/cyber.md#browzers), 분산 된 소셜 네트워크 및 콘텐츠 플랫폼. 우리는 지역 사회와 주인의 이익이 이니디아를 구축하는 것이라고 믿습니다.l [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 유지합니다. 따라서 그래프의 경우 가장 관련성이 있는 검색 결과를 제공합니다.

일반적으로, 우리는 응용 프로그램의 세 가지 유형을 구별 [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph):

- 합의 앱. 재량에 따라 실행할 수 있습니다. [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 지능형 능력을 추가하여
- 온체인 앱. 에 의해 실행할 수 있습니다. [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 가스 에 대한 대가로
- 오프 체인 앱. 를 사용하여 구현할 수 있습니다. [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 실행 환경 내의 입력으로

다음, 상상할 수 있는, 애플 리 케이 션의 목록은 위에서 언급 한 범주를 통합:

Web3 브라우저. 현실에서, 브라우저와 검색은 분리 할 수 있습니다. 그것은 web2 검색을 기반으로 본격적인 web3 브라우저의 출현을 상상하기 어렵다. 현재 블록체인과 분산 기술을 중심으로 브라우저를 개발하기 위한 몇 가지 노력이 있습니다. 그들 모두는 web3에 web2를 포함시키려고 노력하여 고통을 겪습니다. 우리의 접근 방식은 조금 다릅니다. web2는 web3에 대한 안전하지 않은 하위 집합으로 간주합니다. 그래서 우리는 실험적인 웹3 브라우저인 Cyb을 개발하여 [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 더 나은 쿼리에 응답하고 콘텐츠를 더 빠르게 전달할 수 있습니다.

소셜 네트워크. 소셜 네트워크는 그 신비하지 않습니다. 모든 소셜 네트워크 콘텐츠에서 왕입니다. 따라서, 입증 순위는 모든 소셜 네트워크의 기본 빌딩 블록입니다. 모든 유형의 소셜 네트워크는 [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). 또한 사이버는 사용자 간의 관련성에 따라 소셜 네트워크를 만들 수 있으며, 현재 네트워크에서는 달성할 수 없습니다.

프로그래밍 가능한 의미 체계. 현재, 거대한 의미 론적 핵심에서 가장 인기있는 키워드는 [Google](https://google.com/) 다음과 같은 앱의 키워드는 다음과 같습니다. [Youtube](https://youtube.com/), [Facebook](https://facebook.com/), [GitHub](https://github.com/), etc. 그러나, 이러한 성공적인 애플 리케이션의 개발자는 설명 할 수있는 능력이 매우 제한되어 [Google](https://google.com/) 검색 결과를 더 나은 방식으로 구성하는 방법을 제공합니다. Tthe [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 접근 방식은 개발자에게 이 권한을 다시 제공합니다. 이제 개발자는 특정 의미 체계 코어를 대상으로 지정하고 원하는 대로 앱을 인덱싱할 수 있습니다.

작업을 검색합니다. 제안 된 디자인은 블록 체인 (및 얽힘 - 모두) 자산 관련 활동에 대한 기본 지원을 가능하게합니다. (1) 작성자가 소유한 응용 프로그램을 디자인하는 것은 간단하며, (2) 검색 결과에 올바르게 표시되고 (3) (4) 검색 쿼리에 대한 변환의 입증 가능한 어트리뷰션과 함께 거래 가능한 작업을 허용합니다. 전자 상거래는 모든 사람에게 이렇게 쉬운 적이있다.

오프라인 검색. IPFS를 사용하면 글로벌 인터넷 연결이 없는 환경에서 문서를 쉽게 검색할 수 있습니다.. [go-cyber](https://github.com/cybercongress/go-cyber) IPFS를 사용하여 배포할 수 있습니다. 이것은 유비쿼터스, 오프라인 검색에 대한 가능성을 만듭니다!

명령 도구. 명령줄 도구는 검색 엔진의 관련성 있고 구조적인 답변을 사용할 수 있습니다. 실질적으로 다음과 같은 CLI 도구를 구현할 수 있습니다.

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

CLI 내에서 검색 도구는 필연적으로 로봇 전용 의미 론적 코어의 경쟁이 치열한 시장을 만들 것입니다.

자율 로봇. 블록 체인 기술은 디지털 자산을 스스로 관리 할 수있는 장치를 만들 수 있습니다..

```
If a robot can store, earn, spend and invest - they can do everything you can do
```

필요한 것은 특정 물건을 찾을 수있는 능력을 가진 간단하면서도 강력한 상태 현실 도구입니다.. [go-cyber](https://github.com/cybercongress/go-cyber) 최소한의 데이터 소스를 제공하지만 지속적으로 자체 개선되는 데이터 소스를 제공하므로 경제적으로 합리적인 로봇프로그래밍에 필요한 도구를 제공합니다. 에 따르면 [상위 10,000개의 영어 단어](https://github.com/first20hours/google-10000-english) 영어에서 가장 인기있는 단어는 특정 항목에 대한 포인터를 의미하는 정의 기사 'the'입니다. 이 사실은 다음과 같이 설명 할 수 있습니다 : 특정 항목은 우리에게 가장 중요합니다. 그러므로 우리 본질은 독특한 것을 찾는 것입니다. 따라서 로봇에게도 독특한 것들에 대한 이해가 필수적입니다.

언어 수렴. 프로그래머는 에이전트가 사용할 언어에 신경 쓰지 말아야 합니다. 에이전트가 검색을 수행하는 언어를 알 필요가 없습니다. 전체 UTF-8 스펙트럼이 작동합니다. 의미 체계 코어는 열려 있으므로 쿼리에 응답하기 위한 경쟁이 여러 도메인별 영역에 분산될 수 있습니다. 다양한 언어에 대한 의미 론적 코어를 포함. 이러한 통일된 접근 방식은 사이버~바하사에 대한 기회를 창출합니다. 인터넷의 새벽부터, 우리는 빠른 언어 융합의 과정을 관찰. 우리는 국적, 언어, 인종, 이름 또는 인터넷 연결과 는 별개로 전 세계에 걸쳐 진정한 글로벌 단어를 사용합니다. 진정한 글로벌 언어의 꿈은 무엇을 의미하는지에 동의하기 어렵기 때문에 배포하기가 어렵습니다. 그러나 우리는 이 꿈을 실현할 수 있는 도구가 있습니다. 단어가 짧을수록 사이버 ~ 랭크가 더 강력해질 것이라고 예측하는 것은 어렵지 않습니다. 사이버 ~순위에 의해 정렬 된 기호, 단어 및 구의 글로벌, 공개적으로 사용할 수있는 목록은 에서 제공하는 해당 링크 [go-cyber](https://github.com/cybercongress/go-cyber) 모두가 받아 들일 수있는 진정한 글로벌 언어의 출현을위한 기초가 될 수 있습니다. 최근 [과학적 진보](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1) 기계 번역에서 아슬 아슬하지만 구글 규모의 훈련 된 모델없이 적용하고자하는 사람들에게 의미가 없습니다. 제안 된 사이버 ~ 순위는 정확하게이것을 제공합니다.

자기 예측. A. [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 지속적으로 구축할 수 있습니다. [knowledge graph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 그 자체의 존재를 예측 [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 이러한 예측을 해당 상태에 적용합니다. 따라서, [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 경제적 합의에 참여할 수 있습니다. [cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 프로토콜.

유니버설 오라클. A. [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 가장 관련성이 높은 데이터를 키-가치 저장소에 저장할 수 있습니다. 키가 CID이고 값이 실제 콘텐츠의 바이트인 위치입니다. 이는 에이전트가 정리하고자 하는 CID 값과 적용하려는 값에 대해 매 라운드마다 결정을 내릴 때 달성될 수 있습니다. 내 콘텐츠 주소의 유틸리티 측정에 따라 [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph). 유틸리티 측정 값을 계산하기 위해 영웅은 가장 높은 콘텐츠 주소의 콘텐츠 가용성 및 크기를 확인합니다. [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph), 그런 다음 CID의 크기와 순위에 가중치를 둡니다. 긴급 키-값 스토리지는 다음에 쓸 수 있습니다. [합의 컴퓨터](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 에이전트에 대해서만 사용할 수 없습니다. 그러나 프로그램에서 값을 사용할 수 있습니다.

위치 인식 검색. 구성할 수 있습니다. [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 와 함께 [위치 증명](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) 와 같은 현저한 기존 프로토콜을 기반으로 합니다. [Foam](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG). 따라서 web3-agents가 삼각측량을 채굴하고 연결하는 경우 위치 기반 검색도 입증됩니다. [위치 증명](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) 연결된 모든 체인에 대해

링크 관련성에 대한 예측 시장. 우리는 의 순위를 사용하여이 아이디어를 구현할 수 있습니다 [지식 그래프](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 링크 관련성에 대한 예측 시장을 기반으로 합니다. 링크 관련성에 베팅할 수 있는 앱은 약관 방향에 대한 고유한 진실의 원천이 될 수 있으며 에이전트가 더 많은 링크를 제출하도록 동기를 부여할 수 있습니다.

개인 사이버 링크. 개인 정보 보호는 기본입니다. 우리는 개인 정보 보호를 위해 최선을 다하고 있지만, 개인 의 구현을 달성 [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 창세기까지 우리 팀에 대 한 불가능. 따라서 프로토콜 위에 실행될 수 있는 WASM 프로그램에서 작업하는 것은 커뮤니티의 것입니다. 문제는 사이버 ~순위를 계산하는 것입니다. [cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 이전 요청이나 공개 키를 공개하지 않고 웹3 마스터가 제출했습니다. 제로 지식 증명은 일반적으로 매우 비쌉니다. 우리는 검색의 개인 정보 보호가 의도적으로 기능해야한다고 생각하지만,이 단계에서 구현하는 방법을 알고 있는지 확실하지 않습니다.. [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk) 재귀 스나크와 같은 [MimbleWimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg) 구조, 이론적으로, 개인 정보 보호 문제의 일부를 해결할 수 있습니다. 그러나, 그들은 새로운, 테스트되지 않은 어쨌든, 자신의 투명 한 대안보다 계산에 관해서 더 비싼 것입니다.

이것은 확실히 모든 가능한 응용 프로그램의 과도 한 목록, 하지만 참으로 매우 흥미로운 하나.

## 결론

우리는 관련성에 대한 합의 컴퓨터 간의 입증 가능한 통신을 위한 프로토콜을 정의하고 구현했습니다. 이 프로토콜은 사이버 링크를 사용하여 에이전트에 의해 생성되는 지식 그래프의 간단한 아이디어를 기반으로합니다. 사이버 링크는 관련 기계의 개념을 사용하여 합의 컴퓨터에 의해 처리됩니다. 사이버 컨센서스 컴퓨터는 CIDv0/CIDv1을 기반으로 하며 go-IPFS 및 Cosmos-SDK를 기초로 사용합니다. IPFS는 리소스 소비와 관련하여 상당한 이점을 제공합니다. 기본 개체로서의 CID는 단순성에서 견고합니다. 모든 CID에 대해 사이버 ~랭크는 단일 실패 지점 없이 합의 된 컴퓨터에 의해 계산됩니다. Cyber~Rank는 CYB 토큰 가중 페이지랭크로, 시빌 공격과 이기적인 투표로부터 경제적 보호를 받고 있습니다. 랭크와 그래프 나무의 머클 루트를 둘러볼 때마다 게시됩니다. 따라서 모든 컴퓨터는 다른 컴퓨터에 주어진 CID에 대한 가치의 관련성을 증명할 수 있습니다. Sybil 저항은 대역폭 제한을 기반으로 합니다. 프로그램을 실행하는 임베디드 기능은 영감을 주는 애플리케이션을 제공합니다. 시작 주요 목표는 피어 투 피어 콘텐츠 주소 시스템의 인덱싱, 같은 상태 비히클, 같은: IPFS, 군단, 시아, Git, 비트 토런트, 또는 상태 상태, 같은: 비트 코인, 이더리움 및 기타 블록 체인 및 얽힘. 사이버 링크의 제안 된 의미 체계는 합의 컴퓨터 자체에 의해 개체 사이의 의미있는 관계를 예측하기위한 강력한 메커니즘을 제공합니다. 관련성 시스템의 소스 코드는 오픈 소스입니다. 컨센서스 컴퓨터에 의해 축적된 모든 데이터는 처리할 리소스가 있는 경우 누구나 사용할 수 있습니다. 제안된 소프트웨어 구현의 성능은 원활한 상호 작용에 충분합니다. 제안된 구현의 확장성은 현재 존재하는 모든 자체 인증 데이터를 인덱싱하기에 충분하며 Great Web의 수백만 에이전트에게 제공할 수 있습니다. 블록 체인은 표준 거버넌스 모듈을 갖춘 Tendermint 합의 알고리즘에 따라 작동하는 슈퍼 인텔리전스에 의해 관리됩니다. 시스템은 기존의 검색 엔진에 대한 대안을 제공하는 데 필요한 유틸리티를 제공하지만, 이 사용 사례에 국한되지 않습니다. 이 시스템은 다양한 응용 분야에 대해 확장 가능하며 주변의 물체를 자율적으로 이해할 수 있는 경제적으로 합리적이고 자율적인 로봇을 설계할 수 있습니다.

## 참조

1. [학술적 맥락 표류](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN)
2. [아주 새로운 스택](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw)
3. [실제로 검색 엔진 정보 검색](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6)
4. [대적 사례 연구를위한 동기 부여 게임](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9)
5. [분산 된 검색의 아이디어](https://ipfs.io/ipfs/QmXNoGTWLQrcFRb66oS4HafpP1vcLKbVkJrQm4DVvihuoq)
6. [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps)
7. [DAT](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR)
8. [go-cyber](https://github.com/cybercongress/go-cyber)
9. [코스모스--sdk](https://github.com/cosmos/cosmos-sdk)
10. [CIDv1](https://github.com/multiformats/cid#cidv1)
11. [cyber.페이지](http://cyber.page/)
12. [듀라](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md)
13. [식민지](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj)
14. [트루비트](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)
15. [예측의 열역학](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb)
16. [페이지 랭크](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw)
17. [RFC-6962](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG)
18. [IBC 프로토콜](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk)
19. [텐더민트](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ)
20. [웹3 브라우저 비교](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md)
21. [Cyb](https://cyb.ai/)
22. [스프링 랭크](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC)
23. [사이버 프로토콜에서 유효성 검사기 실행](https://cybercongress.ai/docs/go-cyber/run_validator/)
24. [상위 10000 영어 단어](https://github.com/first20hours/google-10000-english)
25. [다국어 신경기계 번역](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1)
26. [거품 폼 ](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG)
27. [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk)
28. [Mimblewimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg)
29. [Tezos](https://ipfs.io/ipfs/QmdSQ1AGTizWjSRaVLJ8Bw9j1xi6CGLptNUcUodBwCkKNS)
30. [소프트웨어 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35)
31. [역사 증명](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs)
32. [IPLD](https://github.com/ipld)
33. [사이버 ~ 의회 조직](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330/)
34. [사이버 ~ 사이버 의회](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8)
35. [우주의 사이버 ~ 의회](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a)
36. [CYB 배포용 멀티시그](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j)
37. [.cyber](https://github.com/cybercongress/dot-cyber)

## 인식

1. @hleb-albau
2. @arturalbov
3. @jaekwon
4. @ebuchman
5. @npopeka
6. @belya
7. @serejandmyself
