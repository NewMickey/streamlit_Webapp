import streamlit as st
import datetime


with st.form(key="profile_form"):
        name = st.text_input("名前")
        address = st.text_input("住所")

        age_category = st.radio(
                "年齢層",
                ("子供(18歳未満)","大人(18歳以上)"))

        hobby = st.multiselect(
                "趣味",
                ("スポーツ", "読書", "プログラミング", "アニメ", "映画", "釣り", "料理"))

        mail_subscribe = st.checkbox("メールマガジンを購読する")

        height = st.slider("身長", min_value=120, max_value=200)

        start_date = st.date_input("開始日", datetime.date(2024, 7, 28))

        color = st.color_picker("テーマカラー", "#00f900")


        submit_btn = st.form_submit_button("送信")
        cancel_btn = st.form_submit_button("キャンセル")

        if submit_btn:
                st.text(f"ようこそ{name}さん、{address}に書類を発送いたしました")

                if age_category == "大人(18歳以上)":
                        st.text(f"あなたの年齢層:{age_category}")
                else:
                        st.text(f"あなたの年齢層:{age_category}")
        
                st.text(f"あなたの趣味:{', '.join(hobby)}。いいですね")
                if height > 170:
                        st.text(f"身長は{height}か、平均より高いですね")
                else:
                        st.text(f"身長は{height}か、これからに期待です")

        elif cancel_btn:
                st.warning("フォームがキャンセルされました")