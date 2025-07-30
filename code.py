import streamlit as st
from datetime import datetime
from PIL import Image
import time

st.set_page_config(page_title = "HAPPY BIRTHDAY POOKIE", layout="centered")

st.markdown("""
    <style>
    /* Hide Streamlit default header and footer */
    #MainMenu, header, footer {
        visibility: hidden;
    }

    /* Optional: hide top blank space */
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
    .nav-button {
        width: 100%;
        margin-bottom: 10px;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE FOR PAGE NAVIGATION ---

if 'section' not in st.session_state:
    st.session_state.section = 'Home'

# --- MAIN MOBILE CONTAINER ---

st.markdown('<div class="container">', unsafe_allow_html=True)

# --- VERTICAL NAVIGATION BUTTONS ---
st.title("HAPPY BIRTHDAY POOKIE")

if st.button("Home", key="home", help = "Home"):
    st.session_state.section = 'Home'
if st.button("Love Confession", key="love", help = "This is my love confession"):
    st.session_state.section = 'Love Confession'
if st.button("Some of my favorite photos", key="photos", help = "Photos"):
    st.session_state.section = 'Some of my favorite photos'
if st.button("Countdown", key="countdown", help = "Countdown"):
    st.session_state.section = 'Countdown'

st.divider()

# --- SECTION CONTENT ---
section = st.session_state.section

if section == 'Home':
    st.header("HAPPY BIRTHDAY ISABELLA!")
    st.markdown("I actually don't know what this is, but I thought it would be a nice gesture for your birthday.")
    st.markdown("Not being there with you makes me deeply sad, but I'm really happy that you're getting to spend your birthday with Naya and Malou.")
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

elif section == 'Love Confession':
    st.header("Dear Isabella,")
    st.markdown("You know I'm kind of a hopeless romantic, so this is a short message for you.")
    st.markdown("Yo sé que, para ti, tu cumpleaños no es un día muy importante, pero para mi lo es. Estamos celebrando tu vida, y estoy segura de que eso es necesario, porque eres maravillosa, Isa. Personalmente, siento que eres un ángel caído del cielo")
    st.markdown("No sé qué haría sin ti, y estoy muy agradecida de que nuestros caminos se hayan cruzado.")
    st.markdown("Te mereces absolutamente todo lo bueno del mundo.")
    st.markdown("Te amo,")
    st.markdown("Catalina")

    spotify_embed_code = """
    <iframe style="border-radius:12px" 
            src="https://open.spotify.com/embed/track/1dGr1c8CrMLDpV6mPbImSI" 
            width="100%" height="80" frameBorder="0" 
            allowtransparency="true" allow="encrypted-media">
    </iframe>
    """
    st.markdown(spotify_embed_code, unsafe_allow_html=True)

elif section == 'Some of my favorite photos':
    st.header("Our Photos")
    st.markdown("I love photos and videos. I love documenting my life and the people I share it with.")
    st.markdown("And I love you, so I love our photos.")
    st.markdown("A continuación, algunas de mis fotos favoritas de las dos.")
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

elif section == 'Countdown':
    st.header("We will see each other again in...")
    target_date = datetime(2025, 8, 18, 10, 0, 0)
    now = datetime.now()
    delta = target_date - now

    if delta.total_seconds() <= 0:
        st.success("The time has arrived... we're together!")
    else:
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        st.subheader(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# --- END CONTAINER ---
st.markdown('</div>', unsafe_allow_html=True)
