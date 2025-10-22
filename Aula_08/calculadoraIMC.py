import streamlit as st # type: ignore

st.header("Calculadora de imc", divider=True)

altura = st.number_input("Digite sua altura:")
peso = st.number_input("Digite seu peso:")

if altura > 0 and peso > 0:
    IMC = peso/(altura**2)
    st.text(f"Seu IMC é: {IMC}")
    
    if IMC < 16:
        st.text(f"Sua classificação é: Magreza grave")
        
    elif IMC >= 16 and IMC < 17:
        st.text(f"Sua classificação é: Magreza moderada")
        
    elif IMC >= 17 and IMC < 18.5:
        st.text(f"Sua classificação é: Magreza leve")
        
    elif IMC >= 18.5 and IMC < 25:
        st.text(f"Sua classificação é: Saudável")
        
    elif IMC >= 25 and IMC < 30:
        st.text(f"Sua classificação é: Sobrepeso")
        
    elif IMC >= 30 and IMC < 35:
        st.text(f"Sua classificação é: obesidade grau I")
        
    elif IMC >= 35 and IMC < 40:
        st.text(f"Sua classificação é: obesidade grau II")

    elif IMC >= 40:
        st.text(f"Sua classificação é: obesidade grau III")