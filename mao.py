import streamlit as st
import cards



quantidade=4

def desenharMao(player):
    Cartas = cards.pegarCartas(player)
    #print(Cartas)
    
    cols = st.columns(quantidade)
    for i,carta in enumerate(Cartas):
        #print(carta)
        col = cols[i%quantidade]
        with col:
            st.image(carta['image'],use_container_width=False)
            if (i+1)%quantidade == 0:
                cols = st.columns(len(Cartas))

    st.markdown("---")
    st.write(player+" "+cards.pontuacao(Cartas))
    if int(cards.pontuacao(Cartas))>21:
        st.error("você estorou")

def desenharMesa(show):
    player = "mesa"
    Cartas = cards.pegarCartas(player)
    #print(Cartas)
    cols = st.columns(len(Cartas))    
    for i,carta in enumerate(Cartas):
        #print(carta)
        col = cols[i%quantidade]
        with col:
            if show == True or i == 0:
                st.image(carta['image'],use_container_width=False)
            else:
                st.image("https://deckofcardsapi.com/static/img/back.png",use_container_width=False)
        if (i+1)%quantidade == 0:
            cols = st.columns(len(Cartas))
    st.markdown("---")
    st.write(player+" ")
    if show == True:
        st.write("Pontuação"+cards.pontuacao(Cartas))

