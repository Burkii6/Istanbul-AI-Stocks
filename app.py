import streamlit as st

# -----------------------------------------------------------------------------
# 1. SAYFA AYARLARI (Browser sekmesinde görünecek kısım)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="İstanbul AI Academy",
    page_icon="🏛️",
    layout="centered"  # Daha derli toplu, kitap gibi bir görünüm için 'centered'
)

# -----------------------------------------------------------------------------
# 2. SESSİZ LÜKS TASARIMI (CSS ile Makyaj)
# -----------------------------------------------------------------------------
# Burası uygulamanın Apple benzeri görünmesini sağlayan stil kodlarıdır.
st.markdown("""
<style>
    /* Ana Arka Plan - Süt Beyazı */
    .stApp {
        background-color: #FAFAFA;
    }
    
    /* Yazı Tipleri - Okunabilir ve Şık */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #1D1D1F; /* Apple Siyahı */
        font-weight: 600;
    }
    
    p {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #333333;
        font-size: 18px;
        line-height: 1.6;
    }

    /* Buton Tasarımı - Minimalist */
    .stButton>button {
        background-color: #000000;
        color: white;
        border-radius: 20px;
        padding: 10px 24px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #333333;
        color: white;
        transform: scale(1.02);
    }
    
    /* Gereksiz Streamlit Menülerini Gizle */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. İÇERİK AKIŞI
# -----------------------------------------------------------------------------

# Başlık Bölümü
st.title("İstanbul AI Academy")
st.caption("FİNANSAL ÖZGÜRLÜK YOLCULUĞU")
st.markdown("---") # İnce bir çizgi

# Giriş Metni
st.markdown("""
Hoş geldiniz. Burası karmaşık borsa terimlerinin olmadığı, finansal okuryazarlığın 
en sade ve rafine hali. 

Amacımız size sadece bilgi vermek değil, paranın mantığını kavramsal olarak hissettirmektir.
Aşağıdaki araç ile küçük birikimlerin zamanla nasıl büyüdüğünü deneyimleyin.
""")

st.write("") # Boşluk
st.write("") # Boşluk

# -----------------------------------------------------------------------------
# 4. İNTERAKTİF BÖLÜM: Bileşik Getiri Simülasyonu
# -----------------------------------------------------------------------------
st.subheader("Bileşik Getirinin Gücü")

# Kullanıcıdan veri alma kutuları (Inputlar)
col1, col2 = st.columns(2)

with col1:
    baslangic_yatirimi = st.number_input("Başlangıç Yatırımı (TL)", value=1000, step=100)
    aylik_ekleme = st.number_input("Aylık Eklenecek Tutar (TL)", value=500, step=50)

with col2:
    yil = st.slider("Kaç Yıl Biriktireceksin?", min_value=1, max_value=30, value=10)
    faiz_orani = st.slider("Yıllık Tahmini Getiri (%)", min_value=1, max_value=100, value=25)

# Hesaplama Motoru (Python'un gücü burada)
toplam_birikim = baslangic_yatirimi
veriler = [baslangic_yatirimi]

for i in range(1, yil + 1):
    # Her yıl ana paraya faiz eklenir + 12 ay boyunca aylık ekleme yapılır
    toplam_birikim = (toplam_birikim + (aylik_ekleme * 12)) * (1 + faiz_orani/100)
    veriler.append(toplam_birikim)

# Sonucu Gösterme
st.write("")
st.metric(label=f"{yil} Yıl Sonunda Ulaşacağın Servet", value=f"{toplam_birikim:,.2f} TL")

# Grafik (Minimalist Çizgi Grafik)
st.line_chart(veriler)

# Motive edici kapanış
if toplam_birikim > 1000000:
    st.success("Tebrikler! Milyoner olma yolunda sağlam bir planınız var.")
else:
    st.info("Küçük damlalar göl olur. Süreyi veya miktarı artırarak sonucu değiştirebilirsin.")
