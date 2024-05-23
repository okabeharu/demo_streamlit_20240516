import streamlit as st
from PIL import Image  

st.title('サブカル系アイドルグループ')
st.title(' :red[マーキュロ] :crossed_flags:')

st.caption('2022年6月24日始動')
st.caption('グループ名は消毒液であるマーキュロクロム液から由来病んだ傷を治す存在になれますように.')

st.caption("""
メンバーは7人
藍咲ユウリ 珖夜ゼラ 翠城ニア 紫月レンゲ 我執キル 芥タマキ 雅楽代カミテ""")

image = Image.open('マーキュロ７代目全体アー写.jpeg')
st.image(image, width=700)