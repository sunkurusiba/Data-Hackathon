import pandas as pd
import re
list =["api_data_aadhar_biometric_0_500000.csv",
       "api_data_aadhar_biometric_500000_1000000.csv",
       "api_data_aadhar_biometric_1000000_1500000.csv",
       "api_data_aadhar_biometric_1500000_1861108.csv"]
df= pd.concat([pd.read_csv(x) for x in list],ignore_index=True )
#print(df)
#print(df.shape)
#print(df['state'].unique())
print(df['state'].nunique())
#print(dicti)
# 2. Define a function to clean state names
def clean_state_name(state):
       # Handle missing values
       if not isinstance(state, str):
              return "Unknown"

       # Step A: Standardize Casing & Whitespace
       # .strip() removes spaces at start/end
       # .title() converts "andhra pradesh" -> "Andhra Pradesh"
       state = state.strip().title()

       # Step B: Fix specific typos and legacy names using a Dictionary
       # This maps 'Incorrect Name' : 'Correct Name'

       dicti = {  # Odisha
              "Orissa": "Odisha",
              "ODISHA": "Odisha",
              "odisha": "Odisha",
              # Jammu and Kashmir
              "Jammu & Kashmir": "Jammu and Kashmir",
              "Jammu And Kashmir": "Jammu and Kashmir",
              "Chhatisgarh": "Chhattisgarh",
              "Uttaranchal": "Uttarakhand",
              "Pondicherry": "Puducherry",
              "Andaman & Nicobar Islands": "Andaman and Nicobar Islands",
              "Andaman And Nicobar Islands": "Andaman and Nicobar Islands",
              "Tamil Nadu": "Tamilnadu",
              "andhra pradesh ": "Andhra pradesh",
              # West Bengal
              "West Bangal": "West Bengal",
              "west Bengal": "West Bengal",
              "West bengal": "West Bengal",
              "WESTBENGAL": "West Bengal",
              "WEST BENGAL": "West Bengal",
              "Westbengal": "West Bengal",
              "West  Bengal": "West Bengal",
              # Dadra and Nagar Haveli and Daman and Diu
              "Dadra and Nagar Haveli": "Dadra and Nagar Haveli and Daman and Diu",
              "Dadra & Nagar Haveli": "Dadra and Nagar Haveli and Daman and Diu",
              "Daman & Diu": "Dadra and Nagar Haveli and Daman and Diu",
              "Daman and Diu": "Dadra and Nagar Haveli and Daman and Diu",
              "Daman And Diu": "Dadra and Nagar Haveli and Daman and Diu",
              "Dadra And Nagar Haveli And Daman And Diu":"Dadra and Nagar Haveli and Daman and Diu",
              "Dadra And Nagar Haveli":"Dadra and Nagar Haveli and Daman and Diu",
       }

       # Return the corrected name if it exists in our dictionary, else return the standardized name
       return dicti.get(state, state)


# 3. Apply the function to the 'state' column
df['state'] = df['state'].apply(clean_state_name)

# 4. Verify the results
print("Unique States after cleaning:")
#print(df['state'].unique())
print(df['state'].nunique())

#State wise correction
df_Odisha=df[df['state']=="Odisha"]
print(df_Odisha['district'].unique())

def clean_districtOD_name(district):
       if not isinstance(district, str):
              return "Unknown"

       district = district.strip().title()
       dicti1={ "JAJPUR":"Jajpur",
                "Jajapur":"Jajpur",
                "jajpur":"Jajpur",
                "Sonapur":"Subarnapur",
                "Anugul":"Angul",
                "ANUGUL":"Angul",
                "Anugal":"Angul",
                "ANGUL":"Angul",
                "Anugul *":"Angul",
                "Khorda":"Khordha",
                "Baudh":"Boudha",
                "NAYAGARH":"Nayagarh",
                "NUAPADA":"Nuapada",
                "BALANGIR":"Balangir",
                ""}


