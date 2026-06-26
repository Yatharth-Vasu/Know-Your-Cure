import streamlit as st

st.title("🌟Know Your Cure")
st.image("https://raw.githubusercontent.com/Yatharth-Vasu/trial-1/main/webapp.png.png" , width = 150)
n1 = st.selectbox(
    "Choose your skin type",
    ["Oily" ,  "Dry" , "Normal" , "Combination" , "Sensitive" , "Delusional Korean Glass SKin😂😂😂"]
)


n2 = st.selectbox("which product do u want" , ["🧼Face wash" , "💧Toner" , "🔬Serum" , "☀️Sunscreen" , "🧴Moisturizer"])
if st.button("Get Your Cure"):

    if( n1 == "Oily" and n2 == "🧼Face wash"  ):
        st.write("""🧼Face Wash :
 
1. The Derma Co 1% Salicylic Acid Gel Face Wash –\n
 https://thedermaco.com/product/1-salicylic-acid-gel-face-wash-the-dermaco-100ml/

2.Minimalist 2% Salicylic Acid + LHA Cleanser –\n
https://beminimalist.co/products/salicylic-lha-2-cleanser

3.Chemist At Play Oil & Acne Control Face Wash –\n
https://innovist.com/products/oil-acne-control-face-wash """)
   
    elif(n1 == 'Oily' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. The Derma Co Pore Minimizing Toner –\n 
https://thedermaco.com/products/2-salicylic-bha-hydrating-toner-150-ml?utm_source=chatgpt.com
                 
2. COSRX AHA/BHA Clarifying Treatment Toner –\n 
https://www.cosrx.com/products/aha-bha-clarifying-treatment-toner
                 
3. Dot & Key Rice Water Hydrating Toner –\n 
https://www.dotandkey.com/products/rice-water-probiotics-hydrating-toner""")
    elif(n1 == 'Oily' and n2 == '🔬Serum'):
        st.write("""🔬Serum :
                 
1. Minimalist Niacinamide 5% Serum –\n 
https://share.google/QfRcS39AXrDWiyk6M
                 
2. The Ordinary Niacinamide 10% + Zinc 1% –\n 
https://share.google/3z694F58JGnIZOyCm
                 
3. The Derma Co Niacinamide Serum –\n 
 https://share.google/bdDY0b0UzeRrPYTat""")
    elif(n1 == 'Oily' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
                 
1. Deconstruct Gel Sunscreen SPF 55 –\n 
https://thedeconstruct.in/products/gel-sunscreen-spf-55?_pos=1&_sid=8646b3465&_ss=r
                 
2. Fixderma Shadow SPF 50+ Gel –\n 
https://www.fixderma.com/products/shadow-spf-50-gel
                 
3. Beauty of Joseon Relief Sun SPF 50+ –\n 
https://beautyofjoseon.com/products/relief-sun-rice-probiotics""")
    elif(n1 == "Oily" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
1. Pond's Super Light Gel –\n 
https://ponds.in/products/super-light-gel-with-hyaluronic-acid-vitamin-e?utm_source=chatgpt.com
                 
2. Minimalist Vitamin B5 10% Moisturizer –\n 
https://beminimalist.co/products/vitamin-b5-10-moisturizer
                 
3. Re'equil Oil Free Moisturiser –\n 
https://www.reequil.com/products/oil-free-mattifying-moisturiser?utm_source=chatgpt.com""")
    elif(n1 == "Dry" and n2 == "🧼Face wash"):
        st.write("""🧼Face Wash :

1. Cetaphil Gentle Skin Cleanser –\n 
https://www.cetaphil.in/products/cleansers/gentle-skin-cleanser/8906005274105.html
                 
2. CeraVe Hydrating Cleanser –\n
https://www.cerave.com/skincare/cleansers/hydrating-facial-cleanser
                 
3. Bioderma Atoderm Gel Moussant –\n
https://www.bioderma.us/all-products/atoderm/shower-gel""")
    elif(n1 == 'Dry' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. Klairs Supple Preparation Facial Toner –\n 
https://www.klairscosmetics.com/product/supple-preparation-facial-toner/
                 
2. Laneige Cream Skin Refiner –\n 
https://www.glamour.com/story/how-to-get-cream-skin?utm_source=chatgpt.com
                 
3. TONYMOLY Wonder Ceramide Mochi Toner –\n 
https://tonymoly.com/products/wonder-ceramide-mochi-toner.do?i_sProductcd=TM20250324000150898""")
    elif(n1 == 'Dry' and n2 == '🔬Serum'):
        st.write("""🔬Serum :
                 
1. L'Oréal Paris Hyaluronic Acid Serum –\n 
 https://www.lorealparis.co.in/revitalift/revitalift-1-5-percent-hyaluronic-acid-serum-30ml
                 
2. Minimalist Hyaluronic Acid 2% Serum –\n 
 https://share.google/doDmSsfL7F3GxLL9N
                 
3. The Ordinary Hyaluronic Acid 2% + B5 –\n 
https://theordinary.com/en-in/hyaluronic-acid-2-b5-serum-original-formulation-100425.html""")
    elif(n1 == 'Dry' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
                 
1. Beauty of Joseon Relief Sun SPF 50+ –\n 
https://beautyofjoseon.com/products/relief-sun-rice-probiotics
                 
2. Isntree Hyaluronic Acid Watery Sun Gel –\n 
https://isntree-global.com/products/isntree-hyaluronic-acid-watery-sun-gel-50ml?utm_source=chatgpt.com
                 
3. Neutrogena Ultra Sheer SPF 50 –\n 
https://www.neutrogena.in/sun/ultra-sheer?utm_source=chatgpt.com""")
    elif(n1 == "Dry" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
                 
1. CeraVe Moisturizing Cream –\n 
https://www.cerave.com/skincare/moisturizers/moisturizing-cream
                 
2. Cetaphil Moisturising Cream –\n 
https://www.cetaphil.in/moisturizers/moisturising-cream/8906005273436.html/?utm_source=chatgpt.com
                 
3. Bioderma Atoderm Crème –\n 
https://www.bioderma-india.in/our-products/atoderm/creme?utm_source=chatgpt.com""")
    elif(n1 == "Normal" and n2 == "🧼Face wash"):
        st.write("""🧼Face Wash :
                 
1. Cetaphil Gentle Skin Cleanser –\n 
https://www.cetaphil.in/products/cleansers/gentle-skin-cleanser/8906005274105.html
                 
2. CeraVe Hydrating Cleanser –\n 
https://www.cerave.com/skincare/cleansers/hydrating-facial-cleanser""")
    elif(n1 == 'Normal' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. Klairs Supple Preparation Unscented Toner –\n 
https://www.klairscosmetics.com/product/supple-preparation-unscented-toner/
                 
2. Dot & Key Rice Water Toner –\n 
https://www.dotandkey.com/products/rice-water-probiotics-hydrating-toner""")
    elif(n1 == 'Normal' and n2 == '🔬Serum'):
        st.write("""🔬Serum : 
                 
1. Minimalist Vitamin C 10% Serum –\n 
https://share.google/nOcxkVWC1qitQubFc
                 
2. L'Oréal Paris Revitalift Hyaluronic Acid Serum –\n 
https://www.lorealparis.co.in/revitalift/revitalift-1-5-percent-hyaluronic-acid-serum-15ml?utm_source=chatgpt.com
                 
3. Plum Vitamin C Serum –\n 
https://plumgoodness.com/products/vitamin-c-face-serum?utm_source=chatgpt.com""")
    elif(n1 == 'Normal' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
                 
1. Minimalist Light Fluid Sunscreen SPF 50 –\n 
https://beminimalist.co/products/light-fluid-spf-50-sunscreen
                 
2. Beauty of Joseon Relief Sun SPF 50+ –\n 
https://beautyofjoseon.com/products/relief-sun-rice-probiotics""")
    elif(n1 == "Normal" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
                 
1. Cetaphil Moisturising Lotion –\n 
https://www.1mg.com/search/all?name=Cetaphil%20Moisturising%20Lotion
                 
2. Neutrogena Hydro Boost Water Gel –\n 
https://www.amazon.in/s?k=Neutrogena+Hydro+Boost+Water+Gel
                 
3. Simple Hydrating Light Moisturiser –\n 
https://www.simpleskincare.in/search?q=hydrating+light+moisturiser""")
    elif(n1 == "Combination" and n2 == "🧼Face wash"):
        st.write("""🧼Face Wash :
                 
1. Simple Refreshing Face Wash –\n 
https://share.google/db7QVLT6yJ4JUYABo
                 
2. Cetaphil Oily Skin Cleanser –\n 
https://share.google/FiG52ygEQ7FeUfHZ6""")
    elif(n1 == 'Combination' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. Dot & Key Rice Water Toner –\n 
https://www.dotandkey.com/products/rice-water-probiotics-hydrating-toner
                 
2. Simple Soothing Facial Toner –\n 
https://www.simpleskincare.in/products/simple-kind-to-skin-soothing-facial-toner-200ml""")
    elif(n1 == 'Combination' and n2 == '🔬Serum'):
        st.write("""🔬Serum : 
                 
1. Minimalist Niacinamide 5% Serum –\n 
https://share.google/QfRcS39AXrDWiyk6M
                 
2. Minimalist Vitamin C 10% Serum –\n 
https://share.google/nOcxkVWC1qitQubFc""")
    elif(n1 == 'Combination' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
1. Minimalist Light Fluid Sunscreen SPF 50 –\n 
https://beminimalist.co/products/light-fluid-spf-50-sunscreen
                 
2. Deconstruct Gel Sunscreen SPF 55 –\n 
https://thedeconstruct.in/products/gel-sunscreen-spf-55?_pos=1&_sid=8646b3465&_ss=r""")
    elif(n1 == "Combination" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
                 
1. Neutrogena Hydro Boost Water Gel –\n 
https://www.amazon.in/s?k=Neutrogena+Hydro+Boost+Water+Gel
                 
2. Simple Hydrating Light Moisturiser –\n 
https://www.simpleskincare.in/search?q=hydrating+light+moisturiser""")
    elif(n1 == "Sensitive" and n2 == "🧼Face wash"):
        st.write("""🧼Face Wash :
                 
1. Cetaphil Gentle Skin Cleanser –\n 
https://www.cetaphil.in/products/cleansers/gentle-skin-cleanser/8906005274105.html
                 
2. CeraVe Hydrating Cleanser –\n 
https://www.cerave.com/skincare/cleansers/hydrating-facial-cleanser
                 
3. Physiogel Daily Moisture Therapy Cleanser –\n 
https://www.nykaa.com/physiogel-dermo-cleanser/p/14373160?utm_source=chatgpt.com""")
    elif(n1 == 'Sensitive' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. Klairs Supple Preparation Unscented Toner –\n 
https://www.klairscosmetics.com/product/supple-preparation-unscented-toner/
                 
2. Pyunkang Yul Essence Toner –\n 
https://pyunkangyul.shop/products/essence-toner?utm_source=chatgpt.com
                 
3. Simple Soothing Facial Toner –\n 
https://www.simpleskincare.in/products/simple-kind-to-skin-soothing-facial-toner-200ml?utm_source=chatgpt.com""")
    elif(n1 == 'Sensitive' and n2 == '🔬Serum'):
        st.write("""🔬Serum :
                 
1. Minimalist Sepicalm 3% Serum –\n 
https://www.1mg.com/otc/minimalist-sepicalm-03-moisturizer-otc716074?utm_source=chatgpt.com
                 
2.The Ordinary Soothing & Barrier Support Serum–\n 
https://theordinary.com/en-in/soothing-barrier-support-serum-100634.html
                 
3. Purito Centella Unscented Serum –\n 
https://purito.com/product/wonder-releaf-centella-serum-unscented/""")
    elif(n1 == 'Sensitive' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
                 
1. La Roche-Posay Anthelios SPF 50+ –\n 
https://www.laroche-posay.com/anthelios
                 
2. Beauty of Joseon Relief Sun SPF 50+ –\n 
https://beautyofjoseon.com/products/relief-sun-rice-probiotics
                 
3. Bioderma Photoderm Max SPF 50+ –\n 
https://www.bioderma-india.in/our-products/photoderm/max-aquafluide-spf-50""")
    elif(n1 == "Sensitive" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
                 
1. Physiogel Daily Moisture Therapy Cream –\n 
https://www.physiogel.com/products/daily-moisture-therapy-cream
                 
2. CeraVe Moisturizing Cream –\n 
https://www.cerave.com/skincare/moisturizers/moisturizing-cream
                 
3. Aveeno Daily Moisturizing Lotion –\n 
https://www.aveeno.com/products/daily-moisturizing-lotion""")
    elif(n1 == "Delusional Korean Glass SKin😂😂😂" and n2 == "🧼Face wash"):
        st.write("""🧼Face Wash :
                 
1. Beauty of Joseon Green Plum Refreshing Cleanser –\n 
https://beautyofjoseon.com/products/green-plum-refreshing-cleanser
                 
2. COSRX Low pH Good Morning Gel Cleanser –\n 
https://www.cosrx.com/products/low-ph-good-morning-gel-cleanser
                 
3. Round Lab 1025 Dokdo Cleanser –\n 
https://roundlab.com/products/1025-dokdo-cleanser""")
    elif(n1 == 'Delusional Korean Glass SKin😂😂😂' and n2 == '💧Toner'):
        st.write("""💧Toner :
                 
1. Anua Heartleaf 77% Soothing Toner –\n 
https://anua.com/products/heartleaf-77-soothing-toner
                 
2. Round Lab 1025 Dokdo Toner –\n 
https://roundlab.com/products/1025-dokdo-toner
                 
3. TIRTIR Milk Skin Toner –\n 
https://tirtir.global/products/milk-skin-toner""")
    elif(n1 == 'Delusional Korean Glass SKin😂😂😂' and n2 == '🔬Serum'):
        st.write("""🔬Serum :
                 
1. Beauty of Joseon Glow Serum (Propolis + Niacinamide) –\n 
https://beautyofjoseon.com/products/glow-serum-propolis-niacinamide
                 
2. Beauty of Joseon Glow Deep Serum (Rice + Alpha-Arbutin) –\n 
https://beautyofjoseon.com/products/glow-deep-serum-rice-alpha-arbutin
                 
3. Anua Niacinamide 10% + TXA 4% Serum –\n 
https://anua.com/products/niacinamide-10-txa-4-dark-spot-correcting-serum""")
    elif(n1 == 'Delusional Korean Glass SKin😂😂😂' and n2 == '☀️Sunscreen'):
        st.write("""☀️Sunscreen :
                 
1. Beauty of Joseon Relief Sun SPF50+ PA++++ –\n 
https://beautyofjoseon.com/products/relief-sun-rice-probiotics
                 
2. Round Lab Birch Juice Moisturizing Sun Cream SPF50+ –\n 
https://roundlab.com/products/birch-moisturizing-uv-sunscreen
                 
3. Isntree Hyaluronic Acid Watery Sun Gel SPF50+ –\n 
https://isntree-global.com/products/isntree-hyaluronic-acid-watery-sun-gel-50ml""")
    elif(n1 == "Delusional Korean Glass SKin😂😂😂" and n2 == '🧴Moisturizer'):
        st.write("""🧴Moisturizer :
                 
1. Beauty of Joseon Dynasty Cream –\n 
https://beautyofjoseon.com/products/dynasty-cream
                 
2.COSRX Advanced Snail 92 All In One Cream –\n 
https://www.cosrx.com/products/advanced-snail-92-all-in-one-cream
                 
3.Round Lab Birch Juice Moisturizing Cream –\n 
https://roundlab.com/products/birch-juice-moisturizing-cream?utm_source=chatgpt.com""")
        
        
        
     

    

