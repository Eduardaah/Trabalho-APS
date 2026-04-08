import streamlit as st

def main():
    st.set_page_config(page_title="Sistema de Conta de Luz", page_icon="💡")
    st.title("💡 Gestão de Consumo: Conta de Luz")
    
    # Criando a lista de contas na memória do navegador
    if 'contas' not in st.session_state:
        st.session_state.contas = []

    # Formulário de Cadastro (Atributos do seu Diagrama)
    st.subheader("Cadastrar Nova Leitura")
    with st.form("form_luz"):
        col1, col2 = st.columns(2)
        with col1:
            data_leitura = st.date_input("Data da Leitura")
            num_leitura = st.number_input("Número da Leitura", min_value=0)
        with col2:
            kw_gasto = st.number_input("Kw Gastos", min_value=0.0)
            valor_pagar = st.number_input("Valor a Pagar (R$)", min_value=0.0)
        
        btn_cadastrar = st.form_submit_button("Salvar Leitura")

    # Lógica do botão (Método cadastrar do seu diagrama)
    if btn_cadastrar:
        nova_leitura = {
            "Data": data_leitura.strftime("%d/%m/%Y"),
            "Leitura": num_leitura,
            "Consumo (Kw)": kw_gasto,
            "Valor (R$)": valor_pagar
        }
        st.session_state.contas.append(nova_leitura)
        st.success("Conta registrada com sucesso!")

    # Exibição e Cálculos (Métodos de Verificação)
    if st.session_state.contas:
        st.divider()
        st.subheader("📊 Histórico de Leituras")
        st.table(st.session_state.contas)
        
        # Cálculos automáticos
        lista_kw = [c["Consumo (Kw)"] for c in st.session_state.contas]
        media = sum(lista_kw) / len(lista_kw)
        maior = max(lista_kw)
        menor = min(lista_kw)
        
        # Painel de Resultados
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Média Consumo", f"{media:.2f} Kw")
        col_b.metric("Maior Gasto", f"{maior} Kw", delta_color="inverse")
        col_c.metric("Menor Gasto", f"{menor} Kw")
    else:
        st.info("Nenhuma conta cadastrada ainda.")

if __name__ == "__main__":
    main()
