import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import os
import sqlite3
from sqlite3 import Connection
URI_SQLITE_DB = "database.db"


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

def main():
    st.image('https://www.freelogodesign.org/file/app/client/thumb/f5c1e3f9-b1c6-4733-884f-1a447312940a_200x200.png?1600360895791')
    st.title("HISTODOOR")
    menu = ["Home","Signup","Login"]
    submenu = ["As a Doctor","As a Patient"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
         st.subheader("Home")
         st.markdown(f'<div class="markdown-text-container stText" style="width: 698px;"><div style="font-size: medium;"> </div>',unsafe_allow_html=True)
         st.text("Dude..!! Here is your medical history..!! ")
    elif choice == "Signup":
         st.text("Username")
         new_username = st.text_input("")
         st.text("Password")
         new_password = st.text_input(" ",type='password')
         st.text("Confirm Password")
         confirm_password = st.text_input("  ", type='password')
         if new_password == confirm_password:
            st.success("Password Confirmed")
         else:
            st.warning("Passwords not the same")
         if st.button("Submit"):
            st.success("Your account was created successfully")
            st.info("Login to get started")
            pass
    elif choice == "Login":
         username = st.sidebar.text_input("Username")
         password = st.sidebar.text_input("Password",type='password')
         if st.sidebar.checkbox("Login"):
            if password == "12345":
               st.subheader("Welcome {}".format(username))
               st.text("Activity")
               activity = st.selectbox("",submenu)
               if activity == "As a Doctor":
                  df=pd.read_csv(r'C:\Users\MAHIMA MANIGANDAN\Desktop\Hack\Datasett.csv')
                  table = df['Aadhar number'].values
                  an = 530118574135
                  name = ["Edit the patient's details","View patient's record"]
                    
            
                  if an == 530118574135:
                    st.write("Enter the patient's Aadhar Number")
                    num = st.text_input("")
                    activity1 = st.selectbox("",name)
                    if activity1 == "Edit the patient's details":
                        add = st.text_input(" ")
                        if st.button("Save"):
                          st.write("The details are saved successfully")
                          
                  
                          def init_db(conn: Connection):
                            conn = get_connection(URI_SQLITE_DB)
                            init_db(conn)

                  
                            display_data(conn)
                            conn.execute(
                              """CREATE TABLE IF NOT EXISTS test
                                 (
                                 INPUT1 STRING,
                                 );"""
                            ) 
                            conn.execute(f"INSERT INTO Datasett (INPUT) VALUES ({input1})")
                            conn.commit()
                            
                          def display_data(conn: Connection):
                            if st.checkbox("View newly added datails"):
                              st.dataframe(get_data(conn))
                              st.write(df[1])
                              st.wrie(input1)

                    elif activity1 == "View patient's record":
                        nam = "Akhilesh"
                        gender = "Male"
                        aanum = "530118574135"
                        age = "62"
                        anae = "No"
                        cret = "231"
                        dia = "No"
                        ef = "25"
                        hbp = "Yes"
                        pla = "253000"
                        sc = "0.9"
                        ss = "140"
                        smo = "Yes"
                        pr = "10"
                        chol = "275"
                        tb = "2.7"
                        db = "1.3"
                        ap = "260"
                        aa = "31"
                        aaa = "56"
                        tp = "7.4"
                        albu = "3"
                        bp = "70"
                        hemo = "10.8"
                        wbc = "4500"
                        rbc = "3.8"
                        sod = "131"
                        pot = "4.2"
                        data = pd.DataFrame({'Medical records': ['Name', 'Gender', 'Aadhar number', 'Age', 'Anaemia','Creatinine_phosphokinase','Diabetes','Ejection_fraction','High_blood_pressure','Platelets','Serum_creatinine','Serum_sodium','Smoking','Pulse Rate','Cholesterol','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin','Blood pressure','Haemoglobin','Wbc Count','Rbc Count','Sodium','Pottasium'],'Values': [nam, gender, aanum, age, anae, cret, dia, ef, hbp, pla, sc, ss, smo, pr, chol, tb, db, ap, aa, aaa, tp, albu, bp, hemo, wbc, rbc, sod, pot]})
                        st.header("History")
                        st.write(data)
                      
                  else:
                    st.write("Enter valid aadhar number and try again")
                      
                  
                  
                    
                    
               elif activity == "As a Patient":
                  df=pd.read_csv(r'C:\Users\MAHIMA MANIGANDAN\Desktop\Hack\Datasett.csv')
                  table = df['Aadhar number'].values
                  aan = 530118574135
                  
                  
                  if aan == 530118574135:
                      st.write("Enter your Aadhar Number")
                      aan = st.text_input("")
                      if st.button("Submit"):
                         
                  
                        nam = "Akhilesh"
                        gender = "Male"
                        aanum = "530118574135"
                        age = "62"
                        anae = "No"
                        cret = "231"
                        dia = "No"
                        ef = "25"
                        hbp = "Yes"
                        pla = "253000"
                        sc = "0.9"
                        ss = "140"
                        smo = "Yes"
                        pr = "10"
                        chol = "275"
                        tb = "2.7"
                        db = "1.3"
                        ap = "260"
                        aa = "31"
                        aaa = "56"
                        tp = "7.4"
                        albu = "3"
                        bp = "70"
                        hemo = "10.8"
                        wbc = "4500"
                        rbc = "3.8"
                        sod = "131"
                        pot = "4.2"
                        weight = "68"
                        data = pd.DataFrame({'Medical records': ['Name', 'Gender', 'Aadhar number', 'Age', 'Anaemia','Creatinine_phosphokinase','Diabetes','Ejection_fraction','High_blood_pressure','Platelets','Serum_creatinine','Serum_sodium','Smoking','Pulse Rate','Cholesterol','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin','Blood pressure','Haemoglobin','Wbc Count','Rbc Count','Sodium','Pottasium','Weight'],'Values': [nam, gender, aanum, age, anae, cret, dia, ef, hbp, pla, sc, ss, smo, pr, chol, tb, db, ap, aa, aaa, tp, albu, bp, hemo, wbc, rbc, sod, pot, weight]})
                        st.header("History")
                        st.write(data)
                       
                     
                        
                    


def get_data(conn: Connection):
    df = pd.read_sql("SELECT * FROM Datasett", con=conn)
    return df

@st.cache(hash_funcs={Connection: id})
def get_connection(path: str):
    """Put the connection in cache to reuse if path does not change between Streamlit reruns.
    NB : https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa
    """
    return sqlite3.connect(path, check_same_thread=False)     
                    
                    
                      

if __name__ == '__main__':
  main()
  