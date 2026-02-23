import streamlit as st

st.set_page_config(
    page_title="Meu Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================
# Estado do Tema
# =========================

if "tema" not in st.session_state:
    st.session_state.tema = "dark"

def alternar_tema():
    if st.session_state.tema == "light":
        st.session_state.tema = "dark"
    else:
        st.session_state.tema = "light"

# =========================
# Bootstrap Icons CDN
# =========================

st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">
""", unsafe_allow_html=True)

# =========================
# CSS Tema
# =========================

if st.session_state.tema == "dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: white;
        }
        section[data-testid="stSidebar"] {
            background-color: #161B22;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        img {
            border-radius: 12px;
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.25);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        img:hover {
            transform: scale(1.02);
            box-shadow: 0px 12px 28px rgba(0, 0, 0, 0.35);
        }
        </style>
    """, unsafe_allow_html=True)

# =========================
# Sidebar
# =========================

with st.sidebar:

    col1, col2 = st.columns([4,1])

    with col1:
        st.markdown("### Menu")

    with col2:
        if st.session_state.tema == "light":
            icon = "☾"   # lua branca
        else:
            icon = "☀"   # sol branco

        if st.button(icon, key="theme_btn"):
            alternar_tema()

    st.markdown("---")

    pagina = st.radio(
        "",
        ["Contexto", "Graficos", "Documentos"]
    )

# =========================
# Conteúdo Principal
# =========================

if pagina == "Contexto":

    st.title("Impactos de Desastres Naturais no Setor Industrial")

    st.markdown("---")

    # =========================
    # BLOCO 1 — Introdução
    # =========================

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Artigo Cientifico")

        st.write("""
        Este projeto foi desenvolvido a partir de uma base de dados pública
        nacional que registra ocorrências de desastres naturais ao redor do Brasil.
        

        Uma plataforma oficial que reúne informações sobre desastres ocorridos em todo o Brasil desde 1991.
        Através dela é possível explorar, filtrar e analisar ocorrências por município, tipo de desastre
        e categoria de impacto, com dados apresentados em gráficos, mapas e tabelas interativas.""")

        st.markdown("""
        **Acesse a base oficial aqui:**  
        https://atlasdigital.mdr.gov.br
        """)

    with col2:
        st.image("Impactos_desastres_naturais/desastres/atlas.png", use_container_width=True)

    st.markdown("---")

    # =========================
    # BLOCO 2 — Artigo Científico
    # =========================

    col3, col4 = st.columns([1, 2])

    with col3:
        st.image("Impactos_desastres_naturais/desastres/desastre_4.jfif", width=230)

    with col4:
        st.subheader("Contexto Científico")

        st.write("""
        O estudo aborda a ocorrência de desastres naturais e seus impactos econômicos,
        humanos e estruturais ao longo dos anos.

        A base Atlas contabiliza diferentes tipos de danos, como:

        • Mortes  
        • Pessoas afetadas  
        • Danos econômicos estimados  
        • Tipo de desastre  
        • Região afetada  
        • Setores impactados  

        A partir dessas informações, é possível analisar padrões,
        frequência e intensidade dos eventos ao longo do tempo.
        """)

    st.markdown("---")

    # =========================
    # BLOCO 3 — Foco do Projeto
    # =========================

    st.subheader("Foco no Setor Industrial")

    col5, col6 = st.columns([2, 1])

    with col5:
        st.write("""
        Após uma série de filtros e análises exploratórias realizadas pela equipe,
        decidiu-se direcionar o estudo para os impactos dos desastres naturais
        especificamente no setor industrial.

        O objetivo principal é compreender:

        • Quais tipos de desastres mais impactam a indústria  
        • Quais regiões sofrem maiores prejuízos industriais  
        • Tendências temporais dos danos econômicos  
        • Relação entre intensidade do desastre e perdas industriais  

        A análise busca oferecer uma visão estratégica que possa
        contribuir para planejamento, prevenção e mitigação de riscos.
        """)

    with col6:
        st.image("Impactos_desastres_naturais/desastres/desastre_3.jfif", width=250)

    st.markdown("---")

elif pagina == "Graficos":

    st.title("Análises Gráficas")
    st.markdown("Visualizações geradas a partir dos dados filtrados do Atlas Digital.")
    st.markdown("---")

    # =========================
    # BLOCO 1
    # =========================

    st.markdown("### Filtros Iniciais")
    col1, col2 = st.columns(2)

    with col1:
        st.image("Impactos_desastres_naturais/graficos/grafico_pizza.png", use_container_width=True)

    with col2:
        st.image("Impactos_desastres_naturais/graficos/barra_linha_tempo.png", use_container_width=True)

    st.write("""
    O primeiro grafico mostra qual a dominancia de casos em relação aos desastres,
    com essa informação da para entender que "Chuvas Intensas" e "Estiagem e Seca" são os principais desastres.
    O segundo grafico de barra mostra os desastres com mais aparição em cada ano, ele foi importante para 
    filtrarmos os anos que a equipe iria filtrar que no caso foram dos anos de 2000 - 2023
             
    """)

    st.markdown("---")

    # =========================
    # BLOCO 2
    # =========================

    st.markdown("### Filtros mais Especificos")

    col3, col4 = st.columns(2)

    with col3:
        st.image("Impactos_desastres_naturais/graficos/barra_suldeste.png", use_container_width=True)

    with col4:
        st.image("Impactos_desastres_naturais/graficos/barra_prejuizo.png", use_container_width=True)

    st.write("""
    Conforme a equipe foi realizando a limpeza dos dados, chegamos na conclusão que a região sudeste
    seria a mais adequada para fazer sobre industria no Brasil. O terceiro grafico mostra qual estado
    foi o mais afetado pelos principais desastres filtrados anteriormente que seria o estado de Minas Gerais.
    O quarto grafico fala sobre a concetração de prejuizo em valores que Minas Gerais sofreu em relação aos
    desastres, que no caso foi acima de 160 milhoes de reais apenas com "Chuvas Intensas".
    """)

    st.markdown("---")

    # =========================
    # BLOCO 3
    # =========================

    st.markdown("### Industria + Base Externa")

    col5, col6 = st.columns(2)

    with col5:
        st.image("Impactos_desastres_naturais/graficos/unidades_senai_quantidade.png", use_container_width=True)

    with col6:
        st.image("Impactos_desastres_naturais/graficos/grafico_senai_cidades.png", use_container_width=True)

    st.write("""
    Essa etapa foi realizada com a intenção de deixar as informações e os dados mais completos, então
    a equipe achou uma base externa do senai de minas gerais, falando das unidades que mais foram afetadas
    e chegaram a sofrer algum tipo de prejuizo. O quinto grafico mostra a quantidade de unidades que sofreram
    prejuizo e 2 linhas adicionais com contagem para ter uma noção dos desastres que a pesquisa decidiu forcar.
    O sexto grafico apenas mostra o nome das cidades das cidades escalando do maior para o menos concluindo
    que Juiz de Fora foi o municipio que acabou sofrendo mais com os desastres naturais.
    """)

    st.markdown("---")

    # =========================
    # BLOCO 4
    # =========================

    st.markdown("### Correlações")

    col7, col8 = st.columns(2)

    with col7:
        st.image("Impactos_desastres_naturais/graficos/mapa_correlacao.png", use_container_width=True)

    with col8:
        st.image("Impactos_desastres_naturais/graficos/corelacao_tempo.png", use_container_width=True)

    st.write("""
    Por fim foi realizado um texte matematico chamado correlação de person para comprovar se o numero
    de desastres naturais impactava no setor industrial. O setimo grafico mostra que a correlação foi
    0.70/1 então é uma correlação forte e positiva, isso significa que enquanto as chuvas e seca crescem
    o setor industrial acaba aumentando o numero de prejuiso. O oitavo grafico mostra uma representação
    do setimo grafico de uma forma mais visivel com foco na linha vermelha que significa a linha de prejuiso.
    """)

elif pagina == "Documentos":

    st.title("Documentação e Bases de Dados")
    st.markdown("---")

    # =========================
    # BLOCO 1 — Texto + Imagem
    # =========================

    col1, col2 = st.columns([2,1])

    with col1:
        st.write("""
        Este trabalho foi publico em 2 congressos e 1 revista do Senai São Paulo 2025

        Segue documentação para insiparação, foto do banner para apoio e
        a opção para baixar as bases que foram utilizadas nesse artigo cientifico
                
        Matheus Parizoti - obrigado.
        """)

    with col2:
        st.image("Impactos_desastres_naturais/grupo.jfif", use_container_width=True)

    st.markdown("---")

    # =========================
    # BLOCO 2 — Documento Principal
    # =========================

    st.subheader("Artigo / Relatório Completo")

    st.write("O documento completo do estudo pode ser visualizado abaixo:")

    # Se for PDF
    with open("./arquivo_original_impactos_setor_industrial.pdf", "rb") as file:
        st.download_button(
            label="Baixar Documento Completo",
            data=file,
            file_name="Artigo_Desastres_Industria.pdf",
            mime="application/pdf"
        )
    with open("./SENAI_Suico_Brasileira.pdf", "rb") as file:
        st.download_button(
            label="Baixar Banner",
            data=file,
            file_name="Banner.pdf",
            mime="application/pdf"
        )

    st.markdown("---")

    # =========================
    # BLOCO 3 — Bases de Dados
    # =========================

    st.subheader("📊 Bases de Dados Utilizadas")

    col3, col4 = st.columns(2)

    # Base 1
    with col3:
        st.markdown("### Base de Dados")

        with open("./df_reduzido.xlsx", "rb") as file:
            st.download_button(
                label="Baixar Base Atlas",
                data=file,
                file_name="df_reduzido.xlsx",
                mime="text/csv"
            )

    # Base 2
    with col4:
        st.markdown("### Base de Dados Senai")

        with open("./unidades_senai.xlsx", "rb") as file:
            st.download_button(
                label="Baixar Base Senai",
                data=file,
                file_name="unidades_senai.xlsx",
                mime="text/csv"
            )