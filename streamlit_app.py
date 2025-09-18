import streamlit as st
import random

# クイズの問題と答えのリストを定義
quizzes = [
    {
        "question": "ボートを前に進めるために、オールを水中で引く動作を何と呼びますか？",
        "options": ["リカバリー", "キャッチ", "フィニッシュ", "ドライブ"],
        "answer": "ドライブ"
    },
    {
        "question": "2人乗りのボートで、各漕手が1本ずつオールを持つ艇種は何ですか？",
        "options": ["ペア", "クォドルプル", "ダブルスカル", "シングルスカル"],
        "answer": "ダブルスカル"
    },
    {
        "question": "ボートのスピードを上げるために、漕手全員がオールを同時に水から上げる動作を何と呼びますか？",
        "options": ["ブレード", "ストレッチャー", "リカバリー", "ドライブ"],
        "answer": "リカバリー"
    },
    {
        "question": "オリンピックで最も速いタイムが出るのは、何メートル競漕ですか？",
        "options": ["1000m", "1500m", "2000m", "5000m"],
        "answer": "2000m"
    },
    {
        "question": "艇の進路をまっすぐにするための、船尾についている舵を何と呼びますか？",
        "options": ["コックス", "ラダー", "ブレード", "ストレッチャー"],
        "answer": "ラダー"
    }
]

# ページタイトルを設定
st.title("🚣 ローイングクイズゲーム")

# セッション状態を初期化
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_number" not in st.session_state:
    st.session_state.question_number = 0
if "quiz_order" not in st.session_state:
    st.session_state.quiz_order = random.sample(range(len(quizzes)), len(quizzes))

# 現在のクイズを取得
current_quiz_index = st.session_state.quiz_order[st.session_state.question_number]
current_quiz = quizzes[current_quiz_index]

# クイズを表示
st.header(f"第 {st.session_state.question_number + 1} 問")
st.write(current_quiz["question"])

# 選択肢をシャッフル
options_shuffled = random.sample(current_quiz["options"], len(current_quiz["options"]))
user_answer = st.radio("以下の選択肢から選んでください:", options_shuffled)

# 回答ボタン
if st.button("回答する"):
    if user_answer == current_quiz["answer"]:
        st.success("正解です！👏")
        st.session_state.score += 1
    else:
        st.error(f"残念！不正解です。正解は「{current_quiz['answer']}」でした。")
    
    # 次の質問へ
    if st.session_state.question_number + 1 < len(quizzes):
        st.session_state.question_number += 1
        st.rerun()
    else:
        st.info("全問終了しました。")
        st.subheader(f"あなたのスコア: {st.session_state.score} / {len(quizzes)}")
        
        # もう一度プレイするボタン
        if st.button("もう一度プレイする"):
            st.session_state.score = 0
            st.session_state.question_number = 0
            st.session_state.quiz_order = random.sample(range(len(quizzes)), len(quizzes))
            st.rerun()

# 現在のスコアを表示
st.sidebar.subheader("現在のスコア")
st.sidebar.write(f"{st.session_state.score} / {st.session_state.question_number}")