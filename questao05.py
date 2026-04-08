import streamlit as st

def main():
    st.title("💰 Controle de Gastos Diários")
    
    if 'gastos' not in st.session_state: st.session_state.gastos = []

    tipo = st.text_input("Tipo de Gasto (Ex: Alimentação)")
    valor = st.number_input("Valor (R$)", min_value=0.0)
    forma = st.selectbox("Forma de Pagamento", ["PIX", "Crédito", "Débito", "Dinheiro"])

    if st.button("Registrar Gasto"):
        st.session_state.gastos.append({"Tipo": tipo, "Valor": valor, "Pagamento": forma})
    
    if st.session_state.gastos:
        st.table(st.session_state.gastos)
        total = sum(g['Valor'] for g in st.session_state.gastos)
        st.metric("Total Gasto", f"R$ {total:.2f}")

if __name__ == "__main__":
    main()
