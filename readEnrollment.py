import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
enroll_1 = pd.read_csv("api_data_aadhar_enrolment_0_500000.csv")
enroll_2 = pd.read_csv("api_data_aadhar_enrolment_500000_1000000.csv")
enroll_3 = pd.read_csv("api_data_aadhar_enrolment_1000000_1006029.csv")
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
print("Unique States after cleaning:")
print(df['state'].unique())
print(f"no. of states is {df['state'].nunique()}")

#Wor of district

# get unique districts of Meghalaya
# print(df[df["state"]== "Meghalaya"]["district"].unique())

# Meghalaya District->
# replace kamrup as state of Meghalaya to Assam
# print(df[df['district']=="Kamrup"]['state'].unique())
df.loc[(df['district']=="Kamrup") & (df['state']=="Meghalaya"), 'state'] = "Assam"
# print(df[df['district']=="kamrup"]['state'].unique())
# changing the jaintia hills to west jaintia hills
df["district"] = df["district"].replace(
    "Jaintia Hills", "West Jaintia Hills"
)
meghalaya_district=df[df["state"]== "Meghalaya"]
print(f"no. of districts in Meghalaya is {meghalaya_district["district"].nunique()}")

# Karnataka District->
# print(df[df["state"]== "Karnataka"]["district"].unique())
df_Karnataka = df[df['state'] == "Karnataka"].copy()
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
print(f"no. of districts in karnataka is {df_Karnataka["district"].nunique()}")

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
print(f"no. of districts in Gujarat is {df_Gujarat['district'].nunique()}")

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
print(f"no. of districts in Delhi is {df_Delhi['district'].nunique()}")

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
print(f"no. of districts in Jharakhand is {df_Jharkhand['district'].nunique()}")

# Nagaland Districts-> is correct
# print(df[df["state"]== "Nagaland"]["district"].unique())
# df_Nagaland = df[df['state'] == "Nagaland"].copy()
# df_Nagaland =

# Manipur Districts-> it is correct
# print(df[df["state"]== "Manipur"]["district"].unique())
# df_Manipur = df[df['state'] == "Manipur"].copy()

# Andhra Pradesh Districts->
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
AndhraPradesh_dict = {
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
df_AndhraPradesh['district'] = df_AndhraPradesh['district'].replace(AndhraPradesh_dict)
print(f"no. of districts in Andhra Pradesh is {df_AndhraPradesh['district'].nunique()}")

# Telengana Districts->
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
print(f"no. of districts in Andhra Pradesh is {df_Telangana['district'].nunique()}")

# Madhya Pradesh Districts->
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
print(f"no. of districts in Madhya Pradesh is {df_MadhyaPradesh['district'].nunique()}")

# Tamil Nadu Districts->
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
print(f"no. of districts in Tamil Nadu is {df_TamilNadu['district'].nunique()}")
# print(df[df["state"]== "Rajasthan"]["district"].nunique())

# Maharashtra Districts->
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

# Rajasthan Districts->
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

# Haryana District->
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
