import streamlit as st

def main():
    st.title("💿 Minha Coleção de CDs")
    
    if 'colecao' not in st.session_state: st.session_state.colecao = []

    with st.expander("Cadastrar Novo CD"):
        titulo = st.text_input("Título do CD")
        artista = st.text_input("Artista Principal")
        ano = st.number_input("Ano", min_value=1900, max_value=2026)
        
        col1, col2 = st.columns(2)
        duplo = col1.checkbox("CD Duplo?")
        coletanea = col2.checkbox("É Coletânea?")
        
        musicas = st.text_area("Lista de Músicas (uma por linha)")

        if st.button("Salvar na Coleção"):
            st.session_state.colecao.append({
                "Título": titulo, "Artista": artista, "Ano": ano,
                "Duplo": "Sim" if duplo else "Não",
                "Coletânea": "Sim" if coletanea else "Não",
                "Músicas": musicas.split('\n')
            })

    busca = st.text_input("🔍 Buscar por Artista")
    if busca:
        resultados = [cd for cd in st.session_state.colecao if busca.lower() in cd['Artista'].lower()]
        st.write(f"Encontrados {len(resultados)} CDs:")
        st.table(resultados)
    else:
        st.table(st.session_state.colecao)

if __name__ == "__main__":
    main()
