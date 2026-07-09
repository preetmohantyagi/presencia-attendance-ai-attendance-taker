import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: var(--snap-primary) !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:var(--snap-cream) !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: var(--snap-cream) !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            :root {
                --snap-primary: #4A2545;
                --snap-primary-light: #F1E4EC;
                --snap-accent: #F2A93B;
                --snap-accent-tint: rgba(242, 169, 59, 0.14);
                --snap-ink: #231D24;
                --snap-cream: #FBF3E7;
                --snap-card: #FFFDF8;
                --snap-border: #EBDFCF;
                --snap-text-heading: #2B2620;
                --snap-text-muted: #7A6F63;
            }

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            .stApp {
                color: var(--snap-text-heading);
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: var(--snap-primary) !important;
                color: var(--snap-cream) !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: var(--snap-accent) !important;
                color: var(--snap-ink) !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: var(--snap-ink) !important;
                color: var(--snap-cream) !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)