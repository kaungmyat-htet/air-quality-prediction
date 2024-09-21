import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
def bkk_cm_model():
  st.header("Air Quality Prediction For BKK & CM")
      # Read the CSV file
  data = pd.read_csv('./src/demo/bkk_cm_model.csv')

  # Convert 'datetime' column to pandas datetime format
  data['datetime'] = pd.to_datetime(data['datetime'])

  # Parameters for pagination
  items_per_page = 50
  total_items = len(data)
  total_pages = (total_items // items_per_page) + (total_items % items_per_page > 0)

  # Create pagination control
  page = st.number_input('Datetime range', min_value=1, max_value=total_pages, step=items_per_page)

  # Determine the range of data for the current page
  start_idx = (page - 1) * items_per_page
  end_idx = min(start_idx + items_per_page, total_items)

  # Paginated data for the current page
  paginated_data = data[start_idx:end_idx]

  # Create a toggle button (radio button) to switch between cities
  city_options = data['city'].unique()
  selected_city = st.radio("Select a city to display", city_options)

  # Filter the data based on the selected city
  city_data = paginated_data[paginated_data['city'] == selected_city]

  # Plotting for the selected city's True AQI and Predicted AQI
  fig, ax = plt.subplots(figsize=(10, 3))

  ax.plot(city_data['datetime'], city_data['true_aqi'], marker='o', label=f'True AQI - {selected_city}')
  ax.plot(city_data['datetime'], city_data['predicted_aqi'], marker='x', label=f'Predicted AQI - {selected_city}')

  ax.set_xlabel('Datetime')
  ax.set_ylabel('AQI')
  ax.set_title(f'AQI for Different Cities (Page {page}/{total_pages})')
  start_datetime = paginated_data['datetime'].min()
  end_datetime = paginated_data['datetime'].max()
  ax.set_title(f'AQI from {start_datetime} to {end_datetime}')
  ax.legend()

  # Display the plot
  plt.xticks(rotation=45)
  ax.set_yticks(range(int(data['true_aqi'].min()), int(data['true_aqi'].max()) + 1))
  st.pyplot(fig)

  # Display the paginated data for reference
  # st.write(paginated_data)

def lstm_bkk_data():
  st.header("LSTM Bangkok Data")
      # Read the CSV file
  data = pd.read_csv('./src/demo/lstm_bkk_data.csv')

  # Convert 'datetime' column to pandas datetime format
  data['datetime'] = pd.to_datetime(data['datetime'])

  # Parameters for pagination
  items_per_page = 10
  total_items = len(data)
  total_pages = (total_items // items_per_page) + (total_items % items_per_page > 0)

  # Create pagination control
  page = st.number_input('Datetime range 1', min_value=1, max_value=total_pages, step=items_per_page)

  # Determine the range of data for the current page
  start_idx = (page - 1) * items_per_page
  end_idx = min(start_idx + items_per_page, total_items)

  # Paginated data for the current page
  paginated_data = data[start_idx:end_idx]

  # Plotting for the selected city's True AQI and Predicted AQI
  fig, ax = plt.subplots(figsize=(10, 3))

  ax.plot(paginated_data['datetime'], paginated_data['true_aqi'], marker='o', label=f'True AQI')
  ax.plot(paginated_data['datetime'], paginated_data['predicted_aqi'], marker='x', label=f'Predicted AQI')

  ax.set_xlabel('Datetime')
  ax.set_ylabel('AQI')
  ax.set_title(f'AQI for Bangkok')
  start_datetime = paginated_data['datetime'].min()
  end_datetime = paginated_data['datetime'].max()
  ax.set_title(f'AQI from {start_datetime} to {end_datetime}')
  ax.legend()

  # Display the plot
  plt.xticks(rotation=45)
  ax.set_yticks(range(int(paginated_data['true_aqi'].min()), int(paginated_data['true_aqi'].max()) + 1))
  st.pyplot(fig)

  # Display the paginated data for reference
  # st.write(paginated_data)

def lstm_cm_data():
  st.header("LSTM Bangkok Data")
      # Read the CSV file
  data = pd.read_csv('./src/demo/lstm_cm_data.csv')

  # Convert 'datetime' column to pandas datetime format
  data['datetime'] = pd.to_datetime(data['datetime'])

  # Parameters for pagination
  items_per_page = 10
  total_items = len(data)
  total_pages = (total_items // items_per_page) + (total_items % items_per_page > 0)

  # Create pagination control
  page = st.number_input('Datetime range 1', min_value=1, max_value=total_pages, step=items_per_page)

  # Determine the range of data for the current page
  start_idx = (page - 1) * items_per_page
  end_idx = min(start_idx + items_per_page, total_items)

  # Paginated data for the current page
  paginated_data = data[start_idx:end_idx]

  # Plotting for the selected city's True AQI and Predicted AQI
  fig, ax = plt.subplots(figsize=(10, 3))

  ax.plot(paginated_data['datetime'], paginated_data['true_aqi'], marker='o', label=f'True AQI')
  ax.plot(paginated_data['datetime'], paginated_data['predicted_aqi'], marker='x', label=f'Predicted AQI')

  ax.set_xlabel('Datetime')
  ax.set_ylabel('AQI')
  ax.set_title(f'AQI for Bangkok')
  start_datetime = paginated_data['datetime'].min()
  end_datetime = paginated_data['datetime'].max()
  ax.set_title(f'AQI from {start_datetime} to {end_datetime}')
  ax.legend()

  # Display the plot
  plt.xticks(rotation=45)
  ax.set_yticks(range(int(paginated_data['true_aqi'].min()), int(paginated_data['true_aqi'].max()) + 1))
  st.pyplot(fig)

  # Display the paginated data for reference
  # st.write(paginated_data)

bkk_cm_model()
lstm_bkk_data()
lstm_cm_data()