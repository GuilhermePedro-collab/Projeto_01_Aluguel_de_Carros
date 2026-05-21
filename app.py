import streamlit as st
st.title('Gp Automotors - Aluguel de Carros ')
st.sidebar.title('Escolha seu modelo: ')
st.sidebar.image('logo.png')

carros = ['Nivus Highline', 'Jeep Commander', 'Hilux sw4', 'Jetta Gli', 'Gs 310']

opcao = st.sidebar.selectbox('Escolha o automovel que voce quer alugar', carros)

st.image(f'{opcao}.png')
st.markdown(f'## Voce alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado? ')
km = st.text_input(f'Quantos km voce rodou com o {opcao}')

if opcao == 'Nivus Highline' :
    diaria = 450

elif opcao == 'Jeep Commander' :
    diaria = 550

elif opcao == 'Hilux sw4' :
    diaria = 550    

elif opcao == 'Jetta Gli' :
    diaria = 500

elif opcao == 'Gs 310' :
    diaria = 320 

if st.button('Calcular') :
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria 
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Voce alugou o {opcao} por {dias} dias e rodou km{km}. O valor total a pgar é R${aluguel_total:.2f}')