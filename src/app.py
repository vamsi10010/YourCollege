import streamlit as st
import kmeans_model

def main():
    st.title("YourCollege - Advanced College Recommender System")
    st.write("This application uses a weighted K-means clustering model to help you find colleges similar to your dream college.")

    st.subheader("Features used by model:")
    for s in ["Total Undergraduate Enrollment",
                "College Expenditure per Student",
                "Percent of Student body in STEM",
                "Female Census in the College",
                "Acceptance Rate",
                "Percentage of incoming students in Top 10% of HS",
                "Graduation Rate",
                "Diversity Index",
                "Average SAT Score"]:
        st.markdown("- " + s)
        
    st.write("Do you wish to evaluate these features upon your preference?")
    
    col1, col2 = st.columns([0.1,1])
    
    st.session_state.disabled = False
    
    if 'yes' in st.session_state or 'no' in st.session_state:
        st.session_state.disabled = True
    
    with col1:
        yes = st.button('Yes', disabled=st.session_state.disabled, key='yes')
    with col2:
        no = st.button('No', disabled=st.session_state.disabled, key='no')  
        
    weights = []    
    
    if yes:
        st.write("yes")
        st.session_state.disabled = False
        cont = st.container()
        weights = preferences(cont)
    elif no:
        st.write("no")
        st.session_state.disabled = False
        weights = [1 for i in range(9)]

    weights

def preferences(cont):
    st.session_state.sliders = False
    weights = []
    labels = ["Total Undergraduate Enrollment",
                "College Expenditure per Student",
                "Percent of Student body in STEM",
                "Female Census in the College",
                "Acceptance Rate",
                "Percentage of incoming students in Top 10% of HS",
                "Graduation Rate",
                "Diversity Index",
                "Average SAT Score"]
    for i in range(9):
        weights.append(cont.slider(label=labels[i], min_value=1, max_value=10, value=5, step=1,
                                   disabled=st.session_state.sliders))
    
    cont.write("Click to confirm your preferences and proceed")
    proceed = cont.button('Continue', disabled=st.session_state.sliders)
    while not proceed:
        pass
    
    st.session_state.sliders = True
    return weights
        
    
        
    
    
if __name__ == '__main__':
    main()