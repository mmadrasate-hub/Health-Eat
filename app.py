import streamlit as st

# إعدادات الصفحة وجعلها واسعة
st.set_page_config(page_title="أكل صحي - حياة أفضل", page_icon="🥗", layout="wide")

# تصميم CSS لتحسين الألوان والواجهة
st.markdown("""
    <style>
    .main { background-color: #f9fbf9; }
    .stApp { background-image: linear-gradient(to right, #ffffff, #f1f8e9); }
    h1 { color: #1b5e20 !important; font-family: 'Cairo', sans-serif; text-align: center; border-bottom: 2px solid #81c784; padding-bottom: 10px; }
    h3 { color: #2e7d32; }
    .stButton>button { background-color: #4caf50; color: white; border-radius: 12px; height: 3em; transition: 0.3s; }
    .stButton>button:hover { background-color: #388e3c; border: none; transform: scale(1.02); }
    .meal-card { background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #4caf50; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("🥗 تطبيق أكل صحي الذكي")

# القائمة الجانبية بتصميم أنيق
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2927/2927347.png", width=100)
st.sidebar.title("القائمة الرئيسية")
choice = st.sidebar.radio("انتقل إلى:", ["🏠 الرئيسية", "🍽️ الوجبات الصحية", "📍 مطاعم صحية", "🤖 مساعد Gemini"])

if choice == "🏠 الرئيسية":
    col1, col2 = st.columns(2)
    with col1:
        st.write("## غير حياتك اليوم!")
        st.write("نقدم لك أفضل الوصفات الصحية المختارة بعناية لتناسب نظامك الغذائي، سواء كنت تهدف لإنقاص الوزن أو بناء العضلات.")
        st.button("ابدأ الآن")
    with col2:
        st.image("https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=800", caption="الغذاء هو الدواء")

elif choice == "🍽️ الوجبات الصحية":
    st.write("### 🥗 اختر وجبتك الصحية المفضلة")
    tab1, tab2, tab3 = st.tabs(["🍳 الإفطار", "🍲 الغداء", "🥗 العشاء"])
    
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.image("https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400", use_container_width=True)
            st.markdown("<div class='meal-card'><b>1. شوفان بالمكسرات</b><br>غني بالألياف والطاقة الصباحية.</div>", unsafe_allow_html=True)
        with c2:
            st.image("https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=400", use_container_width=True)
            st.markdown("<div class='meal-card'><b>2. توست الأفوكادو والبيض</b><br>دهون صحية وبروتين ممتاز.</div>", unsafe_allow_html=True)

    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            st.image("https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400", use_container_width=True)
            st.markdown("<div class='meal-card'><b>1. سلمون مشوي بالهليون</b><br>أوميغا 3 وسعرات منخفضة.</div>", unsafe_allow_html=True)
        with c2:
            st.image("https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400", use_container_width=True)
            st.markdown("<div class='meal-card'><b>2. صدر دجاج مع كينوا</b><br>وجبة متكاملة لبناء العضلات.</div>", unsafe_allow_html=True)

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400", use_container_width=True)
            st.markdown("<div class='meal-card'><b>1. سلطة يونانية فاخرة</b><br>خفيفة ومنعشة قبل النوم.</div>", unsafe_allow_html=True)
        with c2:
            st.image("https://images.unsplash.com/photo-1543339308-43e59d6b73a6?w=400", use_container_width=True)
            st.markdown("<div class='meal-card'><b>2. شوربة العدس العضوية</b><br>بروتين نباتي دافئ ومشبع.</div>", unsafe_allow_html=True)

elif choice == "📍 مطاعم صحية":
    st.write("### 📍 أفضل المطاعم الصحية القريبة منك")
    restaurants = [
        {"الاسم": "مطعم النضارة", "الموقع": "الرياض", "التقييم": "⭐⭐⭐⭐⭐"},
        {"الاسم": "جرين فود", "الموقع": "جدة", "التقييم": "⭐⭐⭐⭐"},
        {"الاسم": "هيلثي كورنر", "الموقع": "دبي", "التقييم": "⭐⭐⭐⭐⭐"}
    ]
    st.table(restaurants)

elif choice == "🤖 مساعد Gemini":
    st.write("### 🤖 اطلب من الذكاء الاصطناعي تصميم وجبتك")
    user_query = st.text_input("مثال: اقترح لي وجبة غداء بـ 400 سعرة حرارية فقط")
    if st.button("اسأل Gemini"):
        st.warning("تحتاج لربط مفتاح API لتفعيل هذه الميزة.")
