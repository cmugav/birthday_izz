import streamlit as st
from datetime import datetime
from PIL import Image
import time

st.set_page_config(page_title = "HAPPY BIRTHDAY POOKIE", layout="centered")

st.markdown("""
    <style>
    #MainMenu, header, footer {
        visibility: hidden;
    }

    .css-18ni7ap.e8zbici2 {
        padding-top: 0rem;
    }

    .container {
        max-width: 375px;
        margin: auto;
        padding: 1.5rem;
        border-radius: 1rem;
        background-color: #f9f9f9;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'section' not in st.session_state:
    st.session_state.section = 'Menu'

# --- MAIN CONTAINER ---
st.markdown('<div class="container">', unsafe_allow_html=True)

# --- MENU ---
if st.session_state.section == 'Menu':
    st.title("HAPPY BIRTHDAY POOKIE")

    st.button("Cumpleaños Feliz", key="home", help="Happy berdei to you",
              on_click=lambda: st.session_state.update(section='Cumpleaños Feliz'))

    st.button("Dear Izzy", key="love", help="A little letter for you",
              on_click=lambda: st.session_state.update(section='Dear Izzy'))

    st.button("Some of my favorite photos", key="photos", help="Photos",
              on_click=lambda: st.session_state.update(section='Some of my favorite photos'))

    st.button("Countdown", key="countdown", help="Countdown",
              on_click=lambda: st.session_state.update(section='Countdown'))

    st.divider()

# --- SECTION CONTENT ---
section = st.session_state.section

if section == 'Cumpleaños Feliz':
    st.header("HAPPY BIRTHDAY ISABELLA!")
    st.markdown("I actually don't know what this is, but I thought it would be a nice gesture for your birthday.")
    st.markdown("It breaks my heart not being with you today. I miss you so much, especially on a day that means so much to me. Still, I'm genuinely happy knowing you're surrounded by friends who love and celebrate you. You deserve all the joy in the world.")
    st.markdown("I hope you have an AMAZING day.")
    st.markdown("Love,")
    st.markdown("Catalina")
    st.write("Some upbeat music for you <3")

    spotify_embed_code = """
    <iframe style="border-radius:12px" 
            src="https://open.spotify.com/embed/track/1AGvj6NzcZf4dwHNlX6kSA" 
            width="100%" height="80" frameBorder="0" 
            allowtransparency="true" allow="encrypted-media">
    </iframe>
    """
    st.markdown(spotify_embed_code, unsafe_allow_html=True)

    st.button("Return to Menu", on_click=lambda: st.session_state.update(section='Menu'))

elif section == 'Dear Izzy':
    st.header("Dear Isabella,")
    st.markdown("Yo sé que, para ti, tu cumpleaños no es un día muy importante.")
    st.markdown("Para mi lo es. Estamos celebrando tu vida, tu llegada al mundo y el cambio que has hecho en él. Eres un ángel caído del cielo y te mereces absolutamente todo, pero todo lo bueno que hay en este mundo.")
    st.markdown("Lamentablemente, no te ha tocado una fácil. A pesar de que te mereces las estrellas, no ha sido una vida fácil para ti.")
    st.markdown("Pero yo quiero hacer tu vida un poco más llevadera. Siempre estaré aquí, pase lo que pase.")
    st.markdown("No sé qué haría sin ti. Estoy muy agradecida de que nuestros caminos se hayan cruzado y todavía más agradecida de tener el placer de ser amada por ti.")
    st.markdown("Siempre voy a estar contigo, dispuesta a ayudarte, apoyarte y amarte, aunque nos separen 12.000 km. La distancia nunca va a cambiar todo lo que siento por ti.")
    st.markdown("Te amo.")
    st.markdown("Catalina")

    spotify_embed_code = """
    <iframe style="border-radius:12px" 
            src="https://open.spotify.com/embed/track/1dGr1c8CrMLDpV6mPbImSI" 
            width="100%" height="80" frameBorder="0" 
            allowtransparency="true" allow="encrypted-media">
    </iframe>
    """
    st.markdown(spotify_embed_code, unsafe_allow_html=True)

    st.button("Return to Menu", on_click = lambda: st.session_state.update(section='Menu'))

elif section == 'Some of my favorite photos':
    st.header("Our Photos")
    st.markdown("I've always loved taking photos and videos, capturing little moments and freezing memories in time.")
    st.markdown("Ever since you came into my life, our memories have become my favorite ones to keep.")
    st.markdown("So here are some of my favorite photos of us, moments I hold close to my heart.")
    try:
        image1 = Image.open("Images/image1.jpeg")
        image2 = Image.open("Images/image2.jpeg")
        image3 = Image.open("Images/image3.jpeg")
        image4 = Image.open("Images/image4.jpeg")
        image5 = Image.open("Images/image5.jpeg")
        image6 = Image.open("Images/image6.jpeg")
        image7 = Image.open("Images/image7.jpeg")
        image8 = Image.open("Images/image8.jpeg")
        image9 = Image.open("Images/image9.jpeg")
        image10 = Image.open("Images/image10.jpeg")
        image11 = Image.open("Images/image11.jpeg")
        st.image([image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11])
    except FileNotFoundError:
        st.warning("⚠️ Add photos to the folder.")
    
    st.button("Return to Menu", on_click=lambda: st.session_state.update(section='Menu'))

elif section == 'Countdown':
    st.header("We'll see each other again in just a little while, the countdown has already begun. I carry your smile and our memories with me every day, but soon I won't have to imagine it anymore. The miles will melt away in...")

    target_date = datetime(2025, 8, 18, 10, 0, 0)
    now = datetime.now()
    delta = target_date - now

    if delta.total_seconds() <= 0:
        st.success("After all the waiting, the distance and the longing, the time has come. We're together!")
    else:
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        st.subheader(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

    st.button("Return to Menu", on_click=lambda: st.session_state.update(section='Menu'))

# --- END CONTAINER ---
st.markdown('</div>', unsafe_allow_html=True)
