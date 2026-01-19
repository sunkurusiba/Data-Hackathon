import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
enroll_1 = pd.read_csv("D:\\dataset\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment_0_500000.csv")
enroll_2 = pd.read_csv("D:\\dataset\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment_500000_1000000.csv")
enroll_3 = pd.read_csv("D:\\dataset\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment_1000000_1006029.csv")
df=pd.concat([enroll_1,enroll_2,enroll_3],axis=0,ignore_index=True)
print("Shape before cleaned dataframe:", df.shape)
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
#Arunachala Pradesh 01
df_Arunachal=df[df['state']=="Arunachal Pradesh"].copy()
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
print("____________________________")
print(df_Arunachal['district'].nunique())
print("____________________________")

#West Bengal 02
df_WB =df[df['state'] == "West Bengal"].copy()
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


# Jammu and Kashmir 03
# replace the kargil dist j&k to ladakh
df.loc[(df['district']=="Kargil") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"
df.loc[(df['district']=="Leh") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"
df.loc[(df['district']=="Leh (ladakh)") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"
df_JK =df[df['state'] == "Jammu and Kashmir"].copy()
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


#ladakh 04
df_Ladakh =df[df['state'] == "Ladakh"].copy()
# print(df_Ladakh['district'].unique())
# print(df_Ladakh['district'].nunique())

dict_Ladakh = {
      "Leh (ladakh)":"Leh",
}
df_Ladakh["district"] = df_Ladakh["district"].str.strip()
df_Ladakh["district"] = df_Ladakh["district"].replace(dict_Ladakh)
# print(df_Ladakh["district"].unique())
# print(df_Ladakh["district"].nunique())


#Puducherry 05
df_Puducherry =df[df['state'] == "Puducherry"].copy()
print(df_Puducherry['district'].unique())
print(df_Puducherry['district'].nunique())

dict_Puducherry = {
      "Pondicherry":"Puducherry",
}
df_Puducherry["district"] = df_Puducherry["district"].str.strip()
df_Puducherry["district"] = df_Puducherry["district"].replace(dict_Puducherry)
print(df_Puducherry["district"].unique())
print(df_Puducherry["district"].nunique())


#Dadra and Nagar Haveli and Daman and Diu 06
df_DNDU =df[df['state'] == "Dadra and Nagar Haveli and Daman and Diu"].copy()
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


#Chandigarh 07
# replace the Rupnagar dist chandigarh to punjab
df.loc[(df['district']=="Rupnagar") & (df['state']=="Chandigarh"), 'state'] = "Punjab"
df_Chandigarh =df[df['state'] == "Chandigarh"].copy()
print(df_Chandigarh['district'].unique())
print(df_Chandigarh['district'].nunique())


#Andaman and Nicobar Islands 08
df_Andaman =df[df['state'] == "Andaman and Nicobar Islands"].copy()
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


#Odisha 09
df_OD =df[df['state'] == "Odisha"].copy()
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


# Karnataka District 10
df_Karnataka=df[df['state'] == "Karnataka"].copy()
print(df_Karnataka['district'].unique())
print(df_Karnataka['district'].nunique())
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


# Gujarat District-> 11
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


# Delhi Districts-> 12
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



# Jharkhand Districts-> 13
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


# Nagaland Districts-> is correct 14
df_Nagaland = df[df['state'] == "Nagaland"].copy()

#Uttar Pradesh 15
df_UP =df[df['state'] == "Uttar Pradesh"].copy()
# print(df_UP['district'].unique())
# print(df_UP['district'].nunique())
dict_UP = {
    # Allahabad → Prayagraj
    "Allahabad": "Prayagraj",

    # Faizabad → Ayodhya
    "Faizabad": "Ayodhya",

    # Sant Ravidas Nagar → Bhadohi
    "Sant Ravidas Nagar": "Bhadohi",
    "Sant Ravidas Nagar Bhadohi": "Bhadohi",

    # Shrawasti → Shravasti
    "Shrawasti": "Shravasti",

    # Siddharth Nagar → Siddharthnagar
    "Siddharth Nagar": "Siddharthnagar",

    # Bara Banki → Barabanki
    "Bara Banki": "Barabanki",

    # Bulandshahar → Bulandshahr
    "Bulandshahar": "Bulandshahr",

    # Bagpat → Baghpat
    "Bagpat": "Baghpat",

    # Kushinagar variants
    "Kushi Nagar": "Kushinagar",
    "Kushinagar *": "Kushinagar",

    # Maharajganj variants
    "Mahrajganj": "Maharajganj",

    # Jyotiba Phule Nagar → Amroha
    "Jyotiba Phule Nagar": "Amroha",

    "Rae Bareli":"Raebareli",
    "Kheri":"Lakhimpur Kheri"
}
df_UP["district"] = df_UP["district"].str.strip()
df_UP["district"] = df_UP["district"].replace(dict_UP)
# print(df_UP['district'].unique())
# print(df_UP['district'].nunique())


# Meghalaya District->16
# replace kamrup as state of Meghalaya to Assam
# print(df[df['district']=="Kamrup"]['state'].unique())
df.loc[(df['district']=="Kamrup") & (df['state']=="Meghalaya"), 'state'] = "Assam"
# print(df[df['district']=="kamrup"]['state'].unique())
# changing the jaintia hills to west jaintia hills
df["district"] = df["district"].replace(
    "Jaintia Hills", "West Jaintia Hills"
)
meghalaya_district=df[df["state"]== "Meghalaya"].copy()
# print(f"no. of districts in Meghalaya is {meghalaya_district["district"].nunique()}")


#Punjab 17
df_Punjab =df[df['state'] == "Punjab"].copy()
# print(df_Punjab['district'].unique())
# print(df_Punjab['district'].nunique())
dict_Punjab = {
    # SAS Nagar variants
    "S.A.S Nagar": "Mohali",
    "S.A.S Nagar(Mohali)": "Mohali",
    "SAS Nagar (Mohali)":"Mohali",
    # Ferozepur variants
    "Ferozepur": "Firozpur",
    # Muktsar variants
    "Sri Muktsar Sahib": "Muktsar",
    # Shaheed Bhagat Singh Nagar variants
    "Nawanshahr": "Shaheed Bhagat Singh Nagar",
}
df_Punjab["district"] = df_Punjab["district"].str.strip()
df_Punjab["district"] = df_Punjab["district"].replace(dict_Punjab)
# print(df_Punjab['district'].unique())
print("punjab",df_Punjab['district'].nunique())

#Assam 18
df_Assam =df[df['state'] == "Assam"].copy()
# print(df_Assam['district'].unique())
# print(df_Assam['district'].nunique())
dict_Assam = {
    # Morigaon
    "Marigaon": "Morigaon",

    # Sivasagar
    "Sibsagar": "Sivasagar",

    # Dima Hasao
    "North Cachar Hills": "Dima Hasao",

    # Tamulpur
    "Tamulpur District": "Tamulpur",

    # Erroneous entry
    "Sribhumi": "Karimganj",
    "Kamrup Metro":"Kamrup Metropolitan"


}
df_Assam["district"] = df_Assam["district"].str.strip()
df_Assam["district"] = df_Assam["district"].replace(dict_Assam)
print(df_Assam['district'].unique())
print("assam",df_Assam['district'].nunique())


#Himachal_Pradesh 19
df_Himachal_Pradesh =df[df['state'] == "Himachal Pradesh"].copy()
dict_Himachal_Pradesh= {
    # Lahaul and Spiti variants
    "Lahul and Spiti": "Lahaul Spiti",
    "Lahul & Spiti": "Lahaul Spiti",
    "Lahaul and Spiti": "Lahaul Spiti",
}
df_Himachal_Pradesh["district"] = df_Himachal_Pradesh["district"].str.strip()
df_Himachal_Pradesh["district"] = df_Himachal_Pradesh["district"].replace(dict_Himachal_Pradesh)
# print(df_Himachal_Pradesh['district'].unique())
print("Himachal_Pradesh",df_Himachal_Pradesh['district'].nunique())


#Goa district correction 20
df_Goa=df[df['state']=="Goa"].copy()    
# print(df_Goa['district'].unique())
# print(df_Goa['district'].nunique())
dict_Goa={ 
       "Bardez":"North Goa",
       }      
df_Goa['district']=df_Goa['district'].str.strip()
df_Goa['district'] = df_Goa['district'].replace(dict_Goa)       
# print("Unique Districts in Goa after cleaning:")
print("goa",df_Goa['district'].nunique())       
#print(np.sort(df_Goa['district'].unique()))


#Uttarakhand district correction 21
df_Uttarakhand=df[df['state']=="Uttarakhand"].copy()
dict_Uttarakhand={ 
       "Hardwar":"Haridwar",
       "Garhwal": "Pauri",
       "Pauri Garhwal":"Pauri",
       "Tehri Garhwal":"Tehri"
       }
df_Uttarakhand['district']=df_Uttarakhand['district'].str.strip()
df_Uttarakhand['district'] = df_Uttarakhand['district'].replace(dict_Uttarakhand)
# print("Unique Districts in Uttarakhand after cleaning:")       
print("Uttarakhand ",df_Uttarakhand['district'].nunique())
# print(np.sort(df_Uttarakhand['district'].unique()))


#Bihar district correction 22
df_Bihar=df[df['state']=="Bihar"].copy()    
# print(df_Bihar['district'].unique())
# print(df_Bihar['district'].nunique())      
dict_Bihar = {
    # Champaran
    "Purbi Champaran": "East Champaran",
    "Purba Champaran": "East Champaran",
    "Pashchim Champaran": "West Champaran",

    # Aurangabad
    "Aurangabad(bh)": "Aurangabad",
    "Aurangabad(BH)": "Aurangabad",

    # Kaimur
    "Kaimur (Bhabua)": "Kaimur",
    "Bhabua": "Kaimur",

    # Purnia
    "Purnea": "Purnia",

    # Munger
    "Monghyr": "Munger",

    # Samastipur
    "Samstipur": "Samastipur",

    # Sheikhpura
    "Sheikpura": "Sheikhpura"
}
df_Bihar['district']=df_Bihar['district'].str.strip()
df_Bihar['district'] = df_Bihar['district'].replace(dict_Bihar)   
# print("Unique Districts in Bihar after cleaning:")
print("bihar",df_Bihar['district'].nunique())     
# print(np.sort(df_Bihar['district'].unique())) 


#Chattisgarh district correction 23
df_Chattisgarh=df[df['state']=="Chhattisgarh"].copy()
dict_Chattisgarh = {
    # Gaurela–Pendra–Marwahi
    "Gaurella Pendra Marwahi": "Gaurela Pendra Marwahi",
    "Gaurela-pendra-marwahi": "Gaurela Pendra Marwahi",

    # Janjgir–Champa
    "Janjgir-champa": "Janjgir Champa",
    "Janjgir - Champa": "Janjgir Champa",
    "Janjgir Champa": "Janjgir Champa",

    # Kabirdham
    "Kabeerdham": "Kabirdham",
    "Kawardha": "Kabirdham",

    # Dantewada
    "Dakshin Bastar Dantewada": "Dantewada",

    # Kanker
    "Uttar Bastar Kanker": "Kanker",

    # Mohla–Manpur–Ambagarh Chowki
    "Mohla-Manpur-Ambagarh Chouki": "Mohla Manpur",
    "Mohalla-Manpur-Ambagarh Chowki": "Mohla Manpur",
    "Manendragarh–Chirmiri–Bharatpur":"Manendragarh",
    "Sarangarh-Bilaigarh":"Sarangarh Bilaigarh",

    "Khairagarh Chhuikhadan Gandai":"hairagarh"
}
df_Chattisgarh['district']=df_Chattisgarh['district'].str.strip()
df_Chattisgarh['district'] = df_Chattisgarh['district'].replace(dict_Chattisgarh)   
# print("Unique Districts in Chattisgarh after cleaning:")
print("chattisgarh",df_Chattisgarh['district'].nunique())     
# print(np.sort(df_Chattisgarh['district'].unique()))


#Mizoram district correction 24
df_Mizoram=df[df['state']=="Mizoram"].copy()
# print(df_Mizoram['district'].unique())     
# print(df_Mizoram['district'].nunique())
dict_Mizoram={"Mammit":"Mamit",
       }
df_Mizoram['district']=df_Mizoram['district'].str.strip()
df_Mizoram['district'] = df_Mizoram['district'].replace(dict_Mizoram)   
# print("Unique Districts in Mizoram after cleaning:")
print("mizoram",df_Mizoram['district'].nunique())     
# print(np.sort(df_Mizoram['district'].unique()))


#Tripura district correction 25
df_Tripura=df[df['state']=="Tripura"].copy()
# print(df_Tripura['district'].unique())     
# print(df_Tripura['district'].nunique())   
dict_Tripura={ "Dhalai  *":"Dhalai"
       }
df_Tripura['district']=df_Tripura['district'].str.strip()
df_Tripura['district'] = df_Tripura['district'].replace(dict_Tripura)   
# print("Unique Districts in Tripura after cleaning:")    
print("tripura",df_Tripura['district'].nunique())     
# print(np.sort(df_Tripura['district'].unique()))


#sikkim district correction 26
df_Sikkim=df[df['state']=="Sikkim"].copy()
# print(df_Sikkim['district'].unique())     
# print(df_Sikkim['district'].nunique())
dict_Sikkim={ "Namchi":"South Sikkim",
          "East":"East Sikkim",
          "North":"North Sikkim",
          "Mangan":"North Sikkim",
          "West":"West Sikkim",
          "South":"South Sikkim"
       }
df_Sikkim['district']=df_Sikkim['district'].str.strip()
df_Sikkim['district'] = df_Sikkim['district'].replace(dict_Sikkim)   
# print("Unique Districts in Sikkim after cleaning:")     
print("sikkim",df_Sikkim['district'].nunique())
# print(np.sort(df_Sikkim['district'].unique()))


#kerla district correction 27
df_Kerla = df[df['state'] == "Kerala"].copy()
dict_Kerla = {
    "Kasargod" : "Kasaragod"
}
df_Kerla["district"] = df_Kerla["district"].str.strip()
df_Kerla["district"] = df_Kerla["district"].replace(dict_Kerla)
# print(df_Kerla.unique())
print("kerla",df_Kerla.nunique())


#Manipur district correction 28
df_Manipur = df[df['state'] == "Manipur"].copy()
# print(df_Manipur['district'].unique())
print(f"no. of districts in Manipur is {df_Manipur['district'].nunique()}")
#Manipur is corectect


# Andhra Pradesh Districts-> 29
# print(df[df["state"]== "Andhra Pradesh"]["district"].nunique())
df.loc[(df['district']=="Mahabub Nagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Mahbubnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Medak") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Nalgonda") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Rangareddi") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Warangal") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Adilabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Hyderabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Karimnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Khammam") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Nizamabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="K.V.Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="K.v. Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Karim Nagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="Mahabubnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
df.loc[(df['district']=="rangareddi") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"

df_AndhraPradesh = df[df['state'] == "Andhra Pradesh"].copy()
dict_AndhraPradesh = {
    # Anantapur
    "Anantapur": "Anantapur",
    "Ananthapur": "Anantapur",
    "Ananthapuramu": "Anantapur",

    # Chittoor
    "Chittoor": "Chittoor",
    "chittoor": "Chittoor",

    # East Godavari
    "East Godavari": "East Godavari",

    # Nellore
    "Spsr Nellore": "Nellore",
    "Sri Potti Sriramulu Nellore": "Nellore",
    "Nellore": "Nellore",

    # Kadapa
    "Cuddapah": "Kadapa",
    "Y. S. R": "Kadapa",

    # NTR
    "N. T. R": "N T Rama Rao",

    # Konaseema
    "Dr. B. R. Ambedkar Konaseema": "Konaseema",

    # Manyam
    "Parvathipuram Manyam": "Manyam",

    # Visakhapatnam
    "Visakhapatanam": "Visakhapatnam",
    "Visakhapatnam": "Visakhapatnam",

    # Others
    "Vizianagaram": "Vizianagaram",
    "Srikakulam": "Srikakulam",
    "West Godavari": "West Godavari",
    "Prakasam": "Prakasam",
    "Krishna": "Krishna",
    "Kurnool": "Kurnool",
    "Nandyal": "Nandyal",
    "Palnadu": "Palnadu",
    "Bapatla": "Bapatla",
    "Guntur": "Guntur",
    "Kakinada": "Kakinada",
    "Eluru": "Eluru",

    # New districts
    "Alluri Sitharama Raju": "Alluri Sitarama Raju",
    "Alluri Sitarama Raju": "Alluri Sitarama Raju",
    "Anakapalli": "Anakapalli",
    "Annamayya": "Annamaya",
    "Sri Sathya Sai": "Sri Satya Sai",
    "Sri Sathya Sai": "Sri Satya Sai",
    "Tirupati": "Sri Balaji"
}
df_AndhraPradesh['district'] = df_AndhraPradesh['district'].str.strip()
df_AndhraPradesh['district'] = df_AndhraPradesh['district'].replace(dict_AndhraPradesh)
print(f"no. of districts in Andhra Pradesh is {df_AndhraPradesh['district'].nunique()}")


# Telengana Districts-> 30
# print(df[df["state"]== "Telangana"]["district"].unique())
df_Telangana = df[df['state'] == "Telangana"].copy()
Telangana_dict = {
    # Hyderabad & RR
    "Hyderabad": "Hyderabad",
    "Ranga Reddy": "Ranga Reddy",
    "Rangareddi": "Ranga Reddy",
    "Rangareddy": "Ranga Reddy",
    "rangareddi": "Ranga Reddy",
    "K.v. Rangareddy": "Ranga Reddy",
    "K.V.Rangareddy": "Ranga Reddy",

    # Medchal
    "Medchal-malkajgiri": "Medchal Malkajgiri",
    "Medchal Malkajgiri": "Medchal Malkajgiri",
    "Medchal−malkajgiri": "Medchal Malkajgiri",
    "Medchal?malkajgiri": "Medchal Malkajgiri",

    # Warangal
    "Warangal": "Warangal",
    "Warangal Rural": "Warangal",
    "Warangal Urban": "Warangal",
    "Warangal (urban)": "Warangal",
    "Hanumakonda": "Hanumakonda",

    # Northern districts
    "Adilabad": "Adilabad",
    "Jagitial": "Jagtial",
    "Jagtial": "Jagtial",
    "Komaram Bheem": "Komaram Bheem",
    "Mancherial": "Mancherial",
    "Nirmal": "Nirmal",

    # Central
    "Karim Nagar": "Karimnagar",
    "Karimnagar": "Karimnagar",
    "Peddapalli": "Peddapalli",
    "Rajanna Sircilla": "Rajanna Sircilla",
    "Siddipet": "Siddipet",

    # South
    "Mahabub Nagar": "Mahbubnagar",
    "Mahabubnagar": "Mahbubnagar",
    "Mahbubnagar": "Mahbubnagar",
    "Nagarkurnool": "Nagarkurnool",
    "Wanaparthy": "Wanaparthy",
    "Jogulamba Gadwal": "Jogulamba",
    "Jogulamba": "Jogulamba",

    # East
    "Nalgonda": "Nalgonda",
    "Suryapet": "Suryapet",
    "Yadadri.": "Yadadri Bhuvanagiri",

    # Others
    "Bhadradri Kothagudem": "Bhadradri Kothagudem",
    "Khammam": "Khammam",
    "Kamareddy": "Kamareddy",
    "Medak": "Medak",
    "Mulugu": "Mulugu",
    "Narayanpet": "Narayanpet",
    "Nizamabad": "Nizamabad",
    "Sangareddy": "Sangareddy",
    "Vikarabad": "Vikarabad",
    "Jangoan": "Jangaon",
    "Jangaon": "Jangaon",
    "Jayashankar Bhupalpally": "Jayashankar"
}
df_Telangana['district'] = df_Telangana['district'].str.strip()
df_Telangana['district'] = df_Telangana['district'].replace(Telangana_dict)
print(f"no. of districts in Telengana is {df_Telangana['district'].nunique()}")


# Madhya Pradesh Districts-> 31
# print(df[df["state"]== "Madhya Pradesh"]["district"].unique())
df_MadhyaPradesh = df[df['state'] == "Madhya Pradesh"].copy()
MadhyaPradesh_dict = {
    # Ashoknagar
    "Ashok Nagar": "Ashoknagar",
    "Ashoknagar": "Ashoknagar",

    # Nimar regions
    "East Nimar": "Khandwa",
    "West Nimar": "Khargone",

    # Hoshangabad
    "Hoshangabad": "Hoshangabad (Narmadapuram)",
    "Narmadapuram": "Hoshangabad (Narmadapuram)",

    # Narsinghpur
    "Narsimhapur": "Narsinghpur",
    "Narsinghpur": "Narsinghpur",

    # Harda
    "Harda *": "Harda",
    "Harda": "Harda",

    # Normal districts
    "Agar Malwa": "Agar Malwa",
    "Alirajpur": "Alirajpur",
    "Anuppur": "Anuppur",
    "Balaghat": "Balaghat",
    "Barwani": "Barwani",
    "Betul": "Betul",
    "Bhind": "Bhind",
    "Bhopal": "Bhopal",
    "Burhanpur": "Burhanpur",
    "Chhatarpur": "Chhatarpur",
    "Chhindwara": "Chhindwara",
    "Damoh": "Damoh",
    "Datia": "Datia",
    "Dewas": "Dewas",
    "Dhar": "Dhar",
    "Dindori": "Dindori",
    "Guna": "Guna",
    "Gwalior": "Gwalior",
    "Indore": "Indore",
    "Jabalpur": "Jabalpur",
    "Jhabua": "Jhabua",
    "Katni": "Katni",
    "Khandwa": "Khandwa",
    "Khargone": "Khargone",
    "Maihar": "Maihar",
    "Mandla": "Mandla",
    "Mandsaur": "Mandsaur",
    "Mauganj": "Mauganj",
    "Morena": "Morena",
    "Neemuch": "Neemuch",
    "Niwari": "Niwari",
    "Pandhurna": "Pandhurna",
    "Panna": "Panna",
    "Raisen": "Raisen",
    "Rajgarh": "Rajgarh",
    "Ratlam": "Ratlam",
    "Rewa": "Rewa",
    "Sagar": "Sagar",
    "Satna": "Satna",
    "Sehore": "Sehore",
    "Seoni": "Seoni",
    "Shahdol": "Shahdol",
    "Shajapur": "Shajapur",
    "Sheopur": "Sheopur",
    "Shivpuri": "Shivpuri",
    "Sidhi": "Sidhi",
    "Singrauli": "Singrauli",
    "Tikamgarh": "Tikamgarh",
    "Ujjain": "Ujjain",
    "Umaria": "Umaria",
    "Vidisha": "Vidisha"
}
df_MadhyaPradesh ['district'] = df_MadhyaPradesh ['district'].str.strip()
df_MadhyaPradesh ['district'] = df_MadhyaPradesh ['district'].replace(MadhyaPradesh_dict )
print(f"no. of districts in Andhra Pradesh is {df_MadhyaPradesh['district'].nunique()}")


# Tamil Nadu Districts-> 32
# print(df[df["state"]== "Tamil Nadu"]["district"].unique())
df_TamilNadu = df[df['state'] == "Tamil Nadu"].copy()
TamilNadu_dict = {
    "Kancheepuram": "Kanchipuram",
    "Kanchipuram": "Kanchipuram",

    "Villupuram": "Viluppuram",
    "Viluppuram": "Viluppuram",

    "Tuticorin": "Thoothukudi",
    "Thoothukkudi": "Thoothukudi",

    "The Nilgiris": "Nilgiris",

    "Tirupathur": "Tirupattur",
    "Tirupattur": "Tirupattur",

    "Namakkal   *": "Namakkal",
    "Namakkal": "Namakkal",

    "Tiruvarur": "Tiruvarur",
    "Thiruvarur": "Tiruvarur",

    # Direct mappings / unchanged
    "Ariyalur": "Ariyalur",
    "Chengalpattu": "Chengalpattu",
    "Chennai": "Chennai",
    "Coimbatore": "Coimbatore",
    "Cuddalore": "Cuddalore",
    "Dharmapuri": "Dharmapuri",
    "Dindigul": "Dindigul",
    "Erode": "Erode",
    "Kallakurichi": "Kallakurichi",
    "Kanyakumari": "Kanyakumari",
    "Karur": "Karur",
    "Krishnagiri": "Krishnagiri",
    "Madurai": "Madurai",
    "Mayiladuthurai": "Mayiladuthurai",
    "Nagapattinam": "Nagapattinam",
    "Perambalur": "Perambalur",
    "Pudukkottai": "Pudukkottai",
    "Ramanathapuram": "Ramanathapuram",
    "Ranipet": "Ranipet",
    "Salem": "Salem",
    "Sivaganga": "Sivaganga",
    "Tenkasi": "Tenkasi",
    "Thanjavur": "Thanjavur",
    "Theni": "Theni",
    "Tiruchirappalli": "Tiruchirappalli",
    "Tirunelveli": "Tirunelveli",
    "Tiruppur": "Tiruppur",
    "Tiruvallur": "Tiruvallur",
    "Tiruvannamalai": "Tiruvannamalai",
    "Vellore": "Vellore",
    "Virudhunagar": "Virudhunagar",
    "Thiruvallur": "Tiruvallur",
    "Kanniyakumari": "Kanyakumari"
}
df_TamilNadu['district'] = df_TamilNadu['district'].str.strip()
df_TamilNadu['district'] = df_TamilNadu['district'].replace(TamilNadu_dict )
print(df_TamilNadu['district'].unique())  
print(f"no. of districts in Tamil Nadu is {df_TamilNadu['district'].nunique()}")


# Maharashtra Districts-> 33
# print(df[df["state"]== "Maharashtra"]["district"].unique())
df_Maharashtra = df[df['state'] == "Maharashtra"].copy()

Maharashtra_dict = {
    "Ahmadnagar": "Ahmednagar",                 # spelling variant
    "Ahmed Nagar": "Ahmednagar",                # spacing variant
    "Bid": "Beed",                              # alternate spelling
    "Buldana": "Buldhana",                      # spelling variant
    "Aurangabad": "Chhatrapati Sambhajinagar",  # renamed officially
    "Chatrapati Sambhaji Nagar": "Chhatrapati Sambhajinagar",  # spelling variant
    "Osmanabad": "Dharashiv",                   # renamed officially
    "Raigarh": "Raigad",                        # spelling variant
    "Raigarh(MH)": "Raigad",                    # variant with suffix
    "Mumbai( Sub Urban )": "Mumbai Suburban",   # spacing variant
    "Mumbai City": "Mumbai City",               # correct, but unify with "Mumbai"
    "Mumbai": "Mumbai City",       # keep official, but unify with other variants
    "Gondiya": "Gondia",                        # spelling variant
    "Gondiya *": "Gondia",                      # duplicate with star
    "Nandurbar *": "Nandurbar",                 # duplicate with star
    "Washim *": "Washim",                       # duplicate with star
    "Hingoli *": "Hingoli",                     # duplicate with star
    "Ahilyanagar": "Ahmednagar",                # unofficial variant sometimes used
    "Dist : Thane": "Thane"                     # variant with prefix
}
df_Maharashtra['district'] = df_Maharashtra["district"].str.strip()
df_Maharashtra['district'] = df_Maharashtra["district"].replace(Maharashtra_dict)
print(f"no. of districts in Maharashtra is {df_Maharashtra['district'].nunique()}")


# Rajasthan Districts-> 34
# print(df[df["state"]== "Rajasthan"]["district"].unique())
df_Rajasthan = df[df['state'] == "Rajasthan"].copy()
Rajasthan_dict = {
    # Ajmer region
    "Ajmer": "Ajmer",
    "Beawar": "Beawar",
    "Kekri": "Kekri",

    # Alwar region
    "Alwar": "Alwar",
    "Khairthal Tijara": "Khairthal Tijara",
    "Kotputli Behror": "Kotputli Behror",

    # Jaipur region
    "Jaipur": "Jaipur",
    "Jaipur Rural": "Jaipur Rural",
    "Dudu": "Dudu",

    # Jodhpur region
    "Jodhpur": "Jodhpur",
    "Jodhpur Rural": "Jodhpur Rural",
    "Phalodi": "Phalodi",

    # Bikaner region
    "Bikaner": "Bikaner",
    "Sri Ganganagar": "Sri Ganganagar",
    "Ganganagar": "Sri Ganganagar",
    "Anupgarh": "Anupgarh",

    # Bharatpur region
    "Bharatpur": "Bharatpur",
    "Deeg": "Deeg",
    "Deeg\xa0": "Deeg",
    "Dholpur": "Dholpur",
    "Dhaulpur": "Dholpur",
    "Karauli": "Karauli",

    # Kota region
    "Kota": "Kota",
    "Jhalawar": "Jhalawar",
    "Baran": "Baran",

    # Udaipur region
    "Udaipur": "Udaipur",
    "Rajsamand": "Rajsamand",
    "Dungarpur": "Dungarpur",
    "Banswara": "Banswara",
    "Salumbar": "Salumbar",
    "Pratapgarh": "Pratapgarh",

    # Nagaur region
    "Nagaur": "Nagaur",
    "Didwana-Kuchaman": "Didwana Kuchaman",

    # Others
    "Sikar": "Sikar",
    "Neem ka Thana": "Neem ka Thana",
    "Jhunjhunun": "Jhunjhunu",
    "Jhunjhunu": "Jhunjhunu",
    "Churu": "Churu",
    "Hanumangarh": "Hanumangarh",
    "Sawai Madhopur": "Sawai Madhopur",
    "Tonk": "Tonk",
    "Pali": "Pali",
    "Barmer": "Barmer",
    "Balotra": "Balotra",
    "Sanchore": "Sanchore",
    "Jalore": "Jalore",
    "Jalor": "Jalore",
    "Sirohi": "Sirohi",
    "Chittorgarh": "Chittorgarh",
    "Chittaurgarh": "Chittorgarh",
    "Shahpura": "Shahpura",
    "Gangapur City": "Gangapur City"
}
df_Rajasthan['district'] = df_Rajasthan["district"].str.strip()
df_Rajasthan['district'] = df_Rajasthan["district"].replace(Rajasthan_dict)
print(f"no. of districts in Rajasthan is {df_Rajasthan['district'].nunique()}")


# Haryana District-> 35
# print(df[df["state"]== "Haryana"]["district"].nunique())
df_Haryana = df[df['state'] == "Haryana"].copy()
Haryana_dict = {
    # Gurugram / Mewat
    "Gurgaon": "Gurugram",
    "Gurugram": "Gurugram",
    "Mewat": "Nuh (Formerly Mewat)",
    "Nuh": "Nuh (Formerly Mewat)",

    # Yamunanagar
    "Yamuna Nagar": "Yamunanagar",
    "Yamunanagar": "Yamunanagar",

    # Jhajjar
    "Jhajjar *": "Jhajjar",
    "Jhajjar": "Jhajjar",

    # Direct mappings / unchanged
    "Ambala": "Ambala",
    "Bhiwani": "Bhiwani",
    "Charkhi Dadri": "Charkhi Dadri",
    "Faridabad": "Faridabad",
    "Fatehabad": "Fatehabad",
    "Hisar": "Hisar",
    "Jind": "Jind",
    "Kaithal": "Kaithal",
    "Karnal": "Karnal",
    "Kurukshetra": "Kurukshetra",
    "Mahendragarh": "Mahendragarh",
    "Palwal": "Palwal",
    "Panchkula": "Panchkula",
    "Panipat": "Panipat",
    "Rewari": "Rewari",
    "Rohtak": "Rohtak",
    "Sirsa": "Sirsa",
    "Sonipat": "Sonipat"
}

df_Haryana['district'] = df_Haryana["district"].str.strip()
df_Haryana['district'] = df_Haryana["district"].replace(Haryana_dict)
print(f"no. of districts in Haryana is {df_Haryana['district'].nunique()}")


# Lakshadweep District-> 35
df_Lakshadweep = df[df['state'] == "Lakshadweep"].copy()
print("Lakshadweep",df[df["state"]== "Lakshadweep"]["district"].nunique())


list_of_dfs = [df_AndhraPradesh,df_Arunachal,df_Assam,
               df_Bihar,df_Chattisgarh,df_Goa,df_Gujarat,
               df_Haryana,df_Himachal_Pradesh,df_Jharkhand,df_Kerla,df_Karnataka,
              df_Maharashtra,df_MadhyaPradesh,df_Manipur,df_Mizoram,
              meghalaya_district,df_Nagaland,df_OD,
              df_Punjab,df_Rajasthan,df_Sikkim,df_TamilNadu,
              df_Telangana,df_Tripura,df_UP,df_Uttarakhand,df_WB,
              df_Delhi,df_Ladakh,df_Puducherry,df_DNDU,
              df_Chandigarh,df_Andaman,df_JK,df_Lakshadweep
              ]

df_cleaned = pd.concat(list_of_dfs, ignore_index=True)  
print("Shape of cleaned dataframe:", df_cleaned.shape)


df_cleaned.to_csv("cleaned_Enrollment_data_1.csv", index=False)