import streamlit as st

def main():
    st.title("🎨 Configurador de Texto (TextoSada)")
    
    texto = st.text_input("Digite o texto de exemplo:", "Texto de Exemplo")
    
    col1, col2 = st.columns(2)
    with col1:
        cor_fonte = st.color_picker("Cor da Fonte", "#000000")
        tamanho_fonte = st.slider("Tamanho da Fonte", 10, 72, 20)
    with col2:
        cor_fundo = st.color_picker("Cor do Fundo", "#FFFFFF")
        tipo_componente = st.selectbox("Tipo de Componente", ["Label", "Botão", "Painel"])

    estilo = f"""
    <div style='background-color: {cor_fundo}; color: {cor_fonte}; font-size: {tamanho_fonte}px; padding: 20px; border-radius: 10px; text-align: center;'>
        {texto}
    </div>
    """
    st.markdown(estilo, unsafe_allow_html=True)
    st.info(f"Componente selecionado: {tipo_componente}")

if __name__ == "__main__":
    main()
