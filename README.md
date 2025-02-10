# Price Pursuits - TODOAPP

## 概要
**Price Pursuits** は、買い物時に購入リストを管理しながら、計算機能を同時に利用できるWebアプリです。メモと計算機を行き来する手間を省き、買い物をスムーズにすることを目的としています。

## 背景
一般的なメモアプリと計算機を併用すると、アプリを切り替える際に誤タップで計算内容が消えてしまうことがありました。これを防ぐため、メモと計算機能を一体化したアプリを開発しました。

## 機能
- **購入リストの管理**
  - 商品名、値段、個数を入力し、リストに追加
  - リストはリアルタイムで合計金額を計算
  - 計算ボタンを押すと、最終的な合計金額を表示
- **シンプルで直感的なUI**
  - 最小限の操作で買い物リストを管理可能
  - スマートフォン対応

## 想定ユーザー
- 買い物時にメモと計算機を併用する人
- 予算管理を意識しながら買い物をしたい人
- 無駄遣いを防ぎたい人

## 使用技術
- **フロントエンド:** HTML, CSS, JavaScript
- **バックエンド:** Python (Django)
- **データベース:** SQLite
- **バージョン管理:** Git, GitHub

## クローン & セットアップ手順
### 1. リポジトリをクローン
```sh
git clone https://github.com/your-username/todoapp.git
cd todoapp
```

### 2. 仮想環境の作成 & パッケージのインストール
```sh
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. マイグレーション & サーバー起動
```sh
python manage.py migrate
python manage.py runserver
```

### 4. アクセス
ブラウザで `http://127.0.0.1:8000/` にアクセスしてアプリを使用できます。

## 今後のアップデート予定
- ユーザーアカウント機能の追加
- クラウド同期機能の実装
- UI/UXの改善

## ライセンス
MIT License

## 開発者
(https://github.com/tatusyanin/todo_project)
