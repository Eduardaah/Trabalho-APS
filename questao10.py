import streamlit as st

def main():
    st.title("🏢 Reserva de Salas de Reunião")
    
    if 'reservas' not in st.session_state: st.session_state.reservas = []

    with st.form("reserva"):
        func = st.text_input("Funcionário Responsável")
        sala = st.selectbox("Escolha a Sala", ["Sala A (Grande)", "Sala B (Média)", "Auditório"])
        data = st.date_input("Data")
        horario = st.time_input("Horário")
        assunto = st.text_area("Assunto da Reunião")
        
        if st.form_submit_button("Confirmar Reserva"):
            st.session_state.reservas.append({
                "Sala": sala, "Data": data, "Hora": horario, 
                "Responsável": func, "Assunto": assunto
            })

    if st.session_state.reservas:
        st.subheader("📅 Próximas Reuniões")
        st.table(st.session_state.reservas)

if __name__ == "__main__":
    main()
