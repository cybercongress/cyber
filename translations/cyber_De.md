# Cyber: Computing the knowledge of the Great Web

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/graph.png" />
</p>

## Abstrakt

Ein Konsens-Computer ermöglicht die Berechnung nachweislich relevanter
Antworten ohne einen meinungsbildenden Vermittler wie zum Beispiel
Google, Amazon oder Facebook in der Mitte. Zustandslose,
inhaltsadressierbare Peer-to-Peer-Kommunikationsnetzwerke wie IPFS und
zustandsbehaftete Konsensus-Computer wie Ethereum können nur einen Teil
der Lösung bieten, die benötigt wird, um ähnliche Antworten zu erhalten.
Es gibt jedoch mindestens 3 Probleme, die mit den eben genannten
Implementierungen verbunden sind. (A) die subjektive Natur der Relevanz.
(B) die Schwierigkeit, Konsens-Computer für übergroße Wissensgraphen zu
skalieren. (C) die mangelnde Qualität solcher Wissensgraphen. Sie sind
anfällig für verschiedene Angriffe, wie z.B. Sybill als auch für
egoistische Vermittler die mit dem Netzwerk agieren. In diesem Dokument
definieren wir ein Protokoll für die belegbare Konsensberechnung von
Relevanz, zwischen IPFS-Objekten, das auf dem Tendermint Konsens von
Cyber-Rank basiert, welcher mit GPU's im Konsens berechnet wird. Da der
Proof-of-stake Konsens bei der Erstverteilung nicht hilfreich ist, haben
wir das Design für ökologische und effiziente Verteilungen skizziert.
Wir glauben, dass eine minimalistische Architektur des Protokolls
entscheidend für die Bildung eines Netzwerks von domänenspezifischen
Wissenskonsenscomputern ist. Als Ergebnis unserer Arbeit werden einige
Anwendungen entstehen, die es noch nie zuvor gegeben hat. Wir werden
dieses Dokument stets mit unserer Vision von möglichen und potentiell
machbaren Anwendungen erweitern.

## Das große Internet

Originalprotokolle des Internets, wie z.B: TCP/IP, DNS, URL und HTTP/S
haben das Internet zu dem gemacht, was es nun ist. Wenn man all die
Vorteile bedenkt, die diese Protokolle für die anfängliche Entwicklung
des Internets gebracht haben, so haben sie zusammen mit ihnen auch
erhebliche Hindernisse auf den mitgebracht. Die Globalität, die eine
lebenswichtige Eigenschaft des Internets ist, ist seit seinen Anfängen
einer realen Bedrohung ausgesetzt. Die Geschwindigkeit der
Netzwerkverbindung nimmt immer weiter ab, während das Internet selbst
aufgrund der allgegenwärtigen staatlichen Eingriffe immer weiterwächst.
Letzteres verursacht Bedenken hinsichtlich der Privatsphäre als
existenzielle Bedrohung der Menschenrechte.

Eine Eigenschaft, die anfangs nicht offensichtlich war, wird mit der
alltäglichen Nutzung des Internets immer klarer: die Fähigkeit,
permanente Links auszutauschen, so dass diese [nicht nach einiger Zeit
nicht mehr zu erreichen
sind](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN).
Die Abhängigkeit von der Architektur eines einzelnen ISP ermöglicht es
Regierungen, Pakete effektiv zu zensieren. Dies ist der letzte Tropfen
der das Fass für jeden Ingenieur im Web-Stack, der sich um die Zukunft
unserer Kinder sorgt, zum Überlaufen bringt.

Andere Eigenschaften mögen zwar nicht so kritisch sein, sind aber
dennoch sehr wünschenswert: Offline- und Echtzeit-Verbindung. Der
durchschnittliche Internetnutzer sollte, auch wenn er offline ist, immer
noch die Möglichkeit haben, mit dem Stand weiter zu arbeiten, den er
bereits hat. Nachdem er eine Verbindung erworben hat, sollte er in der
Lage sein, sich mit dem globalen, aktuellen Stand zu synchronisieren und
weiterhin die Gültigkeit seines eigenen Stands in Echtzeit zu
überprüfen. Derzeit werden diese Eigenschaften auf Anwendungsebene
angeboten. Wir sind der Meinung, dass diese Eigenschaften ebenfalls in
Protokollen auf unterer Ebene integriert werden sollten.

Die Entstehung eines [brandneuen
Web-Stacks](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw)
erschafft eine Chance für ein überlegenes Internet. Die Gemeinschaft
nennt es web3, wir nennen es das großartige Web. Wir sind der Meinung,
dass verschiedene Arten der Kommunikation auf niedriger Ebene
unveränderlich sein und sich über Jahrzehnte nicht verändern sollten,
z.B. unveränderliche Inhaltsverknüpfungen. Sie scheinen sehr
vielversprechend zu sein die konventionellen Protokollstacks Probleme zu
beseitigen. Sie erhöhen die Geschwindigkeit und bieten eine einfache und
leichte zugängliche Verbindung zum neuen Web. Doch wie es bei jedem
Konzept geschieht, das etwas Einzigartiges bietet, tauchen neue Probleme
auf. Eines dieser Probleme ist die allgemeine Suche. Die bestehenden
Suchmaschinen sind restriktive und zentralisierte Datenbanken, denen
jeder vertrauen muss. Diese Suchmaschinen wurden in erster Linie für
Client-Server-Architekturen auf der Grundlage von TCP/IP, DNS, URL und
HTTP/S entwickelt. Das Great Web stellt eine Herausforderung und eine
Chance für eine Suchmaschine dar, die auf neuen Technologien basiert und
speziell für diese Zwecke konzipiert wurde. Überraschenderweise erlaubt
die Architektur der Blockchain, ohne Berechtigungen, den Aufbau einer
Suchmaschine auf eine Art und Weise, die in der Vergangenheit
unzugänglich ist.

## Zum Problem der kontradiktorischen Beispiele

Die [derzeitige Architektur der
Suchmaschinen](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6)
ist ein System, in dem irgendeine Einheit den ganzen Scheiß verarbeitet.
Dieser Ansatz leidet unter einem herausfordernden und eindeutigen
Problem, das selbst von den brillanten Google-Wissenschaftlern noch
nicht gelöst worden ist: [das Problem der kontradiktorischen
Beispiele](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9).
Das Problem, das Google anerkennt, besteht darin, dass es ziemlich
schwierig ist, algorithmisch zu begründen, ob eine bestimmte Probe
kontradiktorisch ist oder nicht. Dies ist unüberlegt, wenn man bedenkt,
wie großartig die Bildungstechnologie an sich ist. Ein
kryptoökonomischer Ansatz kann die Regeln im Spiel verändern. Folglich
kann dieser Ansatz mögliche Sybil-Angriffsvektoren wirksam entfernen. Er
beseitigt die Notwendigkeit, des Modell-Crawlings und der Extraktion von
Bedeutungen durch eine einzige Einheit in hartem Code auszuführen.
Stattdessen gibt er diese Macht der ganzen Welt. Ein lernfähiges,
sybill-resistentes, agentengeneriertes Modell wird wahrscheinlich zu
besser aussagekräftigen Ergebnissen führen.

## Cyber-Protokoll

Im Kern ist das Protokoll sehr minimalistisch und lässt sich mit den
folgenden Schritten ausdrücken:

1.  Berechnen der Genese des Cyber-Protokolls auf der Grundlage der
    definierten Verteilung
2.  Definition des
    [Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
3.  Sammeln von Transaktionen mit einem
    [Konsensuscomputer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
4.  Überprüfung der Gültigkeit der Signaturen
5.  Überprüfung der
    [Bandbreitennutzung](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
6.  Überprüfung ob die Signaturen, Bandbreitenbegrenzung und alle CID's
    gültig sind, anschließend Anwendung von Cyberlink und Transaktionen
7.  Wenn die Signaturen, die Bandbreitenbegrenzung und CIDs alle gültig
    sind, wenden Sie
    [Cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)
    und Transaktionen an
8.  Berechnung des
    [Cyber-Ranks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberrank)
    für jede Runde für die CID's im
    [Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)

Im Rest dieses Dokuments werden das Grundprinzip und die technischen
Einzelheiten des vorgeschlagenen Protokolls erörtert.

## Wissensgraph

Wir stellen einen Wissensgraphen als einen gewichteten Graphen von
gerichteten Verbindungen zwischen Content-Adressen dar. Kurz gesagt,
Inhaltskennungen, CIDs, IPFS-Hashes oder einfach - IPFS-Links. In diesem
Dokument werden wir die oben genannten Begriffe als Synonyme verwenden.

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/knowledge-graph.png" />
</p>

Content-Adressen sind im Wesentlichen Web3-Links. Anstatt das unklare
und veränderliche zu verwenden:

`https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md`

Benutzen wir das Objekt selbst.

`Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH`

Durch die Verwendung von Content-Adressen zum Aufbau des Wissensgraphen
gewinnen wir [die so dringend benötigte](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est)
[IPFS](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps) -
[wie](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR)
die für eine Suchmaschine benötigten, mächtigen P2P-Protokolle:

-   Mesh-Netzwerk zukunftssicher

-   interplanetare Zugänglichkeit

-   Zensur-Widerstand

-   technologische Unabhängigkeit

Unser Wissensgraph wird von den ehrfurchtgebietenden Meistern erstellt.
Die Master fügen sich selbst mit Hilfe einer einzigen Transaktion, einem
Cyberlink, in den Wissensgraphen ein. Dadurch beweisen sie die Existenz
ihrer privaten Schlüssel für Content-Adressen ihrer enthüllten
öffentlichen Schlüssel. Mit Hilfe dieser Mechanik könnte ein
[Konsensuscomputer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
eine nachweisbare Unterscheidung zwischen Subjekten und Objekten auf
einem Wissensgraphen erreichen.

Unsere Implementierung von
[Go-Cyber](https://github.com/cybercongress/go-cyber) basiert auf
[Cosmos-SDK](https://github.com/cosmos/cosmos-sdk)-Identitäten und
Content-Adressen von
[CIDv0/CIDv1](https://github.com/multiformats/cid#cidv0).

Die Master bilden den Wissensgraphen durch Anwendung von
[Cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).

## Cyberlinks

Um zu verstehen, wie Cyberlinks funktionieren, müssen wir den
Unterschied zwischen einem URL-Link (alias ein Hyperlink) und einem
IPFS-Link verstehen. Ein URL-Link zeigt auf den Ort des Inhalts,
wohingegen ein IPFS-Link auf den Inhalt selbst zeigt. Der Unterschied
zwischen Webarchitekturen, die auf Standortverknüpfungen und
Inhaltsverknüpfungen basieren, ist radikal und erfordert einen
einzigartigen Ansatz.

Cyberlink ist ein Ansatz, um zwei Inhaltsadressen oder IPFS-Links
semantisch zu verknüpfen:

````bash
.md syntax: [QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH](Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH)    
.dura syntax: QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH.Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
````

Der obige Cyberlink bedeutet, dass die Darstellung des
[Go-Cybers](https://github.com/cybercongress/go-cyber) während des
[Cyberc0n](https://etherscan.io/token/0x61B81103e716B611Fff8aF5A5Dc8f37C628efb1E)
auf das Cosmos-White-Paper verweist. Das Konzept der Cyberlinks ist eine
Konvention über die einfache Semantik eines Kommunikationsformats in
jedem P2p-Netzwerk:

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/cyberlink.png" />
</p>

Wir sehen, dass ein Cyberlink eine Verbindung zwischen den beiden Links
darstellt. Kinderleicht!

Cyberlink ist eine einfache, aber dennoch mächtige semantische
Konstruktion zum Aufbau eines vorhersagenden Modells des Universums. Das
bedeutet, dass die Verwendung von Cyberlinks anstelle von Hyperlinks uns
mit den Superkräften ausstattet, die für frühere Architekturen von
Suchmaschinen unzugänglich waren.

Cyberlinks können erweitert werden, d.h. sie können Linkchains bilden,
wenn zwei oder mehr Cyberlinks von einem Master bestehen, wobei der
zweite Link im ersten Cyberlink gleich dem ersten Link im zweiten
Cyberlink ist:

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/linkchain.png" />
</p>

Wenn Agenten die nativen IPFS-Links mit etwas semantisch reichhaltigerem
erweitern, z.B. mit
[Dura](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md)-Links,
dann kann ein Konsens über die Ausführungsregeln durch ein bestimmtes
Programm in einem natürlicheren Ansatz erreicht werden.

Die
[Go-Cyber](https://github.com/cybercongress/go-cyber)-Implementierung
von Cyberlinks ist in der
[.cyber](https://github.com/cybercongress/dot-cyber)-Anwendung unseres
experimentellen Web3-Browsers [cyb](https://cyb.ai/) oder unter
[cyber.page](http://cyber.page/) verfügbar.

Die von Mastern eingereichten Cyberlinks werden in einem Merkle-Tree
nach dem
[RFC-6962-Standard](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG)
gespeichert. Dies ermöglicht eine Authentifizierung zum [Nachweis der
Relevanz](https://github.com/serejandmyself/cyber/blob/master/cyber.md#proof-of-relevance).

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/graph-tree.png" />
</p>

Mit Hilfe von
Cyberlinks können wir die Relevanz von Subjekten und Objekten im
[Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
berechnen. Aber wir brauchen einen
[Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer).

## Der Begriff des Konsensus-Computers

Ein Konsensus-Computer ist eine abstrakte Rechenmaschine, die aus der
Interaktion zwischen Agenten entsteht. Ein Konsensus-Computer verfügt
über Kapazitäten in Bezug auf grundlegende Computerressourcen: Speicher
und Berechnung. Für die Interaktion mit Agenten benötigt ein Computer
Bandbreite. Ein idealer Konsensus-Computer ist ein Computer, bei dem:

` die Summe aller Berechnungen und des den Individuen zur Verfügung stehenden Speichers` 
` ist gleich` 
` die Summe aller verifizierten Berechnungen und des Speichers des Konsensus-Rechners` 

Wir wissen das:

` Verifizierungen von Berechnungen < (Berechnungen + Verifizierungen von Berechnungen)` 

Daher werden wir nie in der Lage sein, einen idealen Konsenscomputer zu
erreichen. Das CAP-Theorem und das Skalierbarkeits-Trilemma fügen dieser
Aussage weitere Beweise hinzu.

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/consensus-computer.png" />
</p>

Dennoch kann diese Theorie als Leistungsindikator für einen
Konsensus-Computer dienen. Nachdem wir 6 Jahre lang in
Konsensus-Computer investiert haben, haben wir erkannt, dass der
[Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ)
Konsensus ein ausreichendes Gleichgewicht zwischen der für unsere
Aufgabe erforderlichen Coolness und der Bereitschaft zu seiner
Herstellung aufweist. Deshalb haben wir beschlossen, das
[Cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)-Protokoll
unter Verwendung des Tendermint Konsensus umzusetzen, der sehr eng an
den Cosmos Hub angelehnt ist. Bei der
[Go-Cyber](https://github.com/cybercongress/go-cyber)-Implementierung
handelt es sich um einen 64-Bit-Tendermint Konsensus-Computer, der für
den 64-Byte-String-Space relevant ist. Das ist bei weitem nicht ideal,
zumindest nicht zu 1/146, denn wir haben 146 Validatoren, die dieselben
Berechnungen, die den
[Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
erzeugen, überprüfen.

Wir müssen die Berechnung, Speicherung und Bandbreitenbereitstellung des
Konsensus-Rechners an eine maximale Nachfrage nach Abfragen binden.
Berechnung und Speicherung können im Falle einer grundlegenden
[Relevanzmaschine](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
leicht auf der Grundlage der Bandbreite vorhergesagt werden. Aber
Bandbreite erfordert einen Begrenzungsmechanismus.

## Relevanz-Maschine

Wir definieren eine Relevanzmaschine als eine Maschine, die den Zustand
eines
[Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
auf der Grundlage des Willens der Agenten, die diesen
[Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
lehren und studieren wollen, übergeht. Der Wille wird durch jede
[Cyberverbindung](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks),
die ein Meister herstellt, projiziert. Je mehr Agenten den
[Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
abfragen, desto wertvoller wird das Wissen. Auf der Grundlage dieser
Projektionen kann die Relevanz zwischen den Content-Adressen berechnet
werden. Die Relevanzmaschine ermöglicht eine einfache Konstruktion für
den Suchmechanismus durch Abfrage und Antwortlieferung.

Eine Eigenschaft der Relevanzmaschine ist entscheidend. Sie muss
induktiv schlussfolgernde Eigenschaften haben oder dem Blackbox-Prinzip
folgen:

`Die Maschine sollte in der Lage sein, Vorhersagen ohne Wissen über die
Objekte zu treffen zu können, außer wer, wann und was mit dem Cyberlink verbunden war`

Wenn wir davon ausgehen, dass ein
[Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
einige Informationen über die verknüpften Objekte haben muss, dann wird
die Komplexität eines solchen Modells unvorhersehbar zunehmen. Daher die
hohen Anforderungen des Verarbeitungsrechners an Speicher und
Berechnung. Dank der Inhaltsadressierung muss eine Relevanzmaschine, die
dem Blackbox-Prinzip folgt, keine Daten speichern. Sie kann aber
trotzdem effektiv darauf arbeiten. Die Ableitung von Bedeutung innerhalb
eines
[Konsensus-Computers](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
ist teuer. Daher kann ein solches Design auf der Annahme der Blindheit
beruhen. Anstatt die Bedeutung innerhalb des
[Konsensus-Computers](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
abzuziehen, haben wir ein System entworfen, in dem die
Bedeutungsextraktion gefördert wird. Dies wird dadurch erreicht, dass
die Meister
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)-Token
benötigen, um ihren Willen auszudrücken, auf deren Grundlage die
Relevanzmaschine den Rang berechnen kann.

Im Zentrum des Spam-Schutzsystems steht die Annahme, dass
Schreiboperationen nur von denjenigen ausgeführt werden können, die ein
persönliches Interesse am evolutionären Erfolg der Relevanzmaschine
haben. Jedes 1% der effektiven Beteiligung innerhalb des
[Konsensus-Computers](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
gibt die Möglichkeit, 1% der Bandbreite der möglichen Netzwerke und
deren Rechenkapazitäten zu nutzen. Eine einfache Regel verhindert den
Missbrauch durch die Agenten: ein Paar von Inhaltskennungen darf nur
einmal durch eine Adresse im Cyberspace verlinkt werden.

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/algo1.png" />
</p>

Es gibt nur zwei Möglichkeiten, den effektiven Anteil (aktiver Anteil +
gebundener Anteil) eines Kontos zu ändern: direkte Token-Transfers und
Kautionsgeschäfte.

[Cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
verwendet ein sehr einfaches Bandbreitenmodell. Das Hauptziel dieses
Modells besteht darin, das tägliche Netzwerkwachstum auf eine
vorgegebene Konstante zu reduzieren. Dies geschieht, um Helden
(Validatoren) die Möglichkeit zu geben, zukünftige Investitionen in die
Infrastruktur vorherzusagen. Daher führen wir hier \"Watt\" oder \"W\"
ein. Jedem Nachrichtentyp sind W-Kosten zugeordnet. Die Konstante
\'ErwünschteBandbreite\', bestimmt das wünschenswerte
\'Wiederherstellungsfenster\', das durch den W-Wert ausgegeben wird. Die
Wiederherstellungszeit definiert, wie schnell ein Master seine
Bandbreite von 0 zurück bis zur maximalen Bandbreite wiederherstellen
kann. Ein Meister hat ein Maximum W proportional zu seinem effektiven
Einsatz, der durch die folgende Formel bestimmt wird:

`AgentMaxW = EffectiveStake \* ErwünschteBandbreite`

Der Zeitraum \"AdjustPricePeriod\" fasst zusammen, wie viel W während
des Zeitraums \"RecoveryPeriod\" im letzten Block ausgegeben wurde. Das
Verhältnis \'VerbrauchteBandbreite\' / \'ErwünschteBandbreiten\' wird
als gebrochenes Reserveverhältnis bezeichnet. Wenn die Netzwerknutzung
gering ist, passt das gebrochene Reserveverhältnis die Nachrichtenkosten
so an, dass Master mit einem geringeren Anteil mehr Transaktionen
durchführen können. Wenn die Nachfrage nach Ressourcen zunimmt, steigt
das Mindestreserveverhältnis auf \> 1, wodurch die Kosten der Botschaft
steigen und die endgültige tx-Zählung für einen langfristigen Zeitraum
begrenzt wird (die W-Erholung wird \< dann die W-Ausgaben sein). Da
niemand die gesamte Bandbreite nutzt, die ihm zur Verfügung steht,
können wir innerhalb einer Zielperiode für die Preisneuberechnung sicher
bis zum 100-fachen der fraktionalen Reserven verwenden. Solche
Mechaniken bieten einen Rabatt für die Schaffung von
[Cyberlinking](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks),
wodurch die Nachfrage danach effektiv maximiert wird. Sie können sehen,
dass das vorgeschlagene Design die Nachfrage nach der vollen Bandbreite
benötigt, damit die Relevanz wertvoll wird.

Die menschliche Intelligenz ist so organisiert, dass nicht relevante und
unwichtige Erinnerungen mit der Zeit vergessen werden. Dasselbe kann auf
die Relevanzmaschine angewandt werden. Die Relevanzmaschine kann
[aggressive
Beschneidungsstrategien](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb)
anwenden, z.B. die Beschneidung der Entstehungsgeschichte des
[Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
oder das Vergessen von Verknüpfungen, die weniger relevant werden.

Infolgedessen dient die implementierte Cybernomik der
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)-Token
nicht nur als Willensäußerungs- und Spam-Schutzmechanismus, sondern
fungiert auch als ökonomisches Regulierungsinstrument, das die
Verarbeitungskapazität von Helden und die Nachfrage des Marktes nach
Verarbeitung in Einklang bringen kann. Die Go-Cyber-Implementierung der
Relevanzmaschine basiert auf einem sehr einfachen Mechanismus, der
Cyber\~Rank genannt wird.

## cyber\~Rank

Das Ranking beim Benutzen von einem
[Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
kann herausfordernd sein, da Konsensus-Computer eine strenge Ressourcen
Beschränkung haben. Als ersten müssen wir uns folgendes Fragen: wieso
müssen wir den Rank on-chain berechnen und aufbewahren und können nicht
denselben Weg wie
[Colony](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj)
oder
[Truebit](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)
gehen?

Wenn der Rank innerhalb des
[Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
berechnet wurde, hat man einfachen Zugriff zu der Verteilung des Inhalts
des Ranks und eine einfache Möglichkeit [nachweisbare
Anwendungen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#apps)
auf diesem Rang zu bauen. Daher haben wir entschieden einer kosmischen
Architektur zu folgen. In dem nächsten Abschnitt beschreiben wir den
[proof of
relevance](https://github.com/serejandmyself/cyber/blob/master/cyber.md#proof-of-relevance)
Mechanismus welcher es erlaubt das Netzwerk zu skalieren mithilfe von
domänenspezifischen
[Relevanzmaschine](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)n.
[Diese](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
funktionieren derzeit mit dem IBC Protokoll.

Eventuell muss die
[Relevanzmaschine](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
einen (1) deterministischen Algorithmus enthalten der die Berechnung des
Ranges in einem kontinuierlichen arbeiteten Netzwerk ermöglicht das auf
Größenordnungen von [Google](https://google.com/) skaliert werden kann.
Dazu kommt, ein perfekter Algorithmus (2) muss ein lineares memory und
Rechenkomplexität besitzen. Am wichtigsten ist, dass es die höchste
nachweisbare Vorhersagefähigkeit hat für die Existenz von relevanten
[cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).

Nach [gründlicher
Recherche](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC)
haben wir festgestellt, dass es unmöglich ist eine Wunderwaffe zu
finden. Daher haben wir uns entschieden einen einfacheren kugelsicheren
Weg der das Netzwerk booten kann zu gehen: [Den
Rang](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw)
den Larry und Sergey verwendeten, um ihr vorheriges Netzwerk zu booten.
Das Hauptproblem mit dem ursprünglichen PageRank war, dass er nicht
gegen Sybil-Angriffen resistent war. Jedoch erbt ein token-gewichteter
PageRank, der durch ein tokengewichtetes Bandbreitenmodell begrenzt ist,
nicht das Hauptproblem des naiven PageRank, da er gegen Sybil-Angriffe
resistent ist. Vorerst werden wir es Cyber-Rang nennen, bis etwas
passenderes herauskommt. Der folgende Algorithmus wird auf seine
Implementierung bei Genesis angewendet:

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/algo2.png" />
</p>

Wir verstehen, dass der Ranking Mechanismus immer ein Ablenkungsmanöver
bleiben wird. Aus diesem Grund verlassen wir uns auf die on-chain
Governance Tools die den jeweils am besten geeigneten Mechanismus
definieren können. Wir nehmen an, dass das Netzwerk von einem
Algorithmus zu einem anderen wechseln kann aufgrund von nicht nur
subjectiven Meinungen sondern aufgrund ökonomischen A/B- Tests durch
"hard spooning" der domänenspezifischen
[Relevanzmaschinen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine).

cyber\~Rank schirmt zwei Designentscheidungen ab, die von größter
Wichtigkeit sind: (1) es berücksichtigt die aktuelle Absicht der
Agenten, und (2) es fördert die Ranginflation von
[Cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks).
Die erste Eigenschaft stellt sicher, dass mit cyber\~Rank nicht gespielt
werden kann. Wenn ein Agent beschließt, seine
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)-Token
von seinem Konto zu transferieren, passt die
[Relevanzmaschine](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
alle für dieses Konto relevanten
[Cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)
entsprechend den aktuellen Absichten des Agenten an. Und umgekehrt, wenn
ein Agent
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)-Token
auf sein Konto überweist, gewinnen alle von diesem Konto eingereichten
[Cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)
sofort an Relevanz. Die zweite Eigenschaft ist wesentlich, um nicht in
der Vergangenheit eingefroren zu werden. Da ständig neue Cyberlinks
hinzugefügt werden, werden sie den Rang der bereits bestehenden Links
proportional verringern. Diese Eigenschaft verhindert eine Situation, in
der neue und bessere Inhalte einen niedrigeren Rang haben, nur weil sie
kürzlich eingereicht wurden. Wir erwarten, dass diese Entscheidungen
eine Inferenzqualität für kürzlich hinzugefügte Inhalte am Long Tail des
[Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
ermöglichen.

Wir würden gerne das Problem des Stimmenkaufs diskutieren. Stimmenkauf
als Ereignis ist gar nicht so schlecht. Das Dilemma des Stimmenkaufs
tritt in Systemen auf, in denen die Stimmabgabe die Zuteilung der
Inflationsrate dieses Systems beeinflusst. Zum Beispiel bei
[Steem](http://ipfs.io/ipfs/QmepU77tqMAHHuiSASUvUnu8f8ENuPF2Kfs97WjLn8vAS3)
oder jedem auf einem Fiat-Staat basierenden System. Das Aufkaufen von
Stimmen kann für einen Gegner, der ein Nullsummenspiel anwendet, ohne
die Notwendigkeit, einen Mehrwert zu schaffen, leicht profitabel werden.
Unsere ursprüngliche Idee einer dezentralisierten Suche beruhte auf
diesem Ansatz. Aber wir haben diese Idee verworfen und den Anreiz zur
Bildung des
[Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
auf die Konsensebene verlagert. In einem Umfeld, in dem jeder Teilnehmer
einen gewissen Wert in das System einbringen muss, um das Prognosemodell
zu beeinflussen, wird der Stimmenkauf zu einem NP-harten Problem. Daher
wird es für das System vorteilhaft.

Die aktuelle Implementierung der
[Relevanzmaschine](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
verwendet GPUs zur Berechnung des Rangs. Der Rechner kann auf jede
beliebige Suchanfrage in einem 64-Byte-CID-Raum antworten und relevante
Ergebnisse liefern. Es reicht jedoch nicht aus, ein Netzwerk von
domänenspezifischen
[Relevanzmaschinen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
aufzubauen.
[Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
müssen in der Lage sein, die Relevanz untereinander nachzuweisen.

## Relevanznachweis

Wir haben das Netzwerk unter der Annahme so entworfen als wenn es kein
böswilliges Verhalten in Bezug auf die Suche gibt. Dies kann angenommen
werden, da kein böswilliges Verhalten bei der Suche nach Antworten
gefunden werden kann.  Dieser Ansatz reduziert die Angriffe auf die
Oberfläche erheblich.

````bash
Ranks are computed based on the fact that something was searched, thus linked, and as a result - affected the predictive model
````

Eine gute Analogie wird in der Quantenmechanik beobachtet in der die
Beobachtung selbst das Verhalten beeinflusst. Das ist der Grund wieso
wir keine negative Abstimmung benötigen.  Auf diese Weise entfernen wir
die Subjektivität aus dem Protokoll und können den Relevanz Nachweis
definieren.

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/graph-tree.png" />
</p>

Jede neue CID erhält eine Sequenznummer. Die Nummerierung beginnt bei
null. Dann für jede neue CID um eins erhöht. Daher können wir den Rang
in einem eindimensionalen Array speichern, wobei die Indexe die
CID-Sequenznummern sind. Merkle tree Berechnungen basieren auf den
[RFC-6962
Standard](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG).
Beim Benutzen von Merkle trees können wir effektiv den Rank für jede
gegebene Inhalts Adresse beweisen. Während die Relevanz von Natur aus
immer noch subjektiv ist, haben wir einen kollektiven Beweis dafür, dass
etwas zu einem bestimmten Zeitpunkt für eine bestimmte Community
relevant war. Beim benutzen dieses Beweis Typs können sich zwei
[IBC](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk)
kompatible
[Konsensus-Computers](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
gegenseitig nachweisen. Das bedeutet, dass domänenspezifische
[Relevanzmaschine](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)n
florieren können.

In Bezug auf eine gemeinsame
[go-cyber](https://github.com/cybercongress/go-cyber) Implementation
wird der Merkle tree jede Runde berechnet und sein root-Hash an den ABCI
weitergegeben.

## Geschwindigkeit

Wir benötigen eine sofortige Bestätigung auf Anfragen, um den Nutzern
das Gefühl einer herkömmlichen Webanwendung zu vermitteln. Dies ist eine
machtvolle Architekturale Voraussetzung des ökonomischen Topology und
der Stabilität des
[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
Protokolls. Das vorschlagende Blockchain Design basiert auf den
[Tendermint
Konsensus](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ)
Algorithmus mit 146 Validatoren und hat eine 5 Sekunden schnelle tx
finality time. Die durchschnittliche Bestätigungszeit ist nah an 1
Sekunde und könnte eine komplette Blockchain Interaktion für Agenten
nahezu unsichtbar machen.

Wir bezeichnen eine bestimmte
[go-cyber](https://github.com/cybercongress/go-cyber) Eigenschaft in
diesem Kontext der Geschwindigkeit -- Berechnung des Ranges. Als Teil
des Konsensus, passiert dies parallel zu den Transaktions Bestätigungen
innerhalb der Runden. Eine Runde ist eine Konsensus Variabele die durch
Stakeholder definiert wird. Zu Beginn wird eine Runde auf 20 Blocks
gesetzt. In der Praxis bedeutet dies, dass das Netzwerk alle 100
Sekunden den jetzigen root hash des
[Wissensgraph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)en
bestätigen muss. Das bedeutet, dass jeder eingereichter
[cyberlink](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)
fast direkt ein Teil des
[Wissensgraph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)en
wird und innerhalb eines durchschnittlichen Zeitraumes von 50 Sekunden
einen Rang erhält. In den frühen Tagen von [Google](https://google.com/)
wurde der Rang jede Woche neu berechnet. Wir glauben, dass die Master
des Great Webs gerne das Echtzeitsranking beobachten werden, aber wir
haben entschieden das Netzwerk mit der Annahme zu starten, dass dieses
Fenster ausreicht. Es wird erwartet, dass mit der Entwicklung des
[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
Protokolls die Geschwindigkeit jeder Runde abnimmt. Dies liegt an dem
Wettbewerb zwischen den Heroes. Wir kennen bestimmte Mechanismen um
diese Funktion um Größenordnungen zu beschleunigen:

-   Optimierung des Konsensus Parameters

-   Bessere Parallelisierung der Rangberechnung

-   eine bessere (a [better
    clock](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs))
    Uhr vor dem Konsensus

**Skalierbarkeit**

Wir benötigen eine Architektur welche uns erlaubt die Bedeutung unserer
Idee wie zu [Google](https://google.com/) zu skalieren. Lass uns
annehmen, dass die node Implementation, die auf
[Cosmos-SDK](https://github.com/cosmos/cosmos-sdk) basiert 10k
Transaktionen pro Sekunde berechnen kann. Das würde bedeuten, dass jeden
Tag mindestens 8.64 Millionen Master jeweils 100
[cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)
bestätigen können und gleichzeitig die Suchergebnisse beeinflussen. Dies
reicht aus, um alle Annahmen zu überprüfen, aber nicht genug, um zu
sagen, dass es im aktuellen Internet von der Skalierbarkeit her
funktionieren wird. Nach jetzigem Stand der Forschung unseres Teams
können wir mit Sicherheit behaupten, dass es keine Konsensus Technologie
gibt die die Skalierung einer Blockchain in der Größe in der wir sie
benötigen erlaubt. Daher stellen wir das Konzept von Domänen
spezifischen
[Wissensgraphen](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
vor.

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/network.png" />
</p>


Dies kann entweder auf einer eigenen Domänen spezifischen Suchmaschine
mit [go-cyber](https://github.com/cybercongress/go-cyber) erfolgen
welche auf \\textit{common public knowledge} fokussiert ist. Oder
einfach [go-cyber](https://github.com/cybercongress/go-cyber) als Modul
auf einer existierenden Chain nutzen, z.B. Cosmos Hub. Das
Inter-Blockchain Kommunikationsprotokoll führt gleichzeitige Mechanismen
zum Synchronisieren des Status zwischen
[Relevanzmaschine](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)n
ein. Daher kann in der vorgeschlagenen Such Architektur eine
domänenspezifische
[Relevanzmaschine](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)
aus allgemeinem Wissen lernen. Genauso wie allgemeines Wissen von der
domänenspezifischen
[Relevanzmaschine](https://github.com/serejandmyself/cyber/blob/master/cyber.md#relevance-machine)n
lernen kann.

**Browser**

Wir wollten uns vorstellen, wie das vorschlagende Netzwerk mit einem
Web3-Browser funktionieren würde. Zu unserer Enttäuschung waren wir
nicht in der Lage, einen Web3-Browser zu finden, der die Coolness des
vorgeschlagenen Ansatzes in der Praxis demonstrieren kann. Daher haben
wir uns entschieden einen web3 Browser von Grund auf neu zu entwickeln.
[Cyb](https://cyb.ai/) ist Ihr freundlicher Roboter der als Beispiel
eine [.cyber](https://cyber.page/) Applikation besitzt um mit dem
[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
Protokoll interagieren zu können.

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/cyb.jpg" />
</p>

Als gutes Beispiel haben wir die [cyber.page](https://cyber.page/)
erstellt. Es erlaubt Heroes, Masters und Evangelists mit dem Protokoll
über eine web2 Schnittstelle zu interagieren. Erstelle cyberlinks, sende
Inhalte direkt an IPFS, durchsuche das Great Web, nehme an der
Governance von cyber teil und so weiter. Es kann außerdem als Explorer,
Wallet und Hardware Wallet wie Ledger dienen.

Die aktuellen Suche Ausschnitte sind hässlich. Wir gehen jedoch davon
aus, dass sie mit [IPLD](https://github.com/ipld/specs) problemlos für
verschiedene Arten von Inhalten erweitert werden können. Eventuell
können sie sogar attraktiver als die von [Google](https://google.com/)
werden.

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/architecture.png" />
</p>

Während der Implementation der vorgeschlagenen Architektur haben wir
mindestens 3 Schlüssel Vorteile herausgefunden, die
[Google](https://google.com/) nicht liefern kann mit seinem
konventionellen Ansatz.

-   Die Suchergebnisse können problemlos von jedem P2P-Netzwerk
    geliefert werden, cyber kann Videos abspielen

-   Bezahl Buttons können direkt in die Suche Ausschnitte eingebettet
    werden. Das bedeutet, dass Agenten mit den Suchergebnissen
    interagieren können bzw. Agenten können Dinge direkt in .cyber
    kaufen. Das bedeutet, dass E-Commerce dank einer nachweisbaren
    fairen Konversation gedeihen kann

-   Such Ausschnitte müssten nicht statisch sein aber können interaktiv
    sein z.B. kann .cyber Ihre aktuelle Wallet Balance anzeigen 

## Entwicklung

Aufgrund technischen Beschränkungen müssen wir das Ökosystem mit zwei
Token laufen lassen:
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
und
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)

- [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
ist der ursprüngliche token des souveränen
[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
Protokolls der von dem Tendermint Konsensus Algorithmus unterstützt
wird. Es hat drei verschiedene Hauptnutzen (1) Stacking für Konsensus,
(2) Limitierung der Bandbreite für das abgeben von
[cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks),
und (3) Ausdruck des Willens der Masters für die Berechnung des 
cyber\~Rank.

- [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
(ausgesprochen: Tech) ist eine kreative cyber proto Substanz.
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
ist ein Ethereum ERC-20 kompatibler Token der die Fähigkeit hat Werte in
Form von Kontrolle über die cyber\~Foundation (die Gemeinschaft die DAO
regiert) und das ETH aus den Verteilungsspiel widerspiegelt.
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
wird bei der Erstellung von cyber\~Foundation as an Aragon organization
ausgegeben. Die kreative Macht von
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
kommt von der Möglichkeit einen 1
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
Token pro 1
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
Token zu erhalten wenn vor Ende der cyber\~Auction investiert wurde.

Beide Token bleiben funktionsfähig und behalten unabhängig voneinander
ihren Wert aufgrund ihres von Natur aus sehr unterschiedlichen Nutzens.

Grundsätzlich hat der Entwicklungsprozess folgende Struktur:

1.  cyber\~Congress entwickelt Game of Links

2.  Die Community nimmt an The Game of Links teil

3.  Die Community verifiziert und sag einen Genesis block voraus mit den
    Ergebnissen des Game of Links

4.  cyber\~Congress entwickelt Verträge für cyber\~Foundation und
    cyber\~Auction

5.  Die Community nimmt an der cyber\~Auction nach der Genesis teil.
    Spender stacken
    [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
    Tokens um
    [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
    Tokens zu erhalten

6.  cyber\~Congress verteilt die
    [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
    Tokens kontinuierlich während der cyber\~Auction

7.  cyber\~Congress verbrennt die verbleibenden
    [CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
    und
    [THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
    Tokens und berichtet vom Ende des Erstverteilung Prozesses

cyber\~Congress lebt in Ethereum als ein [Aragon
DAO](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330).
Außerdem operiert es in [2-of-3 multisig in Cyber
network](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8).
cyber\~Congress entwickelt das
[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
Protokoll. Innerhalb des Kontextes von cyber hat der Congress 2 Rollen:

Das Entwickeln und Ausführen des Erstverteilungsprogammes, welches
unmöglich zu automatisieren ist. Weil es keine vertrauenswürdige
Infrastruktur für den Austausch von Nachrichten zwischen ETH und ATOM
gibt, führt cyber\~Congress ein single point of failure in dem Erst
Verteilungsprozess ein. Wir haben entschieden den
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
stackern die
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
Tokens manuell zu senden, da wir denken, dass genau jetzt der richtige
Zeitpunkt ist das Netzwerk zu starten welches wir kreiert haben.
Außerdem glauben wir, dass eine weitergehende Auktion lebenswichtig für
den Erst Verteilungsprozess ist. Falls der cyber\~Congress es nicht
schafft aufgrund von verschiedenen Gründen die Bedingungen der
Verteilung zu erfüllen, hoffen wir, dass die Community es schafft  das
Netzwerk auszubauen und die
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
Tokens wie versprochen zu verteilen. Hoffentlich ist jede Operation
nachweisbar und transparent aufgebaut. Alle Operationen werden mithilfe
von einem [special purpose 2-of-3 multisig account in Cyber
network](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j)
ausgeführt.

Dem wachsen des
[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
Protokolls unterstützen bis die Community die Entwicklung in Form der
cyber\~Foundation übernimmt. ATOMs spenden während dem Game of Links
werden an den [cyber\~Congress Cosmos 2-of-3
multisig](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a)
verteilt. Alle ATOM Spenden die ihre Wurzeln im cyber\~Congress multisig
haben werden dessen Eigentum. Die Rolle von ATOM Spenden ist die
folgende: dank ATOM wollen wir ein Commitment für cyber\~Congress in der
Entwicklung von Cosmos und dem Cyber Ökosystem sichern. ATOM Spenden
werden dem cyber\~Congress stacking Belohnungen ermöglichen und damit
einen nachhaltigen Flow für die kontinuierliche Finanzierung des
[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
Protokolls ermöglichen ohne, dass
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
oder ATOM Tokens fallen werden. 

## CYB

Proof-of-stake Systeme helfen bei der Erst-Distribution nicht. Wir
glauben, dass wenn die Erst Distribution zielgerichtet,
energieeffizient, nachweisbar und transparent und daher zugänglich
gestaltet ist, der anfängliche
[Wissensgraph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
an Qualität und Größe zunehmen wird.

Der Genesis Block von dem cyber Protokoll beinhaltet 1 000 000 000 000
000 CYB (ein petacyb oder 1 PCYB) die wie folgt verteilt sind:

- 750 000 000 000 000 CYB Tokens für die, die
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
tokens bis zum Ende der cyber\~Auction staken (Teilnehmer des
cyber\~Congress, Game of Thrones in ETH und cyber\~Auction)

- 150 000 000 000 000 CYB Tokens für die Teilnehmer bei Game of Links

- 100 000 000 000 000 CYB Tokens als Geschenk tokens für die Ethereum,
Cosmos und Urbit Communitys

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/CYB.svg" />
</p>

Nach der Genesis, können CYB Token nur von Heroes basierend auf den
staking und slashing Parametern erstellt werden. Der Basis Konsens ist,
dass die neu erstellten CYB Token den Stakeholdern zur Verfügung stehen.
Zurzeit gibt es keine Maximale Anzahl von CYB Token. Dies ist auf die
kontinuierliche Inflation zurückzuführen, die den Heroes des Netzwerks
gezahlt wird. Der CYB Token wird mit uint64 implementiert, so dass die
zusätzliche Erstellung von CYB Tokens es um einiges teurer macht
Statusänderungen und Ränge zu berechnen. Wir erwarten eine lebenslange
Währungsstrategie die durch das Governance-System nach der kompletten
Erstverteilung von CYB Tokens sich etablieren wird und die Aktivierung
der smart contract Funktion beginnt. Das startende Parameter der
Inflation wird durch die Governance während des Game of Links
definiert. 

## THC

Das Ziel eine Alternative zu einer [Google-like](https://google.com/)
Struktur zu erstellen erfordert einen sehr großen Aufwand von
verschiedenen Gruppen. Daher haben wir entschieden eine
cyber\~Foundation als Fond einzurichten, die durch eine dezentrale
Engine wie Aragon DAO gesteuert wird. Diese wird mit ETH finanziert und
von den Agenten die an der Erstverteilung teilgenommen haben verwaltet.
Dieser Ansatz schützt den nativen Plattformtoken
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
in den ersten Jahren vor starkem Markt Dumping und sichert eine stabile
Entwicklung des Projektes. Darüber hinaus ermöglicht dies eine
Diversifizierung für die unterliegende Plattform und die die Erweiterung
des Protokolls auf andere Konsensus Computing Architekturen, falls dies
erforderlich ist. 

Für die Auswahl eines Donation Tokens haben wir drei Hauptkriterien
berücksichtigt: der Token muss (1) einer der liquidesten sein, (2) einer
der vielversprechendsten, damit die Community ein solides Investment
sichern kann, auch im Wettbewerb mit solchen Giganten wie
[Google](https://google.com/) und (3) die technischen Fähigkeiten haben,
eine Auktion und eine daraus resultierende Organisation durchzuführen,
ohne sich auf Dritte verlassen zu müssen. Das einzige System, dass diese
Kriterien erfüllt ist ETH, daher wird der Primäre Donation Token ETH
sein.

Vor der Genesis cyber\~Foundation hat 750 000 000 000 000 THC geminted
(siebenhundertfünfzig billiarden) die sich wie folgt aufteilen:

- 600 000 000 000 000 THC tokens werden dem cyber\~Auction contract
zugeschrieben

- 150 000 000 000 000 THC tokens werden dem cyber\~Congress contract
zugeschrieben

<p align="center">
  <img src="https://github.com/serejandmyself/cyber/blob/master/images/THC.svg" />
</p>

Alle Entscheidungen der cyber\~Foundation werden basierend auf den THC
Voting Ergebnissen ausgeführt. Die folgenden Parameter werden
angewendet:

-   Support: 51%

-   Quorum: 51%

-   Vote Dauer: 500 Stunden 

## Geschenke

Wir wollen so vielen Akteuren wie möglich die Möglichkeit geben, den
vorgeschlagenen Ansatz zu bewerten. Aber ohne eine solche Komplexität
wie KYC und/oder Captcha hinzuzufügen. Deshalb haben wir uns dafür
entschieden, 8% der CYB-Marken in Genesis an Ethereum, 1% an Cosmos und
1% an die Urbit-Gemeinschaften zu verschenken. Die folgenden Regeln
werden bei der Reproduktion der Genesis angewendet:

-   Jedes Konto innerhalb des Ethereumnetzwerks, mit mindestens 1
    ausgehenden Transaktion, die kein Vertrag ist und \> 0,001 ETH im
    Block 8080808 hält

-   Jedes Nicht-Null-Konto innerhalb des Cosmos-Hub-3 bei Block 2000000

-   Jedes Konto, das Galaxies (30%), Stars (30%) oder Planets (40%) im
    Block 10677601 entsprechend der Anzahl der Objekte enthält

Der Hauptzweck dieses Geschenks besteht darin, dass jedes Konto in
Genesis mindestens einen Cyberlink innerhalb von 24 Stunden herstellen
kann, wenn das Netzwerk entladen wird. Aus diesem Grund haben wir
beschlossen, die Verteilungskurve etwas gleichmäßiger zu machen und sie
radikal in eine quadratische Kurve umzuwandeln. Daher verteilen wir die
CYB-Token während der Momentaufnahmen proportional zur Quadratwurzel
jedes Kontostandes. Da ein quadratisches Design zu einfach zu spielen
ist, haben wir die Menge der verteilten CYB-Token für die
vorgeschlagenen Blöcke berechnet, bevor diese Tatsache der
Öffentlichkeit bekannt wurde. Wir wenden die quadratische Regel nicht
auf Urbit-Aliens an.

## Game of Links

Ein Spiel für Cosmos Hodler in ATOM. Teilnehmer senden ATOM und wandeln
diese in CYB um. Umso mehr ATOM gesendet wird umso höher ist der Preis
von CYB. Das Spiel startet bei 1 ATOM für 1 GCYB. Das Spiel ist nach 146
seit Beginn vorbei oder wenn der Preis 5x des Start Preises erreicht.
Der Preis von
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
während des Spiels ist in folgender Formel definiert:

f(c) = 40 \* c + 1000

f(c) ist der TCYB Preis in ATOM, das c ist die Anzahl von TCYB Token die
während dem Takeoff gewonnen wurden.

Die Hauptidee ist: Je besser die Take Off Runde funktioniert, umso mehr
Tokens werden an die Teilnehmer ausgezahlt. 100
[TCYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
wird an die Teilnehmer der Take Off Runde ausgezahlt und 50
[TCYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
werden für die Teilnehmer der Game of Links Disziplin geplant. Alle
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
Tokens die im Takeoff bleiben werden am Spielende in den Community Pool
geworfen. Alle
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
tokens die bei den Spielen bleiben kommen zum cyber\~Congress.
Zusätzlich zu den CYB Token, bekommen Game of Links Teilnehmer test EUL
Tokens für das Finale. Ein detailliertes Dokument ([detailed
document](https://cybercongress.ai/game-of-links/)) mit dem Regeln und
Gewinnen für das Spiel wurde veröffentlicht.

## Cyber\~Auction

Ein Spiel für Ethereum hodlers in ETH. Teilnehmer senden ETH und wandeln
es so in THC um. Umso mehr ETH gesendet wird, umso höher ist der Preis
von THX. Das Spiel beginnt bei einem 5-fachen Schlusskurs des Starts in
ETH. Das Spiel endet nach 888 Tagen oder falls sich der Preis um das
5-fache gesteigert hat ausgehend vom Startpreis. Während dieser Phase
werden
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
Token permanent von cyber\~Congress ausgeschüttet. Die Menge basiert auf
die erworbenen
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
Token bis zum Ende der Auktion. Die erworbenen
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
Tokens bieten die Möglichkeit in entsprechender Anzahl
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
Tokens zu erhalten und können zum voten in der cyber\~Foundation genutzt
werden. Der Preis der
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
während der Cyber\~Auction wird in der folgenden Funktion definiert:

g(t)= 1/30 \* t \* p + 5 \* p

g(t) ist der TTHC Preis in ETH, t ist die Anzahl von TTHC tokens die man
während der cyber\~Auction gewonnen hat, p ist der endgültige Preis für
ein CYB umgewandelt in ETH beim Schlusskurs.

Der Startpreis soll den Start Teilnehmern eine 5-fache Prämie für ihr
Risiko geben, vor Genesis in Hardware- und Software-Infrastruktur zu
investieren. cyber\~Auction bietet signifikante Anreize für frühe
Teilnehmer. Nach Ende der Verteilung können die Teilnehmer ihre
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
Tokens freischalten und so nutzen wie sie es wollen z.B. versenden,
umtauschen etc. Das Ergebnis der Auktion ist, dass die Community Zugang
zu dem gesendeten ETH innerhalb der Aragon Organisation bekommt. Nach
Ende der cyber\~Auction werden die verbleibenden
[THC](https://github.com/serejandmyself/cyber/blob/master/cyber.md#thc)
der cyber\~Auction vernichtet. Die folgenden Regeln gelten für
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
Token bei den Verleihungsbedingungen

- cyber\~Congress wird seinen Anteil nicht nutzen und somit wird es ein
passiver Anteil bleiben bis er Verteilt wird
- nach Beendigung cyber\~Auction, werden alle noch vorhandenen
[CYB](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyb)
vernichtet

## Apps

 Wir gehen davon aus, dass der Algorithmus standardmäßig kein qualitativ
hochwertiges Wissen garantiert. Genau wie ein Neugeborenes muss es
Wissen erwerben, um sich weiterzuentwickeln. Das Protokoll selbst bietet
nur ein einfaches Werkzeug: Die Fähigkeit einen
[cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)
mit einem Agenten Stake zwischen zwei content Adressen zu generieren.
Die Analyse des semantischen Kerns, der Verhaltensfaktoren, der anonymen
Daten über die Interessen von Agenten und anderer Tools, die die
Qualität der Suche bestimmen, kann über smart contracts und
Off-Chain-Anwendungen wie zum Beispiel [web3
browsers](https://github.com/serejandmyself/cyber/blob/master/cyber.md#browzers), 
dezentralen sozialen Netzwerken und content Plattformen erfolgen. Wir
glauben, dass es im Interesse der Community und der Master liegt, den
anfänglichen
[Wissensgraph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
zu erstellen und diesen zu pflegen. Der graph soll die am relevantesten
Suchergebnisse liefern.

Im Allgemeinen unterscheiden wir drei Arten von Anwendungen für [Wissensgraphs](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph) 

- Konsensus apps. Können nach Ermessen des [Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) ausgeführt werden, indem intelligente Fähigkeiten hinzugefügt werden
- On-chain apps. Können vom [Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer) im Tausch mit gas ausgeführt werden
- Off-chain apps. Kann mithilfe des [Wissensgraph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
als Eingabe in einer Ausführungsumgebung implementiert werden

Die folgende Liste von Apps konsolidiert die oben genannten Kategorien:

Web3 Browsers. In der Realität sind  Browser und Suche fest miteinander
verbunden. Die Entstehung eines full-blown web3 Browsers welcher auf
Web2 Suche basiert ist schwer vorstellbar. Zurzeit gibt es viele
Anstrengungen ein Browser mit Blockchain und dazugehöriger Technik zu
entwickeln. Unter anderen gibt es hier Beaker, Mist, Brave und Metamask.
Alle davon leiden unter dem Versuch web2 in web3 ein zu betten. Unser
Ansatz ist ein wenig anders. Wir sehen web2 als unsichere Unterbasis für
web3. Deshalb haben wir ein Prototyp web3 Browser entwickelt, Cyb, der
den
[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
Ansatz präsentiert und Queries besser beantwortet und Content schneller
liefert.

Soziale Netzwerke. Soziale Netzwerke sind nicht so mysteriös. In jedem
sozialen Netzwerk ist Inhalt das Wichtigste. Daher ist das nachweisbare
Ranking der Grundbaustein von jedem sozialen Netzwerk. Alle
verschiedenen Typen von sozialen Netzwerken können einfach auf dem
[Wissensgraph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
aufgebaut werden. Cyber kann noch dazu soziale Netzwerke erschaffen, die
auf der Relevanz zwischen Nutzern basiert, was derzeit kein anderes
Netzwerk erreichen kann.

Programmierbare Semantik. Zurzeit sind die am meisten gesuchten Keywords
in dem gigantischen Semantik Kern von [Google](https://google.com/)
Keywords von Apps wie: [Youtube](https://youtube.com/),
[Facebook](https://facebook.com/), [GitHub](https://github.com/), etc.
Jedoch haben die Entwickler dieser erfolgreichen Apps wenig
Möglichkeiten [Google](https://google.com/) zu erklären wie sie ihre
Suchergebnisse in einer besseren Weise strukturieren können.Der
[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
Ansatz gibt diese Macht den Entwicklern zurück. Entwickler können nun
spezifische Semantik Kerne ansteuern und ihre Apps so indexieren wie sie
es wünschen.

Search actions. Das vorgeschlagene Design ermöglicht nativen Support für
die Blockchain (und tangle-ähnlichen) bezogene Tätigkeit. Es ist trivial
Anwendungen zu designen die (1) den Creators gehören (2) korrekte
Suchergebnisse ausgeben und (3) eine transaktion fähige Aktion erlauben,
mit (4) einer nachweisbaren Zuordnung einer Kommunikation über eine Such
Anfrage. E-Commerce war nie einfach für jeden.

Offline Suche. IPFS macht es möglich sehr leicht ein Dokument aus einer
Umgebung zu erhalten ohne einer globalen Internet Verbindung. Selbst
[go-cyber](https://github.com/cybercongress/go-cyber) kann über IPFS
verteilt werden. Dies ermöglicht eine allgegenwärtige offline Suche.

Command tools. Command-line tools können sich auf relevante und
strukturierte Antworten von einer Suchmaschine verlassen. In der Praxis
ist es möglich das folgende CLI tool zu implementieren:

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
Suchwerkzeuge. Suchwerkzeuge innerhalb von CLI werden unweigerlich einen
hart umkämpften Markt mit einem dedizierten semantischen Kern für
Roboter schaffen.

Autonome Roboter. Die Blockchain-Technologie ermöglicht die Erstellung
von Geräten, die digitale Assets selbst verwalten können.

`If a robot can store, earn, spend and invest - they can do everything you can do`

Was benötigt wird, ist ein einfaches, aber leistungsfähiges statisches
reales Werkzeug mit der Fähigkeit, bestimmte Dinge zu finden
[go-cyber](https://github.com/cybercongress/go-cyber) bietet eine
minimalistische, aber sich ständig selbst verbessernde Datenquelle, die
die notwendigen Werkzeuge für die Programmierung wirtschaftlich
rationaler Roboter bietet. Gemäß den [top-10,000 English
words](https://github.com/first20hours/google-10000-english) ist in der
Englischen Sprache das am meisten genutzte Wort der Artikel \'the\',
welcher sozusagen ein Zeiger auf ein bestimmtes Element ist. Dieser Fakt
kann wie folgt erklärt werden: bestimmte Elemente sind am wichtigsten
für uns. Daher liegt es in unserer Natur, einzigartige Dinge zu finden.
Jedoch ist das verstehen von einzigartigen Dingen  Daher ist das
Verständnis einzigartiger Dinge auch für Roboter von entscheidender
Bedeutung.

Language convergence. Ein Programmierer sollte sich keine Gedanken
machen welche Sprache der Agent nutzt. Wir müssen nicht wissen in
welcher Sprache der Agent seine Suche durchführt. Das ganze UTF-8
spectrum ist in Arbeit. Der Semantik Kern ist offen, so kann der
Wettbewerb um die Beantwortung von queries zwischen verschiedene
domänenspezifische Bereiche verteilt werden. Dazu gehören die Semantik
Kerne für verschiedene Sprachen. Dieser einheitliche Ansatz schafft eine
Chance für cyber\~Bahasa. Seit den Anfängen des Internets beobachten wir
einen Prozess der schnellen Sprachlichen Konvergenz. Wir nutzen
globalisierte Wörter auf dem ganzen Planeten. Unabhänig von
Nationalität, Sprache, Rasse, Name oder Internet Verbindung. Der Traum
einer wahren globalen Sprache ist schwer umsetzbar, da man sich einigen
müsste was was bedeutet. Jedoch haben wir die Werkzeuge den Traum wahr
werden zu lassen. Es ist nicht schwierig vorherzusagen, dass umso kürzer
ein Wort ist umso machtvoller wird sein cyber\~Rank sein. Eine globale,
öffentlich verfügbare Liste von Symbolen, Wörtern und Sätzen sortiert
nach cyber\~Rank mit einem entsprechenden Link von
[go-cyber](https://github.com/cybercongress/go-cyber) kann die Grundlage
für die Entstehung einer echten globalen Sprache werden, die jeder
akzeptieren kann. Neue [scientific
advances](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1)
in der maschinellen Übersetzung sind atemberaubend, aber bedeutungslos
für diejenigen, die sie ohne ein Google-scale trained modell anwenden
möchten. Der vorhergesagte cyber\~Rank bietet dies präzise.

Self prediction. Ein
[Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
kann dauerhaft ein
[Wissensgraph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
erstellen mithilfe seiner eigenen Vorhersage durch die existierenden
[cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)
und diese in Vorhersagen auf seinen Zustand anwenden. Daher kann ein
[Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
in der Konsensus Ökonomie des
[cyber](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyber-protocol)
Protokolls mitwirken.

Universal oracle. Ein
[Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
kann die am höchst relevanten Daten in einem key-value-storage
speichern. Hier ist der Schlüssel eine CID und die Werte sind die Bytes
des tatsächlichen Inhalts.Dies kann erreicht werden, indem in jeder
Runde entschieden wird, welchen CID-Wert die Agenten entfernen möchten
und welchen Wert sie anwenden möchten. Basierend auf der Messung der
Nutzer der content addresses innerhalb des
[Wissensgraph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph).
Um die Berechnung der Nutzung zu messen, werden heroes  die
Verfügbarkeit und die Größe des Inhalts für die top-ranked content
Adressen in dem 
[Wissensgraph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
prüfen und dann nach Größe des CIDs und seinem rank gewichten. Der
key-value storage wird nur für den
[Konsensus-Computer](https://github.com/serejandmyself/cyber/blob/master/cyber.md#the-notion-of-a-consensus-computer)
beschreibbar sein und nicht für Agenten. Aber die Werte daraus können
von Programmen genutzt werden.

Standortbasierte Suche. Es ist möglich
[cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)
mit
[Proof-of-Location](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG)
zu erstellen, basierent auf existierende Protokolle wie beispielsweise
[Foam](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG).
Folglich wird eine standortbasierte Suche auch dann nachweisbar, wenn
web3-Agenten triangulations minen und eine
[proof-of-location](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG)
an jede verknüpfte Chain hinzufügen. 

Prediction markets on link relevance. Wir können diese Idee mit hilfe
des Rankings des
[Wissensgraph](https://github.com/serejandmyself/cyber/blob/master/cyber.md#knowledge-graph)
basierend auf einem Vorhersage Markt zur Link Relevanz umsetzen. Eine
App die das Wetten auf Link Relevanz erlaubt kann eine einzigartige
Quelle der Wahrheit für die Richtung der Sätze sein und die Agenten
motivieren mehr Links einzureichen.

Private cyberlinks. Datenschutz ist von grundlegender Bedeutung. Da wir
uns dem Datenschutz verpflichtet fühlen ist das erreichen einer
Implementation von privaten
[cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)
nicht umsetzbar für unser Team bis Genenis. Daher ist es die Aufgabe der
Community an WASM Programmen zu arbeiten die auf dem Protokoll
ausgeführt werden können. Das Problem ist cyber\~Ranks zu berechnen,
basierend auf
[cyberlinks](https://github.com/serejandmyself/cyber/blob/master/cyber.md#cyberlinks)
die durch einen web3-master eingereicht wurden, ohne folgendes zu
enthüllen: ihre vorherige Anfrage und die öffentlichen Schlüssel.
Zero-knowledge proofs sind meistens sehr teuer. Wir glauben, dass der
Datenschutz bei der Suche ein Feature sein sollte, aber wir sind uns
nicht sicher wie wir das zurzeit Implementieren können.
[Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk)
wie rekursive Snarks und
[MimbleWimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg)
Konstruktionen können in der Theorie dieses Problem des Datenschutzes
lösen. Sie sind jedoch neu, ungetestet und in Bezug auf Berechnungen
ohnehin teurer als ihre transparente Alternative. 

Dies ist sicherlich nicht die vollständige Liste aller möglichen
Anwendungen, aber in der Tat eine sehr spannende.

## Fazit

Für die nachweisbare Kommunikation zwischen Konsensus-Computern haben
wir ein Protokoll definiert und implementiert. Das Protokoll basiert auf
der einfachen Idee von Wissensdatenbanken, welche von Agenten generiert
werden, die Cyberlinks nutzen. Cyberlinks werden von einem
Konsensus-Computer verarbeitet der das Konzept der Relevanz-Maschine
nutzt. Der cyber Konsensus-Computer basiert auf CIDv0/CIDv1 und nutzt
go-IPFS und Cosmos-SDK als Grundlage. IPFS bietet signifikante Vorteile
im Bereich Ressourcenverbrauch. CID als primäres Objekt sind Robust in
ihrer Einfachheit. Für jeden CID wird der cyber\~Rank fehlerfrei durch
einen Konsensus-Computer berechnet. Der Cyber\~Rank ist ein CYB Token
basierter PageRank mit ökonomischen Schutz vor Sybil-Attacken und
egoistischen Votings. Jede Runde wird der Merkle root des Ranks und der
graphischen Bäumen veröffentlicht. Infolgedessen kann jeder Computer
jedem anderen Computer die Relevanz des Wertes der gegebenen CID
beweisen. Die Sybil Attacken Widerstandsfähigkeit basiert auf
Limitierung der Bandbreite. Die mitgegebene Fähigkeit Programme
auszuführen bietet Möglichkeiten für neuartige Applikationen. Das
startende primäre Ziel ist das indexing von peer-to-peer content
addresses systems. Entweder Zustandslos wie IPFS, Swarm, Sia, Git,
BitTorrent oder Zustandsbezogen wie Bitcoin, Ethereum und andere
Blockchains und tangles. Die vorgegebene Sematic von cyberlinking bietet
ein robuster Mechanismus um bedeutungsvolle Beziehungen zwischen
Objekten von dem Konsensus-Computer vorauszusagen. Der Source-Code der
Relevanz-Maschine ist open-source. Jedes bisschen von Daten welches sich
bei dem Konsensus-Computer angesammelt hat ist für jeden Verfügbar der
die Ressourcen hat es zu verarbeiten. Die Performance der Vorhersage
Software Einführung ist ausreichend für eine nahtlose Interaktion. Die
Skalierbarkeit der vorhergesagten Einführung ist ausreichend um alle
selbst-authentisierenden Daten welche heutzutage existieren zu
indexieren und an Millionen von Agenten des Großen Webs weiterzugeben.
Die Blockchain wird von einer Superintelligenz verwaltet, die unter dem
Tendermint-Konsensalgorithmus mit einem Standard-Governance-Modul
funktioniert. Obwohl das System die notwendigen Funktionen bietet, um
eine Alternative für eine herkömmliche Suchmaschine darzubieten, ist es
nicht nur auf diesen Anwendungsfall beschränkt. Das System ist für
zahlreiche Anwendungen erweiterbar und ermöglicht die Entwicklung
wirtschaftlich rationaler, eigenständiger Roboter, die Objekte in ihrer
Umgebung autonom verstehen können.

Hinweise

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

## Danksagung

1. @hleb-albau
2. @arturalbov
3. @jaekwon
4. @ebuchman
5. @npopeka
6. @belya
7. @serejandmyself
