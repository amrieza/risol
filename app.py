import streamlit as st

st.title("RISOL MAYO")

# Bagian Home
st.header("Home")
st.write("Nikmati kelezatan Risol Mayo kami yang lezat dan renyah. Segera pesan sekarang!")
st.button("GET IT NOW")

# Bagian About
st.header("About Product")
st.image("images/risol.jpg", caption="Risol Mayo", use_column_width=True)
st.write("Risol mayonnaise adalah jajanan tradisional berbentuk gulungan yang memiliki berbagai isian, dari ragout, telur, hingga smoked beef.")
st.write("Biasanya, risol disajikan dengan cara digoreng dan dimakan bersama saus sambal. Perpaduan rasa renyah dan creamy pada risol ini menciptakan rasa yang gurih.")

# Bagian Footer
st.header("Contact & Follow Us")
st.image("images/logo.png", caption="Risol Mayo Logo", use_column_width=True)
st.write("Follow us on Instagram: [RisolMayoOfficial](https://www.instagram.com/RisolMayoOfficial/)")
st.write("For inquiries, contact us at: info@risolmayo.com")

# Copyright
st.footer("Copyright © 2022 Amrieza Herdiyanto")
