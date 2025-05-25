import streamlit as st
from mao import *
import cards

def vencedor():
    TabelaDePontuacao={ "jogador1":cards.pontos("jogador1"),
                        "jogador2":cards.pontos("jogador2")}
    jogadoresRodada = dict(filter(lambda item: item[1] <= 21, TabelaDePontuacao.items()))
    if len(jogadoresRodada)>=1:
        maior = max(jogadoresRodada.values())
        vencedores = list(filter(lambda item: item[1] == maior, jogadoresRodada.items()))
        return vencedores,maior
    else:
        return [[],1]

if 'p1_disabled' not in st.session_state:
    st.session_state.p1_disabled = False
    st.session_state.p2_disabled = False
    st.session_state.mesa_disabled = False

if st.button("reset"):
    st.session_state.p1_disabled = False
    st.session_state.p2_disabled = False
    st.session_state.mesa_disabled = False
    cards.requisicao("pile/jogador1/return")
    cards.requisicao("pile/jogador2/return")
    cards.requisicao("pile/mesa/return")
    cards.sacar("jogador1")
    cards.sacar("jogador2")
    cards.sacar("mesa")

[x,mesa,y] = st.columns(3)
with mesa:
    if st.session_state.p1_disabled == True and st.session_state.p2_disabled == True:
        [vencedores, maior]=vencedor()
        mesa = cards.pontos("mesa")
        if st.session_state.mesa_disabled == False:
            #banca pode vencer 
            if mesa == 21 or mesa >= vencedores[0][1]:
                st.session_state.mesa_disabled=True
                st.rerun()
            else:
                S3 = st.button("sacar carta", disabled=st.session_state.mesa_disabled,key="banca")
                if S3:
                    pontos=cards.sacar("mesa",1)
                    if (pontos >= 21):
                        st.session_state.mesa_disabled=True
                    st.rerun()
        else:               
            if mesa <=21 and mesa > vencedores[0][1]:
                st.success("A banca vence")
            else:
                if mesa == vencedores[0][1]:
                    st.success(f"Empate entre: A banca e o {vencedores[0][0]} com {maior} pontos.")
                elif len(vencedores) > 1:
                    st.success(f"Empate entre: {', '.join([v[0] for v in vencedores])} com {maior} pontos.")
                else:
                    st.success(f"Vencedor: {vencedores[0][0]} com {maior} pontos.")
        desenharMesa(True)
    else:
        desenharMesa(False)

[jogador1, jogador2] = st.columns(2)
      
with jogador1:
    with st.container():
        desenharMao("jogador1")
        if st.session_state.p1_disabled == False:
            S1 = st.button("sacar carta", disabled=st.session_state.p1_disabled)
            if S1:
                pontos=cards.sacar("jogador1",1)
                if (pontos >= 21):
                    st.session_state.p1_disabled=True
                st.rerun()
            P1 = st.button("parar", disabled=st.session_state.p1_disabled)
            if P1:
                st.session_state.p1_disabled=True
                st.rerun()
                
with jogador2:
    with st.container():
        desenharMao("jogador2")
        if st.session_state.p2_disabled == False:
            S2 = st.button("sacar carta", disabled=st.session_state.p2_disabled,key="sacarp2")
            if S2:
                pontos=cards.sacar("jogador2",1)
                if (pontos >= 21):
                    st.session_state.p2_disabled=True
                st.rerun()
            P2 = st.button("parar", disabled=st.session_state.p2_disabled,key="pararp2")
            if P2:                
                st.session_state.p2_disabled=True
                st.rerun()


