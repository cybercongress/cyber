# cyber: グレートウェブの知識を計算する 

[![img](https://github.com/serejandmyself/cyber/raw/master/images/graph.png)](https://github.com/serejandmyself/cyber/blob/master/images/graph.png)

## 抄録

コンセンサスコンピュータは、Google、Amazon、Facebookなどのような意見のあるブラックボックスの仲介者を介さずに、証明可能な関連性のある答えを計算することを可能にします。IPFSのようなステートレスでコンテンツアドレス指定可能なピアツーピア通信ネットワークや、Ethereumのようなステートフルコンセンサスコンピュータは、類似した回答を得るために必要な解決策のほんの一部を提供することができる。しかしながら、上述した実施形態には、少なくとも３つの問題点がある。ａ）関連性の主観的な性質。Ｂ）オーバーサイズの知識グラフのためのコンセンサスコンピュータのスケーリングの難しさ。Ｃ）そのようなナレッジグラフの間での品質の欠如。それらは、シビル攻撃のような様々な表面攻撃や、相互作用するエージェントの利己的な振る舞いを受けやすい。本文書では、IPFSオブジェクト間の関連性の証明可能なコンセンサス計算のためのプロトコルを定義する。これは、コンセンサスでGPUを用いて計算されるcyber~RankのTendermintコンセンサスに基づくものである。プルーフ・オブ・ステーク・コンセンサスは初期分布には役に立たないので、エコロジカルで効率的な分布ゲームのための設計を概説する。本研究では、このプロトコルの最小化されたアーキテクチャが、ドメイン固有の知識コンセンサスコンピュータのネットワークを形成する上で重要であると考えている。我々の研究の結果、これまでには存在しなかったいくつかのアプリケーションが出現するであろう。我々は、可能性のある機能と潜在的なアプリケーションのビジョンを持って、この文書を拡張する。。

## グレートウェブ

インターネットの元のプロトコル:TCP/IP、DNS、URL、HTTP / Sなど、ウェブは古い場所に、現在のところある。これらのプロトコルがウェブの初期開発のために生み出したすべての利点を考慮すると、彼らはテーブルに大きな障害をもたらしました。グローバル性は、ウェブの重要な財産であることは、創業以来、本当の脅威にさらされています。ユビキタスな政府の介入によりネットワーク自体が成長し続ける一方で、接続の速度は低下し続けます。後者は、人権に対する実存的な脅威としてプライバシーの懸念を引き起こします。

最初に明らかでない1つのプロパティは、インターネットの日常的な使用と重要になります:永久リンクを交換する能力、したがって、彼らは [ は時間が経過しても壊れません。](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN).ISP は一度に 1 つのアーキテクチャに依存することで、政府は効果的にパケットを検閲できます。これは、私たちの子供たちの将来を懸念するすべてのエンジニアのための伝統的なウェブスタックの最後のドロップです。

他のプロパティは、それほど重要ではないかもしれませんが、オフラインとリアルタイム接続という非常に望ましいものです。平均的なインターネットユーザーは、オフラインの間、彼らがすでに保持している状態で作業を続ける能力を持っているはずです。接続を取得した後、グローバル状態と同期し、リアルタイムで自身の状態の有効性を確認し続ける必要があります。現在、これらのプロパティはアプリケーション レベルで提供されています。これらの特性は、下位レベルのプロトコルに統合する必要があると考えています。

の出現[新しいウェブスタック ](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw) 優れたインターネットの機会を創出します。コミュニティはそれをweb3と呼んでいます。私たちはそれをグレートウェブと呼びます。私たちは、さまざまなタイプの低レベル通信は不変であるべきであり、不変のコンテンツリンクなど、何十年も変わるべきではないと考えています。彼らは、従来のプロトコルスタックの問題を取り除くことに非常に有望なようです。彼らはより高速を追加し、新しい Web へのよりアクセスしやすい接続を提供します。しかし、それはユニークなものを提供する任意の概念で起こるように - 新しい問題が現れます。そのような懸念の1つは、汎用的な検索です。既存の汎用検索エンジンは、制限が厳しい集中管理されたデータベースであり、誰もが信頼を強いられています。これらの検索エンジンは、主に TCP/IP、DNS、URL、および HTTP/S に基づくクライアント/サーバー アーキテクチャ用に設計されました。Great Web は、新しいテクノロジに基づいて、これらの目的のために特別に設計された検索エンジンの課題と機会を作成します。驚くべきことに、無許可のブロックチェーンアーキテクチャにより、従来のアーキテクチャにアクセスできない方法で汎用検索エンジンを構築できます。

## 逆問題の例題について

[検索エンジンの現在のアーキテクチャ](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6) いくつかのエンティティがすべてのたわごとを処理するシステムです。このアプローチは、素晴らしいGoogleの科学者でさえ、まだ解決されていない1つの挑戦的で明確な問題に苦しんでいます。 [敵対的な例の問題](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9).Googleが認める問題は、特定のサンプルが敵対的であるかどうかアルゴリズム的に推論することはむしろ困難であるということです。これは、教育技術自体がどれほど素晴らしいかには思いやりのかたたです。暗号経済的なアプローチは、ゲーム内の受益者を変更することができます。したがって、この方法では、可能なシビル攻撃ベクトルが効果的に削除されます。モデルのクロールや意味の抽出を 1 つのエンティティでハードコーディングする必要がなくなります。代わりに、それは全世界にこの力を与えます。学習シビル耐性、エージェント生成モデルは、おそらく桁の予測結果につながります。

## Cyber プロトコル

そのコアでは、プロトコルは非常にミニマルであり、次の手順で表現することができます。

1. 定義された分布に基づいてサイバープロトコルの起源を計算する
2. の状態を定義します。 [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
3. を使用してトランザクションを収集する [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
4. 署名の有効性を確認する
5. を確認してください。 [帯域幅の制限](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
6. DID の有効性を確認する
7. 署名、帯域幅制限、および IID がすべて有効な場合は、 [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) およびトランザクション
8. の無駄を計算する [サイバー~ランク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberrank) 上の CiD の各ラウンドに対して [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)

このドキュメントの残りの部分では、提案されたプロトコルの根拠と技術的な詳細について説明します。

## ナレッジグラフ

ナレッジグラフは、コンテンツアドレス間の有向リンクの加重グラフとして表します。別名、コンテンツ識別情報、IID、IPFSのハッシュ、または単に - IPFSリンク。この文書では、上記の用語を同義語として使用します。

[![img](https://github.com/serejandmyself/cyber/raw/master/images/knowledge-graph.png)](https://github.com/serejandmyself/cyber/blob/master/images/knowledge-graph.png)

コンテンツ アドレスは基本的に web3 リンクです。不明確で変更可能な代わりに:

```
https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md
```

オブジェクト自体を使用します。

```
Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

コンテンツアドレスを使用して、私たちが得るナレッジグラフを構築することによって [そんなに必要な](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est) [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps) - [という感じで](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR) 検索エンジンに必要なp2pプロトコルの超大国:

- メッシュネットワークの将来性
- 惑星間のアクセシビリティ
- 検閲抵抗
- 技術の独立性

私たちの知識グラフは素晴らしいマスターによって生成されます。マスターは、単一のトランザクション、サイバーリンクの助けを借りて知識グラフに自分自身を追加します。それによって、公開された公開鍵のコンテンツ・アドレスに対する秘密鍵の存在を証明します。これらの力学を使用することにより、 [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 知識グラフ上の主題とオブジェクトの間で、顕著な分化を達成できる。

当社の実装 [ゴーサイバー](https://github.com/cybercongress/go-cyber) に基づいています [コスモスSDK](https://github.com/cosmos/cosmos-sdk) アイデンティティと[シドヴェス/シドヴ1](https://github.com/multiformats/cid#cidv0) コンテンツ アドレス。

マスタは、適用することによって知識グラフを形成します [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).

## Cyberlinks

サイバーリンクの機能を理解するには、URLリンク(別名、ハイパーリンク)とIPFSリンクの違いを理解する必要があります。URL リンクは、コンテンツの場所を指し、IPFS リンクがコンテンツ自体を指しているかどうか。ロケーションリンクとコンテンツリンクに基づくWebアーキテクチャの違いは根本的であり、独自のアプローチが必要です。

サイバーリンクは、2 つのコンテンツ アドレス(IPFS リンク)を意味的にリンクするアプローチです。

```
.md syntax: [QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH](Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH)    
.dura syntax: QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH.Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
```

上記サイバーリンクとは、以下のプレゼンテーションを意味します。 [ゴーサイバー](https://github.com/cybercongress/go-cyber) 中 [サイバー0n](https://etherscan.io/token/0x61B81103e716B611Fff8aF5A5Dc8f37C628efb1E) コスモスのホワイトペーパーを参照しています。サイバーリンクの概念は、任意のp2pネットワークにおける通信形式の単純なセマンティクスに関する慣習です。

[![img](https://github.com/serejandmyself/cyber/raw/master/images/cyberlink.png)](https://github.com/serejandmyself/cyber/blob/master/images/cyberlink.png)

サイバーリンクは、2つのリンク間のリンクを表していることがわかります。簡単に簡単!

サイバーリンクは、単純でありながら、宇宙の予測モデルを構築するための強力な意味構造です。これは、ハイパーリンクの代わりにサイバーリンクを使用することで、汎用検索エンジンの以前のアーキテクチャにアクセスできない超大国を提供します。

サイバーリンクは拡張することができ、すなわち、1つのマスターから2つ以上のサイバーリンクサブシストがある場合、リンクチェーンを形成することができ、最初のサイバーリンクの2番目のリンクは2番目のサイバーリンクの最初のリンクと等しくなります。

[![img](https://github.com/serejandmyself/cyber/raw/master/images/linkchain.png)](https://github.com/serejandmyself/cyber/blob/master/images/linkchain.png)

エージェントが、意味的に豊かな何かとネイティブIPFSリンクを拡張する場合、 [つらい](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md) リンクを使用すると、特定のプログラムによる実行ルールに関するコンセンサスを、より自然なアプローチで得ることができます。

の [ゴーサイバー](https://github.com/cybercongress/go-cyber) サイバーリンクの実装は、 [サイバー](https://github.com/cybercongress/dot-cyber) 実験的なウェブ3ブラウザのアプリ [Cyb](https://cyb.ai/)、または、 [サイバー.ページ](http://cyber.page/).

マスターによって提出されたサイバーリンクは、次に従ってメルクルの木に保存されています [RFC-6962 標準](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG).これにより、認証が可能になります。 [関連性の証明](https://github.com/serejandmyself/cyber/blob/master/cyber.md#proof-of-relevance).

[![img](https://github.com/serejandmyself/cyber/raw/master/images/graph-tree.png)](https://github.com/serejandmyself/cyber/blob/master/images/graph-tree.png)

サイバーリンクを使用して、私たちは、上の被験者とオブジェクトの関連性を計算することができます [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).しかし、私たちは必要です[コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer).

## コンセンサスコンピュータの概念

コンセンサスコンピュータは、エージェント間の相互作用から生じる抽象的なコンピューティングマシンです。コンセンサス コンピュータは、基本的なコンピューティング リソース(メモリと計算)の観点から容量を持っています。エージェントと対話するには、コンピュータに帯域幅が必要です。理想的なコンセンサスコンピュータは、次のコンピュータです。

```
the sum of all the computations and memory available to individuals`
`is equal to`
`the sum of all the verified computations and memory of the consensus computer
```

私たちはそれを知っています:

```
verifications of computations < (computations + verifications of computations)
```

したがって、理想的なコンセンサスコンピュータを達成することは決してできません。CAP 定理とスケーラビリティ トリレンマは、このステートメントにより多くの証明を追加します。

[![img](https://github.com/serejandmyself/cyber/raw/master/images/consensus-computer.png)](https://github.com/serejandmyself/cyber/blob/master/images/consensus-computer.png)

しかし、この理論は、コンセンサスコンピュータのパフォーマンス指標として機能することができます。コンセンサスコンピュータへの投資の6年後、私たちは、そのことを認識するようになりました。 [テンダーミント](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) コンセンサスは、私たちのタスクに必要なクールさと、その生産の準備との間に十分なバランスを持っています。したがって、我々は実装することを決定しました [サイバー](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) コスモスハブに非常に近い設定を持つテンダーミントコンセンサスを使用してプロトコル。 [ゴーサイバー](https://github.com/cybercongress/go-cyber) 実装は、64 バイトの文字列空間に関連する 64 ビットの Tendermint コンセンサス コンピュータです。同じ計算を検証する146のバリデータを持っているので、これは少なくとも1/146として、はるかに理想的ではありません [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

コンセンサスコンピュータの計算、ストレージ、帯域幅の供給を、クエリの最大需要にバインドする必要があります。基本的な場合の計算と保存 [関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 帯域幅に基づいて簡単に予測できます。ただし、帯域幅には制限メカニズムが必要です。

## 関連性マシン

関連性マシンは、状態を遷移するマシンとして定義します。 [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 教えることを希望するエージェントの意志に基づいて、それを研究する [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).意志は、すべての人によって投影されます [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) a master does. The more agents inquire the [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)知識が価値あるほど価値が高くなる。これらの予測に基づいて、コンテンツ・アドレス間の関連性を計算できます。関連性マシンは、クエリを実行して回答を提供することで、検索メカニズムの簡単な構築を可能にします。

関連性マシンの1つの特性が重要です。それは誘導推論特性を持っているか、ブラックボックスの原則に従う必要があります。

```
The machine should be able to interfere with predictions without any knowledge about the objects,`
`except for who, when and what was cyberlinked
```

もし我々が仮定するならば、 [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) リンクされたオブジェクトに関する情報を持っている必要があり、その後、そのようなモデルの複雑さは予測不能に成長します。したがって、メモリと計算のための処理コンピュータの高い要件。ブラックボックスの原則に従う関連性マシンに対処するコンテンツのおかげで、データを保存する必要はありません。しかし、それでも効果的に操作することができます。内部の意味の控除 [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 高価です。したがって、このような設計は仮定の失明に依存することができます。の内部の意味を差し引く代わりに、 [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)を意味する抽出を奨励するシステムを設計しました。これは、必要なマスターのために達成されます [Cyb](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 関連性マシンがランクを計算できる意志を表すトークン。

スパム保護システムの中心には、関連性マシンの進化的成功に既得権益を持つ人だけが書き込み操作を実行できる仮定があります。有効なステークの1%ごとに、 [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) は、ネットワークの帯域幅とコンピューティング機能の 1% を使用する能力を提供します。単純なルールは、エージェントからの悪用を防ぎます:コンテンツ識別者のペアは、アドレスによってサイバーリンクされる可能性があります。

[![img](https://github.com/serejandmyself/cyber/raw/master/images/algo1.png)](https://github.com/serejandmyself/cyber/blob/master/images/algo1.png)

口座の有効なステーク(アクティブな株式+債券)を変更する方法は、直接トークン転送とボンディング操作の2つの方法だけです。

[サイバー](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) は非常に単純な帯域幅モデルを使用します。このモデルの主な目標は、毎日のネットワークの増加を一定に減らすことです。これは、将来のインフラへの投資を予測する能力を持つ英雄(バリデータ)に対応するために行われます。したがって、ここでは「ワット」または「W」を紹介します。各メッセージタイプには W コストが割り当てられています。定数 「DesirableBandwidth」は、W 値によって消費される望ましい '回復ウィンドウ' を決定します。回復期間は、マスタが帯域幅を 0 から最大帯域幅に戻す速度を定義します。マスターは、次の式によって決定される、彼の効果的なステークに比例して最大Wを有する:

```
AgentMaxW = EffectiveStake * DesirableBandwidth
```

期間「アジャスタプライス期間」は、最新のブロックの「回復期間」の期間中に費やされたWの量を合計します。「使用済み帯域幅」/「望ましい帯域幅」の比率は、分数準備率と呼ばれます。ネットワークの使用率が低い場合、小数の準備率はメッセージのコストを調整して、低いステークを持つマスタがコミットするトランザクションを増やすようにします。リソースの需要が増加すると、分数準備率は 1 を超え、その結果、メッセージのコストが増加し、長期的な期間の最終的な tx カウントが制限されます (W リカバリは W 支出になります)。誰も所有している帯域幅のすべてを使用しないため、価格再計算目標期間内に最大100倍の分限準備金を安全に使用できます。このような力学は、作成するための割引を提供します [サイバーリンキング](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)したがって、その需要を効果的に最大化します。提案された設計では、関連性が価値を持つように、完全な帯域幅が必要であることがわかります。

人間の知性は、関連性が無く、重要な記憶が時間の経過とともに忘れられないような方法で組織されています。同じを関連性マシンに適用できます。関連性マシンは実装できます [積極的な剪定戦略](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb)など、形成の歴史の剪定など、 [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)、または関連性の低いリンクを忘れる。

その結果、実装されたサイバノミクスは[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)トークンは、意志表現とスパム保護メカニズムとしてだけでなく、英雄の処理能力と処理に対する市場の需要を調整できる経済規制ツールとしても機能します。関連性マシンのサイバー実装は、サイバー~ランクと呼ばれる非常に簡単なメカニズムに基づいています。

## cyber~ランク

を使用してランキングを行います。 [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) コンセンサス コンピュータには深刻なリソース制約があるため、困難な場合があります。まず、なぜランクをオンチェーンで計算して保存し、同じ方法に従わない必要があるのかを自問する必要があります。 [コロニー](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj) または[トゥルービット](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)?

ランクが内部で計算されたとき [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 1 つは、そのランクのコンテンツ配布に簡単にアクセスでき、簡単に [実現可能なアプリケーションを構築する](https://github.com/serejandmyself/cyber/blob/master/cyber.md#apps) そのランクの上に。したがって、私たちはより宇宙的な建築に従うことにしました。次のセクションでは、[関連性の証明](https://github.com/serejandmyself/cyber/blob/master/cyber.md#proof-of-relevance) このメカニズムにより、ネットワークはドメイン固有の機能を活用して拡張できます。[関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).これらは、IBC プロトコルのおかげで同時に動作します。

最終的には、 [関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) (1)決定論的アルゴリズムを取得する必要があり、それ自体が同類の桁にスケーリングできる、連続的に追加されるネットワーク上のランクの計算を可能にします[Google](https://google.com/).さらに、完全なアルゴリズム(2)は、線形メモリと計算の複雑さを持っている必要があります。最も重要なことは、(3)関連性の存在のための最高の予測能力を持っている必要があります [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).

後[徹底的な研究](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC)では、銀の弾丸を入手することは不可能であることがわかりました。したがって、ネットワークをブートストラップできる、より基本的で防弾的な方法を見つけることにしました。 [ランク](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw) ラリーとセルゲイは、彼らの前のネットワークをブートストラップするために使用されます。元のPageRankの重要な問題は、シビル攻撃に対して耐性がなかったということです。しかし、トークン加重帯域幅モデルによって制限されているトークン加重 PageRank は、シビル攻撃に対して耐性があるため、ナイーブ PageRank の重要な問題を継承しません。当分の間、もっと適したものが現れるまで、サイバー~ランクと呼びます。ジェネシスでの実装には、次のアルゴリズムが適用されます。

[![img](https://github.com/serejandmyself/cyber/raw/master/images/algo2.png)](https://github.com/serejandmyself/cyber/blob/master/images/algo2.png)

私たちは、ランキングメカニズムが常に赤いニシンのままであることを理解しています。そのため、特定の時点で最も適したメカニズムを定義できるオンチェーンガバナンスツールに頼ることを期待しています。ネットワークは、単に主観的な意見に基づくのではなく、ドメイン固有の「ハードスプーン」を通じて経済的なa / bテストに基づいて、あるアルゴリズムから別のアルゴリズムに切り替えることができると仮定します [関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).

cyber~Rankは最も重要な2つの設計決定を保護します:(1)エージェントの現在の意図を説明し、(2)のランクインフレを奨励します。 [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).最初のプロパティは、サイバー〜ランクでゲームができないことを保証します。エージェントが転送を決定した場合 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)トークンはアカウントから外れ、 [関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) すべての調整を行います。 [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) エージェントの現在の意図に従って、このアカウントに関連します。また、エージェントが[CYB](https://github.com/serejandmyself/サイバー/ブロブ/マスター/サイバー.md#cyb)トークンを自分のアカウントに転送した場合も、すべての [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) このアカウントから提出されると、すぐにより多くの関連性が得られます。2番目のプロパティは、過去にセメントを取得するために不可欠です。新しいように [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) を継続的に追加すると、既存のリンクのランクが比例して希薄になります。このプロパティは、最近送信されたという理由だけで、新しいコンテンツのランクが低くなる状況を防ぎます。これらの決定は、最近追加されたコンテンツの推論品質を、長い末尾に提供することを期待しています。 [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

私たちは投票購入の問題について話し合いたいと思います。オカレンスとしての投票購入はそれほど悪くありません。投票購入のジレンマは、投票がそのシステムインフレの割り当てに影響を与えるシステム内に現れます。例えば [スティーム](http://ipfs.io/ipfs/QmepU77tqMAHHuiSASUvUnu8f8ENuPF2Kfs97WjLn8vAS3) または任意のフィアット状態ベースのシステム。投票購入は、価値を追加する必要なしにゼロサムゲームを採用する敵対者にとって簡単に利益を上げることができます。分散検索の当初のアイデアは、このアプローチに基づいていました。しかし、我々はその考えを拒絶し、形成のインセンティブを取り除いた。 [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)コンセンサスレベルに。すべての参加者が予測モデルに影響を与えるためにシステムに何らかの価値をもたらす必要がある環境では、投票購入はNP困難な問題になります。したがって、システムにとって有益となる。

の現在の実装 [関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) は、GPU を利用してランクを計算します。マシンは、64 バイトの CID スペース内の任意の検索要求に対して、適切な結果に応答して配信できます。ただし、ドメイン固有のネットワークを構築するには十分ではありません。 [関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine). [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 互いに関連性を証明する能力を持っている必要があります。

## 関連性の証明

私たちは、検索に関しては、悪意のある行動のようなものは存在しないことを前提にネットワークを設計しました。これは、答えを見つけるつもりで悪意のある行動が見つからないと仮定することができます。このアプローチにより、表面攻撃を大幅に削減できます。

```
Ranks are computed based on the fact that something was searched, thus linked, and as a result - affected the predictive model
```

良いたとえは、観察自体が行動に影響を与える量子力学で観察されます。このため、否定的な投票などの要件はありません。これを行うことで、プロトコルから主観性を取り除き、関連性の証明を定義することができます。

[![img](https://github.com/serejandmyself/cyber/raw/master/images/graph-tree.png)](https://github.com/serejandmyself/cyber/blob/master/images/graph-tree.png)

新しい CID ごとにシーケンス番号が付けられます。番号付けはゼロから始まります。次に、新しい CID ごとに 1 ずつインクリメントします。したがって、インデックスがCIDシーケンス番号である1次元配列にランクを格納することができます。マークルの木の計算は、 [RFC-6962 標準](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG).Merkle のツリーを使用して、特定のコンテンツ アドレスのランクを効果的に証明できます。関連性は本質的に主観的ですが、ある時点で特定のコミュニティに何かが関連していたという集団的証拠があります。

このタイプの証明を使用する任意の2 [IBC 互換](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk) [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 互いに関連性を証明できる。これは、ドメイン固有の [関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine) 繁栄することができます。

共通の関連性において [コンセンサスコンピュータ](https://github.com/cybercongress/go-cyber)Merkle ツリーは、すべてのラウンドを計算し、そのルートハッシュは ABCI にコミットされます。

## スピード

従来のWebアプリケーションの感覚をユーザーに提供するには、即時確認時間が必要です。これは、経済的なトポロジとスケーラビリティを形作る強力なアーキテクチャ要件です。 [サイバー](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) プロトコル。提案されたブロックチェーン設計は、[テンダーミントコンセンサス](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ)アルゴリズムは146のバリデータを備え、速い5秒のtx最終時間を有する。平均確認時間は1秒に近く、複雑なブロックチェーンの相互作用をエージェントにはほとんど見えなくすることができます。

私たちは、1つの特定のを示します[ゴーサイバー](https://github.com/cybercongress/go-cyber) 速度 - ランク計算のコンテキストでプロパティ。コンセンサスの一部として、ラウンド内のトランザクション検証と並行して発生します。ラウンドは、利害関係者によって定義されるコンセンサス変数です。開始時点では、1ラウンドは20ブロックに設定されます。実際には、これは、ネットワークが[ナレッジグラフ]の現在のルートハッシュに100秒ごとに合意しなければならないことを示しています(https://github.com/serejandmyself/サイバー/ブロブ/マスター/サイバー.md#ナレッジグラフ)。これは、すべての [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)提出されたの一部となります。 [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) ほぼ瞬時に50秒の平均期間内のランクを取得します。の初期の頃に [Google](https://google.com/) ランクはおよそ毎週再計算されました。私たちは、グレートウェブのマスターは、リアルタイムでのランキングの変化を観察して喜んでいると信じていますが、このウィンドウで十分であると仮定してネットワークを立ち上げることにしました。の発展に伴い、 [サイバー](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) 各ラウンドの速度が低下します。これは英雄同士の競争によるものです。この関数の桁を速くするメカニズムを認識しています。

- コンセンサスパラメータの最適化

- ランク計算のより良い並列化

- a [より良い時計](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs)コンセンサスの前に

  ## スケーラビリティ

  私たちは[Google](https://google.com/)のようなものの重要性にアイデアをスケールすることを可能にするアーキテクチャを必要とします。そのノードの実装を、次のベースと仮定します。 [コスモスSDK](https://github.com/cosmos/cosmos-sdk) 1 秒あたり 10,000 トランザクションを処理できます。これは、毎日、少なくとも864万人のマスターが100人を提出できることを意味します [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)また、検索結果に同時に影響を与えます。これは、野生のすべての仮定を検証するのに十分ですが、インターネットの現在の規模で動作するとは言うだけでは不十分です。私たちのチームが行っている最先端の研究を考えると、私たちは安全に私たちが必要とするサイズに特定のブロックチェーンをスケーリングすることを可能にするコンセンサス技術が存在しないと述べることができます。そこで、ドメイン固有の概念を紹介します。[ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).

  [![img](https://github.com/serejandmyself/cyber/raw/master/images/network.png)](https://github.com/serejandmyself/cyber/blob/master/images/network.png)

  フォークで独自のドメイン固有の検索エンジンを起動できます。 [ゴーサイバー](https://github.com/cybercongress/go-cyber)に焦点を当て、textit{共通の知識} に焦点を当てています。または、単に既存のチェーン、すなわちコスモスハブにモジュールとして[ゴーサイバー](https://github.com/サイバーコングレス/ゴーサイバー)を差し込みます。ブロックチェーン間通信プロトコルは、間の同期状態の同時メカニズムを導入します[関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).したがって、提案された検索アーキテクチャでは、ドメイン固有 [関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)常識から学ぶことが出来るでしょう。共通の知識がドメイン固有から学べるのと同じように [関連性マシン](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).

  ## ブロウザー

  提案されたネットワークがweb3ブラウザでどのように動作するかを想像したいと考えました。私たちの失望に私たちは[できませんでした](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md) 提案されたアプローチのクールさを実際に示すことができるweb3ブラウザを見つける。このため、Web3ブラウザをゼロから開発することにしました。 [Cyb](https://cyb.ai/) iサンプルを持っているあなたのフレンドリーなロボット[サイバー](https://cyber.page/) と対話するためのアプリケーション [サイバー](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) プロトコル.

  [![img](https://github.com/serejandmyself/cyber/raw/master/images/cyb.jpg)](https://github.com/serejandmyself/cyber/blob/master/images/cyb.jpg)

  配信の良い例として、我々は作成しました [サイバー.ページ](https://cyber.page/).これは、英雄、マスターや伝道者がweb2ゲートウェイを介してプロトコルと対話することができます。サイバーリンクの作成、IPFS へのコンテンツの直接ピン留め、グレート ウェブの検索、サイバーのガバナンスへの参加など。また、詳細なエクスプローラ、財布として機能し、元帳デバイスなどのハードウェア財布をポケットすることができます。

  現在の検索スニペットは醜い。しかし、我々は、彼らが簡単に使用して拡張することができると推測します [IPLD](https://github.com/ipld/specs) 異なる種類のコンテンツに対して。最終的には、彼らはのものよりもさらに魅力的になることができます [Google](https://google.com/).

  [![img](https://github.com/serejandmyself/cyber/raw/master/images/architecture.png)](https://github.com/serejandmyself/cyber/blob/master/images/architecture.png)

  提案されたアーキテクチャの実装中に、我々は少なくとも3つの主要な利点を実現しました。[Google](https://google.com/) おそらく、従来のアプローチでは実現できないでしょう。

  - 検索結果は、任意のp2pネットワークから簡単に配信することができます:例えば.cyberはビデオを再生することができます
  - 支払いボタンは、検索スニペットに埋め込むことができます。つまり、エージェントは検索結果とやり取りでき、例えばエージェントは.cyberでアイテムを購入できます。これは、電子商取引が、変換の帰属を示すおかげで、かなり繁栄できることを意味します。
  - 検索スニペットは静的である必要はありませんが、対話的に使用できます。例えば.cyberはあなたの現在の財布のバランスを提供することができます

  ## 展開

  技術的な制限により、2つのトークンを使用してエコシステムをブートストラップする必要があります。 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) そして[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)

  - [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) は主権者のネイティブトークンです [サイバー](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) テンダーミントコンセンサスアルゴリズムによって動力を与えられたプロトコル。それは3つの主要な用途を有する:(1)コンセンサスのための賭け、(2)送信のための帯域幅制限 [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)、および(3)サイバー〜ランクの計算のためのマスターの意志の表現。
  - [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) (技術として発音)創造的なサイバープロト物質です。 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) サイバー基盤(DAOを支配するコミュニティ)と配布ゲームからのETHを制御する形でユーティリティ価値を持つイーサリアムERC-20互換トークンであること。 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) は、サイバー財団のアラゴン組織の創設時に放出されます。の創造的な力 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 1を受け取る能力から来る [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) token per each 1 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) サイバーの終わりの前に既得権を持つ場合のトークン〜オークション。

  両方のトークンは機能し続け、本質的に非常に異なるユーティリティのために互いに独立して価値を追跡します。

  全体として、展開プロセスは次の構造を持ちます。

  1. サイバー~議会はリンクのゲームを展開します
  2. コミュニティは、リンクのゲームに参加しています
  3. コミュニティは、リンクのゲームからの結果とジェネシスブロックを検証し、提案します
  4. サイバー~議会は、サイバー〜財団とサイバー〜オークションのための契約を展開します
  5. コミュニティは、創世記の後にサイバー〜オークションに参加しています。寄付者のステーク[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 取得するトークン [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) トークン
  6. サイバー~議会が配布 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) サイバー中に継続的にトークン~オークション
  7. サイバー~議会は残りの火傷 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) そして[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 初期配布プロセスの終了に関するトークンとレポート

  サイバー~議会はエテリアムに住んでいます。 [アラゴンダオ](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330).また、運用[サイバーネットワークにおける2-of-3マルチシグ](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8).サイバー~議会は、 [サイバー](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) プロトコル。サイバーの文脈の中で、議会は2つの役割を持っています:

  1. 初期配布プログラムを展開して実行する場合、自動化は不可能です。ETHとATOMの間でメッセージ交換のための信頼できないインフラストラクチャが存在しないため、サイバー・ディー・コングレスは、初期の配信プロセスで単一障害点を導入します。私たちは、送信することにしました [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) トークンの受け取り [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) 今、私たちが作成したネットワークを立ち上げるのにふさわしい時だと感じているので、手動で賭け込む。また、最初の流通プロセスには、継続的なオークションが不可欠であると考えています。サイバー~議会が考えられる理由で配布の面で義務を果たさない場合、私たちはコミュニティがネットワークをフォークアウトし、配布できることを願っています [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)約束されたとおりのトークン。うまくいけば、すべての操作は、明らかに、透過的に設計されています。すべての操作は、 [サイバーネットワーク内の特別な目的2-of-3マルチシグアカウント](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j).
  2. の成長をサポート [サイバー](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) コミュニティがサイバー~財団の形で開発を引き継ぐまでプロトコルを推進します。リンクのゲーム中にATOMでの寄付は、に配布されます[サイバー~議会コスモス2-of-3マルチシグ](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a).サイバーにルーティングされているすべてのATOMの寄付〜議会マルチシグは、その財産になります。ATOMの寄付の役割は次のとおりです:ATOMのおかげで、我々は、コスモスとサイバー生態系の両方の開発におけるサイバー〜議会のためのコミットメントを確保したい。ATOMの寄付は、サイバー〜議会が賭けの報酬を使用し、持続可能な流れに到達することを可能にし、継続的な資金調達のために、 [サイバー](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) どちらもダンプする必要のないプロトコル [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) また、ATOMトークン。

  ## Cyb

  ステークの証明システムは、初期配布には役立たない。初期分布が意図的に設計され、エネルギー効率が高く、実証可能かつ透過的に、したがってアクセス可能な場合、初期[ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 品質とサイズが向上します。

  サイバープロトコルのジェネシスブロックには、1 000 000 000 000 000 CYB(1ペタシブまたは1 PCYB)トークンが次のように分類されています。

  - 750 000 000 000 000 CYBトークンを持っている人のための [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) サイバーの終わりまでトークン~オークション(サイバーの参加者〜議会、ETHとサイバー〜オークションの玉座のゲーム)
  - リンクのゲームの参加者のための150 000 000 000 000 CYBトークン
  - イーサリアム、コスモス、アービットのコミュニティへの贈り物として100 000 000 000 CYBトークン

  [![img](https://github.com/serejandmyself/cyber/raw/master/images/CYB.svg?sanitize=true)](https://github.com/serejandmyself/cyber/blob/master/images/CYB.svg)

  創世記の後、CYBトークンは、賭けとスラッシュのパラメータに基づいて英雄によってのみ作成することができます。基本的なコンセンサスは、新しく作成されたCYBトークンが利害関係者の処分にあるということです。

  現在のところ、CYBトークンの最大量というものはありません。これは、ネットワークの英雄に支払われる継続的なインフレによるものです。CYB トークンは uint64 を使用して実装されるため、追加の CYB トークンを作成すると、状態の変化とランクの計算にかかるコストが大幅に高くなります。我々は、CYBトークンの完全な初期流通とスマートコントラクトの機能の活性化の後、ガバナンスシステムによって生涯にわたる金融戦略が確立されることを期待する。インフレの開始パラメータは、リンクのゲーム中にガバナンスを介して定義されます。

  ## THC

  代替の作成の目標 [グーグルに似ています](https://google.com/) 構造は、様々なグループからの並外れた努力を必要とします。そこで、アラゴンダオなどの分散型エンジンを通じて管理するファンドとしてサイバー~ファウンデーションを設立することにしました。ETHに課金され、初期配布に参加したエージェントによって管理されます。このアプローチにより、ネイティブプラットフォームトークンの過度の市場ダンプから保護することができます - [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) その仕事の最初の年の間に、安定した開発を保障する。さらに、これにより、基盤となるプラットフォームを多様化し、プロトコルを他のコンセンサスコンピューティングアーキテクチャに拡張することができます。

  寄付のトークンを選択しながら、私たちは3つの主要な基準に従いました:トークンは(1)最も液体の1つ、(2)最も有望でなければならないので、コミュニティはそのような巨人と比較しても競争力のある堅実な投資袋を確保することができます [Google](https://google.com/), (3)オークションを実行する技術的能力を有し、結果の組織は、いかなる第三者にも依存することなく、これらの基準に一致する唯一のシステムはイーサリアムであり、したがって、寄付の主なトークンはETHになります。

  創世記サイバー〜財団に先立って、750 000 000 000 000 THC(705テラチ)は次のように分解して採掘しました:

  - 600 000 000 000 000 THCトークンは、サイバーに割り当てられている〜オークション契約
  - 150 000 000 000 000 THCトークンは、サイバーに割り当てられている〜議会の契約

  [![img](https://github.com/serejandmyself/cyber/raw/master/images/THC.svg?sanitize=true)](https://github.com/serejandmyself/cyber/blob/master/images/THC.svg)

  サイバー・ファンデーションによる全ての決定は、THC投票の結果に基づいて実行されます。次のパラメータが適用されます。

  - サポート: 51%
  - クォーラム: 51%
  - 投票期間:500時間

  ## ギフト

  私たちは、提案されたアプローチをできるだけ多くのエージェントに評価する能力を与えたいと考えています。しかし、KYCやキャプチャなどの複雑さを加えることなく。そのため、創世記のトークンをイーサリアムに、コスモスに1%、アービットコミュニティに1%を贈ることを選びました。ジェネシスを再現するには、次の規則が適用されます。

  - Ethereum基盤ネットワーク内のすべてのアカウントは、契約ではない少なくとも1つの発信トランザクションを持ち、ブロック8080808で> 0.001 ETHを保持しています
  - ブロック2000000のコスモスハブ3内のすべての非ゼロアカウント
  - 銀河を保有するすべてのアカウント(30%)、星(30%)、または惑星(40%)オブジェクトの数に応じてブロック10677601で

  この贈り物の主な目的は、創世記のすべてのアカウントが少なくとも1を作ることができるようにすることです [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) ネットワークがアンロードされると、24時間のスペースで。そのため、分布曲線をもう少し均等にし、それを2次曲線に根本的に変更することにしました。したがって、私たちは [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) スナップショット中の各口座残高の平方根に比例してトークンを使用します。二次的なデザインはゲームが簡単すぎるので、分散の量を計算しました [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)この事実が一般に知られる前に提案されたブロックのトークン。私たちは、アービットエイリアンに二次ルールを適用しません.

  ## リンクゲーム

  ATOMのコスモスホドラーのためのゲーム。参加者はCYBと引き換えにATOMを寄付します。ATOMが寄付されるほどCYBの価格は高くなります。ゲームは1 GCYBあたり1 ATOMから始まります。ゲームは、離陸寄付の開始から146日が経過したとき、または価格が開始価格から5倍に上昇した場合に終わりました。の価格 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 離陸中は、次の関数で定義されます。

  f(c) = 40 * c + 1000

  ここで、f(c) は ATOM の TCYB 価格で、c は離陸時に獲得した TCYB トークンの量です。

  重要なアイデアは、離陸寄付ラウンドが優れているほど、分野の参加者がより多くの支払いを受け取るようになります。100 [TCYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) は、離陸寄付の参加者に割り当てられ、50 [TCYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) は、ゲーム・オブ・リンクの分野の参加者のために割り当てられます。すべての [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 離陸から残っているトークンは、ゲームの終了時にコミュニティプールに割り当てられます。すべての [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 規律から残っているトークンは、サイバーに割り当てられます〜議会。CYBトークンに加えて、ゲーム・オブ・リンクは、最終的な休暇ドナー全員にテストEULトークンを割り当てます。A[詳細なドキュメント](https://cybercongress.ai/game-of-links/) は、ゲームのルールと規定を持って公開されています。

  ## Cyber~オークション

  ETHのイーサリアム・ホドラーズのためのゲーム。参加者はTHCと引き換えにETHを寄付します。ETHが寄付されるほどTHCの価格は高くなります。ゲームは、ETHの離陸の5倍の終値である価格から始まります。ゲームは、開始から888日が経過したとき、または価格が開始価格から5倍に上昇した場合に終わりました。このフェーズ中 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) tokensは、既得権をもとにサイバー会議によって継続的に配布されます。[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) オークションが終了するまでトークン。帰属 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) トークンは、受け取る能力を提供します[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) それに応じてトークン、およびサイバー〜財団内の投票権。の価格 [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) サイバー中にオークションは、次の機能によって定義されます。

  g(t)= 1/30 * t * p + 5 * p

  ここで g(t) は ETH の TTHC 価格、t はサイバー中に獲得した TTHC トークンの量です。〜オークション、p は閉じ時点で ETH に変換された 1 つの CYB の離陸の結果の価格です。

  開始価格は、ジェネシスの前にハードウェアとソフトウェアインフラストラクチャに投資するリスクに対して、離陸参加者に5倍のプレミアムを与えるように設計されています。サイバー~オークションは、初期の参加者に大きなインセンティブを与えます。配布が終了すると、参加者は [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc) トークンを使用し、彼らが望むようにそれらを使用します, すなわち、転送, 交換, 等.オークションの結果、コミュニティはアラゴンの組織内で寄付されたすべてのETHにアクセスできるようになります。サイバーの終了後、オークション、残りはすべて [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)サイバー上で〜オークション契約は、実証可能に燃やされなければなりません。以下のルールが適用されます。 [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) 以下のトークン [分布のためのマルチシグ](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j):

  - サイバー~議会は、その株式を委任しません、 そして、その結果、それが配布されるまで受動的な株式のままになります
  - サイバーの終わり以降のオークション、残り [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb) トークンは、有効に書き込む必要があります

  ## Apps

  提案されたアルゴリズムは、デフォルトで高品質の知識を保証するものではないと仮定します。新生児と同じように、さらに発展するためには知識を身につける必要があります。プロトコル自体は、単純なツールを 1 つだけ提供します。 [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 2 つのコンテンツ アドレスの間にエージェントが取り付けられている。

  セマンティックコア、行動要因、エージェントの関心に関する匿名データ、および検索の質を決定するその他のツールの分析は、スマートコントラクトやオフチェーンアプリケーションを介して達成できます。 [web3 ブラウザ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#browzers)、分散型ソーシャルネットワークとコンテンツプラットフォーム。私たちは、初期を構築することがコミュニティとマスターの利益であると信じています[ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) とそれを維持する。したがって、グラフでは、最も関連性の高い検索結果を提供します。

  一般に、3種類のアプリケーションを [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph):

  - コンセンサス アプリ。の裁量で実行することができます。 [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) 知的能力を追加することによって
  - オンチェーン アプリ。によって実行することができます。[コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) in exchange for gas
  - オフチェーンアプリ。を使用して実装できます。 [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 実行環境内の入力として

  次のアプリの一覧は、上記のカテゴリを統合します。

  Web3 ブラウザ。実際には、ブラウザと検索は切っても切れない関係にあります。web2検索に基づく本格的なweb3ブラウザの出現を想像するのは難しいです。現在、ブロックチェーンや分散技術の周りにブラウザを開発するためのいくつかの努力があります。それらのすべては、web2をweb3に埋め込もうとすることに苦しんでいます。私たちのアプローチは少し異なります。Web2 は、web3 の安全でないサブセットと見なされます。そこで、実験的なweb3ブラウザ、Cybを開発し、[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) より良いクエリに応答し、より速くコンテンツを配信するアプローチ。

  ソーシャルネットワーク。ソーシャルネットワークは、それほど神秘的ではありません。どんなソーシャルネットワークのコンテンツでも王様です。したがって、立定可能なランキングは、ソーシャルネットワークの基本的な構成要素です。ソーシャルネットワークのすべてのタイプは、簡単に [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).サイバーは、現在のネットワークでは達成できないユーザー間の関連性に基づいてソーシャルネットワークを作成することもできます。

  プログラム可能なセマンティクス。現在、巨大なセマンティックコアの中で最も人気のあるキーワード[Google](https://google.com/)は、次のようなアプリのキーワードです。 [Youtube](https://youtube.com/), [Facebook](https://facebook.com/), [GitHub](https://github.com/)など。しかし、これらの成功したアプリの開発者は、説明する能力が非常に限られています [Google](https://google.com/) 検索結果をより良い方法で構造化する方法。[サイバー](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) この方法は、開発者にこのパワーを取り戻します。開発者は、特定のセマンティクスコアをターゲットにして、自分の望むようにアプリをインデックス化できるようになりました。

  検索アクション。提案された設計により、ブロックチェーン(およびもつれ)アセットに関連するアクティビティのネイティブサポートが可能になります。(1)クリエイターが所有するアプリケーションを設計するのは簡単で、(2)検索結果に正しく表示され、(3)検索クエリの変換を示す(4)のアトリビューションを伴う取引可能なアクションを許可します。電子商取引は、誰にとってもこれほど簡単ではありませんでした。

  オフライン検索。IPFSは、グローバルインターネット接続のない環境から文書を簡単に取得することを可能にします。 [ゴーサイバー](https://github.com/cybercongress/go-cyber) それ自体は IPFS を使用して配布できます。これは、ユビキタス、オフライン検索の可能性を作成します!

  コマンド ツール。コマンドライン ツールは、検索エンジンからの関連する構造化された回答に依存できます。実際には、次の CLI ツールを実装できます。

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

  CLI内から検索ツールは必然的にロボット専用のセマンティックコアの競争の激しい市場を作り出します。

  自律ロボット。ブロックチェーン技術は、デジタル資産を自分で管理できるデバイスの作成を可能にします。

  ```
  If a robot can store, earn, spend and invest - they can do everything you can do
  ```

  必要なのは、特定のものを見つける機能を備えたシンプルで強力なステートリアリティツールです。 [ゴーサイバー](https://github.com/cybercongress/go-cyber) は、経済的に合理的なロボットをプログラミングするために必要なツールを提供する、最小限の、しかし継続的に自己改善データソースを提供します。聞いたところでは [トップ10,000英語の単語](https://github.com/first20hours/google-10000-english) 英語で最も一般的な単語は、特定の項目へのポインタを意味する定義記事'the'です。この事実は次のように説明することができます:特定の項目は私たちにとって最も重要です。ですから、私たちの性質は、ユニークなものを見つけることです。したがって、ロボットにとっても、ユニークなものの理解が不可欠です。

  言語の収束。プログラマは、エージェントが使用する言語を気にしないでください。エージェントが検索を実行している言語を知る必要はありません。UTF-8スペクトラム全体が機能しています。セマンティック コアはオープンであるため、クエリに応答するための競合が、ドメイン固有の領域に分散される可能性があります。さまざまな言語のセマンティック コアを含む。この統一されたアプローチは、サイバー〜バハサのための機会を作成します。インターネットの黎明以降、我々は急速な言語の収束の過程を観察する。国籍、言語、人種、名前、インターネット接続とは無関係に、地球全体で真にグローバルな言葉を使っています。真にグローバルな言語の夢は、何を意味するのかについて合意するのは難しいので、展開するのは難しいです。しかし、私たちはこの夢を実現するためのツールを持っています。単語が短いほど、そのサイバー〜ランクがより強力になることを予測するのは難しいことではありません。サイバーによってソートされたシンボル、単語、フレーズのグローバルな、一般に利用可能なリスト〜ランク、対応するリンクによって提供されます [ゴーサイバー](https://github.com/cybercongress/go-cyber) 誰もが受け入れることができる真にグローバルな言語の出現のための基礎になることができます。最近 [科学的進歩](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1) 機械翻訳では、Googleスケールの訓練を受けたモデルなしでそれらを適用したい人には息をのむが、無意味です。提案されたサイバー〜ランクは正確にこれを提供しています。

  自己予測。A[コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) を継続的に構築することができます。 [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) の存在を予測する独自の上に [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) これらの予測をその状態に適用します。したがって、 [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) の経済的コンセンサスに参加することができます。[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol) プロトコル。

  ユニバーサルオラクル。A [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) は、最も関連性の高いデータをキー値ストレージに格納できます。キーが CID で、値が実際のコンテンツのバイトです。これは、エージェントがどのCID値を剪定し、どの値を適用したいかに関して、すべてのラウンドで決定を下すことによって達成することができます。内のコンテンツ アドレスのユーティリティメジャーに基づいて、 [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).ユーティリティ メジャーを計算するために、ヒーローは、最上部のコンテンツ アドレスの可用性とサイズをチェックします。[ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)を選択し、その後、DID のサイズとそのランクに重みを付ける。緊急のキー値ストレージは、次の [コンセンサスコンピュータ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) エージェントに対してのみ、およびエージェントには使用しません。しかし、値はプログラムで使用できます。

  位置認識検索。を構築することが可能です[サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) と[場所の証明](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) のような顕著な既存のプロトコルに基づいて [泡](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG).その結果、web3 エージェントが三角測量を採掘し、アタッチする場合、ロケーションベースの検索も実行できるようになります。 [場所の証明](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) リンクされたチェーンごとに。

  リンク関連性に関する予測市場。このアイデアは、ランキングを使用して実装できます。 [ナレッジグラフ](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) リンクの関連性に関する予測市場に基づいています。リンクの関連性に賭けることを可能にするアプリは、用語の方向性のための真実のユニークなソースとなり、エージェントがより多くのリンクを提出する動機付けになります.

  プライベートサイバーリンク。プライバシーは基本的なものです。プライバシーに取り組む一方で、プライベートの実装を達成 [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) 創世記までの私たちのチームにとっては不可能です。したがって、プロトコルの上で実行できるWASMプログラムに取り組むのはコミュニティの必要です。問題は、サイバー~ランクを計算することです。 [サイバーリンク](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks) Web3 マスターが、以前の要求も公開キーも明らかにせずに送信します。一般的に、ゼロ知識の証明は非常に高価です。検索のプライバシーは設計上の特徴であるべきだと考えていますが、この段階で実装する方法を知っていることは分かりません。[Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk) 再帰的なスナークと同じように[ミンブルウィンブル](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg) 建設は、理論的には、プライバシーの懸念の一部を解決することができます。しかし、彼らは新しく、テストされていないものであり、とにかく、その透明な代替よりも計算に関して高価になります。

  これは確かにすべての可能なアプリケーションの過剰なリストではなく、確かに非常にエキサイティングなものです。

  ## 結論

  我々は、関連性に関するコンセンサスコンピュータ間の、定型可能な通信のためのプロトコルを定義し、実装した。このプロトコルは、サイバーリンクを使用してエージェントによって生成されるナレッジグラフの単純なアイデアに基づいています。サイバーリンクは、関連性マシンの概念を使用してコンセンサスコンピュータによって処理されます。サイバーコンセンサスコンピュータはCIDv0/CIDv1に基づいており、基盤としてGO-IPFSとCosmos-SDKを使用しています。IPFS は、リソース消費に関して大きなメリットを提供します。CID は、プライマリ オブジェクトとしての堅牢性が高く、そのシンプルさを実現します。すべてのCIDについて、サイバー〜ランクは、単一点障害のないコンセンサスコンピュータによって計算されます。サイバーリートランクはCYBトークン加重PageRankで、シビル攻撃や利己的な投票から経済的保護を受けています。ランクツリーとグラフツリーの各ラウンドのメルクルルートが公開されます。したがって、すべてのコンピュータは、特定の CID に対する値の関連性を他のコンピュータに証明できます。シビル抵抗は帯域幅制限に基づいています。プログラムを実行する組み込み機能は、感動的なアプリケーションを提供します。最初の第一の目標は、IPFS、Swarm、Sia、Git、BitTorrent、またはステートフル(ビットコイン、イーサリアム、その他のブロックチェーンやもつれなど)など、ステートレスなピアツーピアコンテンツアドレスシステムのインデックス作成です。サイバーリンキングの提案されたセマンティクスは、コンセンサスコンピュータ自体によってオブジェクト間の有意義な関係を予測するための堅牢なメカニズムを提供します。関連性マシンのソース コードはオープン ソースです。コンセンサスコンピュータによって蓄積されたデータのすべてのビットは、それを処理するためのリソースがあれば誰でも利用できます。提案されたソフトウェア実装のパフォーマンスは、シームレスな対話のために十分です。提案された実装のスケーラビリティは、現在存在するすべての自己認証データをインデックス化するのに十分であり、それを Great Web の何百万ものエージェントに提供できます。ブロックチェーンは、標準ガバナンスモジュールを使用してTendermintコンセンサスアルゴリズムの下で機能するスーパーインテリジェンスによって管理されています。システムは従来の検索エンジンの代替手段を提供するために必要なユーティリティを提供しますが、このユースケースだけに限定されません。このシステムは、数多くのアプリケーションに拡張可能であり、周囲の物体を自律的に理解できる経済的に合理的な自己所有のロボットを設計することが可能です。

  ## 参照

  1. [学術的文脈の漂流](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN)
  2. [ブランドの新しいスタック](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw)
  3. [検索エンジンの情報検索の実践](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6)
  4. [敵対的な例の研究のための動機付けゲーム](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9)
  5. [分散検索のアイデア](https://ipfs.io/ipfs/QmXNoGTWLQrcFRb66oS4HafpP1vcLKbVkJrQm4DVvihuoq)
  6. [IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps)
  7. [それ](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR)
  8. [ゴーサイバー](https://github.com/cybercongress/go-cyber)
  9. [コスモスsdk](https://github.com/cosmos/cosmos-sdk)
  10. [シドゥヴ1](https://github.com/multiformats/cid#cidv1)
  11. [サイバー.ページ](http://cyber.page/)
  12. [つらい](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md)
  13. [コロニー](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj)
  14. [トゥルービット](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)
  15. [予測の熱力学](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb)
  16. [Pagerank](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw)
  17. [RFC-6962](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG)
  18. [IBC プロトコル](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk)
  19. [テンダーミント](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ)
  20. [web3 ブラウザの比較](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md)
  21. [Cyb](https://cyb.ai/)
  22. [スプリングランク](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC)
  23. [サイバー プロトコルで検証コントロールを実行する](https://cybercongress.ai/docs/go-cyber/run_validator/)
  24. [トップ10000英語の単語](https://github.com/first20hours/google-10000-english)
  25. [多言語神経機械翻訳](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1)
  26. [泡](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG)
  27. [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk)
  28. [ミンブルブル](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg)
  29. [テゾス](https://ipfs.io/ipfs/QmdSQ1AGTizWjSRaVLJ8Bw9j1xi6CGLptNUcUodBwCkKNS)
  30. [ソフトウェア 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35)
  31. [歴史の証明](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs)
  32. [IPLD](https://github.com/ipld)
  33. [サイバー~議会組織](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330/)
  34. [サイバー~サイバー会議](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8)
  35. [サイバー~コスモスの議会](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a)
  36. [CYB 分布のマルチシグ](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j)
  37. [サイバー](https://github.com/cybercongress/dot-cyber)

  ## 謝辞

  1. @hlebアルバウ
  2. @arturalbov
  3. @jaekwon
  4. @ebuchman
  5. @npopeka
  6. @belya
  7. @serejandmyself
