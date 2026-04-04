import streamlit as st

st.markdown("# Calculadora")
op = st.radio("Qual operação deseja realizar?", [
              "Adição", "Subtração", "Multiplicação", "Divisão"])
col1, col2 = st.columns(2)
with col1:
    n1 = st.number_input("Escolha o primeiro número", -10000, 10000, value=0)
with col2:
    n2 = st.number_input("Escolha o segundo número", -10000, 10000, value=0)

match op:
    case "Adição":
        resul = n1 + n2
    case "Subtração":
        resul = n1 - n2
    case "Multiplicação":
        resul = n1*n2
    case "Divisão":
        if n2 == 0:
            st.error("Divisão por 0")
        else:
            resul = n1/n2

sinais = {
    "Adição": "+",
    "Subtração": "-",
    "Multiplicação": "*",
    "Divisão": "/"
}

if not (op == "Divisão" and n2 == 0):
    st.title("Resultado")
    
    if op == "Divisão":
        st.latex(fr"\Huge \frac{{{n1}}}{{{n2}}}" "\ " "=" "\ " fr"{resul}")
    else:
        st.latex(rf"\Huge {n1}""\ " rf"{sinais[op]}" "\ " rf"{n2}" "\ " "=" "\ " fr"{resul}")