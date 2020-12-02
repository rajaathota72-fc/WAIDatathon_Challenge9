import streamlit as st
def sound_func():
    import sounddevice as sd
    import soundfile as sf
    filename = 'audio_files/wa1.wav'
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    sd.wait(3000)
def name(Name):
    return "Hey "+Name+"! Fill other details to get Recommendation report"
import re
skill_list = ["html","css","php","bootstrap","js"]
def presence(expertise):
    skills_youhave = []
    skill_str = str(expertise)
    for i in skill_list:
        x = re.search(i,skill_str )
        if x:
            skills_youhave.append(i)
    set1 = set(skill_list) - set(skills_youhave)
    List = list(set1)
    return List
print(presence(expertise="html,css,js"))
def main():
    #sound_func()
    st.sidebar.audio("audio_files/wa1.wav")
    st.sidebar.title("Let me know you")
    template = """
       <div style = "background-color : black; padding : 10px;">
       <h1 style = "color:white;text-align:center;"> Intelligent Recommender System </h1>
       </div>
       """
    st.markdown(template, unsafe_allow_html=True)
    st.image("eva.jpeg",width=700)
    Name = st.sidebar.text_input("Your Name")
    if len(Name)>2:
        st.success(name(Name))
    radio_1 = st.sidebar.radio("Freelance Experience", ["Beginner", "Already in Field"])
    if radio_1 == "Already in Field":
        slider_1 = st.sidebar.slider("Years of Experience", 0, 10, 1)
    dropdown_1 = st.sidebar.selectbox("Field of Interest", ("Select one","Web Development", "Graphic Design", "Video Design"))
    if dropdown_1 == "Web Development":
        st.write("1. Here is the Analysis of earnings by Freelancers in your field")
        st.write("Minimum earning is $5/hour")
        st.write("Maximum earning is $30/hour")
        st.write("27% of Freelancers earn $10/hour")
        st.image("Freelancers v:s amounts graph.png")
        st.write("2. Skills of Freelancers as Web developers")
        st.image("wordcloud.png",width=700)
        st.sidebar.text("Write about your skills")
        skills = st.sidebar.text_input("Type here")
        if st.sidebar.button("Submit to get Recommendation"):
            result = presence(skills)
            st.text("Recommendation for your Skill enhancement")
            st.success(result)
            st.balloons()
            st.button("Go to Courses")
if __name__ == "__main__":
    main()