```markdown
# Universe Club Auto Blog Poster

ユニバース倶楽部向けブログ自動投稿ツールです。  
**画像をアップロードするだけで、過去コメントを参考にした高品質な記事を生成し、WordPressへ自動投稿**します。

## 特徴

- 画像アップロード → Claudeによる魅力的な記事自動生成
- 過去の投稿・コメントを考慮した内容の一貫性
- WordPress REST API連携（featured image自動設定）
- 生成内容の確認・編集機能
- Docker対応で環境構築が簡単

## 技術スタック

**バックエンド**
- Python 3.11+ + FastAPI
- LangChain + LiteLLM（Claudeメイン）
- Celery + Redis

**フロントエンド**
- Next.js 15 (App Router) + TypeScript
- Tailwind CSS + shadcn/ui

**インフラ**
- Docker + Docker Compose
- Vercel（フロント） / Railway・VPS（バック）

## 環境構築

### 必須ツール
- Node.js 20以上
- Python 3.11以上
- Docker / Docker Compose

### セットアップ手順

```bash
# リポジトリをクローン
git clone <your-repo-url>
cd universe-auto-blogger

# バックエンド
cd backend
cp .env.example .env
pip install -r requirements.txt

# フロントエンド
cd ../frontend
cp .env.example .env.local
npm install

# 起動（開発時）
docker-compose up -d
```

または個別に起動することも可能です。

## ディレクトリ構成

```bash
/
├── backend/          # FastAPI
├── frontend/         # Next.js
├── docker-compose.yml
├── .env.example
└── .gitignore
```

## .gitignore の主な設定

- `.env`
- `.env.local`
- `__pycache__`
- `node_modules`
- `.next`
- アップロード一時ファイル など

**重要**: `.env` ファイルにはAPIキーやパスワードが含まれるため、絶対にGitにコミットしないでください。

## 利用可能なスクリプト（例）

**Backend**
- `uvicorn app.main:app --reload`

**Frontend**
- `npm run dev`

## Claude

このプロジェクトはClaudeを使った開発を想定しています。

## ライセンス
MIT License

---