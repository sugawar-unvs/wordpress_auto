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
├── backend/                          # FastAPI バックエンド
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPIアプリケーション エントリポイント
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── v1/                    # API v1 (バージョニング対応)
│   │   │       ├── __init__.py
│   │   │       ├── router.py          # ルーター集約
│   │   │       └── endpoints/         # エンドポイント別ファイル
│   │   │           ├── __init__.py
│   │   │           ├── uploads.py     # 画像アップロード
│   │   │           ├── posts.py       # 記事生成・取得
│   │   │           └── comments.py    # 過去コメント取得
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py             # pydantic-settings 環境変数管理
│   │   │   ├── dependencies.py       # FastAPI Dependencies
│   │   │   ├── security.py           # APIキー認証
│   │   │   └── celery_app.py         # Celery設定
│   │   ├── schemas/                   # Pydantic スキーマ
│   │   │   ├── __init__.py
│   │   │   ├── upload.py
│   │   │   └── post.py
│   │   ├── services/                  # ビジネスロジック
│   │   │   ├── __init__.py
│   │   │   ├── upload_service.py     # 画像保存処理
│   │   │   ├── post_service.py      # 記事生成フロー
│   │   │   ├── wp_service.py        # WordPress REST API連携
│   │   │   └── ai_service.py        # Claude/LiteLLM記事生成
│   │   └── tasks/                     # Celery非同期タスク
│   │       ├── __init__.py
│   │       └── post_task.py          # 記事生成タスク
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── test_health.py
│   │   └── services/
│   │       └── __init__.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── .env.example
│
├── frontend/                         # Next.js 15 フロントエンド
│   ├── src/
│   │   ├── app/                      # App Router
│   │   │   ├── layout.tsx            # ルートレイアウト
│   │   │   ├── page.tsx              # ホームページ
│   │   │   ├── loading.tsx           # 共通ローディングUI
│   │   │   ├── error.tsx             # 共通エラーUI
│   │   │   ├── not-found.tsx         # 404ページ
│   │   │   └── globals.css           # TailwindベースCSS
│   │   ├── components/
│   │   │   ├── upload-form.tsx       # 画像アップロードフォーム
│   │   │   └── ui/                   # shadcn/ui コンポーネント
│   │   │       ├── button.tsx
│   │   │       ├── toast.tsx
│   │   │       └── toaster.tsx
│   │   ├── hooks/
│   │   │   └── use-toast.ts          # トースト通知フック
│   │   └── lib/
│   │       ├── utils.ts              # cn() ユーティリティ
│   │       └── api.ts                # バックエンドAPIクライアント
│   ├── public/                       # 静的アセット
│   ├── Dockerfile
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── .env.example
│
├── prompts/                          # Claudeプロンプトテンプレート
├── docker-compose.yml                # Docker Compose (backend + celery + frontend + redis)
├── .gitignore
└── README.md
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