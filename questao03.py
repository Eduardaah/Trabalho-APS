import streamlit as st

def main():
    st.title("🚶 Controle de Boneco")

    if 'pos_x' not in st.session_state: st.session_state.pos_x = 0
    if 'pos_y' not in st.session_state: st.session_state.pos_y = 0

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("⬆️ Subir"): st.session_state.pos_y -= 1
    
    col4, col5, col6 = st.columns([1,2,1])
    with col4:
        if st.button("⬅️ Esquerda"): st.session_state.pos_x -= 1
    with col6:
        if st.button("➡️ Direita"): st.session_state.pos_x += 1
        
    with col2:
        if st.button("⬇️ Descer"): st.session_state.pos_y += 1

    st.write(f"**Posição Atual:** X: {st.session_state.pos_x} | Y: {st.session_state.pos_y}")
    st.write("🕺" + " " * st.session_state.pos_x + " (O boneco está se movendo!)")

if __name__ == "__main__":
    main()
