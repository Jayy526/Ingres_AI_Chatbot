import streamlit as st
import requests
import os
import pandas as pd
import tempfile


st.title("INGRES AI Chatbot 💧")

# Create tabs for different functionalities
tab1, tab2 = st.tabs(["💬 Chat", "📊 Upload Data"])

with tab1:
    question = st.text_input("Ask about groundwater:")
    if st.button("Ask"):
        resp = requests.post("http://127.0.0.1:8000/ask", json={"question": question})
        answer = resp.json()["answer"]
        
        # Check if the answer contains a chart URL
        if answer.endswith('.png') and answer.startswith('/static/'):
            # Display the chart image
            st.image(answer, caption="Generated Chart", use_column_width=True)
            st.write("Chart generated successfully!")
        else:
            # Display regular text response
            st.write(answer)

with tab2:
    st.header("📁 Upload Groundwater Data")
    st.write("Upload Excel (.xlsx) or CSV files containing groundwater measurements")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=['csv', 'xlsx', 'xls'],
        help="Upload Excel or CSV files with groundwater data"
    )
    
    if uploaded_file is not None:
        try:
            # Process the uploaded file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(uploaded_file)
            
            st.success(f"✅ File uploaded successfully: {uploaded_file.name}")
            st.write(f"📊 Data shape: {df.shape[0]} rows, {df.shape[1]} columns")
            
            # Show data preview
            st.subheader("📋 Data Preview")
            st.dataframe(df.head(10))
            
            # Show column information
            st.subheader("📝 Column Information")
            col_info = pd.DataFrame({
                'Column': df.columns,
                'Type': df.dtypes,
                'Non-null Count': df.count(),
                'Null Count': df.isnull().sum()
            })
            st.dataframe(col_info)
            
            # Upload to database
            if st.button("💾 Upload to Database"):
                with st.spinner("Processing and uploading data..."):
                    # Send file to backend for processing
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    response = requests.post("http://127.0.0.1:8000/upload", files=files)
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.success(f"✅ {result['message']}")
                        st.write(f"📊 Processed {result['rows_processed']} rows")
                        if result.get('errors'):
                            st.warning(f"⚠️ {result['errors']} rows had errors")
                    else:
                        st.error(f"❌ Upload failed: {response.text}")
                        
        except Exception as e:
            st.error(f"❌ Error processing file: {str(e)}")
            st.write("Please check your file format and try again.")
    
    # Show sample data format
    st.subheader("📋 Expected Data Format")
    st.write("Your file should contain columns like:")
    sample_data = {
        'well_id': ['W001', 'W002', 'W003'],
        'location_name': ['Downtown', 'North District', 'South District'],
        'latitude': [28.6139, 28.7041, 28.5355],
        'longitude': [77.2090, 77.1025, 77.3910],
        'water_level_meters': [12.3, 15.2, 8.9],
        'measurement_date': ['2023-01-15', '2023-01-15', '2023-01-15'],
        'quality_ph': [7.2, 6.9, 7.5],
        'quality_tds': [450.5, 520.1, 380.2]
    }
    sample_df = pd.DataFrame(sample_data)
    st.dataframe(sample_df)