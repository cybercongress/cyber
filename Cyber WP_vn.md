# cyber: Tính toán kiến thức của Great Web

<p align="center">
  <img src="images/graph.png" />
</p>


## Mở đầu

Một máy tính đồng thuận cho phép tìm ra những câu trả lời liên quan có thể chứng minh mà mà không cần bất kỳ blackbox trung gian cố định nào như Google, Amazon hoặc Facebook. Mạng truyền thông ngang hàng có thể truy cập nội dung và không có trạng thái như IPFS, các máy tính đồng thuận có trạng thái như Ethereum đều có thể cung cấp một phần giải pháp cần thiết để đưa ra được những đáp án giống nhau. Tuy nhiên, có ít nhất 3 vấn đề xảy ra khi triển khai những điều nói trên. (A) bản chất mang tính chủ quan khi nói đến sự liên quan. (B) khó khăn khi mở rộng quy mô máy tính đồng thuận cho các Sơ đồ tri thức (Knowledge Graph) ngoại cỡ. (C) thiếu chất lượng giữa các Sơ đồ tri thức như vậy. Chúng dễ gặp phải nhiều loại tấn công bề mặt khác nhau, chẳng hạn như tấn công Sybil, và hành vi ích kỷ của các tác nhân tương tác. Trong tài liệu này, chúng tôi định nghĩa một giao thức tính toán đồng thuận liên quan có thể chứng minh giữa các đối tượng IPFS dựa trên thuật toán đồng thuận Tendermint của cyber\~Rank, được tính bằng cách sử dụng GPU. Vì thuật toán đồng thuận Bằng chứng cổ phần (Proof of Stake) không có tác dụng trong phân phối ban đầu, chúng tôi phác thảo nên thiết kế cho hệ sinh thái và cuộc chơi phân phối hiệu quả. Chúng tôi tin rằng một kiến trúc giao thức tối giản rất quan trọng cho sựviệc hình thành nên một mạng lưới các máy tính đồng thuận tri thức có tên miền cụ thể. Từ kết quả công việc của mình, một số ứng dụng chưa từng tồn tại trước đây sẽ dần nổi lên. Chúng tôi mở rộng tài liệu này với tầm nhìn về các tính năng và ứng dụng tiềm năng có thể có.

## The Great Web

Giao thức gốc của Internet như: TCP/IP, DNS, URL và HTTP/S lại đưa web đến một điểm cũ, nơi nó nằm ở vị trí như bây giờ. Xem xét tất cả những lợi ích các giao thức này đem lại cho sự phát triển web ban đầu, cùng với lợi ích thì chúng cũng mang lại không ít trở ngại đáng kể. Tính toàn cầu là một tính chất quan trọng của web lại đang phải chịu mối đe dọa thực sự kể từ khi ra đời. Tốc độ kết nối tiếp tục giảm đi trong khi mạng vẫn tự phát triển do sự can thiệp của chính phủ có mặt khắp nơi. Thứ hai là nó gây ra mối đe dọa hiện hữu cho vấn đề nhân quyền.

Một trong những tính chất không rõ tàng ngay từ đầu lại trở nên quan trọng với việc sử dụng Internet hàng ngày: khả năng trao đổi liên kết vĩnh viễn, do đó, chúng [sẽ không bị hỏng theo thời gian](https://ipfs.io/ipfs/QmNhaUrhM7KcWzFYdBeyskoNyihrpHvUEBQnaddwPZigcN). Phụ thuộc vào kiến trúc của ISP mỗi một lần cho phép các chính phủ có thể kiểm duyệt hiệu quả. Đây cơ hội cuối trong web-stack truyền thống cho mọi kỹ sư quan tâm đến tương lai thế hệ sau này của chúng ta.

Các tính chất khác có thể không quá quan trọng, nhưng lại rất được mong muốn: kết nối ngoại tuyến và theo thời gian thực. Người sử dụng Internet thông thường, trong khi ngoại tuyến vẫn nên có khả năng làm việc ở trạng thái hiện tại. Sau khi có được kết nối họ sẽ có thể đồng bộ với trạng thái toàn cầu và tiếp tục xác minh tính hợp lệ cho trạng thái của chính họ theo thời gian thực. Hiện tại, các thuộc tính này được cung cấp ở cấp độ ứng dụng. Chúng tôi tin rằng những tính chất này nên được tích hợp vào các giao thức ở cấp thấp hơn.

Một [web-stack mới](https://ipfs.io/ipfs/Qmf2rKkDPSsvdudwSmdDPbZuYae8XRV26c1wAFCCvg8Dhw) nổi lên tạo cơ hội cho một Internet vượt trội. Cộng đồng gọi nó là web3 còn chúng tôi gọi nó là Great Web. Chúng tôi cho rằng các loại thông tin cấp thấp khác nhau cần phải bất biến và không nên thay đổi trong nhiều thập kỷ, ví dụ như các liên kết nội dung bất biến. Chúng có vẻ rất hứa hẹn khi có thể loại bỏ các vấn đề của giao thức stack thông thường. Chúng thêm vào tốc độ lớn hơn và cung cấp kết nối dễ truy cập hơn cho các web mới. Tuy nhiên, cũng giống như những gì xảy ra với bất kỳ ý tưởng mới nào đem lại - một vấn đề mới xuất hiện. Một trong những mối quan tâm như vậy là tìm kiếm đa năng. Các công cụ tìm kiếm đa năng hiện có vẫn còn hạn chế và cơ sở dữ liệu tập trung khiến tất cả mọi người buộc phải tin tưởng nó. Những công cụ tìm kiếm được thiết kế chủ yếu cho kiến trúc máy chủ-khách, dựa trên TCP/IP, DNS, URL và HTTP/S. Great Web tạo ra cả thách thức và cơ hội cho một công cụ tìm kiếm có thể dựa trên những công nghệ mới nổi và được thiết kế đặc biệt cho những mục đích này. Đáng ngạc nhiên là kiến trúc blockchain không cho phép xây dựng một công cụ tìm kiếm đa năng theo cách không thể tiếp cận với kiến trúc trước đó.

## Về vấn đề ví dụ đối nghịch

[Cấu trúc các công cụ tìm kiếm hiện tại](https://ipfs.io/ipfs/QmeS4LjoL1iMNRGuyYSx78RAtubTT2bioSGnsvoaupcHR6) là một hệ thống nơi một số đối tượng phải xử lý tất cả các tác vụ. Cách tiếp cận này gặp phải vấn đề trở ngại và khác biệt mà vẫn chưa được giải quyết, ngay cả bởi các nhà khoa học uyên bác của Google: [vấn đề ví dụ đối nghịch](https://ipfs.io/ipfs/QmNrAFz34SLqkzhSg4wAYYJeokfJU5hBEpkT4hPRi226y9). Vấn đề mà Google thừa nhận là thuật toán khá khó để lý giải cho dù một ví dụ cụ thể có phải là đối nghịch hay không. Không cần bàn cãi về công nghệ giáo dục trong chính nó tuyệt vời ra sao. Một cách tiếp cận kinh tế crypto có thể thay đổi những người hưởng lợi trong cuộc chơi. Do đó, cách tiếp cận này sẽ loại bỏ hiệu quả tấn công vector Sybil có thể xảy ra. Nó loại bỏ yêu cầu phải thu thập mô hình mã cứng và có nghĩa là trích xuất ra bởi một đối tượng duy nhất. Thay vào đó, nó cung cấp cho sức mạnh này cho toàn thế giới. Một mô hình học kháng Sybil được tạo bởi các tác nhân có thể sẽ dẫn đến thứ tự độ lớn có kết quả dễ đoán hơn.

## Giao thức Cyber

Điểm cốt lõi của giao thức lại rất tối giản và có thể được giải thích như các bước sau:

1. Tính toán nguồn gốc của giao thức Cyber dựa trên sự phân phối được xác định
2. Xác định trạng thái của [Sơ đồ tri thức](#knowledge-graph)
3. Gom giao dịch lại bằng cách sử dụng một [máy tính đồng thuận](#the-notion-of-a-consensus-computer)
4. Kiểm tra tính hợp lệ của chữ ký
5. Kiểm tra [giới hạn băng thông](#relevance-machine)
6. Kiểm tra tính hợp lệ của CIDs
7. Nếu cả chữ ký, giới hạn băng thông và CIDs hợp lệ, áp dụng [cyberlinks](#cyberlinks) và giao dịch
8. Tính giá trị [cyber\~Rank](#cyberrank) cho mỗi vòng cho CID trên [sơ đồ tri thức](#knowledge-graph)

Phần sau của tài liệu này thảo luận về lý do và các chi tiết kỹ thuật của giao thức được đề xuất.

## Sơ đồ tri thức

Chúng tôi biểu thị một sơ đồ tri thức dưới dạng đồ thị có trọng số của các liên kết được định hướng giữa các địa chỉ nội dung. Hay là định danh nội dung, CIDs, IPFS hashes, hoặc đơn giản là - liên kết IPFS. Trong tài liệu này, chúng tôi sẽ sử dụng các thuật ngữ trên như từ đồng nghĩa.

<p align="center">
  <img src="images/knowledge-graph.png" />
</p>


Địa chỉ nội dung về cơ bản là các liên kết web3. Thay vì sử dụng link không rõ ràng và có thể thay đổi:   

`https://github.com/cosmos/cosmos/blob/master/WHITEPAPER.md`

Chúng tôi sử dụng chính đối tượng:

`Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH`

Bằng cách sử dụng địa chỉ nội dung để xây dựng sơ đồ tri thức, chúng tôi có được [rất nhiều](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est) [IPFS cần thiết](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps) - [như](https://ipfs.io/ipfs/QmXHGmfo4sjdHVW2MAxczAfs44RCpSeva2an4QvkzqYgfR) siêu sức mạnh của giao thức p2p được mong muốn cho một công cụ tìm kiếm:

- mạng lưới bằng chứng tương lai
- khả năng truy cập liên hành tinh
- chống kiểm duyệt
- độc lập về công nghệ

Sơ đồ tri thức của chúng tôi được tạo ra bởi các chuyên gia hàng đầu. Những chuyên gia này thêm mình vào sơ đồ tri thức nhờ sự giúp đỡ của một giao dịch duy nhất, một CyberLink. Qua đó, họ chứng minh sự tồn tại của private key cho các địa chỉ nội dung của các public key đã biết của họ. Bằng cách sử dụng cơ chế này, một [máy tính đồng thuận](#the-notion-of-a-consensus-computer) có thể đạt được sự khác biệt có thể chứng minh giữa các chủ đề và các đối tượng trên một sơ đồ tri thức.

Việc triển khai [go-cyber](https://github.com/cybercongress/go-cyber) của chúng tôi dựa trên định danh [cosmos-SDK](https://github.com/cosmos/cosmos-sdk) và các địa chỉ nội dung [CIDv0/CIDv1](https://github.com/multiformats/cid#cidv0).

Các chuyên gia hình thành sơ đồ tri thức bằng cách ứng dụng [cyberlinks](#cyberlinks).

## Cyberlinks

Để hiểu cách cyberlinks hoạt động chúng ta cần phải hiểu về sự khác biệt giữa một liên kết URL (hay hyperlink) và giữa một liên kết IPFS. Một liên kết URL trỏ đến vị trí của nội dung, trong khi một liên kết IPFS trỏ đến chính nội dung của nó. Sự khác biệt giữa các kiến trúc web dựa trên các liên kết vị trí và liên kết nội dung là nguyên lý cơ bản và đòi hỏi một cách tiếp cận duy nhất.

Cyberlink là một cách tiếp cận để liên kết hai địa chỉ nội dung, hoặc liên kết IPFS, về cú pháp là:

````bash
.md syntax: [QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH](Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH)    
.dura syntax: QmdvsvrVqdkzx8HnowpXGLi88tXZDsoNrGhGvPvHBQB6sH.Qme4z71Zea9xaXScUi6pbsuTKCCNFp5TAv8W5tjdfH7yuH
````

Các CyberLink ở trên có nghĩa là đại diện cho [go-cyber](https://github.com/cybercongress/go-cyber) trong [cyberc0n](https://etherscan.io/token/0x61B81103e716B611Fff8aF5A5Dc8f37C628efb1E) đang tham chiếu đến Sách trắng của Cosmos. Khái niệm về cyberlinks là một quy ước xung quanh ngữ nghĩa đơn giản của một định dạng giao thức trong bất kỳ mạng P2P nào:

<p align="center">
  <img src="images/cyberlink.png" />
</p>


Chúng ta có thể thấy rằng một Cyberlink đại diện cho một liên kết giữa hai liên kết. Khá dễ hiểu phải không!

CyberLink là một cấu trúc ngữ nghĩa đơn giản nhưng mạnh mẽ để xây dựng một mô hình dự đoán vũ trụ, có nghĩa là sử dụng cyberlinks thay vì hyperlinks cung cấp cho chúng ta với sức mạnh rất lớn mà không thể tiếp cận bằng kiến trúc công cụ tìm kiếm đa năng trước đây.

Cyberlinks có thể được mở rộng, tức là có thể hình thành linkchains nếu có hai hoặc nhiều cyberlinks còn lại từ một cyberlink master, nơi liên kết thứ hai trong Cyberlink đầu tiên tương đương với liên kết đầu tiên trong Cyberlink thứ hai:

<p align="center">
  <img src="images/linkchain.png" />
</p>


Nếu các tác nhân mở rộng liên kết IPFS tự nhiên với một thứ có ngữ nghĩa phong phú hơn, với liên kết [dura](https://github.com/cybercongress/cyb/blob/dev/docs/dura.md), sau đó đồng thuận về các quy tắc thực thi bằng một chương trình cụ thể theo cách tiếp cận tự nhiên hơn.

Triển khai [go-cyber](https://github.com/cybercongress/go-cyber) cho cyberlinks là khả dụng trong ứng dụng [.cyber](https://github.com/cybercongress/dot-cyber) của trình duyệt web3 thử nghiệm [cyb](https://cyb.ai), hoặc tại [cyber.page](http://cyber.page).

Các cyberlinks được gửi bởi link master được lưu trữ trong một cây Merkle theo [tiêu chuẩn RFC-6962](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). Điều này cho phép xác thực [bằng chứng liên quan](#proof-of-relevance).

<p align="center">
  <img src="images/graph-tree.png" />
</p>


Sử dụng cyberlink chúng ta có thể tính được mức độ liên quan của các chủ đề và đối tượng trên [sơ đồ tri thức](#knowledge-graph). Nhưng chúng ta cần một [máy tính đồng thuận](#the-notion-of-a-consensus-computer).

## Khái niệm về máy tính đồng thuận

Một máy tính đồng thuận là một cỗ máy tính toán trừu tượng xuất hiện từ sự tương tác giữa các tác nhân. Một máy tính đồng thuận có khả năng về tài nguyên điện toán cơ bản: bộ nhớ và điện toán. Để tương tác với các tác nhân một máy tính cần băng thông. Một máy tính đồng thuận lý tưởng cần:

`tổng tất cả các tính toán và bộ nhớ khả dụng cho các cá nhân`     
`tương đương với`    
`tổng tất cả các tính toán và bộ nhớ đã xác minh của máy tính đồng thuận`    


Chúng ta biết rằng:

`xác minh tính toán < (tính toán + xác minh tính toán)`    

Do đó, chúng ta sẽ không bao giờ có thể đạt đến một máy tính đồng thuận lý tưởng. Định lý CAP và khả năng mở rộng trilemma tăng thêm bằng chứng cho tuyên bố này.

<p align="center">
  <img src="images/consensus-computer.png" />
</p>


Tuy nhiên, lý thuyết này có thể hoạt động như một chỉ số hiệu suất cho một máy tính đồng thuận. Sau 6 năm đầu tư vào các máy tính đồng thuận, chúng tôi đã nhận ra rằng đồng thuận [Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) có sự cân bằng đủ tốt giữa độ ổn định cần thiết cho nhiệm vụ của chúng tôi và sự sẵn sàng cho sản xuất của nó. Vì thế chúng tôi đã quyết định triển khai giao thức [cyber](#cyber-protocol) sử dụng thuật toán đồng thuận Tendermint, có thiết lập rất gần với Cosmos Hub. Triển khai [go-cyber](https://github.com/cybercongress/go-cyber) trên một máy tính đồng thuận Tendermint 64-bit phù hợp cho không gian string 64-byte. Nó không được lý tưởng, ít nhất là 1/146, bởi vì chúng tôi có 146 node xác nhận xác minh các tính toán tương tự tạo ra [sơ đồ tri thức](#knowledge-graph).

Chúng tôi phải liên kết tính toán, lưu trữ và nguồn băng thông của máy tính đồng thuận cho nhu cầu truy vấn tối đa. Tính toán và lưu trữ, trong trường hợp [máy liên quan](#relevance-machine) cơ bản có thể dự đoán dễ dàng dựa trên băng thông. Nhưng băng thông đòi hỏi một cơ chế giới hạn.

## Máy liên quan

Chúng tôi định nghĩa máy liên quan là một máy chuyển trạng thái của một [sơ đồ tri thức](#knowledge-graph) dựa trên ý muốn của tác nhân muốn dạy và nghiên cứu về [sơ đồ tri thức](#knowledge-graph) đó. Ý muốn được dự báo bởi mỗi [cyberlinks](#cyberlinks) mà một cyberlink master thực hiện. Càng nhiều tác nhân truy vấn [sơ đồ tri thức](#knowledge-graph), những kiến thức càng trở nên có giá trị hơn. Dựa trên các dự đoán này, sự liên quan giữa các địa chỉ nội dung có thể được tính toán. Máy liên quan cho phép xây dựng đơn giản cơ chế tìm kiếm qua truy vấn và cung cấp câu trả lời.

Một tính chất của máy liên quan rất quan trọng. Nó phải có tính suy luận quy nạp hoặc theo nguyên tắc Blackbox:

`Máy sẽ có thể can thiệp vào các dự đoán mà không có bất kỳ kiến thức nào về các đối tượng,`  `ngoại trừ ai, khi nào và cái gì đã được liên kết qua cyberlink`   

Nếu chúng ta cho rằng một [máy tính đồng thuận](#the-notion-of-a-consensus-computer) phải có một số thông tin về các đối tượng được liên kết, sau đó sự phức tạp của một mô hình như vậy sẽ phát triển không thể dự đoán. Do đó yêu cầu máy tính xử lý cần có bộ nhớ và khả năng tính toán cao. Nhờ nội dung truy cập một máy liên quan theo nguyên tắc Blackbox, không cần phải lưu trữ dữ liệu. Nhưng, vẫn có thể hoạt động hiệu quả trên nó. Việc suy đoán ngữ nghĩa bên trong một [máy tính đồng thuận](#the-notion-of-a-consensus-computer) rất đắt đỏ. Do đó, một thiết kế như vậy có thể phụ thuộc vào giả định mù. Thay vì suy luận ngữ nghĩa trong [máy tính đồng thuận](#the-notion-of-a-consensus-computer), chúng tôi đã thiết kế một hệ thống khuyến khích trả về ngữ nghĩa. Điều này đạt được do các link master cần [CYB](#cyb) tokens để bày tỏ mong muốn của chúng, dựa trên đó, máy tính phù hợp có thể tính xếp hạng.

Phần lõi của hệ thống bảo vệ chống spam là một giả định rằng các hoạt động ghi có thể được thực hiện chỉ bởi những người quan tâm đến sự phát triển thành công của máy liên quan. Mỗi 1% số stake hiệu quả trong [máy tính đồng thuận](#the-notion-of-a-consensus-computer) cho khả năng sử dụng 1% băng thông của mạng khả dụng và khả năng tính toán của nó. Một quy tắc đơn giản ngăn chặn việc lạm dụng các tác nhân: một cặp định danh nội dung có thể được liên kết bởi một địa chỉ chỉ một lần.

<p align="center">
  <img src="images/algo1.png" />
</p>


Chỉ có hai cách để thay đổi stake hiệu quả (stake hoạt động + stake cố định) của một tài khoản: chuyển token trực tiếp và các hoạt động chuyển vào stake.

[Cyber](#cyber-protocol) sử dụng một mô hình băng thông rất đơn giản. Mục tiêu chính của mô hình này là để giảm tốc độ tăng trưởng mạng hàng ngày xuống một hằng số nhất định. Điều này được thực hiện để phù hợp với heroes (bên xác nhận) với khả năng dự báo bất kỳ khoản đầu tư trong tương lai vào cơ sở hạ tầng. Vì vậy ở đây chúng tôi giới thiệu 'watts' hay 'W'. Mỗi loại thông điệp có mức phí W được định sẵn. Hằng số 'DesirableBandwidth', xác định 'RecoveryWindow' mong muốn chi tiêu theo giá trị W. Thời gian phục hồi xác định cách một master có thể phục hồi băng thông của họ từ 0 trở lại băng thông tối đa nhanh như thế nào. Một master có tỷ lệ W tối đa với stake hiệu quả của nó, được xác định theo công thức sau đây:

`AgentMaxW = EffectiveStake * DesirableBandwidth`

Thời gian 'AdjustPricePeriod' tổng hợp số W đã dùng cho khoảng thời gian 'RecoveryPeriod' trong khối mới nhất. Tỉ lệ 'SpentBandwidth' / 'DesirableBandwidths' được gọi là tỷ lệ dự trữ phân đoạn. Khi việc sử dụng mạng thấp, tỷ lệ dự trữ phân đoạn điều chỉnh chi phí tin nhắn để cho phép master với stake thấp hơn thực hiện giao dịch nhiều hơn. Khi nhu cầu về tài nguyên tăng, tỷ lệ dự trữ phân đoạn tiến tới > 1, do đó, tăng chi phí tin nhắn và hạn chế số TX cuối cùng cho một khoảng thời gian dài (W phục hồi sẽ < W sử dụng sau). Vì không ai sử dụng tất cả băng thông sở hữu của họ, chúng tôi có thể sử dụng an toàn tới 100x phân đoạn trong khoảng thời gian mục tiêu tính lại giá. Cơ chế như vậy đem lại giảm giá khi tạo ra [cyberlinking](#cyberlinks), bởi vậy, tối đa nhu cầu một cách hiệu quả cho nó. Bạn có thể thấy rằng các đề xuất thiết kế nhu cầu toàn bộ băng thông cho sự liên quan để trở nên có giá trị.

Trí tuệ con người được tổ chức theo cách như vậy, ví thế ký ức bị lãng quên theo thời gian là không liên quan và không quan trọng. Cùng có thể được áp dụng cho các máy liên quan. Máy liên quan có thể thực hiện [chiến lược tinh gọn tích cực](https://ipfs.io/ipfs/QmP81EcuNDZHQutvdcDjbQEqiTYUzU315aYaTyrVj6gtJb), chẳng hạn như, tinh gọn lịch sử hình thành của [sơ đồ tri thức](#knowledge-graph), hoặc quên các liên kết trở nên ít liên quan hơn.

Kết quả là cybernomics [CYB](#cyb) tokens được triển khai đóng vai trò không chỉ như cơ chế biểu hiện mong muốn và chống spam, mà còn có chức năng như một công cụ quy định kinh tế có thể sắp xếp công suất xử lý của heroes và nhu cầu thị trường để xử lý. Triển khai Go-cyber của máy liên quan dựa trên một cơ chế rất đơn giản, được gọi là: Cyber\~Rank.

## cyber\~Rank

Xếp hạng sử dụng một [máy tính đồng thuận](#the-notion-of-a-consensus-computer) có thể gặp khó khăn, vì máy tính đồng thuận có những hạn chế lớn về tài nguyên. Trước tiên, chúng ta phải tự hỏi: tại sao cần phải tính toán và lưu trữ thứ hạng trên chuỗi và không làm theo cùng một cách như [Colony](https://ipfs.io/ipfs/QmZo7eY5UdJYotf3Z9GNVBGLjkCnE1j2fMdW2PgGCmvGPj) hay [Truebit](https://ipfs.io/ipfs/QmTrxXp2xhB2zWGxhNoLgsztevqKLwpy5HwKjLjzFa7rnD)?

Khi xếp hạng được tính trong [máy tính đồng thuận](#the-notion-of-a-consensus-computer) một người có thể dễ dàng truy cập vào phân phối nội dung của thứ hạng đó và [xây dựng ứng dụng có thể chứng minh](#apps) một cách dễ dàng trên xếp hạng đó. Do đó, chúng tôi đã quyết định đi theo một kiến trúc phổ quát nhiều hơn nữa. Trong phần tiếp theo, chúng tôi mô tả cơ chế [bằng chứng liên quan](#proof-of-relevance), cho phép mạng lưới mở rộng quy mô với sự giúp đỡ của [máy liên quan](#relevance-machine) tên miền cụ thể. Chúng hoạt động đồng thời nhờ giao thức IBC.

Cuối cùng, [máy liên quan](#relevance-machine) cần có được (1) một thuật toán xác định, mà sẽ cho phép tính toán xếp hạng trên một mạng lưới nối tiếp liên tục, mà chính nó có thể mở rộng quy mô có thể mở rộng theo thứ tự độ lớn như [Google](https://google.com). Ngoài ra, một thuật toán hoàn hảo (2) phải có bộ nhớ tuyến tính và độ phức tạp tính toán. Quan trọng nhất, nó phải có (3) khả năng dự đoán có thể chứng minh cao nhất cho sự tồn tại của các [cyberlinks](#cyberlinks) liên quan.

Sau khi [nghiên cứu chuyên sâu](https://ipfs.io/ipfs/QmTJPJ55ePgR2MS1HoAtyqS1mteVLXUjAS4H8W97EEopxC), chúng tôi thấy rằng không thể có được những phương pháp hiệu quả tức thì. Vì vậy, chúng tôi đã quyết định tìm một cách cơ bản hơn, hiệu quả, có thể kích hoạt mạng lưới: [xếp hạng](http://ipfs.io/ipfs/QmbuE2Pfcsiji1g9kzmmsCnptqPEn3BuN3BhnZHrPVsiVw) mà Larry và Sergey sử dụng để ra mắt sản phẩm trước của họ. Vấn đề quan trọng với PageRank ban đầu là nó không kháng được tấn công Sybil. Tuy nhiên, một trọng số token PageRank bị giới hạn bởi một mô hình băng thông trọng số token không kế thừa các vấn đề quan trọng của PageRank ban đầu, bởi vì - nó có khả năng kháng tấn công Sybil. Hiện tại, chúng tôi sẽ gọi nó là cyber\~Rank, cho đến khi một thứ phù hợp hơn có thể thay thế. Thuật toán sau đây được áp dụng cho việc triển khai tại Genesis:

<p align="center">
  <img src="images/algo2.png" />
</p>


Chúng tôi hiểu rằng cơ chế Xếp hạng sẽ luôn vẫn là một thứ đánh lạc hướng. Đây là lý do tại sao chúng tôi trông chờ vào các công cụ quản trị trên dây chuỗi có thể xác định cơ chế phù hợp nhất tại một thời gian nhất định. Chúng tôi giả sử rằng mạng có thể chuyển từ một thuật toán sang cơ chế khác, không chỉ đơn giản dựa trên ý kiến chủ quan, mà là về thử nghiệm kinh tế a/b thông qua 'hard spooning' của tên miền cụ thể [máy liên quan](#relevance-machine).

cyber\~Rank bảo vệ hai quyết định thiết kế có tầm quan trọng nhất: (1) nó tính cả các mục đích hiện tại của các tác nhân, và (2) nó khuyến khích tăng xếp hạng của [cyberlinks](#cyberlinks). Tính chất đầu tiên đảm bảo rằng không thể đánh cược cyber\~Rank. Nếu một tác nhân quyết định chuyển [CYB](#cyb) tokens của họ ra khỏi tài khoản, [máy liên quan](#relevance-machine) sẽ điều chỉnh tất cả [cyberlinks](#cyberlinks) liên quan cho tài khoản này theo ý định hiện tại của tác nhân. Và ngược lại, nếu một tác nhân chuyển [CYB](#cyb) tokens vào tài khoản của họ, tất cả [cyberlinks](#cyberlinks) được gửi từ tài khoản này sẽ có được nhiều liên quan hơn tức thì. Tính chất thứ hai là rất cần thiết để không bị gắn với quá khứ. Khi [cyberlinks](#cyberlinks) mới liên tục được thêm vào, chúng sẽ làm loãng thứ hạng của các liên kết đã tồn tại tương ứng. Tính chất này nhằm ngăn cản trường hợp khi nội dung mới và tốt hơn lại có thứ hạng thấp hơn vì nó đã được gửi gần đây. Chúng tôi hy vọng các quyết định này sẽ tăng chất lượng suy luận cho nội dung mới được thêm vào gần đây vào phần sau khá dài của [sơ đồ tri thức](#knowledge-graph).

Chúng tôi rất thích thảo luận về vấn đề mua phiếu bầu. Mua phiếu bầu xuất hiện không hề xấu. Những vấn đề nan giải với mua phiếu bầu xuất hiện trong hệ thống nơi bỏ phiếu ảnh hưởng đến việc phân bổ các hệ thống lạm phát. Ví dụ:, [Steem](http://ipfs.io/ipfs/QmepU77tqMAHHuiSASUvUnu8f8ENuPF2Kfs97WjLn8vAS3) hoặc bất kỳ hệ thống dựa trên trạng thái fiat nào. Mua phiếu bầu có thể dễ dàng sinh lời cho đối thủ sử dụng một trò chơi Zero-Sum mà không cần phải thêm vào giá trị. Ý tưởng ban đầu của chúng tôi về một công cụ tìm kiếm phi tập trung dựa trên cách tiếp cận này. Nhưng, chúng tôi đã bỏ ý tưởng đó đi, xóa bỏ những ưu đãi từ sự hình thành của [sơ đồ tri thức](#knowledge-graph) sang mức đồng thuận. Trong môi trường mọi người tham gia phải đem lại một số giá trị cho hệ thống để ảnh hưởng đến mô hình dự đoán, việc mua phiếu bầu trở thành vấn đề trở ngại cho NP. Do đó lại trở nên có lợi cho hệ thống.

Việc triển khai [máy liên quan](#relevance-machine) hiện tại sử dụng GPUs để tính xếp hạng. Máy có thể trả lời và cung cấp kết quả phù hợp cho bất kỳ yêu cầu tìm kiếm nào trong một không gian CID 64 byte. Tuy nhiên, nó là không đủ để xây dựng một mạng lưới [máy liên quans](#relevance-machine) tên miền cụ thể. [Máy tính đồng thuận](#the-notion-of-a-consensus-computer) phải có khả năng chứng minh sự liên quan với nhau.

## Bằng chứng liên quan

Chúng tôi đã thiết kế mạng lưới theo giả định sẽ liên quan đến tìm kiếm và sẽ không tồn tại những hành vi xấu. Hay có thể được coi là không được tìm thấy hành vi xấu nào trong mục đích tìm kiếm câu trả lời. Cách tiếp cận này làm giảm đáng kể các cuộc tấn công bề mặt.

````bash
Xếp hạng được tính dựa trên thực tế là một thứ gì đó đã được tìm kiếm, do đó được liên kết, và kết quả là ảnh hưởng đến mô hình dự đoán
````

Một sự tương tự như vậy được thấy trong cơ học lượng tử, nơi mà chính các quan sát ảnh hưởng đến hành vi. Đây là lý do tại sao chúng tôi không yêu cầu bỏ phiếu tiêu cực. Bằng cách này, chúng tôi loại bỏ tính chủ quan ra khỏi giao thức và chúng tôi có thể xác định bằng chứng về mức độ liên quan.

<p align="center">
  <img src="images/graph-tree.png" />
</p>


Mỗi CID mới nhận được một số thứ tự. Việc đánh số bắt đầu từ 0. Sau đó tăng thêm 1 cho mỗi CID mới. Do đó, chúng ta có thể lưu trữ thứ hạng trong một mảng một chiều, trong đó các chỉ số là số thứ tự CID. Tính toán cây Merkle dựa trên [tiêu chuẩn RFC-6962](https://ipfs.io/ipfs/QmZpJLmc3T2L1FLUxzvU3P8MBCPe15fEmUyVS7Bz8ZKMhG). Sử dụng cây Merkle, chúng tôi có thể chứng minh hiệu quả thứ hạng cho bất kỳ địa chỉ nội dung nào. Trong khi về bản chất vẫn là sự liên quan chủ quan, chúng tôi có một tập hợp chứng minh cho một thứ gì đó có phù hợp với một cộng đồng nhất định tại một số thời điểm.

Sử dụng loại bằng chứng này bất kỳ hai [máy tính đồng thuận](#the-notion-of-a-consensus-computer) [tương thích IBC](https://ipfs.io/ipfs/QmSGbrGAPZtR6Q1jHHe8mmS3bLBehKmfp9ZYvrg5ycaZuk) nào cũng có thể chứng minh sự liên quan này với nhau. Điều này có nghĩa là [máy liên quan](#relevance-machine) tên miền cụ thể có thể phát triển mạnh.

Liên quan đến việc triển khai [go-cyber](https://github.com/cybercongress/go-cyber) chung, cây Merkle được tính mỗi vòng và hàm băm gốc của nó được gắn với ABCI.

## Tốc độ

Chúng tôi yêu cầu thời gian xác nhận ngay lập tức để cung cấp cho người dùng cảm giác của một ứng dụng web thông thường. Đây là một yêu cầu kiến trúc mạnh mẽ hình thành topo kinh tế và khả năng mở rộng của giao thức [cyber](#cyber-protocol). Thiết kế blockchain được đề xuất dựa trên thuật toán [đồng thuận Tendermint](https://ipfs.io/ipfs/QmaMtD7xDgghqgjN62zWZ5TBGFiEjGQtuZBjJ9sMh816KJ) với 146 bên xác nhận và có thời gian hoàn thành giao dịch nhanh chóng chỉ 5s. Thời gian xác nhận trung bình gần 1s và có thể làm cho tương tác blockchain phức tạp gần như không đáng kể với các tác nhân.

Chúng tôi biểu thị một tính chất [go-cyber](https://github.com/cybercongress/go-cyber) đặc biệt trong phần tính toán tốc độ - thứ hạng. Là một phần của đồng thuận, nó xảy ra song song với xác nhận giao dịch trong vòng. Một vòng là một biến đồng thuận được xác định bởi các stakeholders. Khi khởi đầu, một vòng được đặt thành 20 khối. Thực tế có nghĩa là cứ sau mỗi 100 giây mạng phải đồng ý về các Hash gốc hiện tại của [sơ đồ tri thức](#knowledge-graph). Điều này tức là [cyberlink](#cyberlinks) đã gửi trở thành một phần của [sơ đồ tri thức](#knowledge-graph) gần như ngay lập tức và thu được thứ hạng trong một khoảng thời gian trung bình là 50 giây. Trong những ngày đầu xếp hạng [Google](https://google.com) đã được tính lại khoảng mỗi tuần. Chúng tôi tin rằng master của Great web sẽ hài lòng khi quan sát thứ hạng thay đổi theo thời gian thực, nhưng, đã quyết định để khởi động mạng với một giả định rằng cửa sổ này là đủ. Dự kiến rằng với sự phát triển của giao thức [cyber](#cyber-protocol) vận tốc của mỗi vòng sẽ giảm. Điều này là do sự cạnh tranh giữa các heroes. Chúng tôi chú ý đến một số cơ chế nhất định để thực hiện lệnh chức năng này nhanh hơn:

- tối ưu hóa các tham số đồng thuận
- song song tốt hơn khi tính xếp hạng
- một [clock tốt hơn](https://ipfs.io/ipfs/QmbsKzizZVVVzPbZvg1qSsNMkwmA3MFufgXb3MFqbSnmPs) trước sự đồng thuận

## Khả năng mở rộng

Chúng tôi yêu cầu một kiến trúc cho phép mở rộng ý tưởng đáng kể như [Google](https://google.com). Hãy để chúng tôi giả định việc triển khai node dựa trên [Cosmos-SDK](https://github.com/cosmos/cosmos-sdk) có thể xử lý 10k giao dịch mỗi giây. Có nghĩa là mỗi ngày ít nhất 8,64 triệu master sẽ có thể gửi 100 [cyberlinks](#cyberlinks) mỗi lần, và tác động đến kết quả tìm kiếm cùng một lúc. Điều này là đủ để xác minh tất cả các giả định ra trong tự nhiên, nhưng, không đủ để nói rằng nó sẽ hoạt động ở quy mô Internet hiện nay. Những nghiên cứu hiện đại được thực hiện bởi đội ngũ của chúng tôi giúp chỉ ra một cách an toàn rằng không có công nghệ đồng thuận nào hiện nay cho phép mở rộng một blockchain cụ thể tới quy mô chúng tôi yêu cầu. Do đó, chúng tôi giới thiệu khái niệm về tên miền cụ thể [sơ đồ tri thức](#knowledge-graph).

<p align="center">
  <img src="images/network.png" />
</p>


Một trong hai có thể khởi động một tên miền riêng cho công cụ tìm kiếm cụ thể bằng cách phân nhánh [go-cyber](https://github.com/cybercongress/go-cyber), tập trung vào \textit{kiến thức chung công khai}. Hoặc đơn giản là cắm [go-cyber](https://github.com/cybercongress/go-cyber) làm một module vào chuỗi hiện tại, vd Cosmos Hub. Giao thức liên lạc liên blockchain giới thiệu các cơ chế đồng thời về trạng thái đồng bộ hóa giữa [các máy liên quan](#relevance-machine). Do đó, trong kiến trúc tìm kiếm được đề xuất, tên miền cụ thể [máy liên quan](#relevance-machine) sẽ có thể học hỏi từ kiến thức phổ biến. Cũng giống như kiến thức phổ biến có thể học hỏi từ tên miền cụ thể [máy liên quan](#relevance-machine).

## Browzers

Chúng tôi mong muốn hình dung ra cách mạng lưới được đề xuất sẽ hoạt động với một trình duyệt web3. Tuy nhiên đáng thất vọng là chúng tôi [không đủ khả năng](https://github.com/cybercongress/cyb/blob/master/docs/comparison.md) tìm một trình duyệt web3 có thể giới thiệu cách tiếp cận hoạt động đề xuất thoải mái nhất. Đây là lý do tại sao chúng tôi đã quyết định phát triển một trình duyệt web3 từ đầu. [Cyb](https://cyb.ai) là robot thân thiện của bạn có một mẫu ứng dụng [.cyber](https://cyber.page) để tương tác với giao thức [cyber](#cyber-protocol).

<p align="center">
  <img src="images/cyb.jpg" />
</p>


Một ví dụ tốt là chúng tôi đã tạo ra [cyber.page](https://cyber.page/). Nó cho phép heroes, master và người truyền giáo tương tác với giao thức qua một cổng web2. Tạo cyberlinks, ghim nội dung trực tiếp đến IPFS, tìm kiếm trên Great Web, tham gia vào việc quản trị của Cyber và tương tự. Nó cũng có thể hoạt động như một trình explorer chuyên sâu, một ví và có thể là ví phần cứng đóng gói như các thiết bị Ledger.

Các đoạn mã tìm kiếm hiện tại chưa được tốt lắm. Nhưng chúng tôi đoán rằng chúng có thể dễ dàng được mở rộng bằng cách sử dụng [IPLD](https://github.com/ipld/specs) cho mỗi loại nội dung khác nhau. Cuối cùng, chúng có thể trở nên hấp dẫn hơn so với những thứ của [Google](https://google.com).

<p align="center">
  <img src="images/architecture.png" />
</p>


Trong quá trình triển khai kiến trúc được đề xuất, chúng tôi đã nhận ra ít nhất 3 lợi ích chính mà [Google](https://google.com) có lẽ sẽ không có khả năng cung cấp với cách tiếp cận thông thường của nó:

- kết quả tìm kiếm có thể dễ dàng phân phối từ bất kỳ mạng P2P nào: ví dụ như .cyber có thể phát video
- các nút thanh toán có thể được nhúng ngay vào các đoạn tìm kiếm. Tức là các tác nhân có thể tương tác với kết quả tìm kiếm, ví dụ: các tác nhân có thể mua một mặt hàng ngay trong .cyber. Nhờ vậy thương mại điện tử có thể phát triển mạnh mẽ nhờ vào phân bổ chuyển đổi có thể chứng minh được
- đoạn tìm kiếm không phải là tĩnh nhưng vẫn có thể tương tác. Ví dụ: .cyber có thể cung cấp số dư ví hiện tại của bạn

## Triển khai

Do hạn chế kỹ thuật, chúng tôi phải khởi đầu hệ sinh thái bằng cách sử dụng 2 token: [THC](#thc) và [CYB](#cyb)

- [CYB](#cyb) là token gốc của giao thức [cyber](#cyber-protocol) cao nhất được hỗ trợ bởi thuật toán đồng thuận Tendermint. Nó có 3 trường hợp sử dụng chính: (1) staking cho đồng thuận, (2) băng thông hạn chế cho việc nộp [cyberlinks](#cyberlinks), và (3) biểu hiện ý muốn của master cho việc tính toán cyber\~Rank.

- [THC](#thc) (đọc như công nghệ) là một nền tảng proto cyber sáng tạo. [THC](#thc) là token tương thích Ethereum ERC-20 có giá trị tiện ích dưới dạng kiểm soát cyber\~Foundation (cộng đồng quản lý DAO) và ETH từ các trò chơi phân tán. [THC](#thc) được phát hành trong quá trình tạo ra cyber\~Foundation dưới dạng một tổ chức Aragon. Sức sáng tạo của [THC](#thc) đến từ khả năng nhận 1 [CYB](#cyb) token cho mỗi 1 [THC](#thc) token khi được giao trước khi kết thúc cyber\~Auction.

Cả hai token vẫn sẽ hoạt động và theo dõi giá trị độc lập với nhau bởi tính chất rất khác nhau của chúng.

Nhìn chung, quá trình triển khai có cấu trúc như sau:

1. cyber\~Congress triển khai Game of Links
2. Cộng đồng tham gia vào Game of Links
3. Cộng đồng xác minh và đề xuất một khối Genesis với kết quả từ Game of Links
4. cyber\~Congress triển khai hợp đồng cho cyber\~Foundation và cyber\~Auction
5. Cộng đồng tham gia vào cyber\~Auction sau Genesis. Người ủng hộ stake [THC](#thc) tokens để nhận [CYB](#cyb) tokens
6. cyber\~Congress phân phối [CYB](#cyb) tokens liên tục trong cyber\~Auction
7. cyber\~Congress hủy số [CYB](#cyb) và [THC](#thc) tokens còn lại sau đó báo cáo kết thúc quá trình phân phối ban đầu

cyber~Congress hoạt động trên Ethereum dưới dạng một [Aragon DAO](https://mainnet.aragon.org/#/cybercongress/0x4feb2bcc5907e7779130c093eef8fb44502c1330). Nó cũng vận hành [2-trong-3 multisig của Cyber network](https://cyber.page/network/cyber/contract/cyber1latzme6xf6s8tsrymuu6laf2ks2humqvdq39v8). cyber\~Congress đã phát triển giao thức [cyber](#cyber-protocol). Trong bối cảnh không gian mạng, Congress có 2 vai trò:

1. Triển khai và thực hiện chương trình phân phối ban đầu, hoàn toàn không thể tự động hóa. Vì không có cơ sở hạ tầng không cần sự tin cậy để trao đổi thông điệp giữa ETH và ATOM, cyber\~Congress giới thiệu một điểm duy nhất của sự thất bại trong quá trình phân phối ban đầu. Chúng tôi đã quyết định gửi [CYB](#cyb) tokens tới người stake [THC](#thc) bằng tay bởi chúng tôi cảm thấy rằng bây giờ là thời điểm thích hợp để khởi động mạng lưới đã tạo ra. Chúng tôi cũng tin rằng một cuộc đấu giá đang diễn ra sẽ rất quan trọng cho quá trình phân phối ban đầu. Nếu cyber\~Congress thất bại trong việc hoàn thành nghĩa vụ phân phối dù bất kỳ lý do nào, chúng tôi hy vọng rằng cộng đồng sẽ có thể Fork ra mạng mới và phân phối [CYB](#cyb) tokens như đã hứa. Hy vọng rằng, mọi hoạt động được thiết kế có thể chứng minh và minh bạch. Tất cả các hoạt động sẽ được thực hiện bằng [tài khoản multisig 2 trong 3 mục đích đặc biệt trong mạng Cyber](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j).

2. Hỗ trợ tăng trưởng cho giao thức [cyber](#cyber-protocol) cho đến khi cộng đồng đưa ra sự phát triển dưới hình thức cyber\~Foundation. Ủng hộ bằng ATOMs trong Game of Linkssẽ được phân bố tới [cyber\~Congress Cosmos 2-of-3 multisig](https://www.mintscan.io/account/cosmos1latzme6xf6s8tsrymuu6laf2ks2humqv2tkd9a). Tất cả ATOM đóng góp được chuyển đến cyber\~Congress multisig sẽ trở thành tài sản của nó. Vai trò của ATOM tặng là như sau: nhờ ATOM chúng tôi muốn bảo đảm một cam kết cho cyber\~Congress trong sự phát triển của cả hệ sinh thái Cosmos và Cyber. Đóng góp ATOM sẽ cho phép cyber\~Congress sử dụng phần thưởng Staking và đạt đến nguồn cung bền vững, cho việc tài trợ liên tục giao thức [cyber](#cyber-protocol) mà không cần phải xả [CYB](#cyb) hay ATOM tokens.

## CYB

Hệ thống Proof-of-stake không giúp cho việc phân phối ban đầu. Chúng tôi tin rằng nếu việc phân phối ban đầu được thiết kế có mục đích, hiệu quả năng lượng, có thể chứng minh và minh bạch, do đó có thể truy cập, [sơ đồ tri thức](#knowledge-graph) sẽ sớm đạt được chất lượng và quy mô mong muốn.

Khối Genesis của giao thức Cyber chứa 1 000 000 000 000 000 CYB (một petacyb hoặc 1 PCYB) token được chia nhỏ như sau:

- 750 000 000 000 000 CYB tokens cho ai stake [THC](#thc) tokens cho đến khi kết thúc cyber\~Auction (người tham gia vào cyber\~Congress, Game of Thrones trong ETH và cyber\~Auction)
- 150 000 000 000 000 CYB tokens cho người tham gia vào Game of Links
- 100 000 000 000 000 CYB tokens làm quà cho cộng đồng Ethereum, Cosmos và Urbit

<p align="center">
  <img src="images/CYB.svg" />
</p>


Sau Genesis, CYB tokens chỉ có thể được tạo ra bởi các heroes dựa trên các thông số Staking và cắt giảm. Cơ sở đồng thuận là các token CYB mới được tạo ra trong việc xử lý stakeholders.

Hiện tại không có số lượng CYB token tối đa. Điều này là do lạm phát liên tục được trả cho các heroes của mạng. CYB token được triển khai bằng cách sử dụng uint64, do đó, việc tạo ra token CYB bổ sung làm nó đắt hơn đáng kể để tính toán thay đổi về trạng thái và xếp hạng. Chúng tôi mong đợi một chiến lược tiền tệ lâu dài được thành lập bởi hệ thống quản trị sau khi phân phối CYB token ban đầu hoàn toàn và kích hoạt các chức năng của hợp đồng thông minh. Các thông số lạm phát ban đầu sẽ được xác định qua quản trị trong Game of Links.

## THC

Mục tiêu tạo ra sự thay thế cho một cấu trúc [giống Google](https://google.com) yêu cầu nỗ lực rất lớn từ các nhóm khác nhau. Do đó, chúng tôi đã quyết định thiết lập cyber\~Foundation làm quỹ, được quản lý qua một công cụ phi tập trung như một Aragon DAO. Nó được trả bằng ETH và quản lý bởi các tác nhân đã tham gia vào lần phân phối ban đầu. Cách tiếp cận này sẽ cho phép bảo vệ khỏi nguy cơ bị xả mạnh token nền tảng gốc trên thị trường - [CYB](#cyb) trong những năm đầu hoạt động của mình, do đó, đảm bảo phát triển ổn định. Ngoài ra, điều này cho phép đa dạng hóa nền tảng cơ bản và mở rộng giao thức cho các kiến trúc máy tính đồng thuận khác, nếu nhu cầu như vậy phát sinh.

Trong khi chọn token đóng góp, chúng tôi đã tuân theo ba tiêu chí chính: Token phải (1) thanh khoản nhất, (2) hứa hẹn nhất, do đó, một cộng đồng có thể đảm bảo một khoản đầu tư bền vững để cạnh tranh ngay cả với những gã khổng lồ như [Google](https://google.com), và (3) có khả năng kỹ thuật để thực hiện đấu giá và kết quả là một tổ chức không dựa vào bất kỳ bên thứ ba nào. Hệ thống duy nhất phù hợp với các tiêu chí này là Ethereum, do đó token ủng hộ chính sẽ là ETH.

Trước đó Genesis cyber\~Foundation đã tạo ra 750 000 000 000 000 THC (bảy trăm năm mươi terathc) được chia nhỏ như sau:

- 600 000 000 000 000 THC tokens được phân bổ tới hợp đồng cyber\~Auction
- 150 000 000 000 000 THC tokens được phân bổ tới hợp đồng cyber\~Congress

<p align="center">
  <img src="images/THC.svg" />
</p>


Tất cả quyết định từ cyber\~Foundation sẽ được thực hiện dựa trên kết quả bỏ phiếu THC. Các thông số sau sẽ được áp dụng:

- Hỗ trợ: 51\%
- Quorum: 51\%
- Thời gian bỏ phiếu: 500 giờ

## Quà tặng

Chúng tôi muốn cung cấp khả năng đánh giá cách tiếp cận đề xuất cho nhiều tác nhân nhất có thể. Tuy nhiên không cần thêm những quá trình phức tạp như KYC và/hoặc Capcha. Đó là lý do tại sao chúng tôi chọn tặng 8% số [CYB](#cyb) tokens trong Genesis đến Ethereum, 1% cho Cosmos, và 1% cho cộng đồng Urbit. Các quy tắc sau được áp dụng để tái tạo Genesis:

- Mọi tài khoản trong mạng lưới nền tảng Ethereum có ít nhất 1 giao dịch gửi đi không phải là hợp đồng và giữ > 0,001 ETH tại block 8080808
- Mọi tài khoản non-zero trong Cosmos hub-3 tại block 2000000
- Mọi tài khoản giữ galaxies (30%), stars (30%), hoặc planets (40%) tại block 10677601 theo số đối tượng

Mục đích chính của số quà này là để mỗi tài khoản trong Genesis để có thể tạo ít nhất 1 [cyberlink](#cyberlinks) trong không gian 24 giờ khi mạng khôn tải. Đây là lý do khiến chúng tôi ra quyết định làm cho đường cong phân phối đều hơn một chút và thay đổi nó triệt để thành một đường cong bậc hai. Do đó, chúng tôi phân phối [CYB](#cyb) tokens tương ứng với căn bậc hai mỗi số dư tài khoản trong quá trình snapshot. Bởi một thiết kế bậc hai rất dễ chơi, chúng tôi đã tính toán số lượng [CYB](#cyb) tokens được phân phối cho các khối được đề xuất trước khi thực tế này được biết đến rộng rãi. Chúng tôi không áp dụng quy tắc bậc hai cho cộng đồng Urbit.

## Game of Links

Một trò chơi cho người giữ Cosmos bằng ATOM. Những người tham gia ủng hộ ATOM để đổi lấy CYB. Càng nhiều ATOM được tặng, giá CYB càng cao. Trò chơi bắt đầu từ 1 ATOM mỗi 1 GCYB. Trò chơi kết thúc khi 146 ngày đã trôi qua kể từ khi bắt đầu quyên góp Takeoff, hoặc nếu giá đã tăng gấp 5 lần so với giá khởi điểm. Giá [CYB](#cyb) trong Takeoff được tính theo công thức sau:

f(c) = 40 * c + 1000 

với f(c) là giá TCYB theo ATOM, c là số TCYB tokens thắng trong Takeoff.

Ý tưởng chính là: vòng ủng hộ Takeoff thực hiện càng tốt thì càng có nhiều người tham gia khác nhau sẽ nhận được. 100 [TCYB](#cyb) được phân bổ cho những ai tham gia quyên góp Takeoff và 50 [TCYB](#cyb) cho ai tham gia phần Game of Links. Tất cả [CYB](#cyb) tokens còn lại từ Takeoff, được phân bổ vào quỹ cộng đồng vào cuối trò chơi. Tất cả [CYB](#cyb) tokens còn lại từ các phần khác được phân bổ cho cyber\~Congress. Ngoài CYB tokens, Game of Links phân bổ EUL tokens thử nghiệm cho tất cả những người ủng hộ Takeoff cho đến cuối. Một [tài liệu chi tiết](https://cybercongress.ai/game-of-links/) đã được xuất bản với các quy tắc và quy định cho trò chơi.

## Cyber\~Auction

Một trò chơi cho người giữ Ethereum với ETH. Người tham gia ủng hộ ETH để đổi lấy THC. Ủng hộ nhiều ETH hơn thì giá của THC sẽ cao hơn. Trò chơi bắt đầu từ giá gấp 5x giá đóng cửa của Takeoff trong ETH. Trò chơi kết thúc khi hoặc 888 ngày đã trôi qua kể từ ngày thành lập hoặc nếu giá đã tăng 5x từ giá khởi điểm. Trong giai đoạn này [CYB](#cyb) tokens được phân bổ liên tục bởi cyber\~Congress, dựa trên số [THC](#thc) tokens được phát hành dần cho đến khi kết thúc đấu giá. [THC](#thc) tokens được phát dần đem lại khả năng nhận [CYB](#cyb) tokens tương ứng, và quyền biểu quyết trong cyber\~Foundation. Giá [THC](#thc) trong Cyber\~Auction được xác định theo công thức sau:

g(t)= 1/30 * t * p + 5 * p

với g(t) là giá TTHC theo ETH, t là số TTHC tokens thắng trong cyber\~Auction, p là giá kết quả của Takeoff cho một CYB được chuyển đổi thành ETH lúc đóng cửa.

Giá khởi điểm được thiết kế để cung cấp cho những người tham gia Takeoff 5x phí bảo hiểm nếu có rủi ro khi đầu tư vào cơ sở hạ tầng phần cứng và phần mềm trước Genesis. cyber\~Auction đem lại ưu đãi đáng kể cho những người tham gia từ sớm. Sau khi kết thúc phân phối, người tham gia sẽ có thể mở khóa [THC](#thc) tokens và dùng chúng theo ý muốn, vd di chuyển, giao dịch, vv. Theo kết quả đấu giá, cộng đồng sẽ có quyền truy cập vào tất cả các ETH quyên góp trong tổ chức Aragon. Sau khi kết thúc cyber\~Auction, tất cả số [THC](#thc) còn lại trên hợp đồng cyber\~Auction phải được hủy. Những quy định sau áp dụng cho [CYB](#cyb) tokens dưới [multisig cho phân phối](https://cyber.page/network/cyber/contract/cyber147drnke9676972jr3anklkj7pzgwjw47cp2u7j):

- cyber\~Congress sẽ không ủy thác stake của mình, và kết quả là, nó sẽ vẫn là một stake thụ động cho đến khi nó được phân phối
- sau khi kết thúc cyber\~Auction, tất cả số [CYB](#cyb) tokens còn lại cần phải được hủy

## Ứng dụng

Chúng tôi cho rằng thuật toán đề xuất không đảm bảo kiến thức chất lượng cao theo mặc định. Giống một đứa trẻ, nó cần phải học thêm kiến thức để phát triển hơn nữa. Giao thức nó tự cung cấp chỉ là một công cụ đơn giản: khả năng tạo ra một [cyberlinks](#cyberlinks) với một tác nhân stake giữa hai địa chỉ nội dung.

Phân tích ngữ nghĩa chính, các yếu tố hành vi, dữ liệu ẩn danh về mối quan tâm của các tác nhân và các công cụ khác xác định chất lượng tìm kiếm, có thể đạt được thông qua hợp đồng thông minh và ứng dụng ngoài chuỗi, chẳng hạn như: [web3 browsers](#browzers), mạng xã hội và nền tảng nội dung phi tập trung. Chúng tôi tin rằng, đó là sự quan tâm của cộng đồng và master để xây dựng [sơ đồ tri thức](#knowledge-graph) ban đầu và duy trì nó. Do đó, đối với sơ đồ, để cung cấp kết quả tìm kiếm có liên quan nhất.

Nói chung, chúng tôi phân biệt ba loại ứng dụng cho [sơ đồ tri thứcs](#knowledge-graph):

- Ứng dụng đồng thuận. Có thể chạy theo quyết định của [máy tính đồng thuận](#the-notion-of-a-consensus-computer) bằng cách thêm khả năng thông minh
- Ứng dụng trên chuỗi. Có thể chạy bằng [máy tính đồng thuận](#the-notion-of-a-consensus-computer) để đổi lấy gas
- Ứng dụng ngoài chuỗi. Có thể được triển khai bằng cách sử dụng [sơ đồ tri thức](#knowledge-graph) như đầu vào trong một môi trường thực thi

Danh sách các ứng dụng sau đây, hoàn toàn có thể hình dung và hợp nhất các danh mục nêu trên:

Web3 browsers. Trong thực tế, trình duyệt và tìm kiếm là không thể tách rời. Thật khó hình dung ra một trình duyệt web3 full-blown nổi lên mà lại dựa trên tìm kiếm web2. Hiện tại, một số bên đang nỗ lực phát triển trình duyệt dựa vào công nghệ blockchain và phân tán. Trong số đó có Beaker, Mist, Brave và Metamask. Tất cả họ đều gặp phải khó khăn khi nhúng web2 vào web3. Cách tiếp cận của chúng tôi sẽ khác một chút. Vì coi web2 là tập con không an toàn cho web3, chúng tôi đã phát triển một trình duyệt web3 thử nghiệm, Cyb, giới thiệu cách tiếp cận [cyber](#cyber-protocol) để phản hồi truy vấn tốt hơn và cung cấp nội dung nhanh hơn.

Mạng xã hội. Mạng xã hội không còn là bí ẩn nữa. Trong bất kỳ mạng xã hội nào nội dung cũng đóng vai trò quan trọng nhất. Do đó, xếp hạng có thể chứng minh là khối xây dựng nền móng của bất kỳ mạng xã hội nào. Tất cả các loại mạng xã hội có thể dễ dàng được xây dựng trên một [sơ đồ tri thức](#knowledge-graph). Cyber cũng có thể tạo ra mạng xã hội dựa trên mối quan hệ giữa người dùng, mà không có mạng hiện tại nào có thể làm được.

Ngữ nghĩa có thể lập trình. Hiện nay, các từ khóa phổ biến nhất trong phần ngữ nghĩa chính khổng lồ của [Google](https://google.com) là các từ khóa từ những ứng dụng như: [Youtube](https://youtube.com), [Facebook](https://facebook.com), [GitHub](https://github.com), vv. Tuy nhiên, các nhà phát triển những ứng dụng thành công đó lại có khả năng rất hạn chế khi giải thích cách [Google](https://google.com) cấu trúc kết quả tìm kiếm theo hướng tốt hơn. Cách tiếp cận [cyber](#cyber-protocol) đưa quyền này cho các nhà phát triển. Các nhà phát triển hiện có thể nhắm mục tiêu đến những ngữ chính nghĩa cụ thể và trỏ đến các ứng dụng đó khi họ muốn.

Hành động tìm kiếm. Thiết kế đề xuất cho phép hỗ trợ riêng những hoạt động liên quan đến tài sản blockchain (và có vẻ như làm mọi thứ rối hơn). Việc thiết kế các ứng dụng không quan trọng như vậy thường là (1) thuộc sở hữu của những người tạo ra nó, (2) xuất hiện chính xác trong kết quả tìm kiếm và (3) cho phép một hành động có thể giao dịch, với (4) biểu hiện có thể chứng minh của một chuyển đổi cho một truy vấn tìm kiếm. Thương mại điện tử nhờ vậy trở nên dễ dàng cho tất cả mọi người.

Tìm kiếm ngoại tuyến. IPFS cho phép truy xuất tài liệu dễ dàng từ một môi trường mà không cần kết nối internet toàn cầu. [go-cyber](https://github.com/cybercongress/go-cyber) tự nó có thể được phân tán nhờ IPFS, nhờ vậy có khả năng tìm kiếm mọi nơi, ngoại tuyến!

Công cụ lệnh. Công cụ dòng lệnh có thể dựa vào câu trả lời liên quan và có cấu trúc từ một công cụ tìm kiếm. Thực tế có thể nói rằng công cụ CLI sau đây có thể triển khai:

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

Công cụ tìm kiếm, từ trong CLI chắc chắn sẽ tạo ra một thị trường ngữ nghĩa chính dành riêng cho robot đầy tính cạnh tranh.

Robot tự trị. Công nghệ Blockchain cho phép tạo ra các thiết bị có thể quản lý tài sản kỹ thuật số.

`Nếu một robot có thể lưu trữ, kiếm tiền, chi tiêu và đầu tư - chúng có thể làm mọi thứ bạn có thể làm`

Những thứ cần thiết khá đơn giản, nhưng vẫn là một công cụ thực tế, hiện đại và mạnh mẽ với khả năng tìm kiếm cụ thể hơn. [go-cyber](https://github.com/cybercongress/go-cyber) cung cấp một nguồn dữ liệu tối giản, nhưng liên tục tự cải thiện, cung cấp các công cụ cần thiết để lập trình các robot hợp lý về mặt kinh tế. Theo [top-10,000 từ Tiếng Anh](https://github.com/first20hours/google-10000-english) thì từ phổ biến nhất trong ngôn ngữ tiếng Anh là mạo từ xác định 'The', có nghĩa là chỉ đến một đối tượng cụ thể. Thực tế này có thể được giải thích như sau: các đối tượng cụ thể có tầm quan trọng nhất với chúng tôi. Do đó về bản chất chúng tôi đi tìm những thứ độc nhất. Vì vậy mà hiểu biết về những thứ độc nhất là rất cần thiết cho robot.

Hội tụ ngôn ngữ. Lập trình viên không nên quan tâm đến ngôn ngữ mà một tác nhân sẽ sử dụng. Chúng tôi không cần biết ngôn ngữ các tác nhân đang dùng để tìm kiếm. Toàn bộ phổ UTF-8 đang hoạt động. Ngữ nghĩa chính hoàn toàn mở cho nên việc cạnh tranh để trả lời các truy vấn có thể phân tán trên nhiều tên miền khu vực cụ thể khác nhau và bao gồm ngữ nghĩa chính cho các ngôn ngữ khác nhau. Cách tiếp cận thống nhất này tạo cơ hội cho cyber\~Bahasa. Từ buổi bình minh của Internet, chúng tôi đã quan sát thấy một quá trình hội tụ ngôn ngữ nhanh chóng. Chúng tôi sử dụng các từ toàn cầu thực sự trên toàn bộ hành tinh, độc lập với quốc tịch, ngôn ngữ, chủng tộc, tên hoặc kết nối Internet. Ước mơ về một ngôn ngữ thật sự toàn cầu rất khó để triển khai bởi vì chưa có sự thống nhất để đồng ý về một thứ có nghĩa chính xác là gì. Tuy nhiên, chúng tôi có các công cụ để biến ước mơ này thành sự thật. Không khó để dự đoán ra một từ ngắn hơn thì sẽ có cyber\~Rank của nó mạnh hơn. Trên toàn cầu, danh sách các ký hiệu, từ và cụm từ công khai sẵn có được sắp xếp theo cyber\~Rank với một liên kết tương ứng được cung cấp bởi [go-cyber](https://github.com/cybercongress/go-cyber) có thể trở thành nền tảng cho sự nổi lên của một ngôn ngữ chính thức toàn cầu mà mọi người có thể chấp nhận. [Những tiến bộ khoa học](https://ipfs.io/ipfs/QmQUWBhDMfPKgFt3NfbxM1VU22oU8CRepUzGPBDtopwap1) gần đâytrong dịch máy thực sự rất ấn tượng nhưng lại vô nghĩa với những người muốn áp dụng chúng mà không được đào tạo theo mô hình chuẩn của Google. cyber\~Rank được đề xuất cung cấp chính xác điều này.

Tự dự đoán. Một [máy tính đồng thuận](#the-notion-of-a-consensus-computer) có thể xây [sơ đồ tri thức](#knowledge-graph) liên tục nhờ vào khả năng tự dự đoán sự tồn tại của [cyberlinks](#cyberlinks) và áp dụng những dự đoán này vào tình trạng của nó. Nhờ vậy một [máy tính đồng thuận](#the-notion-of-a-consensus-computer) có thể tham gia vào đồng thuận kinh tế của giao thức [cyber](#cyber-protocol).

Oracle phổ quát. Một [máy tính đồng thuận](#the-notion-of-a-consensus-computer) có thể lưu trữ dữ liệu liên quan nhất trong nơi lưu trữ khóa-giá trị, khóa là một CID và giá trị là các byte của nội dung thực tế. Nó hoạt động bằng cách đưa ra quyết định mỗi vòng, trong trường hợp mà CID có giá trị tác nhân muốn làm gọn và giá trị mà chúng muốn áp dụng dựa trên mức độ tiện ích của các địa chỉ nội dung trong [sơ đồ tri thức](#knowledge-graph). Để tính mức độ tiện ích, heroes kiểm tra tính khả dụng và kích thước của nội dung cho các địa chỉ nội dung xếp hạng hàng đầu trong [sơ đồ tri thức](#knowledge-graph), sau đó đặt trọng số lên kích cỡ CIDs và xếp hạng của nó. Lưu trữ khóa-giá trị khẩn cấp sẽ khả dụng chỉ cho [máy tính đồng thuận](#the-notion-of-a-consensus-computer) để viết và không dành cho tác nhân. Tuy nhiên giá trị có thể được sử dụng trong các chương trình.

Tìm kiếm chú ý đến vị trí. Có thể xây dựng [cyberlinks](#cyberlinks) với [Bằng chứng vị trí](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) dựa trên các giao thức đáng chú ý hiện tại như [Foam](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG). Do đó, tìm kiếm dựa trên vị trí cũng có thẻ chứng minh, nếu tác nhân web3 sẽ khai thác các Phép đạc tam giác (triangulation) và đính kèm [bằng chứng vị trí](https://ipfs.io/ipfs/QmZYKGuLHf2h1mZrhiP2FzYsjj3tWt2LYduMCRbpgi5pKG) cho mỗi chuỗi được liên kết.

Dự đoán thị trường theo những mối liên hệ có liên kết với nhau. Chúng ta có thể thực hiện ý tưởng này bằng cách sử dụng bảng [sơ đồ tri thức](#knowledge-graph) dựa trên một dự đoán thị trường từ liên kết có liên quan. Một ứng dụng cho phép đặt cược vào những mối liên hệ có liên kết với nhau, có thể trở thành một nguồn sự thật duy nhất cho hướng của các điều khoản, cũng như thúc đẩy các tác nhân gửi thêm liên kết.

Cyberlink cá nhân. Quyền riêng tư là nền tảng. Trong khi chúng tôi cam kết bảo mật, triển khai thành công [cyberlinks](#cyberlinks) cá nhân không khả thi đối với đội ngũ của chúng tôi cho đến thời điểm Genesis. Do đó, nó tùy thuộc cộng đồng để làm việc với các chương trình WASM, mà có thể được thực hiện trên giao thức. Vấn đề là để tính cyber\~Rank, dựa trên [cyberlinks](#cyberlinks) được gửi bởi một web3-masters mà không tiết lộ cả: yêu cầu trước đó của chúng cũng như các public key. Chứng minh không kiến thức, nói chung rất tốn kém. Chúng tôi tin rằng tính riêng tư khi tìm kiếm phải là một tính năng theo thiết kế, nhưng chúng tôi vẫn chưa chắc liệu mình có biết cách triển khai nó trong giai đoạn này. [Coda](https://ipfs.io/ipfs/Qmdje3AmtsfjX9edWAxo3LFhV9CTAXoUvwGR7wHJXnc2Gk) như Snarks đệ quy và xây dựng [MimbleWimble](https://ipfs.io/ipfs/Qmd99xmraYip9cVv8gRMy6Y97Bkij8qUYArGDME7CzFasg), về lý thuyết, có thể giải quyết một phần mối quan tâm về quyền riêng tư. Nhưng chúng còn mới và chưa được kiểm tra, và dù sao cũng sẽ đắt hơn theo tính toán so với sự thay thế đã rõ ràng của chúng.

Đây chắc chắn chưa phải là danh sách cuối cùng của tất cả các ứng dụng khả thi, nhưng thực sự là một ứng dụng rất thú vị.

## Kết luận

Chúng tôi xác định và triển khai một giao thức giao tiếp có thể chứng minh, giữa những máy tính đồng thuận có liên quan. Giao thức này dựa trên ý tưởng đơn giản về sơ đồ tri thức, được tạo ra bởi các tác nhân qua việc sử dụng cyberlinks. Cyberlinks được xử lý bởi một máy tính đồng thuận bằng cách sử dụng ý tưởng về máy liên quan. Máy tính đồng thuận cyber dựa trên CIDv0/CIDv1 và sử dụng go-IPFS & Cosmos-SDK làm nền tảng. IPFS cung cấp lợi ích đáng kể liên quan đến việc tiêu thụ tài nguyên. CID là đối tượng chính giúp tăng cường sự đơn giản của chúng. Với mỗi CID, cyber\~Rank được tính bằng máy tính đồng thuận không có điểm lỗi duy nhất. Cyber\~Rank là một CYB token trọng số PageRank, với khả năng bảo vệ kinh tế khỏi tấn công Sybil và tự bỏ phiếu. Mỗi vòng xếp hạng của cây Merkle và cây đồ thị được công bố. Do đó, mỗi máy tính có thể chứng minh cho bất kỳ máy tính khác về mức độ liên quan giá trị cho một CID. Kháng Sybil dựa vào giới hạn băng thông. Khả năng nhúng để thực thi các chương trình cung cấp các ứng dụng truyền cảm hứng. Mục tiêu chính ban đầu là việc lập chỉ mục các hệ thống địa chỉ nội dung ngang hàng, hoặc là không trạng thái như: IPFS, Swarm, SIA, git, BitTorrent hoặc Stateful, chẳng hạn như: Bitcoin, Ethereum và các blockchains cũng như tangles khác. Các ngữ nghĩa cyberlinking đề xuất cung cấp một cơ chế mạnh mẽ để dự đoán các mối quan hệ có ý nghĩa giữa các đối tượng bởi chính máy tính đồng thuận. Máy liên quan sử dụng mã nguồn mở. Mỗi bit dữ liệu được tích lũy bởi máy tính đồng thuận sẽ khả dụng cho bất cứ ai nếu họ có tài nguyên để xử lý nó. Hiệu quả triển khai phần mềm được đề xuất là đủ cho tương tác liền mạch. Triển khai được đề xuất có đủ khả năng mở rộng để lập chỉ mục tất cả dữ liệu tự xác thực tồn tại ngày nay và có thể phục vụ nó cho hàng triệu tác nhân của Great Web. Blockchain được quản lý bởi một Superintelligence, hoạt động theo thuật toán đồng thuận Tendermint với module quản trị tiêu chuẩn. Mặc dù hệ thống cung cấp nhiều tiện ích cần thiết để đem lại sự thay thế cho một công cụ tìm kiếm thông thường, nó không bị giới hạn chỉ sử dụng trường hợp này. Hệ thống này hoàn toàn có khả năng mở rộng cho nhiều ứng dụng và giúp nó có thể thiết kế một nền kinh tế hợp lý, những robot tư nhân có thể tự động hiểu những đối tượng xung quanh chúng.

## Tham khảo

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

## Lời cảm ơn

1. @hleb-albau
2. @arturalbov
3. @jaekwon
4. @ebuchman
5. @npopeka
6. @belya
7. @serejandmyself
