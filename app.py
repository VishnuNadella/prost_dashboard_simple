from pymongo import *
import streamlit as st


pwd = st.secrets["pwd"]

connection_str = f"mongodb+srv://application:{pwd}@prostcluster.bs9tpgw.mongodb.net/?retryWrites=true&w=majority"

cluster = MongoClient(connection_str)
print(cluster.database_names())
db = cluster["prostDB"]
mn_evnts = db.collection_names()
print(mn_evnts)
collection = db["members"]


Total_count = len([i for i in collection.find({})])
Attended_count = len([i for i in collection.find({"attended": True})])
Remaining_count = len([i for i in collection.find({"attended": False})])


cnt = len([i for i in collection.find({"qr.uid1.attended": False})])
print("Total_count: ", cnt)

for i in range(10):
    key_str = f"qr.uid{i + 1}.attended"
    cnt = len([i for i in collection.find({key_str: False})])
    Remaining_count += cnt

print(Attended_count, Remaining_count)




st.title("PROST")

atten_cnt_str = f"Attended Count:  {Attended_count}"
remin_cnt_str = f"Pending Count:  {Remaining_count}"
st.header(atten_cnt_str)
st.header(remin_cnt_str)


email = st.text_input("Enter Email ID to search:")
req_det = collection.find_one({"email": email})

if req_det is not None and email != "":
    st.write(req_det)
elif req_det is None and email != "":
    st.error("No data has been found with this Email ID")



# phone_no = input("Enter Phone number to search: ")
# print(req_name)
