import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import os



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
               activity = st.selectbox(" ",submenu)
               if activity == "As a Doctor":
                  df=pd.read_csv(r'C:\Users\MAHIMA MANIGANDAN\Desktop\Hack\Datasett.csv')
                  table = df['Aadhar number'].values
                  st.write("Enter the patient's Aadhar number")
                  an = st.text_input("")
                  name = ["Edit the patient's details","View patient's record"]
                  for i in range (300):
                    if an == table[i]:
                      activity1 = st.selectbox(" ",name)
                      if activity1 == "Edit the patient's details":
                        add = st.text_input("")
                        if st.button("Save"):
                          st.write("The datails are saved successfully")
                          st.write(df[i]+add)
                      elif activity1 == "View patient's record":
                        nam = df['Name'].values
                        gender = df['Gender'].values
                        aanum = df['Aadhar number'].values
                        age = df['age'].values
                        anae = df['anaemia'].values
                        cret = df['creatinine_phosphokinase'].values
                        dia = df['diabetes'].values
                        ef = df['ejection_fraction'].values
                        hbp = df['high_blood_pressure'].values
                        pla = df['platelets'].values
                        sc = df['serum_creatinine'].values
                        ss = df['serum_sodium'].values
                        smo = df['smoking'].values
                        pr = df['Pulse Rate'].values
                        chol = df['chol'].values
                        tb = df['Total_Bilirubin'].values
                        db = df['Direct_Bilirubin'].values
                        ap = df['Alkaline_Phosphotase'].values
                        aa = df['Alamine_Aminotransferase'].values
                        tp = df['Total_Protiens'].values
                        albu = df['Albumin'].values
                        bp = df['Bp'].values
                        hemo = df['Hemo'].values
                        wbc = df['Wbcc'].values
                        rbc = df['Rbcc'].values
                        sod = df['Sod'].values
                        pot = df['Pot'].values
                        data = pd.DataFrame({'Patients details': ['Name', 'Gender', 'Aadhar number', 'Age', 'Anaemia','Creatinine_phosphokinase','Diabetes','Ejection_fraction','High_blood_pressure','Platelets','Serum_creatinine','Serum_sodium','Smoking','Pulse Rate','Cholesterol','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin','Blood pressure','Haemoglobin','Wbc Count','Rbc Count','Sodium','Pottasium'],'Medical records': [nam, gender, aanum, age, anae, cret, dia, ef, hbp, pla, sc, ss, smo, pr, chol, tb, db, ap, aa, tp, albu, bp, hemo, wbc, rbc, sod, pot]})
                        st.write(data)
                      break
                    else:
                      st.write("Enter a valid aadhar number")
                      break
                    i=i+1
                  
                    
                    
               elif activity == "As a Patient":
                  df=pd.read_csv(r'C:\Users\MAHIMA MANIGANDAN\Desktop\Hack\Datasett.csv')
                  table = df['Aadhar number'].values
                  st.write("Enter your Aadhar Number")
                  aan = st.text_input("")
                  for i in range (300):
                      if aan == table[i]:
                        nam = df['Name'].values
                        gender = df['Gender'].values
                        aanum = df['Aadhar number'].values
                        age = df['age'].values
                        anae = df['anaemia'].values
                        cret = df['creatinine_phosphokinase'].values
                        dia = df['diabetes'].values
                        ef = df['ejection_fraction'].values
                        hbp = df['high_blood_pressure'].values
                        pla = df['platelets'].values
                        sc = df['serum_creatinine'].values
                        ss = df['serum_sodium'].values
                        smo = df['smoking'].values
                        pr = df['Pulse Rate'].values
                        chol = df['chol'].values
                        tb = df['Total_Bilirubin'].values
                        db = df['Direct_Bilirubin'].values
                        ap = df['Alkaline_Phosphotase'].values
                        aa = df['Alamine_Aminotransferase'].values
                        tp = df['Total_Protiens'].values
                        albu = df['Albumin'].values
                        bp = df['Bp'].values
                        hemo = df['Hemo'].values
                        wbc = df['Wbcc'].values
                        rbc = df['Rbcc'].values
                        sod = df['Sod'].values
                        pot = df['Pot'].values
                        data = pd.DataFrame({'Patients details': ['Name', 'Gender', 'Aadhar number', 'Age', 'Anaemia','Creatinine_phosphokinase','Diabetes','Ejection_fraction','High_blood_pressure','Platelets','Serum_creatinine','Serum_sodium','Smoking','Pulse Rate','Cholesterol','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin','Blood pressure','Haemoglobin','Wbc Count','Rbc Count','Sodium','Pottasium'],'Medical records': [nam, gender, aanum, age, anae, cret, dia, ef, hbp, pla, sc, ss, smo, pr, chol, tb, db, ap, aa, tp, albu, bp, hemo, wbc, rbc, sod, pot]})
                        st.write(data)
                        break
                      elif aan != table[i]:
                        st.write("Enter a valid Aadhar number")
                        break
                      i=i+1
                  
                    
                    
                      

if __name__ == '__main__':
  main()