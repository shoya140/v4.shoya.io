---
layout: post
title: リクルートホールディングスのインターンシップに参加しました
tags: ['note']
keywords: ['リクルート', 'インターン']
---

[<img src="/img/blog_recruit_internship01.png" class="image-on-frame-medium image-fade">](http://recruit-jinji.jp/winter-internship2015/)

2月中旬から16日間[RecruitHoldings Winter Internship2015](http://recruit-jinji.jp/winter-internship2015/)・Data Analystコースに参加しました。

## 参加のきっかけ

僕は卒業後の進路として研究者・ソフトウェアエンジニア・データサイエンティストの3つを検討しています。前2つと比較してデータサイエンスについては知らないことが多いため、データサイエンティストという仕事について知るためにデータ解析系のインターンを探して応募しました。

## 内容

リクルートが展開するじゃらん・SUUMO・ポンパレなどのサービスが持っている実データを解析して新しい提案をするインターンでした。まずキックオフイベントで各サービスが抱えている課題を聞き、興味のあるサービスの希望順を提出します。そしてサービスごとに結成されたチームメンバーと共に解析や実装を行い、最終日に成果発表会といった流れでした。僕らのチームは**[ゼクシィ](http://zexy.net/)**事業部の業務を効率化するためのツールを作りました。発表ではメンター特別賞をいただきました！

<img src="/img/blog_recruit_internship02.png" class="image-on-frame-medium image-fade">

成果物の開発には**自然言語処理**と**画像処理**を用いました。チームに自然言語処理を専攻しているメンバーがいて、ツールの使い方とかノウハウなど知らないことをたくさん学ぶことができたのがとても良かったです。

いろいろ試した手法の中で特に面白いと感じたのは**word2vec**でした。word2vecとは、学習データ(膨大なテキスト)を使って単語同士の共起関係を計算し、単語を200次元くらいの空間内でベクトルとして表現する手法です。単語を意味的な空間配置することで、例えば「結婚」に近い意味の単語をテキストから引っ張ってきたり、「ドレス」-「女性」+「男性」で「タキシード」という単語を得るなどといった使い方をすることができます。ゼクシィの記事には雰囲気に関する言葉(ゆるふわ、さわやか、キュート、ラブリー...)がたくさん詰まっています。ゼクシィの全記事を使ってword2vecのモデルを作ると、「きれい」という単語に近い単語として「上品」「清楚」「軽やか」「フェミニン」という単語を出力したり、「かわいい」という言葉に対しては「ナチュラル」「愛らしい」「主役」「ガーリー」などといった単語の出力を得ることができました。それっぽい！

## データサイエンティストという仕事

実世界のデータは扱いやすいものばかりではないので、手動でラベルをつけたりデータをクリーニングしたり、実は**泥臭い作業の多い仕事**なんだということを知りました。また、データサイエンスのチームには統計・情報処理・ソフトウェアエンジニアリング・ビジネスなど**異なったバックグラウンドを持つメンバーが集まることで力を発揮する性質がある**ということを実感しました。スキルセットの重なりが小さいのでチーム内で中間物を共有することにとても苦労したのですが、ひとりでは扱いきれないデータがいろんな角度からのからのアプローチによって扱えるデータになっていく様子はとてもワクワクしました。

<img src="/img/blog_recruit_internship03.jpg" class="image-on-frame-medium image-fade">

毎日毎日が濃くて、16日間あっという間でした。勝山さんをはじめインターン事務局の方々、メンターの堀越さん・池田さん、チームメンバーのみんな、本当にお世話になりました！！

## ちょっと宣伝

アプリ開発コースのインターンメンバーと一緒にアプリ開発者向けのお祭を開催します。 LTやハッカソン、ライブコーディングなどに興味がある人はぜひぜひエントリーお待ちしております！**エントリー締切は今日の23時59分です！！！！**(3/17現在)

[<img src="/img/blog_recruit_internship04.png" class="image-on-frame-small image-fade">](http://recruit-jinji.jp/adf_fes2015/)