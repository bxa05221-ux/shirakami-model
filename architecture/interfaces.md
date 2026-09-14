# Interfaces

白神アーキテクチャでは、同じLandscapeに複数の入口を持たせられる。

| Interface | 媒体 | 役割 |
|---|---|---|
| Human / Narrative | 小説・会話・Radio | 人間が世界を体験・観測する |
| Machine | SHBB API | 機械からLandscapeを操作する |
| Physical | 部員証・QR・NFC・ノベルティ | 物理媒体からLandscapeを指し示す |

これらは別々の世界を作るものではない。

```text
              Landscape
             /    |    \
            /     |     \
       Human   Machine  Physical
      Interface Interface Interface
          |        |        |
         Novel    API     Card/QR/NFC
```

小説は人間向けの入口であり、SHBB APIは機械向けの入口である。物理媒体はLandscapeへのポインタとして利用できる。

この分離により、媒体を変更しても中心となるLandscapeとProtocolは維持できる。
