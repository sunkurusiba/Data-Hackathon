import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
enroll_1 = pd.read_csv("D:\\dataset\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment_0_500000.csv")
enroll_2 = pd.read_csv("D:\\dataset\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment_500000_1000000.csv")
enroll_3 = pd.read_csv("D:\\dataset\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment_1000000_1006029.csv")
df=pd.concat([enroll_1,enroll_2,enroll_3],axis=0,ignore_index=True)
# print(df.shape)
# print(df["state"].nunique())
# print(df["state"].unique())
df.drop(df[df['state'] == "100000"].index,inplace=True,axis=0)
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

        "Jammu And Kashmir": "Jammu and Kashmir",
        "Jammu & Kashmir": "Jammu and Kashmir",

        "Pondicherry": "Puducherry",

        "Andaman & Nicobar Islands": "Andaman and Nicobar Islands",
        "Andaman And Nicobar Islands": "Andaman and Nicobar Islands",

        "andhra pradesh ": "Andhra Pradesh",
        # West Bengal
        "WEST BENGAL": "West Bengal",
        "West Bangal": "West Bengal",
        "Westbengal": "West Bengal",
        "West bengal": "West Bengal",
        "WESTBENGAL": "West Bengal",
        "West  Bengal": "West Bengal",

        # Dadra and Nagar Haveli and Daman and Diu
        "The Dadra And Nagar Haveli And Daman And Diu": "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra & Nagar Haveli": "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra and Nagar Haveli": "Dadra and Nagar Haveli and Daman and Diu",
        "Daman and Diu": "Dadra and Nagar Haveli and Daman and Diu",
        "Daman & Diu": "Dadra and Nagar Haveli and Daman and Diu",
        "Daman And Diu": "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra And Nagar Haveli": "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra And Nagar Haveli And Daman And Diu": "Dadra and Nagar Haveli and Daman and Diu",
    }

    # # Return the corrected name if it exists in our dictionary, else return the standardized name
    return dicti.get(state, state)

# 3. Apply the function to the 'state' column
df['state'] = df['state'].apply(clean_state_name)

# 4. Verify the results
# print("Unique States after cleaning:")
# print(df['state'].unique())
# print(df['state'].nunique())

#district wise correction
#Arunachala Pradesh
df_Arunachal=df[df['state']=="Arunachal Pradesh"]
# print(df_Arunachal['district'].unique())
# print(df_Arunachal['district'].nunique())

def clean_districtArunachal_name(district):
       if not isinstance(district, str):
              return "Unknown"

       district = district.strip().title()
       dictiacp={ "Leparada":"Lepa Rada",
                }
       return dictiacp.get(district,district)

df_Arunachal['district']=df_Arunachal['district'].apply(clean_districtArunachal_name)
# print("Unique Districts in Arunachal Pradesh after cleaning:")
# print(df_Arunachal['district'].unique())
# print(df_Arunachal['district'].nunique())

#West Bengal
df_WB =df[df['state'] == "West Bengal"]
# print(df_WB['district'].unique())
# print(df_WB['district'].nunique())

dict_WB = {
      "Coochbehar":"Cooch Behar",
      "Koch Bihar":"Cooch Behar",

      "Darjiling":"Darjeeling",

      "Dinajpur Uttar":"Uttar Dinajpur",
      "North Dinajpur":"Uttar Dinajpur",

      "Dinajpur Dakshin":"Dakshin Dinajpur",
      "South Dinajpur":"Dakshin Dinajpur",

      "24 Paraganas North":"North 24 Parganas",
      "North Twenty Four Parganas":"North 24 Parganas",

      "24 Paraganas South":"South 24 Parganas",
      "South Twenty Four Parganas":"South 24 Parganas",
      "South 24 parganas":"South 24 Parganas",
      "South 24 Pargana":"South 24 Parganas",

      "Hugli":"Hooghly",
      "HOOGHLY":"Hooghly",
      "hooghly":"Hooghly",
      "Hooghiy":"Hooghly",

      "Haora":"Howrah",
      "HOWRAH":"Howrah",
      "Hawrah":"Howrah",

      "NADIA":"Nadia",
      "nadia":"Nadia",

      "Maldah":"Malda",
      "MALDA":"Malda",

      "KOLKATA":"Kolkata",

      "Bardhaman":"Purba Bardhaman",
      "Barddhaman":"Purba Bardhaman",
      "Burdwan":"Purba Bardhaman",

      "Medinipur West":"Paschim Medinipur",
      "West Midnapore":"Paschim Medinipur",
      "Medinipur":"Paschim Medinipur",
      "West Medinipur":"Paschim Medinipur",

      "East Midnapore":"Purba Medinipur",
      "East Midnapur":"Purba Medinipur",

      "Puruliya":"Purulia"
}
df_WB["district"] = df_WB["district"].str.strip()
df_WB["district"] = df_WB["district"].replace(dict_WB)

# print(df_WB["district"].unique())
# print(df_WB["district"].nunique())


# Jammu and Kashmir
# replace the kargil dist j&k to ladakh
df.loc[(df['district']=="Kargil") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"
df.loc[(df['district']=="Leh") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"
df.loc[(df['district']=="Leh (ladakh)") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"
df_JK =df[df['state'] == "Jammu and Kashmir"]
# print(df_JK['district'].unique())
# print(df_JK['district'].nunique())

dict_jk = {
    "Punch": "Poonch",
    "punch": "Poonch",
    "Rajauri": "Rajouri",
    "Baramula": "Baramulla",
    "Shupiyan": "Shopian",
    "Badgam": "Budgam",
    "Bandipore": "Bandipora",
    "Bandipur": "Bandipora",
    "Kathua": "Kathua",
}
df_JK["district"] = df_JK["district"].str.strip()
df_JK["district"] = df_JK["district"].replace(dict_jk)
# print(df_JK["district"].unique())
# print(df_JK["district"].nunique())


#ladakh
df_Ladakh =df[df['state'] == "Ladakh"]
# print(df_Ladakh['district'].unique())
# print(df_Ladakh['district'].nunique())

dict_Ladakh = {
      "Leh (ladakh)":"Leh",
}
df_Ladakh["district"] = df_Ladakh["district"].str.strip()
df_Ladakh["district"] = df_Ladakh["district"].replace(dict_Ladakh)
# print(df_Ladakh["district"].unique())
# print(df_Ladakh["district"].nunique())


#Puducherry
df_Puducherry =df[df['state'] == "Puducherry"]
# print(df_Puducherry['district'].unique())
# print(df_Puducherry['district'].nunique())

dict_Puducherry = {
      "Pondicherry":"Puducherry",
}
df_Puducherry["district"] = df_Puducherry["district"].str.strip()
df_Puducherry["district"] = df_Puducherry["district"].replace(dict_Puducherry)
# print(df_Puducherry["district"].unique())
# print(df_Puducherry["district"].nunique())


#Lakshadweep
df_DNDU =df[df['state'] == "Dadra and Nagar Haveli and Daman and Diu"]
# print(df_DNDU['district'].unique())
# print(df_DNDU['district'].nunique())

dict_DNDU = {
      "Dadra And Nagar Haveli":"Dadra and Nagar Haveli",
      "Dadra & Nagar Haveli":"Dadra and Nagar Haveli",
}
df_DNDU["district"] = df_DNDU["district"].str.strip()
df_DNDU["district"] = df_DNDU["district"].replace(dict_DNDU)
# print(df_DNDU["district"].unique())
# print(df_DNDU["district"].nunique())


#Chandigarh
# replace the Rupnagar dist chandigarh to punjab
df.loc[(df['district']=="Rupnagar") & (df['state']=="Chandigarh"), 'state'] = "Punjab"
df_Chandigarh =df[df['state'] == "Chandigarh"]
# print(df_Chandigarh['district'].unique())
# print(df_Chandigarh['district'].nunique())


#Andaman and Nicobar Islands
df_Andaman =df[df['state'] == "Andaman and Nicobar Islands"]
# print(df_Andaman['district'].unique())
# print(df_Andaman['district'].nunique())

dict_Andaman = {
      "Nicobars":"Nicobar",
      "North And Middle Andaman":"North Middle Andaman",
      "Andamans":"North Middle Andaman",

}
df_Andaman["district"] = df_Andaman["district"].str.strip()
df_Andaman["district"] = df_Andaman["district"].replace(dict_Andaman)
# print(df_Andaman["district"].unique())
# print(df_Andaman["district"].nunique())


#Odisha
df_OD =df[df['state'] == "Odisha"]
# print(df_OD['district'].unique())
# print(df_OD['district'].nunique())
dict_OD = {
    # Khordha
    "Khorda": "Khordha",

    # Angul
    "Anugul": "Angul",
    "Anugal": "Angul",
    "ANUGUL": "Angul",
    "ANGUL": "Angul",

    # Baleswar
    "Baleswar": "Balasore",
    "Baleshwar": "Balasore",

    # Baudh / Boudh
    "Baudh": "Boudh",

    # Jajpur
    "JAJPUR": "Jajpur",
    "Jajapur": "Jajpur",
    "Jagatsinghapur": "Jagatsinghpur",
    "jajpur": "Jajpur",

    # Kendrapara
    "Kendrapara *": "Kendrapara",

    # Nuapada
    "NUAPADA": "Nuapada",

    # Subarnapur (Sonapur)
    "Sonapur": "Subarnapur",

    # Sundargarh
    "Sundergarh": "Sundargarh",
    "Sundergarh": "Sundargarh",

    #Nabarangpur
    "Nabarangapur": "Nabarangpur",
}
df_OD["district"] = df_OD["district"].str.strip()
df_OD["district"] = df_OD["district"].replace(dict_OD)
# print(df_OD["district"].unique())
# print(df_OD["district"].nunique())


# Karnataka District
df_Karnataka=df[df['state'] == "Karnataka"]
print(df_OD['district'].unique())
print(df_OD['district'].nunique())
Karnataka_dict={
        # Bangalore
        "Bengaluru": "Bangalore Urban",
        "Bengaluru Urban": "Bangalore Urban",
        "Bangalore": "Bangalore Urban",
        "Bengaluru South": "Bangalore Urban",
        "Bangalore Rural": "Bangalore Rural",
        "Bengaluru Rural": "Bangalore Rural",

        # Mysore
        "Mysuru": "Mysore",
        "Mysore": "Mysore",

        # Kalaburagi
        "Gulbarga": "Kalaburagi",
        "Kalaburagi": "Kalaburagi",

        # Belagavi / Bellary / Vijayapura
        "Belagavi": "Belgaum",
        "Belgaum": "Belgaum",
        "Ballari": "Bellary",
        "Bellary": "Bellary",
        "Bijapur": "Vijayapura",
        "Bijapur(KAR)": "Vijayapura",
        "Vijayapura": "Vijayapura",

        # Chamarajanagar variations
        "Chamrajanagar": "Chamarajanagar",
        "Chamrajnagar": "Chamarajanagar",
        "Chamarajanagar *": "Chamarajanagar",

        # Chikkamagaluru variations
        "Chickmagalur": "Chikkamagaluru",
        "Chikmagalur": "Chikkamagaluru",
        "Chikkamagaluru": "Chikkamagaluru",

        # Hassan
        "Hasan": "Hassan",
        "Hassan": "Hassan",

        # Ramanagara
        "Ramanagar": "Ramanagara",
        "Ramanagara": "Ramanagara",

        # Shivamogga
        "Shimoga": "Shimoga",
        "Shivamogga": "Shimoga",

        # Tumakuru
        "Tumakuru": "Tumkur",
        "Tumkur": "Tumkur",

        # Yadgir
        "Yadgir": "Yadgir",
        "yadgir": "Yadgir",

        # Others
        "Bagalkot *": "Bagalkot",
        "Gadag *": "Gadag",
        "Haveri *": "Haveri",
        "Udupi *": "Udupi",
        "Davangere": "Davanagere"

}
df_Karnataka['district'] = df_Karnataka['district'].str.strip()
df_Karnataka["district"] = df_Karnataka["district"].replace(Karnataka_dict)
# print(f"no. of districts in karnataka is {df_Karnataka["district"].nunique()}")


# Gujarat District->
# print(df[df["state"]== "Gujarat"]["district"].unique())
df_Gujarat = df[df['state'] == "Gujarat"].copy()
Gujarat_dict = {
    "Ahmedabad": "Ahmedabad",
    "Ahmadabad": "Ahmedabad",

    "Amreli": "Amreli",
    "Anand": "Anand",

    "Arvalli": "Aravalli",
    "Aravalli": "Aravalli",

    "Banas Kantha": "Banaskantha",
    "Banaskantha": "Banaskantha",

    "Bharuch": "Bharuch",
    "Bhavnagar": "Bhavnagar",
    "Botad": "Botad",

    "Chhotaudepur": "Chhota Udaipur",
    "Chhota Udaipur": "Chhota Udaipur",

    "Dohad": "Dahod",
    "Dahod": "Dahod",

    "Dang": "Dang",
    "The Dangs": "Dang",

    "Devbhumi Dwarka": "Devbhoomi Dwarka",
    "Devbhoomi Dwarka": "Devbhoomi Dwarka",

    "Gandhinagar": "Gandhinagar",
    "Gir Somnath": "Gir Somnath",

    "Jamnagar": "Jamnagar",
    "Junagadh": "Junagadh",

    "Kheda": "Kheda",

    "Kachchh": "Kutch",
    "Kutch": "Kutch",

    "Mahisagar": "Mahisagar",

    "Mahesana": "Mehsana",
    "Mehsana": "Mehsana",

    "Morbi": "Morbi",

    "Narmada": "Narmada",
    "Navsari": "Navsari",

    "Panchmahals": "Panchmahal",
    "Panch Mahals": "Panchmahal",
    "Panchmahal": "Panchmahal",

    "Patan": "Patan",
    "Porbandar": "Porbandar",
    "Rajkot": "Rajkot",

    "Sabarkantha": "Sabarkantha",
    "Sabar Kantha": "Sabarkantha",

    "Surat": "Surat",

    "Surendra Nagar": "Surendranagar",
    "Surendranagar": "Surendranagar",

    "Tapi": "Tapi",
    "Vadodara": "Vadodara",
    "Valsad": "Valsad"
}
df_Gujarat['district'] = df_Gujarat['district'].str.strip()
df_Gujarat["district"] = df_Gujarat["district"].replace(Gujarat_dict)
# print(f"no. of districts in Gujarat is {df_Gujarat['district'].nunique()}")


# Delhi Districts->
# print(df[df["state"]== "Delhi"]["district"].unique())
df_Delhi = df[df['state'] == "Delhi"].copy()
Delhi_dict = {
    "North East": "North East Delhi",
    "North East ": "North East Delhi",
    "Najafgarh": "South West Delhi",
    "North West Delhi": "North West Delhi (Rohini)",
    "North East   *": "North East Delhi"
}
df_Delhi['district'] = df_Delhi['district'].str.strip()
df_Delhi["district"] = df_Delhi["district"].replace(Delhi_dict)
# print(f"no. of districts in Delhi is {df_Delhi['district'].nunique()}")



# Jharkhand Districts->
# print(df[df["state"]== "Jharkhand"]["district"].unique())
df_Jharkhand = df[df['state'] == "Jharkhand"].copy()
Jharkhand_dict = {
    "East Singhbum": "East Singhbhum",
    "Purbi Singhbhum": "East Singhbhum",
    "Pashchimi Singhbhum": "West Singhbhum",

    "Hazaribag": "Hazaribagh",

    "Palamau": "Palamu",

    "Kodarma": "Koderma",

    "Pakaur": "Pakur",

    "Sahibganj": "Sahebganj",

    "Garhwa ": "Garhwa",
    "Garhwa *": "Garhwa",

    "Bokaro ": "Bokaro",
    "Bokaro *": "Bokaro",

    "Seraikela-Kharsawan": "Seraikela Kharsawan",
    "Seraikela-kharsawan": "Seraikela Kharsawan"
}

df_Jharkhand['district'] = df_Jharkhand['district'].str.strip()
df_Jharkhand['district'] = df_Jharkhand['district'].replace(Jharkhand_dict)
# print(f"no. of districts in Jharakhand is {df_Jharkhand['district'].nunique()}")


# Nagaland Districts-> is correct
# Manipur Districts->  is correct
