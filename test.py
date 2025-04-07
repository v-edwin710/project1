import pypyodbc as odbc
import requests
import time

# API Hosting Configuration
API_HOSTS = {
    "tblSO3": "http://10.2.4.40:5000/api/data",
}

# Database Connection Settings
DRIVER_NAME = 'SQL Server'
SERVER_NAME = '122.248.215.5,2918'
DATABASE_NAME = 'lvpacmes1'
USERNAME = 'your_username'
PASSWORD = 'your_password'
USERNAME = 'vitx_Lucas'  # If using SQL Auth
PASSWORD = '$ViTrox$Lucas'

# Connection String
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    UID={USERNAME};
    PWD={PASSWORD};
"""

# Function to fetch data from API
def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            print(f"❌ Failed to fetch data from {api_url}. Status Code:", response.status_code)
            return []
    except Exception as e:
        print(f"❌ Error fetching data from {api_url}: {str(e)}")
        return []

# Function to create a new table dynamically based on API attributes
def create_table(cursor, table_name, sample_data):
    if not sample_data:
        print(f"⚠️ No sample data available to create table {table_name}.")
        return

    # Extract column names, ensuring 'id' is the primary key
    columns = [f"[{key}] NVARCHAR(MAX)" for key in sample_data.keys() if key.lower() != "id"]  # Exclude 'id' first
    columns_sql = ", ".join(columns)

    # Define primary key for 'id' if it exists
    id_column = "[id] INT PRIMARY KEY," if "id" in sample_data else ""

    create_table_query = f"""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{table_name}' AND xtype='U')
    CREATE TABLE {table_name} (
        {id_column}
        {columns_sql}
    );
    """
    cursor.execute(create_table_query)

# Function to insert/update data into SQL Server dynamically
def insert_data():
    try:
        # Establish database connection
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        print("\n🔄 Checking API for new data...")

        for table_name, api_url in API_HOSTS.items():
            # Fetch data from API
            data_list = fetch_api_data(api_url)

            if data_list:
                # Create table dynamically based on API data structure
                create_table(cursor, table_name, data_list[0])

                for row in data_list:
                    # Extract column names and values dynamically
                    columns = [col for col in row.keys()]
                    values = tuple(row.values())

                    # Check if the record already exists
                    primary_key_column = "id" if "id" in row else columns[0]  # Use 'id' if exists, otherwise first column
                    cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {primary_key_column} = ?", (row[primary_key_column],))
                    exists = cursor.fetchone()[0]

                    if exists:
                        # Update existing record dynamically
                        update_columns = ", ".join([f"[{col}] = ?" for col in columns])
                        update_query = f"UPDATE {table_name} SET {update_columns} WHERE {primary_key_column} = ?;"
                        cursor.execute(update_query, values + (row[primary_key_column],))
                    else:
                        # Insert new record dynamically
                        insert_query = f"INSERT INTO {table_name} ([{'], ['.join(columns)}]) VALUES ({', '.join(['?'] * len(values))});"
                        cursor.execute(insert_query, values)

                conn.commit()
                print(f"✅ Processed {len(data_list)} records for table {table_name}.")
            else:
                print(f"⚠️ No new data for table {table_name}.")

        cursor.close()
        conn.close()
    except odbc.DatabaseError as e:
        print("❌ Database connection failed:", str(e))

# Continuous data retrieval every second
while True:
    insert_data()
    time.sleep(1)  # Wait 1 second before the next API call
