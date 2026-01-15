import pandas as pd
import numpy as np
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
df_Odisha=df[df['state']=="Odisha"].copy()
print(df_Odisha['district'].nunique())

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
                "Anugul  *":"Angul",
                "Khorda":"Khordha",
                "Khordha  *":"Khordha",
                "Baudh":"Boudh",
                "NAYAGARH":"Nayagarh",
                "NUAPADA":"Nuapada",
                "BALANGIR":"Balangir",
                "Baleshwar":"Balasore",
                "Baleswar":"Balasore",
                "Sundargarh":"Sundergarh",
                "Jagatsinghapur":"Jagatsinghpur",

                }
       return dicti1.get(district,district)

df_Odisha['district']=df_Odisha['district'].apply(clean_districtOD_name)
print("Unique Districts in Odisha after cleaning:")
print(df_Odisha['district'].nunique())


#Andhra Pradesh district correction
df_AP=df[df['state']=="Andhra Pradesh"].copy()
print(df_AP['district'].nunique())

# Replace Warangal from andhra pradesh to Telangana
#print(df[df['district']=="Warangal"].shape)
df.loc[(df['district']=="Warangal") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Warangal"]['state'].unique())

#Replace Adilabad from andhra pradesh to Telangana
print(df[df['district']=="Adilabad"]['state'].unique())
df.loc[(df['district']=="Adilabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Adilabad"]['state'].unique())

#Replace Hyderabad from andhra pradesh to Telangana
print(df[df['district']=="Hyderabad"]['state'].unique())
df.loc[(df['district']=="Hyderabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Hyderabad"]['state'].unique())


#Replace Nizamabad from andhra pradesh to Telangana
print(df[df['district']=="Nizamabad"]['state'].unique())              
df.loc[(df['district']=="Nizamabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Nizamabad"]['state'].unique())

#Replace khammam from andhra pradesh to Telangana
print(df[df['district']=="Khammam"]['state'].unique())         
df.loc[(df['district']=="Khammam") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Khammam"]['state'].unique())

#Replace Karimnagar from andhra pradesh to Telangana
print(df[df['district']=="Karimnagar"]['state'].unique())
df.loc[(df['district']=="Karimnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Karimnagar"]['state'].unique())

#Replace Rangareddy from andhra pradesh to Telangana
print(df[df['district']=="Rangareddi"]['state'].unique())
df.loc[(df['district']=="Rangareddi") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Rangareddi"]['state'].unique())
print(df[df['district']=="Rangareddy"]['state'].unique())
df.loc[(df['district']=="Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Rangareddy"]['state'].unique())

#Replace Medak from andhra pradesh to Telangana
print(df[df['district']=="Medak"]['state'].unique())
df.loc[(df['district']=="Medak") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Medak"]['state'].unique())

#Replace Mahbubnagar from andhra pradesh to Telangana
print(df[df['district']=="Mahbubnagar"]['state'].unique())
df.loc[(df['district']=="Mahbubnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Mahbubnagar"]['state'].unique())





df_AP=df[df['state']=="Andhra Pradesh"].copy()
print(df_AP['district'].unique())

def clean_districtAP_name(district):
       if not isinstance(district, str):
              return "Unknown"

       district = district.strip().title()
       dicti2={ "Kurnool  *":"Kurnool",
                "Cuddapah":"Kadapa",
                "Cuddapah  *":"Kadapa",
                "Chittoor  *":"Chittoor",
                "Sri Potti Sriramulu Nellore":"Nellore",
                "Sri Potti Sriramulu Nellore  *":"Nellore",
                "Srikakulam  *":"Srikakulam",
                "Vishakhapatnam":"Visakhapatnam",
                "Vishakhapatnam  *":"Visakhapatnam",
                "Vizianagaram  *":"Vizianagaram",
                "Ananthapur":"Anantapur",
                "Sri Sathya Sai":"Sri Satya Sai",
                "chittoor":"Chittoor",
                "Annamayya":"Annamaya",
                "Y. S. R.":"Kadapa",
                "Ananthapuramu":"Anantapur",
                "Cuddapah" :"Kadapa",
                "Alluri Sitharama Raju":"Alluri Sitarama Raju",
                "N. T. R.":"N T Rama Rao" ,
                "Dr. B. R. Ambedkar Konaseema":"Konaseema",
                "Parvathipuram Manyam":"Manyam",
                ""

                }
       return dicti2.get(district,district)

df_AP['district']=df_AP['district'].apply(clean_districtAP_name)
print(df_AP['district'].nunique())


