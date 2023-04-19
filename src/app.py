import streamlit as st
import kmeans_model as kmeans

def main():
    st.title("YourCollege - Advanced College Recommender System")
    st.write("This application uses a weighted K-means clustering model to help you find colleges similar to your dream college.")

    labels = ["Type of College (Public or Private)",
                "Total Undergraduate Enrollment",
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
    
    if 'start_model' not in st.session_state:
        st.session_state.start_model = False
    
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
        # st.write("yes")
        st.session_state.disabled = False
        
        if 'sliders' not in st.session_state:
            st.session_state.sliders = False
                  
        if 'cont' not in st.session_state:
            st.session_state.cont_button = False
        else:
            if st.session_state.cont_button:
                st.session_state.sliders = True
        
        st.session_state.weights = [st.slider(label=labels[i], min_value=1, max_value=10, value=5, step=1,
                                   disabled=st.session_state.sliders) for i in range(10)]
        
        st.write("Click to confirm your preferences and proceed")
            
        st.session_state.cont_button = st.button('Continue', disabled=st.session_state.sliders, key = 'cont')
        
        if st.session_state.cont_button:
            st.session_state.start_model = True
            st.experimental_rerun()
        
        print("sliders: " + str(st.session_state.sliders))
        print(st.session_state.weights)
    elif st.session_state.no_button:
        # st.write("no")
        st.session_state.disabled = False
        st.session_state.start_model = True
        st.session_state.weights = [1 for i in range(10)]
    
    print("start model: " + str(st.session_state.start_model))
    
    if 'colleges' not in st.session_state:
        st.session_state.colleges = None
    
    if 'output' not in st.session_state:
        st.session_state.output = None
    
    if 'get_output' not in st.session_state:
        st.session_state.get_output = False
        
    if 'dream' not in st.session_state:
        st.session_state.dream = ''

    
    if st.session_state.start_model:
        st.session_state.colleges = kmeans.train(st.session_state.weights)
        st.session_state.start_model = False
        st.session_state.get_output = True
        
    if st.session_state.get_output:
        st.session_state.dream = st.selectbox("Choose your dream college:", options=st.session_state.colleges)
        
        st.session_state.output = kmeans.find_colleges(st.session_state.colleges, st.session_state.dream)
        st.session_state.output['College Type'] = ['Private' if s == 1 else 'Public' for s in st.session_state.output['Private']]
        st.session_state.output['Full-time Undergraduates'] = st.session_state.output['F.Undergrad']
        st.session_state.output['Average SAT'] = st.session_state.output['SAT%'] * 1600
        st.session_state.output['Acceptance Rate'] = round(st.session_state.output['acceptance_rate'] * 100, 2)
        st.session_state.output['Graduation Rate'] = round(st.session_state.output['grad_rate'] * 100, 2)
        
        
        st.experimental_data_editor(st.session_state.output[['NAME', 'College Type', 'Full-time Undergraduates', 'Average SAT', 'Acceptance Rate', 'Graduation Rate']], disabled=True)
   
if __name__ == '__main__':
    main()