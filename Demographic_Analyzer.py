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

print(df.shape)

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
        "Andaman & Nicobar Islands" : "Andaman and Nicobar Islands",
        "Andaman And Nicobar Islands" : "Andaman and Nicobar Islands",
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

df_UP = df[df['state']=="Uttar Pradesh"].copy()
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
df_UP['district'] = df_UP["district"].str.strip()
df_UP['district'] = df_UP['district'].replace(Correct_district)

# print(df_UP.unique())
# print(df_UP.nunique())


# replace the Rupnagar dist chandigarh to punjab
df.loc[(df['district']=="Rupnagar") & (df['state']=="Chandigarh"), 'state'] = "Punjab"
df.loc[(df['district']=="Mohali") & (df['state']=="Chandigarh"), 'state'] = "Punjab"
df_PB = df[df['state']=="Punjab"].copy()
Correct_district={
    "Firozpur": "Ferozepur",
    "Muktsar": "Sri Muktsar Sahib",
    "SAS Nagar (Mohali)": "S.A.S. Nagar (Mohali)",
    "S.A.S Nagar(Mohali)": "S.A.S. Nagar (Mohali)",
    "Mohali": "S.A.S. Nagar (Mohali)",
    "Nawanshahr": "Shaheed Bhagat Singh Nagar"
}
df_PB['district'] = df_PB["district"].str.strip()
df_PB['district'] = df_PB['district'].replace(Correct_district)

# print(df_PB['district'].unique())
# print(df_PB['district'].nunique())


df_MP = df[df['state']=="Madhya Pradesh"].copy()
Correct_district = {
    "Hoshangabad": "Narmadapuram",   # renamed officially
    "East Nimar": "Khandwa",         # East Nimar is the old name for Khandwa
    "West Nimar": "Khargone",        # West Nimar is the old name for Khargone
    "Narsimhapur": "Narsinghpur",    # spelling variant
    "Harda *": "Harda",              # duplicate with star
    "Ashok Nagar": "Ashoknagar"      # official spelling is one word
}
df_MP['district'] = df_MP["district"].str.strip()
df_MP['district'] = df_MP['district'].replace(Correct_district)

# print(df_MP.unique())
# print(df_MP.nunique())

df.loc[(df['district']=="Aurangabad") & (df['state']=="Bihar"), 'state'] = "Maharashtra"
df_MH = df[df['state']=="Maharashtra"].copy()
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
df_MH['district'] = df_MH["district"].str.strip()
df_MH['district'] = df_MH['district'].replace(Correct_district)

# print(df_MH.unique())
# print(df_MH.nunique())

df_HP = df[df['state']=="Himachal Pradesh"].copy()
Correct_district = {
    "Lahul and Spiti" : "Lahaul Spiti",
    "Lahul & Spiti" : "Lahaul Spiti",
    "Lahaul and Spiti" : "Lahaul Spiti",
}
df_HP['district'] = df_HP["district"].str.strip()
df_HP['district'] = df_HP['district'].replace(Correct_district)

# print(df_HP.unique())
# print(df_HP.nunique())

df_HR = df[df['state'] == "Haryana"].copy()
Correct_district = {
    "Yamuna Nagar": "Yamunanagar"
}
df_HR['district']= df_HR['district'].str.strip()
df_HR['district'] = df_HR['district'].replace(Correct_district) 

# print(df_HR.unique())
# print(df_HR.nunique())

df_KL = df[df['state'] == "Kerala"].copy()
Correct_district = {
    "Kasargod" : "Kasaragod"
}
df_KL['district'] = df_KL["district"].str.strip()
df_KL['district'] = df_KL['district'].replace(Correct_district)

# print(df_KL.unique())
# print(df_KL.nunique())

df_TR = df[df['state'] == "Tripura"].copy()
Correct_district = {
    "Dhalai  *" : "Dhalai"
}
df_TR['district'] = df_TR["district"].str.strip()
df_TR['district'] = df_TR['district'].replace(Correct_district)

df.drop(df[df['district'] == "Balianta"].index,inplace=True,axis=0)
df_OD = df[df['state'] == "Odisha"].copy()

dicti1={ "JAJPUR":"Jajpur",
                "Jajapur":"Jajpur",
                "jajpur":"Jajpur",
                "Jajapur  *":"Jajpur",
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
                "Bhadrak(R)" : "Bhadrak"
}

df_OD['district'] = df_OD['district'].str.strip()
df_OD['district'] = df_OD['district'].replace(dicti1)


#Andhra Pradesh district correction
# df_AP=df[df['state']=="Andhra Pradesh"].copy()
# print(df_AP['district'].nunique())

# Replace Warangal from andhra pradesh to Telangana
#print(df[df['district']=="Warangal"].shape)
df.loc[(df['district']=="Warangal") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Warangal"]['state'].unique())

#Replace Adilabad from andhra pradesh to Telangana
#print(df[df['district']=="Adilabad"]['state'].unique())
df.loc[(df['district']=="Adilabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Adilabad"]['state'].unique())

#Replace Hyderabad from andhra pradesh to Telangana
#print(df[df['district']=="Hyderabad"]['state'].unique())
df.loc[(df['district']=="Hyderabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Hyderabad"]['state'].unique())


#Replace Nizamabad from andhra pradesh to Telangana
#print(df[df['district']=="Nizamabad"]['state'].unique())              
df.loc[(df['district']=="Nizamabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Nizamabad"]['state'].unique())

#Replace khammam from andhra pradesh to Telangana
#print(df[df['district']=="Khammam"]['state'].unique())         
df.loc[(df['district']=="Khammam") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Khammam"]['state'].unique())

#Replace Karimnagar from andhra pradesh to Telangana
#print(df[df['district']=="Karimnagar"]['state'].unique())
df.loc[(df['district']=="Karimnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Karimnagar"]['state'].unique())
#print(df[df['district']=="Karim Nagar"]['state'].unique())
df.loc[(df['district']=="Karim Nagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Karim Nagar"]['state'].unique())

#Replace Rangareddy from andhra pradesh to Telangana
#print(df[df['district']=="Rangareddi"]['state'].unique())
df.loc[(df['district']=="Rangareddi") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Rangareddi"]['state'].unique())
#(df[df['district']=="Rangareddy"]['state'].unique())
df.loc[(df['district']=="Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Rangareddy"]['state'].unique())
#(df[df['district']=="K.v. Rangareddy"]['state'].unique())
df.loc[(df['district']=="K.v. Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="K.v. Rangareddy"]['state'].unique())
#(df[df['district']=="K.V. Rangareddy"]['state'].unique())
df.loc[(df['district']=="K.V. Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="K.V. Rangareddy"]['state'].unique())
#(df[df['district']=="rangareddi"]['state'].unique())
df.loc[(df['district']=="rangareddi") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="rangareddi"]['state'].unique())
#(df[df['district']=="K.V.Rangareddy"]['state'].unique())
df.loc[(df['district']=="K.V.Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="K.V.Rangareddy"]['state'].unique())


#Replace Medak from andhra pradesh to Telangana
#print(df[df['district']=="Medak"]['state'].unique())
df.loc[(df['district']=="Medak") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Medak"]['state'].unique())

#Replace Mahbubnagar from andhra pradesh to Telangana
#print(df[df['district']=="Mahbubnagar"]['state'].unique())
df.loc[(df['district']=="Mahbubnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Mahbubnagar"]['state'].unique())
#print(df[df['district']=="Mahabub Nagar"]['state'].unique())
df.loc[(df['district']=="Mahabub Nagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Mahabub Nagar"]['state'].unique())
#print(df[df['district']=="Mahabubnagar"]['state'].unique())
df.loc[(df['district']=="Mahabubnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Mahabubnagar"]['state'].unique())

#Replace Nalgonda from andhra pradesh to Telangana
#print(df[df['district']=="Nalgonda"]['state'].unique())
df.loc[(df['district']=="Nalgonda") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
# print(df[df['district']=="Nalgonda"]['state'].unique())



df_AP=df[df['state']=="Andhra Pradesh"].copy()
# print(df_AP['district'].nunique())

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
        "Y. S. R":"Kadapa",
        "Ananthapuramu":"Anantapur",
        "Cuddapah" :"Kadapa",
        "Alluri Sitharama Raju":"Alluri Sitarama Raju",
        "N. T. R.":"N T Rama Rao" ,
        "Dr. B. R. Ambedkar Konaseema":"Konaseema",
        "Parvathipuram Manyam":"Manyam",
        "Sri Potti Sriramulu Nellore":"Nellore"

}

df_AP['district'] = df_AP['district'].str.strip()
df_AP['district'] = df_AP['district'].replace(dicti2)

# print(df_AP.unique())
# print(df_AP.nunique())


#Telengana district correction
df_Telangana=df[df['state']=="Telangana"].copy()

dictio3= {
    "K.v. Rangareddy": "Rangareddy",
    "K.V.Rangareddy": "Rangareddy",
    "rangareddi": "Rangareddy",
    "Rangareddi": "Rangareddy",
    "Medchal-malkajgiri": "Medchal–Malkajgiri",
    "Medchal?malkajgiri": "Medchal–Malkajgiri",
    "Medchal−malkajgiri": "Medchal–Malkajgiri",
    "Medchalâ\x88\x92malkajgiri": "Medchal–Malkajgiri",
    "Mahbubnagar": "Mahabubnagar",
    "Mahabub Nagar": "Mahabubnagar",
    "Karim Nagar": "Karimnagar",
    "Jangoan": "Jangaon",
    "Warangal Urban": "Hanumakonda",   # officially renamed
    "Warangal (urban)": "Hanumakonda",
    "Warangal Rural": "Warangal",
    "Yadadri.": "Yadadri Bhuvanagiri"
}
df_Telangana['district']=df_Telangana['district'].str.strip()
df_Telangana['district'] = df_Telangana['district'].replace(dictio3)
# print(df_Telangana['district'].unique())
# print(df_Telangana['district'].nunique())



#Tamil Nadu district correction
df_TamilNadu=df[df['state']=="Tamil Nadu"].copy()
 
dictio4 ={ "Thiruvarur": "Tiruvarur",
    "Tiruvarur": "Tiruvarur",
    "Viluppuram": "Villupuram",
    "Thiruvallur": "Tiruvallur",
    "Kancheepuram": "Kanchipuram",
    "Kanchipuram": "Kanchipuram",
    "Tirupattur": "Tirupathur",
    "Tuticorin": "Thoothukkudi",
    "Kanniyakumari": "Kanyakumari"
    }

df_TamilNadu['district']=df_TamilNadu['district'].str.strip()
df_TamilNadu['district'] = df_TamilNadu['district'].replace(dictio4)
# print(df_TamilNadu['district'].unique())
# print(df_TamilNadu['district'].nunique())
# print("Unique Districts in Tamil Nadu after cleaning:")
# print(df_TamilNadu['district'].nunique())
#print(np.sort(df_TamilNadu['district'].unique()))


#Rajasthan district correction
df_Rajasthan=df[df['state']=="Rajasthan"].copy()
dictio5={ "JHUNJHUNU":"Jhunjhunu",
    "JHUNJHUNU  *":"Jhunjhunu",
    "Jhalawar  *":"Jhalawar",
    "Banswara  *":"Banswara",
    "Baran  *":"Baran",
    "Dhaulpur":"Dholpur",
    "Dhaulpur  *":"Dholpur",
    "Dholpur  *":"Dholpur",
    "Sawai Madhopur  *":"Sawai Madhopur",
    "Chittaurgarh":"Chittorgarh",
    "Jalort":"Jalore",
    "Jalor":"Jalore",
    "Jhunjhunun":"Jhunjhunu"
}
df_Rajasthan['district']=df_Rajasthan['district'].str.strip()
df_Rajasthan['district'] = df_Rajasthan['district'].replace(dictio5)
# print(df_Rajasthan['district'].unique())
# print(df_Rajasthan['district'].nunique())
# print("Unique Districts in Rajasthan after cleaning:")
# print(df_Rajasthan['district'].nunique()) 
#print(np.sort(df_Rajasthan['district'].unique()))


# replace kamrup as state of Meghalaya to Assam
# print(df[df['district']=="Kamrup"]['state'].unique())
df.loc[(df['district']=="Kamrup") & (df['state']=="Meghalaya"), 'state'] = "Assam"
# print(df[df['district']=="kamrup"]['state'].unique())
# changing the jaintia hills to west jaintia hills
df["district"] = df["district"].replace(
    "Jaintia Hills", "West Jaintia Hills"
)
meghalaya_district=df[df["state"]== "Meghalaya"].copy()
# print(meghalaya_district['district'].unique())
# print(meghalaya_district['district'].nunique())


#Assam district correction
df_Assam=df[df['state']=="Assam"].copy()
dictio6={ "Darrang  *":"Dhubri",   
       "Dhibrugarh  *":"Dibrugarh",
       "Kokrajhar  *":"Kokrajhar",
       "Lakhimpur  *":"Lakhimpur",
       "Sibsagar":"Sivasagar",
       "Sibsagar  *":"Sivasagar",
       "Tinsukia  *":"Tinsukia",
       "North Cachar Hills" : "Dima Hasao",
       "Tamulpur District" : "Tamulpur",
       "Sribhumi": "Karimganj",
       "Kamrup Metro":"Kamrup Metropolitan"
}
df_Assam['district']=df_Assam['district'].str.strip()
df_Assam['district'] = df_Assam['district'].replace(dictio6)   
# print(df_Assam['district'].unique())     
# print(df_Assam['district'].nunique())


#Goa district correction
df_Goa=df[df['state']=="Goa"].copy()      
dictio7={ "NORTH GOA":"North Goa",
       "SOUTH GOA":"South Goa",
       "Bardez":"North Goa",
       "Tiswadi":"North Goa",
       "Bicholim":"North Goa",
}      
df_Goa['district']=df_Goa['district'].str.strip()
df_Goa['district'] = df_Goa['district'].replace(dictio7)       
# print(df_Goa['district'].unique())
# print(df_Goa['district'].nunique())


#Uttarakhand district correction
df_Uttarakhand=df[df['state']=="Uttarakhand"].copy()
dictio8={ 
       "Hardwar":"Haridwar",
       "Tehri Garhwal" : "Tehri",
       "Pauri Garhwal" : "Pauri",
       "Garhwal" : "Pauri"
}
df_Uttarakhand['district']=df_Uttarakhand['district'].str.strip()
df_Uttarakhand['district'] = df_Uttarakhand['district'].replace(dictio8)
# print(df_Uttarakhand['district'].unique())
# print(df_Uttarakhand['district'].nunique())


#Bihar district correction
# df_Bihar=df[df['state']=="Bihar"].copy()         

#Replace Aurangabad from bihar to Maharashtra
#print(df[df['district']=="Aurangabad"]['state'].unique())     
# print(df[df['district']=="Aurangabad"]['state'].unique())


df_Bihar=df[df['state']=="Bihar"].copy()         
     
dictio9={ "Aurangabad(bh)":"Aurangabad(BH)",
         "Bhabua":"Kaimur",
         "Monghyr":"Munger",
         "Purba Champaran":"East Champaran",
         "Purnea":"Purnia",
         "Kaimur (Bhabua)":"Kaimur",
         "Sheikpura":"Sheikhpura",
         "Pashchim Champaran":"West Champaran",
         "Samsatipur":"Samastipur",
         "Samstipur":"Samastipur"
}
df_Bihar['district']=df_Bihar['district'].str.strip()
df_Bihar['district'] = df_Bihar['district'].replace(dictio9)   
# print(df_Bihar['district'].unique())
# print(df_Bihar['district'].nunique())
# print("Unique Districts in Bihar after cleaning:")
# print(df_Bihar['district'].nunique())     
#print(np.sort(df_Bihar['district'].unique()))   


#Chattisgarh district correction
df_Chattisgarh=df[df['state']=="Chhattisgarh"].copy()
dictio10={ "Dhamtari  *":"Dhamtari",
       "Dakshin Bastar Dantewada":"Dantewada",
       "Janjgir - Champa":"Janjgir Champa",
       "Janjgir-champa":"Janjgir Champa",
       "Kanker  *":"North Bastar Kanker",
       "North Bastar Kanker":"Kanker",
       "Uttar Bastar Kanker":"Kanker",
       "Kawardha":"Kabirdham",
       "Kabeerdham":"Kabirdham",
       "Manendragarh–Chirmiri–Bharatpur":"Manendragarh",
       "ManendragarhChirmiriBharatpur":"Manendragarh",
       "Mohla-Manpur-Ambagarh Chouki":"Mohla Manpur",
       "Mohalla-Manpur-Ambagarh Chowki":"Mohla Manpur"

       }
df_Chattisgarh['district']=df_Chattisgarh['district'].str.strip()
df_Chattisgarh['district'] = df_Chattisgarh['district'].replace(dictio10)   
# print(df_Chattisgarh['district'].unique())     
# print(df_Chattisgarh['district'].nunique())


#Mizoram district correction
df_Mizoram=df[df['state']=="Mizoram"].copy()
dictio11={"Mammit":"Mamit",
       }
df_Mizoram['district']=df_Mizoram['district'].str.strip()
df_Mizoram['district'] = df_Mizoram['district'].replace(dictio11)   
# print(df_Mizoram['district'].unique())     
# print(df_Mizoram['district'].nunique())


#sikkim district correction
df_Sikkim=df[df['state']=="Sikkim"].copy()
dictio13={ "Namchi":"South Sikkim",
          "East":"East Sikkim",
          "North":"North Sikkim",
          "Mangan":"North Sikkim",
          "West":"West Sikkim",
          "South":"South Sikkim"
       }
df_Sikkim['district']=df_Sikkim['district'].str.strip()
df_Sikkim['district'] = df_Sikkim['district'].replace(dictio13)   
# print(df_Sikkim['district'].unique())     
# print(df_Sikkim['district'].nunique())


#Arunachala Pradesh
df_Arunachal=df[df['state']=="Arunachal Pradesh"].copy()

def clean_districtArunachal_name(district):
       if not isinstance(district, str):
              return "Unknown"

       district = district.strip().title()
       dictiacp={ "Leparada":"Lepa Rada",
                }
       return dictiacp.get(district,district)

df_Arunachal['district']=df_Arunachal['district'].apply(clean_districtArunachal_name)
# print(df_Arunachal['district'].unique())
# print(df_Arunachal['district'].nunique())


#West Bengal
df_WB =df[df['state'] == "West Bengal"].copy()

dict_WB = {
      "Coochbehar":"Cooch Behar",
      "Koch Bihar":"Cooch Behar",

      "Darjiling":"Darjeeling",

      "Dinajpur Uttar":"Uttar Dinajpur",
      "North Dinajpur":"Uttar Dinajpur",

      "Dinajpur Dakshin":"Dakshin Dinajpur",
      "South Dinajpur":"Dakshin Dinajpur",

      "24 Paraganas North":"North 24 Parganas",
      "South DumDum(M)":"North 24 Parganas",
      "North Twenty Four Parganas":"North 24 Parganas",
      "Naihati Anandabazar":"North 24 Parganas",

      "24 Paraganas South":"South 24 Parganas",
      "South  Twenty Four Parganas":"South 24 Parganas",
      "South Twenty Four Parganas":"South 24 Parganas",
      "South 24 parganas":"South 24 Parganas",
      "South 24 Pargana":"South 24 Parganas",
      "South 24 pargana":"South 24 Parganas",

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
      "East midnapore":"Purba Medinipur",
      "East Midnapur":"Purba Medinipur",
      "east midnapore":"Purba Medinipur",


      "Puruliya":"Purulia",

      "Bally Jagachha":"Howrah",
      "Domjur":"Howrah",
}
df_WB["district"] = df_WB["district"].str.strip()
df_WB["district"] = df_WB["district"].replace(dict_WB)
# print(df_WB['district'].unique())
# print(df_WB['district'].nunique())


# Jammu and Kashmir
# replace the kargil dist j&k to ladakh
df.loc[(df['district']=="Kargil") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"
df.loc[(df['district']=="Leh") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"
df.loc[(df['district']=="Leh (ladakh)") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"


df_JK = df[df['state'] == "Jammu and Kashmir"].copy()
#print(df_JK[df_JK["district"]=="?"])
df_JK = df_JK[df_JK["district"] != "?"].dropna()

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
    "udhampur": "Udhampur"
}
df_JK["district"] = df_JK["district"].str.strip()
df_JK["district"] = df_JK["district"].replace(dict_jk)
# print(df_JK['district'].unique())
# print(df_JK['district'].nunique())


# print("Unique Districts in Jammu and Kashmir after cleaning:")
#(np.sort(df_JK["district"].unique()))
# print(df_JK["district"].nunique())


#ladakh
df_Ladakh =df[df['state'] == "Ladakh"].copy()

dict_Ladakh = {
      "Leh (ladakh)":"Leh",
}
df_Ladakh["district"] = df_Ladakh["district"].str.strip()
df_Ladakh["district"] = df_Ladakh["district"].replace(dict_Ladakh)
# print(df_Ladakh['district'].unique())
# print(df_Ladakh['district'].nunique())



#Puducherry

#Replace Vilupuram from puducherry to tamil nadu
#print(df[df['district']=="Viluppuram"]['state'].unique())
# df.loc[(df['district']=="Viluppuram") & (df['state']=="Puducherry"), 'state'] = "Tamil Nadu"
# print(df[df['district']=="Vilupuram"]['state'].unique())

#Replace Cuddalore from puducherry to tamil nadu
#print(df[df['district']=="Cuddalore"]['state'].unique())
# df.loc[(df['district']=="Cuddalore") & (df['state']=="Puducherry"), 'state'] = "Tamil Nadu"
# print(df[df['district']=="Cuddalore"]['state'].unique())


df_Puducherry =df[df['state'] == "Puducherry"].copy()

dict_Puducherry = {
      "Pondicherry":"Puducherry",
}
df_Puducherry["district"] = df_Puducherry["district"].str.strip()
df_Puducherry["district"] = df_Puducherry["district"].replace(dict_Puducherry)
# print(df_Puducherry['district'].unique())
# print(df_Puducherry['district'].nunique())


#Lakshadweep
df_Lakshadweep =df[df['state'] == "Lakshadweep"]
# print(df_Lakshadweep['district'].unique())

#Dadra and Nagar Haveli and Daman and Diu
df_DNDU =df[df['state'] == "Dadra and Nagar Haveli and Daman and Diu"].copy()

dict_DNDU = {
      "Dadra And Nagar Haveli":"Dadra and Nagar Haveli",
      "Dadra & Nagar Haveli":"Dadra and Nagar Haveli",
}
df_DNDU['district']= df_DNDU["district"].str.strip()
df_DNDU["district"] = df_DNDU["district"].replace(dict_DNDU)
# print(df_DNDU['district'].unique())
# print(df_DNDU['district'].nunique())
# print(df_DNDU)


# Karnataka District 10
df_Karnataka=df[df['state'] == "Karnataka"].copy()
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
# print(df_Karnataka['district'].unique())
# print(df_Karnataka['district'].nunique())
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
# print(df_Gujarat['district'].unique())
# print(df_Gujarat['district'].nunique())
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
# print(df_Delhi['district'].unique())
# print(df_Delhi['district'].nunique())



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
# print(df_Jharkhand['district'].unique())
# print(df_Jharkhand['district'].nunique())

# Nagaland Districts-> is correct 14
df_Nagaland = df[df['state'] == "Nagaland"].copy()

df_Manipur = df[df['state'] == "Manipur"].copy()


#Chandigarh 07
df_Chandigarh =df[df['state'] == "Chandigarh"].copy()
# print(df_Chandigarh['district'].unique())
# print(df_Chandigarh['district'].nunique())


#Andaman and Nicobar Islands 08
df_Andaman =df[df['state'] == "Andaman and Nicobar Islands"].copy()
dict_Andaman = {
      "Nicobars":"Nicobar",
      "North And Middle Andaman":"North Middle Andaman",
      "Andamans":"North Middle Andaman",

}
df_Andaman["district"] = df_Andaman["district"].str.strip()
df_Andaman["district"] = df_Andaman["district"].replace(dict_Andaman)
# print(df_Andaman["district"].unique())
# print(df_Andaman["district"].nunique())


list_of_dfs = [df_AP,df_Arunachal,df_Assam,
               df_Bihar,df_Chattisgarh,df_Goa,df_Gujarat,
               df_HR,df_HP,df_Jharkhand,df_KL,df_Karnataka,
              df_MH,df_MP,df_Manipur,df_Mizoram,
              meghalaya_district,df_Nagaland,df_OD,
              df_PB,df_Rajasthan,df_Sikkim,df_TamilNadu,
              df_Telangana,df_TR,df_UP,df_Uttarakhand,df_WB,
              df_Delhi,df_Ladakh,df_Puducherry,df_DNDU,
              df_Chandigarh,df_Andaman,df_JK,df_Lakshadweep
              ]

df_cleaned = pd.concat(list_of_dfs, ignore_index=True)  
print("Shape of cleaned dataframe:", df_cleaned.shape)


df_cleaned.to_csv("cleaned_Demographic_data.csv", index=False)
