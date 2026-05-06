import streamlit as st
import qrcode
from io import BytesIO

st.title("UPI QR Code Generator")

# User inputs
upi_id = st.text_input("Enter UPI ID", "9611936796@ybl")
bank_name = st.text_input("Enter Name", "State Bank of India")
amount = st.text_input("Enter Amount (optional)")
note = st.text_input("Enter Note (optional)")

# Generate UPI link
upi_link = f"upi://pay?pa={upi_id}&pn={bank_name.replace(' ', '%20')}&cu=INR"

if amount:
    upi_link += f"&am={amount}"
if note:
    upi_link += f"&tn={note.replace(' ', '%20')}"

if st.button("Generate QR Code"):
    # Create QR
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(upi_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Display image
    st.image(img, caption="Your UPI QR Code")

    # Save to buffer for download
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download QR Code",
        data=byte_im,
        file_name="upi_qr.png",
        mime="image/png"
    )
