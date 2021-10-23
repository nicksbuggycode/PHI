import streamlit as st

first = st.selectbox('I feel', ['happy', 'sad', 'like a chicken'])
second = st.selectbox('Therefore',['I must peck', 'I mustnt peck', "I'll pick a peck"])
third = st.selectbox('In summary',['Love you noah'])

submit = st.button('click me!!')

if submit:
    st.write('Enjoy your note output below')
    st.write(" ")
    st.write("Here is some standard text that can be inserted wherever in the output: The patient was seen at xyz facility for abc indication")
    st.write(f"I feel {first}, Therefore {second}, In summary {third}")
    print('have a nice day')