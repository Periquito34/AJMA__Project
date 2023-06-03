import streamlit as st
from graphviz import Digraph

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}


def decode_morse_code(morse_code):
    morse_code = morse_code.strip().split(' ')
    decoded_message = ''
    for code in morse_code:
        if code == '/':
            decoded_message += ' '  # Espacio en blanco entre palabras
        else:
            for key, value in morse_code_dict.items():
                if code == value:
                    decoded_message += key
                    break
    return decoded_message


def encode_to_morse_code(message):
    message = message.upper()
    encoded_message = ''
    for char in message:
        if char == ' ':
            encoded_message += '/ '  # Espacio vacío en Morse como '/'
        elif char in morse_code_dict:
            # Un espacio para separar las letras en código Morse
            encoded_message += morse_code_dict[char] + ' '
    return encoded_message


def generate_binary_tree(word):
    G = Digraph()
    nodes = list(word)
    G.attr(rankdir='LR')  # Orientación del gráfico de izquierda a derecha
    G.attr('node', shape='circle')  # Forma de los nodos
    G.attr('node', style='filled')  # Estilo de los nodos

    for i in range(len(nodes)):
        G.node(str(i), label=nodes[i])

    if len(nodes) > 1:
        for i in range(1, len(nodes)):
            G.edge(str(i // 2), str(i))

    st.graphviz_chart(G.source)


def codificador():
    st.markdown(
    """
    <style>
    .custom-header {
        color: #31333F;
        font-size: 45px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown('<p class="custom-header">DECODIFICADOR</p><br>', unsafe_allow_html=True)

    option = st.radio("Selecciona una opción:",
                      ("Decodificar Morse", "Convertir a Morse"))

    if option == "Decodificar Morse":
        morse_code = st.text_input("Ingresa el mensaje en Código Morse")
        if st.button("Decodificar"):
            decoded_message = decode_morse_code(morse_code)
            st.success(f"Mensaje decodificado: {decoded_message}")
            generate_binary_tree(decoded_message)

    elif option == "Convertir a Morse":
        message = st.text_input("Ingresa el mensaje en texto")
        if st.button("Convertir"):
            encoded_message = encode_to_morse_code(message)
            st.success(f"Mensaje en Código Morse: {encoded_message}")
            generate_binary_tree(message)
