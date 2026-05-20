import streamlit as st

cor_de_fundo = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #082032;
    text-color: #ffffff;
}
</style>
"""
st.markdown(cor_de_fundo, unsafe_allow_html=True)

st.set_page_config(page_title="Parceria", page_icon="💻", layout="wide")
st.title("Empresas Parceiras")
st.write("interaja com nossas empresas parceiras.")


col1, col2, col3 = st.columns(3)

with col1:
    st.image("space.jpg",width=600)
    st.title("SpaceX")
    st.write("É uma empresa aeroespacial privada americana que projeta, fabrica e lança foguetes e espaçonaves avançadas, com a missão final de baratear o acesso ao espaço e viabilizar a colonização humana em outros planetas.")
    st.link_button("Acessar SpaceX","https://www.spacex.com/")

with col2:
    st.image("apple.webp",width=600)
    st.title("Apple")
    st.write("é uma empresa multinacional norte-americana que tem o objetivo de projetar e comercializar produtos eletrônicos de consumo, software de computador e computadores pessoais. ")
    st.link_button("Acessar Apple","https://www.apple.com/br/")



with col3:
    st.image("net.jpg",width=600)
    st.title("Netflix")
    st.write("É um serviço de streaming que oferece uma ampla variedade de séries, filmes e documentários premiados em milhares de aparelhos conectados à internet.")
    st.link_button("Acessar Netflix","https://www.netflix.com/br/")
