import streamlit as st
from datetime import datetime, timedelta

def main():
    st.title("💊 Gestão de Medicamentos")
    
    nome = st.text_input("Nome do Paciente")
    remedio = st.text_input("Nome do Remédio")
    data_ini = st.date_input("Data de Início")
    dias = st.number_input("Quantidade de dias", min_value=1)
    vezes = st.number_input("Vezes ao dia", min_value=1)

    if st.button("Gerar Planilha de Horários"):
        st.subheader(f"Planilha para: {nome}")
        intervalo = 24 // vezes
        data_atual = datetime.combine(data_ini, datetime.min.time())
        
        for i in range(int(dias * vezes)):
            st.write(f"⏰ Tomar {remedio} em: {data_atual.strftime('%d/%m/%Y às %H:%M')}")
            data_atual += timedelta(hours=intervalo)

if __name__ == "__main__":
    main()
