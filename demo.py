import streamlit as st

st.title('サブカル系アイドルグループ')
st.title(':red[マーキュロ] :crossed_flags:')

st.caption('2022年6月24日始動')
st.caption('グループ名は消毒液であるマーキュロクロム液から由来病んだ傷を治す存在になれますように.')
st.caption('A caption with _italics_ :blue[colors] and emojis :')

col1, col2, col3 = st.beta_columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", use_column_width=True)
    
with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", use_column_width=True)