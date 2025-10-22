import streamlit as st # type: ignore

st.header("Conversor de moedas", divider=True)

opcoes = ["Dolar", "Euro"]

opcao_selecionada = st.selectbox("Escolha a moeda para qual deseja converter:", opcoes)

valor = st.number_input("Digite o valor em reais que deseja converter.")

dolar = valor * 5.4
euro = valor * 6.27

if valor > 0:
    if opcao_selecionada == "Dolar":

        st.text(f"O valor em dolares é: {dolar}")
    elif opcao_selecionada == "Euro":
        st.text(f"O valor em euros é: {euro}")