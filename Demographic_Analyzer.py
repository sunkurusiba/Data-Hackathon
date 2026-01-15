import pandas as pd
import os

BASE_DIR = os.getcwd() + "\\api_data_aadhar_demographic\\"
data_files = ["api_data_aadhar_demographic_0_500000.csv",
                "api_data_aadhar_demographic_500000_1000000.csv",
                "api_data_aadhar_demographic_1000000_1500000.csv",
                "api_data_aadhar_demographic_1500000_2000000.csv",
                "api_data_aadhar_demographic_2000000_2071700.csv",
            ]
df = pd.DataFrame()
for FILE_NAME in data_files:
    df1 = pd.read_csv(BASE_DIR+FILE_NAME)
    df = pd.concat([df,df1])

# print(df.shape)       # size of data frame is returned
del df1
# non_state = ["100000","BALANAGAR","Darbhanga","Madanapalle","Puttenahalli","Raja Annamalai Puram"]

# Dropping all the unwanted datas
df.drop(df[df['state'] == "100000"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "BALANAGAR"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Darbhanga"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Nagpur"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Jaipur"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Madanapalle"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Puttenahalli"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Raja Annamalai Puram"].index,inplace=True,axis=0)


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

    dicti = {
        "Andaman & Nicobar Islands" : "Andman and Nicobar Islands",
        "Andaman And Nicobar Islands" : "Andman and Nicobar Islands",
        "andhra pradesh" : "Andhra Pradesh",
        "Chhatisgarh" : "Chhattisgarh",
        "Dadra & Nagar Haveli" : "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra and Nagar Haveli" : "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra And Nagar Haveli" : "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra And Nagar Haveli And Daman And Diu" : "Dadra and Nagar Haveli and Daman and Diu",
        "Daman & Diu" : "Dadra and Nagar Haveli and Daman and Diu",
        "Daman and Diu" : "Dadra and Nagar Haveli and Daman and Diu",
        "Daman And Diu" : "Dadra and Nagar Haveli and Daman and Diu",
        "Jammu & Kashmir" : "Jammu and Kashmir",
        "Jammu And Kashmir" : "Jammu and Kashmir",
        "ODISHA" : "Odisha",
        "odisha" : "Odisha",
        "Orissa" : "Odisha",
        "Pondicherry" : "Puducherry",
        "Uttaranchal" : "Uttrakhand",
        "WEST BENGAL" : "West Bengal",
        "WESTBENGAL" : "West Bengal",
        "West Bangal" : "West Bengal",
        "West Bengli" : "West Bengal",
        "West bengal" : "West Bengal",
        "West  Bengal" : "West Bengal",
        "Westbengal" : "West Bengal",
        "westbengal" : "West Bengal",
        "Uttarakhand" : "Uttrakhand",
    }

    return dicti.get(state, state)

# replacing the improper occurences of the 
df['state'] = df['state'].apply(clean_state_name)

df_UP = df[df['state']=="Uttar Pradesh"]
Correct_district = {
    "Allahabad": "Prayagraj",
    "Faizabad": "Ayodhya",
    "Sant Ravidas Nagar": "Bhadohi",
    "Sant Ravidas Nagar Bhadohi": "Bhadohi",
    "Jyotiba Phule Nagar": "Amroha",
    "Jyotiba Phule Nagar *": "Amroha",
    "Mahrajganj": "Maharajganj",
    "Bagpat": "Baghpat",
    "Baghpat *": "Baghpat",
    "Bulandshahar": "Bulandshahr",
    "Bara Banki" : "Barabanki",
    "Chitrakoot *": "Chitrakoot",
    "Chandauli *": "Chandauli",
    "Kushinagar *": "Kushinagar",
    "Raebareli": "Rae Bareli"
}
df_UP = df_UP["district"].str.strip()
df_UP = df_UP.replace(Correct_district)

print(df_UP.unique())
print(df_UP.nunique())


df_PB = df[df['state']=="Punjab"]
Correct_district={
    "Firozpur": "Ferozepur",
    "Muktsar": "Sri Muktsar Sahib",
    "SAS Nagar (Mohali)": "S.A.S. Nagar (Mohali)",
    "S.A.S Nagar(Mohali)": "S.A.S. Nagar (Mohali)",
    "Nawanshahr": "Shaheed Bhagat Singh Nagar"
}
df_PB = df_PB["district"].str.strip()
df_PB = df_PB.replace(Correct_district)

# print(df_PB.unique())
# print(df_PB.nunique())


df_MP = df[df['state']=="Madhya Pradesh"]
Correct_district = {
    "Hoshangabad": "Narmadapuram",   # renamed officially
    "East Nimar": "Khandwa",         # East Nimar is the old name for Khandwa
    "West Nimar": "Khargone",        # West Nimar is the old name for Khargone
    "Narsimhapur": "Narsinghpur",    # spelling variant
    "Harda *": "Harda",              # duplicate with star
    "Ashok Nagar": "Ashoknagar"      # official spelling is one word
}
df_MP = df_MP["district"].str.strip()
df_MP = df_MP.replace(Correct_district)

# print(df_MP.unique())
# print(df_MP.nunique())

df_MH = df[df['state']=="Maharashtra"]
Correct_district = {
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
df_MH = df_MH["district"].str.strip()
df_MH = df_MH.replace(Correct_district)

# print(df_MH.unique())
# print(df_MH.nunique())

df_HP = df[df['state']=="Himachal Pradesh"]
Correct_district = {
    "Lahul and Spiti" : "Lahaul Spiti",
    "Lahul & Spiti" : "Lahaul Spiti",
    "Lahaul and Spiti" : "Lahaul Spiti",
}
df_HP = df_HP["district"].str.strip()
df_HP = df_HP.replace(Correct_district)

# print(df_HP.unique())
# print(df_HP.nunique())

df_HR = df[df['state'] == "Haryana"]
Correct_district = {
    "Yamuna Nagar": "Yamunanagar"
}
df_HR = df_HR['district'].str.strip()
df_HR = df_HR.replace(Correct_district) 

# print(df_HR.unique())
# print(df_HR.nunique())

df_KL = df[df['state'] == "Kerala"]
Correct_district = {
    "Kasargod" : "Kasaragod"
}
df_KL = df_KL["district"].str.strip()
df_KL = df_KL.replace(Correct_district)

# print(df_KL.unique())
# print(df_KL.nunique())

df_TR = df[df['state'] == "Tripura"]
Correct_district = {
    "Dhalai  *" : "Dhalai"
}
df_TR = df_TR["district"].str.strip()
df_TR = df_TR.replace(Correct_district)

# print(df_TR.unique())
# print(df_TR.nunique())

# for names in target_state.keys():
#     df.replace({'state':names},target_state[names])

# ls = list(df['state'].unique())
# ls.sort()
# print(ls)
# print(df[df['state'] == 'BALANAGAR'].shape)
# print(df['district'].nunique())
# print(df.to_string())