import pandas as pd
import numpy as np
import csv
import email.mime.text
# Read in the csv
df = pd.read_csv("./Regional_Mil_and_Civ_Review.csv")
who_df = pd.read_csv("./dist_foa_coco.csv")
# convert '-' to to zeros on 'LAST_IDP_UPDATED_MTHS' column to fix "ValueError: invalid literal for int() with base 10: '-'"
## change the special characters ('-') to '0' (https://www.statology.org/pandas-remove-special-characters/)
df['LAST_IDP_UPDATED_MTHS'] = df['LAST_IDP_UPDATED_MTHS'].str.replace('\W', '0', regex=True)
## change the NaN values to zero
df['LAST_IDP_UPDATED_MTHS'] = df['LAST_IDP_UPDATED_MTHS'].fillna(0)
# df['LAST_IDP_UPDATED_MTHS'] = df['LAST_IDP_UPDATED_MTHS'].astype(float)

# convert the LAST_IDP_UPDATED_MTHS column to int64 (https://sparkbyexamples.com/pandas/pandas-convert-column-to-int/)
df['LAST_IDP_UPDATED_MTHS'] = df['LAST_IDP_UPDATED_MTHS'].apply(np.int64)
# Drop the columns nobody needs to see
df = df.drop(columns=['PERSON_ID','PERSON_NAME','REGION','COMPO','COMMAND','UIC','UIC_STATE','ORG_DESC','APT','HI_DEGREE','LVL_DESC','AGE','SEX','YRS_OF_SERVICE','WF_STATUS','AFA','ACL','CERT_BELOW_POSITION','NOT_CERTIFIED','WAIVER_TYPE','WAIVER_GRANTED_DATE','WAIVER_EXPIRATION_DATE'])

# check the data types to figure out why the 'LAST_IDP_UPDATED_MTHS' won't work in idp_fail
print(df.dtypes)

def office_report(dist,foa):
    # Pull out just the 1102s and put them in a dataframe
    clp_fail = df[(df['OCC_SERIES'] == '1102')& (df['CLP'] <40)]
    no_Eth = df[(df['OCC_SERIES'] == '1102')&(df['ETHICS_TRAINING_COMPLETED_FY23'] == '-')]
    idp_fail = df[(df['OCC_SERIES'] == '1102')& (df['LAST_IDP_UPDATED_MTHS'] <=6)]

    # Pull out the starting characters of ORG_STRUCTURE_CODE
    _clp_fail = clp_fail[(clp_fail.ORG_STRUCTURE_CODE.str.startswith(foa))]
    _noEth = no_Eth[(no_Eth.ORG_STRUCTURE_CODE.str.startswith(foa))]
    _idp_fail = idp_fail[(idp_fail.ORG_STRUCTURE_CODE.str.startswith(foa))]
    # Write that to it's own file
    _clp_fail.to_csv(f"{dist}_clp_fail.csv",index = False)
    _noEth.to_csv(f"{dist}_noEth.csv",index = False)
    _idp_fail.to_csv(f"{dist}_idp_fail.csv",index=False)
    return print(dist,foa)

print(office_report('nwk','G5P'))
print(office_report('nab','E1P'))
print(office_report('sam','K5P'))
