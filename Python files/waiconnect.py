import streamlit as st
st.sidebar.title("Let me know you")
template = """
    <div style = "background-color : black; padding : 10px;">
    <h1 style = "color:white;text-align:center;">WAI Connect</h1>
    </div>
    """
st.markdown(template, unsafe_allow_html=True)
st.image("waiconnect.jpeg",width=698)
import cosinesimilarity as cs
def name(Name):
    return "Hey "+Name+"! Fill other details to get Connected!"

lookingfor = ["html css bootstrap","css design php","bootstrap laravel css","html php bootstrap","drupel html js","js css php","html bottstrap css",
"applicationdesign css html","php html css","html css js"]
skills_ihave =["drupel html js","js css php","html bottstrap css",
"applicationdesign css html","php html css","html css js","html css bootstrap","css design php","bootstrap laravel css","html php bootstrap" ]
freelancers = ["Anna", "Laura", "Nazia", "Fathima", "Iffat", "Siham", "Samira", "Ayesha", "Nafiza", "Kizal"]
clients = ["Kickstart","Cupist","Alexandria","Amenim","Starling","Creatisch","Fizza Kraft","Women AI","Samara","Brillianto"]
def client_recommender(text1):
    import cosinesimilarity as cs
    cs_index = []
    for i in range(len(lookingfor)):
        x = cs.cosinesimilarity(text1,i)
        cs_index.append(x)
    indexes = []
    for j in cs_index:
        if j > 0.5:
            m = cs_index.index(j)
            indexes.append(m)
    client_recommendation = []
    for k in indexes:
        n = clients[k]
        client_recommendation.append(n)
    return client_recommendation
Name = st.sidebar.text_input("Your Name")
if len(Name)>2:
        st.success(name(Name))
radio_2 = st.sidebar.radio("I am a ", ["Freelancer", "Entrepreneur"])
if radio_2 == "Freelancer":
    slider_2 = st.sidebar.slider("Years of Experience", 0, 10, 1)
    hourly_price = st.sidebar.text_input("Enter your hourly rate in $")
    st.sidebar.text("Write about your skills")
    skillset = st.sidebar.text_input("skills separated by space")
    if st.sidebar.button("Find my clients"):
        st.write("Here are your recommended Clients , click to know more")
        st.success("1.WAI"+"      2.Brillianto"+"       3.FizzaKraft")
if radio_2 == "Entrepreneur":
    st.sidebar.text_input("Enter your company")
    lookingfor = st.sidebar.text_input("What skills you are looking for")
    pricing_per_hour = st.sidebar.text_input("Enter your pricing per hour")
    if st.sidebar.button("Find Freelancers"):
        st.write("Here are your recommended freelancers , click to know more")
        st.success("1.Anna"+"      2.Iffat"+"       3.Siham")