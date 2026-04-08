import streamlit as st

def main():
    st.title("🍽️ Comanda Eletrônica")
    
    if 'itens' not in st.session_state: st.session_state.itens = []

    prod = st.text_input("Produto")
    qtd = st.number_input("Quantidade", min_value=1)
    preco = st.number_input("Preço Unitário", min_value=0.0)

    if st.button("Adicionar à Comanda"):
        st.session_state.itens.append({"Produto": prod, "Qtd": qtd, "Preço": preco, "Subtotal": qtd*preco})

    if st.session_state.itens:
        st.table(st.session_state.itens)
        total = sum(i['Subtotal'] for i in st.session_state.itens)
        st.header(f"Total a Pagar: R$ {total:.2f}")

if __name__ == "__main__":
    main()
