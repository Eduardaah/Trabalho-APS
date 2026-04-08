import streamlit as st

def main():
    st.title("🛒 Lista de Compras Inteligente")
    
    if 'itens_compra' not in st.session_state: st.session_state.itens_compra = []

    with st.form("add_item"):
        col1, col2 = st.columns(2)
        produto = col1.text_input("Produto")
        unidade = col2.text_input("Unidade (ex: kg, un)")
        
        qtd_prevista = st.number_input("Qtd Prevista", min_value=0.0)
        preco_est = st.number_input("Preço Estimado (R$)", min_value=0.0)
        
        if st.form_submit_button("Adicionar à Lista"):
            st.session_state.itens_compra.append({
                "Produto": produto, "Unid": unidade, 
                "Previsto": qtd_prevista, "Estimado": preco_est,
                "Real": 0.0, "Total": 0.0
            })

    if st.session_state.itens_compra:
        st.subheader("📋 Itens na Lista")
        for i, item in enumerate(st.session_state.itens_compra):
            col_a, col_b = st.columns([3, 1])
            item["Real"] = col_a.number_input(f"Qtd Real comprada de {item['Produto']}", key=f"real_{i}")
            item["Total"] = item["Real"] * item["Estimado"]
            
        st.table(st.session_state.itens_compra)
        total_geral = sum(item["Total"] for item in st.session_state.itens_compra)
        st.header(f"Total da Compra: R$ {total_geral:.2f}")

if __name__ == "__main__":
    main()
