import streamlit as st 
from PIL import Image
import time


st.title("streamlit 入門")

"start!!"

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
"Done"

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')


option = st.sidebar.slider('your condition', 0, 100, 50)
options = st.sidebar.text_input("what is your hobby?")
st.write('your hobby is ',options)
st.write("your condition : ", option)

option = st.selectbox(
    'choose the number',
    options=list(range(1, 11)))

'the chosen num : ', option
if st.checkbox('show image'):

    st.write("display image")
    image = Image.open("image.png")
    st.image(image, caption="numpy", use_column_width=True)

