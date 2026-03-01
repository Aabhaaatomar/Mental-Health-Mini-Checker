import streamlit as st # type: ignore
st.title("Mental Health Mini Checker")
st.write("This is a simple mental health mini checker that will help you to check your mental health status based on your answers to the questions below. Please answer the questions honestly and accurately to get the best results.")
st.write("Please rate the following topics on a scale of 1 to 5, where 1 is the lowest and 5 is the highest.")

questions = [
    "Energy levels",
    "Sleep quality",
    "Stress levels",
    "Mood",
    "Physical health",
    "Work-life balance",
    "Self-esteem",
    "Overall satisfaction with life",
    "Diet and nutrition",
]
scores = []
for question in questions:
    score = st.slider(question, 1.0, 5.0, 3.0)
    scores.append(score)

if st.button("Check Mental Health Status"):
    avg_score = sum(scores) / len(scores)
    st.write(f"Your average score is: {avg_score:.2f}")
    
    if avg_score >= 4:
        st.write("Your mental health status is: Healthy")
        st.write("You seem healthy, continue taking good care of yourself and maintain a balanced lifestyle.")
        
    elif avg_score >= 3:
        st.write("Your mental health status is: Moderately Healthy")
        st.write("You look healthy but you can still improve your mental health by taking care of yourself and maintaining a balanced lifestyle.")
        
    elif avg_score >= 2:
        st.write("Your mental health status is: Need to Improve")
        st.write("You overthink and need to calm your mind and take care of yourself.")
        
    else:
        st.write("Your mental health status is: Stressed")
        st.write("You are struggling to stay happy and really need to take good care of yourself and seek support if needed.")
        
    st.success(f"Your score is: {avg_score:.2f}")    
    st.success("Mental health check completed!")
    
    