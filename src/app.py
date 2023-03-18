import streamlit as st
import kmeans_model

def main():
    st.title("YourCollege - Advanced College Recommender System")
    st.write("This application uses a weighted K-means clustering model to help you find colleges similar to your dream college.")

    labels = ["Total Undergraduate Enrollment",
                "College Expenditure per Student",
                "Percent of Student body in STEM",
                "Female Census in the College",
                "Acceptance Rate",
                "Percentage of incoming students in Top 10% of HS",
                "Graduation Rate",
                "Diversity Index",
                "Average SAT Score"]
    st.subheader("Features used by model:")
    for s in labels:
        st.markdown("- " + s)
        
    st.write("Do you wish to evaluate these features upon your preference?")
    
    col1, col2 = st.columns([0.1,1])
    
    st.session_state.disabled = False
    
    if 'yes' in st.session_state or 'no' in st.session_state:
        print("a button is in session state")
        st.session_state.disabled = True
    else:
        st.session_state.yes_button = False
        st.session_state.no_button = False
    
    with col1:
        yes = st.button('Yes', disabled=st.session_state.disabled, key='yes')
    with col2:
        no = st.button('No', disabled=st.session_state.disabled, key='no')  
    
    if not (st.session_state.yes_button or st.session_state.no_button):
        st.session_state.yes_button = yes
        st.session_state.no_button = no
        
    st.session_state.weights = []
    
    print(st.session_state.yes_button)
    print(st.session_state.no_button)
    
    if st.session_state.yes_button:
        st.write("yes")
        st.session_state.disabled = False
        st.session_state.sliders = False
        st.session_state.weights = [st.slider(label=labels[i], min_value=1, max_value=10, value=5, step=1,
                                   disabled=st.session_state.sliders) for i in range(9)]
        print(st.session_state.weights)
        st.write("Click to confirm your preferences and proceed")
        proceed = st.button('Continue', disabled=st.session_state.sliders)
        while not proceed:
            pass
        
        st.session_state.sliders = True
    elif st.session_state.no_button:
        st.write("no")
        st.session_state.disabled = False
        st.session_state.weights = [1 for i in range(9)]

    st.session_state.weights

   
if __name__ == '__main__':
    main()