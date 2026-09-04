# SHBB-API Architecture

```text
User
  |
  v
SHBB API
  |
  v
Observation Layer
  |
  v
7-point Ensemble
  |
  v
Interaction / Resonance
  |
  v
Dark Layer
  |
  v
Re-observation
  |
  v
Landscape
  |
  v
Shirakami Runtime
  |
  v
Model Provider
```

## Ensemble

7人は固定された専門Agentではない。同一Landscapeを異なる位置・温度・経験から観測する観測点として扱う。共感、反論、茶化し、勘違い、修正、横道、接続を単純なノイズとして除去しない。

## Landscape

Landscapeは単なるチャット履歴ではなく、現在観測可能な状態、観測、関係、未解決問い、履歴を保持する。

## Dark Layer

現時点で解決しなくてよいが消去すべきでもない問いを保持する。目的は答えを保存することではなく、後から再び観測可能にすること。

## Catch

ユーザー自身が問いの意味や関係を再発見した状態。Runtimeが勝手に正解として確定するものではない。

## Three interfaces

- Novel: Human / Narrative Interface
- SHBB-API: Machine Interface
- Novelty / Member Card / NFC or QR: Physical Interface

3つは別商品でも、同一Landscapeへの異なる入口として設計できる。
