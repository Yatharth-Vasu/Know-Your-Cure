
import streamlit as st

st.title("Know Your Cure")
n1 = st.text_input("Enter Your Skin Type")
if st.button("Identify Cure"):

    if( n1.lower() in ["oily"]  ):
        print("""Oily & Acne-Prone Skin:
 *Face Wash* -
1. The Derma Co 1% Salicylic Acid Gel Face Wash
2. Minimalist 2% Salicylic Acid Cleanser
3. Chemist At Play Oil & Acne Control Face Wash
 *Toner* -
1. The Derma Co Pore Minimizing Toner
2. COSRX AHA/BHA Clarifying Treatment Toner
3. Dot & Key Rice Water Toner
 *Serum* -
1. Minimalist Niacinamide 5% Serum
2. The Ordinary Niacinamide 10% + Zinc 1%
3. The Derma Co Niacinamide Serum
 *Moisturizer* -
1. Pond's Super Light Gel
2. Minimalist Vitamin B5 10% Moisturizer
3. Re'equil Oil Free Moisturiser
 *Sunscreen* -
1. Deconstruct Gel Sunscreen SPF 55
2. Fixderma Shadow SPF 50+ Gel
3. Beauty of Joseon Relief Sun SPF 50+""")
    elif(n1.lower() in ["dry"]):
        print("""_Dry skin :
              _ 
 *Face Wash* -
1. Cetaphil Gentle Skin Cleanser
2. CeraVe Hydrating Cleanser
3. Bioderma Atoderm Gel Moussant
 *Toner* -
1. Klairs Supple Preparation Toner
2. Laneige Cream Skin Refiner
3. TONYMOLY Wonder Ceramide Mocchi Toner
 *Serum* -
1. L'Oréal Paris Hyaluronic Acid Serum
2. Minimalist Hyaluronic Acid 2% Serum
3. The Ordinary Hyaluronic Acid 2% + B5
 *Moisturizer* -
1. CeraVe Moisturizing Cream
2. Cetaphil Moisturising Cream
3. Bioderma Atoderm Crème
 *Sunscreen* -
1. Beauty of Joseon Relief Sun SPF 50+
2. Isntree Hyaluronic Acid Watery Sun Gel
3. Neutrogena Ultra Sheer SPF 50""")
    elif(n1.lower() in ["normal"]):
        print("""""")
    elif(n1.lower() in ["combination"]):
        print("""Combination Skin
              
Face Wash: Simple Refreshing Face Wash, Cetaphil Oily Skin Cleanser
Toner: Dot & Key Rice Water Toner, Simple Soothing Facial Toner
Serum: Minimalist Niacinamide 5% Serum, Minimalist Vitamin C 10% Serum
Moisturizer: Neutrogena Hydro Boost Water Gel, Simple Hydrating Light Moisturiser
Sunscreen: Minimalist Light Fluid Sunscreen SPF 50, Deconstruct Gel Sunscreen SPF 55""")

    elif(n1.lower() in ["sensitive"]):
        print("""Sensitive Skin
              
Face Wash
Cetaphil Gentle Skin Cleanser
CeraVe Hydrating Cleanser
Physiogel Daily Moisture Therapy Cleanser
Toner
Klairs Supple Preparation Unscented Toner
Pyunkang Yul Essence Toner
Simple Soothing Facial Toner
Serum
Minimalist Sepicalm 3% Serum
The Ordinary Soothing & Barrier Support Serum
Purito Centella Unscented Serum
Moisturizer
Physiogel Daily Moisture Therapy Cream
CeraVe Moisturizing Cream
Aveeno Daily Moisturizing Lotion
Sunscreen
La Roche-Posay Anthelios SPF 50+
Beauty of Joseon Relief Sun SPF 50+
Bioderma Photoderm Max SPF 50+""")
    else:
        print("""alien skin u have""")
