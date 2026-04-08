import streamlit as st

def main():
    st.title("👥 Cadastro Geral: Herança")
    
    tipo_cadastro = st.radio("Selecione o tipo de cadastro:", ["Funcionário", "Cliente"])
    
    # Atributos da Superclasse (Pessoa)
    st.subheader("Dados Básicos (Pessoa)")
    nome = st.text_input("Nome Completo")
    nasc = st.date_input("Data de Nascimento")
    tel = st.text_input("Telefone")

    # Atributos específicos (Herança)
    if tipo_cadastro == "Funcionário":
        st.subheader("Dados Profissionais")
        matricula = st.text_input("Matrícula")
        salario = st.number_input("Salário Base", min_value=0.0)
    else:
        st.subheader("Dados de Cliente")
        codigo = st.text_input("Código do Cliente")
        profissao = st.text_input("Profissão")

    if st.button(f"Cadastrar {tipo_cadastro}"):
        st.success(f"{tipo_cadastro} {nome} cadastrado com sucesso na branch master!")
        st.balloons()

if __name__ == "__main__":
    main()
