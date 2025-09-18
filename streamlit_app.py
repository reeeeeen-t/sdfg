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
        "question": "2人乗りのボートで、各漕手が2本ずつオールを持つ艇種は何ですか？",
        "options": ["ペア", "クォドルプル", "ダブルスカル", "シングルスカル"],
        "answer": "ダブルスカル"
    },
    {
        "question": "ボート競技で、漕手が進行方向に対して背中を向けて座る理由は何ですか？",
        "options": ["推進力を最大化するため", "視界を確保するため", "バランスを保つため", "ルールで定められているため"],
        "answer": "推進力を最大化するため"
    },
    {
        "question": "ボートのスピードを上げるために、漕手全員がオールを同時に水から上げる動作を何と呼びますか？",
        "options": ["ブレード", "ストレッチャー", "リカバリー", "ドライブ"],
        "answer": "リカバリー"
    },
    {
        "question": "オリンピックのボート競技の距離は何メートルですか？",
        "options": ["1000m", "1500m", "2000m", "5000m"],
        "answer": "2000m"
    },
    {
        "question": "艇の進路をまっすぐにするための、船尾についている舵を何と呼びますか？",
        "options": ["コックス", "ラダー", "ブレード", "ストレッチャー"],
        "answer": "ラダー"
    },
    {
        "question": "1分間にオールを漕ぐ回数を表す専門用語は何ですか？",
        "options": ["ピッチ", "ストローク", "レート", "テンポ"],
        "answer": "レート"
    },
    {
        "question": "ボート競技において、漕手ではなく、艇の舵をとり、クルーに指示を出す役割の選手を何と呼びますか？",
        "options": ["バウ", "ストローク", "コックス", "ステア"],
        "answer": "コックス"
    },
    {
        "question": "オールが水に押し戻され、ハンドルが腹部に強く当たるアクシデントを俗に何と呼びますか？",
        "options": ["腹切り", "キャッチ・ア・クラブ", "クラッチ", "ハングオーバー"],
        "answer": "腹切り"
    },
    {
        "question": "ボート競技で使われる艇の最も速い艇種は何ですか？",
        "options": ["シングルスカル", "ダブルスカル", "舵手付きフォア", "エイト"],
        "answer": "エイト"
    }
]

# セッション状態を初期化
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_number" not in st.session_state:
    st.session_state.question_number = 0
if "quiz_order" not in st.session_state:
    st.session_state.quiz_order = random.sample(range(len(quizzes)), len(quizzes))
if "answered" not in st.session_state:
    st.session_state.answered = False
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

# ページタイトルを設定
st.title("🚣 ローイングクイズゲーム")

# ゲームの状態を管理する
# ここで `st.session_state.question_number` がクイズの総数未満であることを確認
if st.session_state.question_number < len(quizzes):
    # クイズの表示
    current_quiz_index = st.session_state.quiz_order[st.session_state.question_number]
    current_quiz = quizzes[current_quiz_index]

    st.header(f"第 {st.session_state.question_number + 1} 問")
    st.write(current_quiz["question"])

    # 回答済みの場合は結果を表示、未回答の場合は選択肢を表示
    if st.session_state.answered:
        # ユーザーが選択した答えを表示
        st.write(f"あなたの答え: **{st.session_state.user_answer}**")
        
        # 正解/不正解の表示
        if st.session_state.user_answer == current_quiz["answer"]:
            st.success("正解です！👏")
        else:
            st.error(f"残念！不正解です。正解は「{current_quiz['answer']}」でした。")
        
        # 次の質問へ進むボタン
        if st.button("次の問題へ"):
            st.session_state.question_number += 1
            st.session_state.answered = False
            st.rerun()
    else:
        # 未回答の場合の選択肢表示
        options_shuffled = random.sample(current_quiz["options"], len(current_quiz["options"]))
        user_answer = st.radio("以下の選択肢から選んでください:", options_shuffled, key=st.session_state.question_number)

        # 回答ボタン
        if st.button("回答する"):
            st.session_state.user_answer = user_answer
            st.session_state.answered = True
            
            # 正解の場合、スコアを加算
            if user_answer == current_quiz["answer"]:
                st.session_state.score += 1
                st.balloons()
            st.rerun()

else:
    # 全問終了後の表示
    st.info("全問終了しました。")
    st.subheader(f"あなたの最終スコア: {st.session_state.score} / {len(quizzes)}")
    
    # もう一度プレイするボタンを大きく表示
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>もう一度プレイしますか？</h3>", unsafe_allow_html=True)
    if st.button("🚣 最初からやり直す", key="restart_button"):
        st.session_state.score = 0
        st.session_state.question_number = 0
        st.session_state.answered = False
        st.session_state.quiz_order = random.sample(range(len(quizzes)), len(quizzes))
        st.rerun()

# 現在のスコアをサイドバーに表示
st.sidebar.subheader("現在の進行状況")
st.sidebar.write(f"**スコア**: {st.session_state.score} / {st.session_state.question_number}")
st.sidebar.progress(st.session_state.question_number / len(quizzes))