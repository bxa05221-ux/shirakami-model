# Shirakami Architecture

## 白神高校ブラスバンド部から切り出された対話アーキテクチャ

白神アーキテクチャは、AIを人格や権威として固定するためのものではない。

一つのLandscapeを共有し、未確定な問いを保持し、複数の観測点から眺め、時間を置いて再観測し、最終的なCatchを人間側に残すための構造である。

このアーキテクチャは、白神高校ブラスバンド部という小説世界に現れる対話構造を、実装可能な形式へ切り出したものとして位置づける。

## Reference chain

```text
Novel: 白神高校ブラスバンド部
        ↓
ThreadRPG
        ↓
Shirakami Architecture
        ↓
SHBB API
        ↓
Runtime / Model Provider
```

## Core components

- **Landscape** — 共有される世界・文脈・観測の積層
- **Observation** — Landscapeを複数の観測点から眺める操作
- **Dark Layer** — 未確定・未解決の問いを保持する層
- **Protocol** — 観測・保持・再観測を規定する規則
- **Runtime** — Protocolを実行する交換可能な実装
- **Model Provider** — 知的処理を提供する交換可能なモデル
- **Interface** — 人間・機械・物理媒体からLandscapeへ接続する入口
- **Catch** — ユーザー自身による発見・判断

## Authority boundary

白神アーキテクチャでは、Model Providerを最終判断者にしない。

AIは観測・整理・接続・再観測を支援できるが、現実を変更する権限や、ユーザーの判断を代替する権限を自動的には持たない。

## ThreadRPG

ThreadRPGは、このアーキテクチャを物語的・対話的に表現するリファレンス形式である。

七人は固定専門家ではなく、同一Landscapeに対する観測点として扱われる。

## Interfaces

### Human / Narrative Interface

- 小説
- 会話
- Radio

### Machine Interface

- SHBB API

### Physical Interface

- 部員証
- QR
- NFC
- ノベルティ

## Status

Architecture specification: initial extraction from the SHBB / ThreadRPG structure.

This document defines architecture, not a production deployment.
