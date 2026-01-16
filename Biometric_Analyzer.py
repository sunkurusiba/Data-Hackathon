# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')
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
#print(df[df['district']=="Adilabad"]['state'].unique())
df.loc[(df['district']=="Adilabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Adilabad"]['state'].unique())

#Replace Hyderabad from andhra pradesh to Telangana
#print(df[df['district']=="Hyderabad"]['state'].unique())
df.loc[(df['district']=="Hyderabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Hyderabad"]['state'].unique())


#Replace Nizamabad from andhra pradesh to Telangana
#print(df[df['district']=="Nizamabad"]['state'].unique())              
df.loc[(df['district']=="Nizamabad") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Nizamabad"]['state'].unique())

#Replace khammam from andhra pradesh to Telangana
#print(df[df['district']=="Khammam"]['state'].unique())         
df.loc[(df['district']=="Khammam") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Khammam"]['state'].unique())

#Replace Karimnagar from andhra pradesh to Telangana
#print(df[df['district']=="Karimnagar"]['state'].unique())
df.loc[(df['district']=="Karimnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Karimnagar"]['state'].unique())
#print(df[df['district']=="Karim Nagar"]['state'].unique())
df.loc[(df['district']=="Karim Nagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Karim Nagar"]['state'].unique())

#Replace Rangareddy from andhra pradesh to Telangana
#print(df[df['district']=="Rangareddi"]['state'].unique())
df.loc[(df['district']=="Rangareddi") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Rangareddi"]['state'].unique())
#(df[df['district']=="Rangareddy"]['state'].unique())
df.loc[(df['district']=="Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Rangareddy"]['state'].unique())
#(df[df['district']=="K.v. Rangareddy"]['state'].unique())
df.loc[(df['district']=="K.v. Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="K.v. Rangareddy"]['state'].unique())
#(df[df['district']=="K.V. Rangareddy"]['state'].unique())
df.loc[(df['district']=="K.V. Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="K.V. Rangareddy"]['state'].unique())
#(df[df['district']=="rangareddi"]['state'].unique())
df.loc[(df['district']=="rangareddi") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="rangareddi"]['state'].unique())
#(df[df['district']=="K.V.Rangareddy"]['state'].unique())
df.loc[(df['district']=="K.V.Rangareddy") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="K.V.Rangareddy"]['state'].unique())


#Replace Medak from andhra pradesh to Telangana
#print(df[df['district']=="Medak"]['state'].unique())
df.loc[(df['district']=="Medak") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Medak"]['state'].unique())

#Replace Mahbubnagar from andhra pradesh to Telangana
#print(df[df['district']=="Mahbubnagar"]['state'].unique())
df.loc[(df['district']=="Mahbubnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Mahbubnagar"]['state'].unique())
#print(df[df['district']=="Mahabub Nagar"]['state'].unique())
df.loc[(df['district']=="Mahabub Nagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Mahabub Nagar"]['state'].unique())
#print(df[df['district']=="Mahabubnagar"]['state'].unique())
df.loc[(df['district']=="Mahabubnagar") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Mahabubnagar"]['state'].unique())

#Replace Nalgonda from andhra pradesh to Telangana
#print(df[df['district']=="Nalgonda"]['state'].unique())
df.loc[(df['district']=="Nalgonda") & (df['state']=="Andhra Pradesh"), 'state'] = "Telangana"
print(df[df['district']=="Nalgonda"]['state'].unique())





df_AP=df[df['state']=="Andhra Pradesh"].copy()
print(df_AP['district'].nunique())

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
                "Sri Potti Sriramulu Nellore":"Nellore"

                }
       return dicti2.get(district,district)

df_AP['district']=df_AP['district'].apply(clean_districtAP_name)
print(df_AP['district'].nunique())


#Telengana district correction
df_Telangana=df[df['state']=="Telangana"].copy()
#print(df_Telangana['district'].unique())
print(df_Telangana['district'].nunique())

dictio3= {
    "K.v. Rangareddy": "Rangareddy",
    "K.V.Rangareddy": "Rangareddy",
    "rangareddi": "Rangareddy",
    "Rangareddi": "Rangareddy",
    "Medchal-malkajgiri": "Medchal–Malkajgiri",
    "Medchal?malkajgiri": "Medchal–Malkajgiri",
    "Medchal−malkajgiri": "Medchal–Malkajgiri",
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
print("Unique Districts in Telangana after cleaning:")
print(df_Telangana['district'].nunique())
#print(np.sort(df_Telangana['district'].unique()))



#Tamil Nadu district correction
df_TamilNadu=df[df['state']=="Tamilnadu"].copy()
#print(df_TamilNadu['district'].unique())
print(df_TamilNadu['district'].nunique())
 
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
print("Unique Districts in Tamil Nadu after cleaning:")
print(df_TamilNadu['district'].nunique())
#print(np.sort(df_TamilNadu['district'].unique()))


#Rajasthan district correction
df_Rajasthan=df[df['state']=="Rajasthan"].copy()
#print(df_Rajasthan['district'].unique())
print(df_Rajasthan['district'].nunique())
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
    "Jhunjhunun":"Jhunjhunu"
    }
df_Rajasthan['district']=df_Rajasthan['district'].str.strip()
df_Rajasthan['district'] = df_Rajasthan['district'].replace(dictio5)
print("Unique Districts in Rajasthan after cleaning:")
print(df_Rajasthan['district'].nunique()) 
#print(np.sort(df_Rajasthan['district'].unique()))


#Assam district correction
df_Assam=df[df['state']=="Assam"].copy()
#print(df_Assam['district'].unique())     
print(df_Assam['district'].nunique())
dictio6={ "Darrang  *":"Dhubri",   
       "Dhibrugarh  *":"Dibrugarh",
       "Kokrajhar  *":"Kokrajhar",
       "Lakhimpur  *":"Lakhimpur",
       "Sibsagar":"Sivasagar",
       "Sibsagar  *":"Sivasagar",
       "Tinsukia  *":"Tinsukia"
       }
df_Assam['district']=df_Assam['district'].str.strip()
df_Assam['district'] = df_Assam['district'].replace(dictio6)   
print("Unique Districts in Assam after cleaning:")
print(df_Assam['district'].nunique()) 
#print(np.sort(df_Assam['district'].unique()))


#Goa district correction
df_Goa=df[df['state']=="Goa"].copy()      
#print(df_Goa['district'].unique())
print(df_Goa['district'].nunique())
dictio7={ "NORTH GOA":"North Goa",
       "SOUTH GOA":"South Goa",
       "Bardez":"North Goa",
       "Tiswadi":"North Goa",
       }      
df_Goa['district']=df_Goa['district'].str.strip()
df_Goa['district'] = df_Goa['district'].replace(dictio7)       
print("Unique Districts in Goa after cleaning:")
print(df_Goa['district'].nunique())       
#print(np.sort(df_Goa['district'].unique()))


#Uttarakhand district correction
df_Uttarakhand=df[df['state']=="Uttarakhand"].copy()
#print(df_Uttarakhand['district'].unique())
print(df_Uttarakhand['district'].nunique())
dictio8={ 
       "Hardwar":"Haridwar"
       }
df_Uttarakhand['district']=df_Uttarakhand['district'].str.strip()
df_Uttarakhand['district'] = df_Uttarakhand['district'].replace(dictio8)
print("Unique Districts in Uttarakhand after cleaning:")       
print(df_Uttarakhand['district'].nunique())
#print(np.sort(df_Uttarakhand['district'].unique()))


#Bihar district correction
df_Bihar=df[df['state']=="Bihar"].copy()         
#print(df_Bihar['district'].unique())

#Replace Aurangabad from bihar to Maharashtra
#print(df[df['district']=="Aurangabad"]['state'].unique())     
df.loc[(df['district']=="Aurangabad") & (df['state']=="Bihar"), 'state'] = "Maharashtra"
print(df[df['district']=="Aurangabad"]['state'].unique())


df_Bihar=df[df['state']=="Bihar"].copy()         
#print(df_Bihar['district'].unique())

print(df_Bihar['district'].nunique())     
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
print("Unique Districts in Bihar after cleaning:")
print(df_Bihar['district'].nunique())     
#print(np.sort(df_Bihar['district'].unique()))   


#Chattisgarh district correction
df_Chattisgarh=df[df['state']=="Chhattisgarh"].copy()
#print(df_Chattisgarh['district'].unique())     
print(df_Chattisgarh['district'].nunique())
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
print("Unique Districts in Chattisgarh after cleaning:")
print(df_Chattisgarh['district'].nunique())     
#print(np.sort(df_Chattisgarh['district'].unique()))


#Mizoram district correction
df_Mizoram=df[df['state']=="Mizoram"].copy()
#print(df_Mizoram['district'].unique())     
print(df_Mizoram['district'].nunique())
dictio11={"Mammit":"Mamit",
       }
df_Mizoram['district']=df_Mizoram['district'].str.strip()
df_Mizoram['district'] = df_Mizoram['district'].replace(dictio11)   
print("Unique Districts in Mizoram after cleaning:")
print(df_Mizoram['district'].nunique())     
#print(np.sort(df_Mizoram['district'].unique()))



#Tripura district correction
df_Tripura=df[df['state']=="Tripura"].copy()
#print(df_Tripura['district'].unique())     
print(df_Tripura['district'].nunique())   
dictio12={ "Dhalai  *":"Dhalai"
       }
df_Tripura['district']=df_Tripura['district'].str.strip()
df_Tripura['district'] = df_Tripura['district'].replace(dictio12)   
print("Unique Districts in Tripura after cleaning:")    
print(df_Tripura['district'].nunique())     
#print(np.sort(df_Tripura['district'].unique()))


#sikkim district correction
df_Sikkim=df[df['state']=="Sikkim"].copy()
#print(df_Sikkim['district'].unique())     
print(df_Sikkim['district'].nunique())
dictio13={ "Namchi":"South Sikkim",
          "East":"East Sikkim",
          "North":"North Sikkim",
          "West":"West Sikkim",
          "South":"South Sikkim"
       }
df_Sikkim['district']=df_Sikkim['district'].str.strip()
df_Sikkim['district'] = df_Sikkim['district'].replace(dictio13)   
print("Unique Districts in Sikkim after cleaning:")     
print(df_Sikkim['district'].nunique())
#print(np.sort(df_Sikkim['district'].unique()))


#Arunachala Pradesh
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
print("Unique Districts in Arunachal Pradesh after cleaning:")
#print(np.sort(df_Arunachal['district'].unique()))
print(df_Arunachal['district'].nunique())



#West Bengal
df_WB =df[df['state'] == "West Bengal"].copy()
# print(df_WB['district'].unique())
print(df_WB['district'].nunique())

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

      "24 Paraganas South":"South 24 Parganas",
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
print("Unique Districts in West Bengal after cleaning:")
#print(np.sort(df_WB["district"].unique()))
print(df_WB["district"].nunique())


# Jammu and Kashmir
# replace the kargil dist j&k to ladakh
df.loc[(df['district']=="Kargil") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"
df.loc[(df['district']=="Leh") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"
df.loc[(df['district']=="Leh (ladakh)") & (df['state']=="Jammu and Kashmir"), 'state'] = "Ladakh"


df_JK = df[df['state'] == "Jammu and Kashmir"].copy()
#print(df_JK[df_JK["district"]=="?"])
df_JK = df_JK[df_JK["district"] != "?"].dropna()
#print(df_JK['district'].unique())
print(df_JK['district'].nunique())

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


print("Unique Districts in Jammu and Kashmir after cleaning:")
#(np.sort(df_JK["district"].unique()))
print(df_JK["district"].nunique())


#ladakh
df_Ladakh =df[df['state'] == "Ladakh"].copy()
# print(df_Ladakh['district'].unique())
print(df_Ladakh['district'].nunique())

dict_Ladakh = {
      "Leh (ladakh)":"Leh",
}
df_Ladakh["district"] = df_Ladakh["district"].str.strip()
df_Ladakh["district"] = df_Ladakh["district"].replace(dict_Ladakh)

print("Unique Districts in Ladakh after cleaning:")
#print(df_Ladakh["district"].unique())
print(df_Ladakh["district"].nunique())


#Puducherry

#Replace Vilupuram from puducherry to tamil nadu
#print(df[df['district']=="Viluppuram"]['state'].unique())
df.loc[(df['district']=="Viluppuram") & (df['state']=="Puducherry"), 'state'] = "Tamilnadu"
print(df[df['district']=="Vilupuram"]['state'].unique())

#Replace Cuddalore from puducherry to tamil nadu
#print(df[df['district']=="Cuddalore"]['state'].unique())
df.loc[(df['district']=="Cuddalore") & (df['state']=="Puducherry"), 'state'] = "Tamilnadu"
print(df[df['district']=="Cuddalore"]['state'].unique())


df_Puducherry =df[df['state'] == "Puducherry"].copy()
# print(df_Puducherry['district'].unique())
print(df_Puducherry['district'].nunique())

dict_Puducherry = {
      "Pondicherry":"Puducherry",
}
df_Puducherry["district"] = df_Puducherry["district"].str.strip()
df_Puducherry["district"] = df_Puducherry["district"].replace(dict_Puducherry)
print("Unique Districts in Puducherry after cleaning:")
#print(df_Puducherry["district"].unique())
print(df_Puducherry["district"].nunique())


#Lakshadweep
df_Lakshadweep =df[df['state'] == "Lakshadweep"]
print(df_Lakshadweep['district'].unique())

#Dadra and Nagar Haveli and Daman and Diu
df_DNDU =df[df['state'] == "Dadra and Nagar Haveli and Daman and Diu"]
# print(df_DNDU['district'].unique())
print(df_DNDU['district'].nunique())

dict_DNDU = {
      "Dadra And Nagar Haveli":"Dadra and Nagar Haveli",
      "Dadra & Nagar Haveli":"Dadra and Nagar Haveli",
}
df_DNDU["district"] = df_DNDU["district"].str.strip()
df_DNDU["district"] = df_DNDU["district"].replace(dict_DNDU)
print("Unique Districts in Dadra and Nagar Haveli and Daman and Diu after cleaning:")
print(df_DNDU["district"].unique())
print(df_DNDU["district"].nunique())


# #Chandigarh
# # replace the Rupnagar dist chandigarh to punjab
# df.loc[(df['district']=="Rupnagar") & (df['state']=="Chandigarh"), 'state'] = "Punjab"
# df_Chandigarh =df[df['state'] == "Chandigarh"]
# # print(df_Chandigarh['district'].unique())
# # print(df_Chandigarh['district'].nunique())


# #Andaman and Nicobar Islands
# df_Andaman =df[df['state'] == "Andaman and Nicobar Islands"]
# # print(df_Andaman['district'].unique())
# # print(df_Andaman['district'].nunique())

# dict_Andaman = {
#       "Nicobars":"Nicobar",
#       "North And Middle Andaman":"North Middle Andaman",
#       "Andamans":"North Middle Andaman",

# }
# df_Andaman["district"] = df_Andaman["district"].str.strip()
# df_Andaman["district"] = df_Andaman["district"].replace(dict_Andaman)
# # print(df_Andaman["district"].unique())
# # print(df_Andaman["district"].nunique())