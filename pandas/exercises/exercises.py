import pandas as pd
import numpy as np

def proportion_of_education():

    df = pd.read_csv('./csvFiles/NISPUF17.csv')
    df=df['EDUC1']

    all_childrens=len(df)
    less_than_12=len(df[df == 1])/all_childrens
    high_school=len(df[df == 2])/all_childrens
    more_than_high_school_but_not_college=len(df[df == 3])/all_childrens
    college=len(df[df == 4])/all_childrens


    result ={
        "less than high school": less_than_12,
        "high school":high_school,
        "more than high school but not college":more_than_high_school_but_not_college,
        "college":college
    }

    return result

print(proportion_of_education())

# assert type(proportion_of_education())==type({}), "You must return a dictionary."
# assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
# assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
# assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
# assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
# assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."

def average_influenza_doses():
    df = pd.read_csv('./csvFiles/NISPUF17.csv')
    df=df[['CBF_01','P_NUMFLU']][ ( (df['CBF_01'] == 1) | (df['CBF_01'] == 2) ) & (df['P_NUMFLU']>=0) ]

 
    breast_feed=df[ df['CBF_01']==1 ]
    no_breast_feed=df[df['CBF_01']==2]

    len_breast_feed=len(breast_feed)
    len_no_breast_feed=len(no_breast_feed)

    average_for_breast= np.sum(breast_feed['P_NUMFLU'])/len_breast_feed
    average_for_no_breast= np.sum(no_breast_feed['P_NUMFLU'])/len_no_breast_feed

    result = (average_for_breast,average_for_no_breast)

    return result

print(average_influenza_doses())

# assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."

def chickenpox_by_sex():
    df = pd.read_csv('./csvFiles/NISPUF17.csv')
    df=df[['SEX','HAD_CPOX','P_NUMVRC']]

    male_CPOX = df[ (df['SEX'] == 1) & (df['HAD_CPOX']==1) & (df['P_NUMVRC']>0)]
    male_no_CPOX = df[ (df['SEX'] == 1) & (df['HAD_CPOX']==2) & (df['P_NUMVRC']>0)]

    female_CPOX = df[ (df['SEX'] == 2) & (df['HAD_CPOX']==1) & (df['P_NUMVRC']>0)]
    female2_no_CPOX = df[ (df['SEX'] == 2) & (df['HAD_CPOX']==2) & (df['P_NUMVRC']>0)]


    ratio_male= len(male_CPOX)/len(male_no_CPOX)
    ratio_female=len(female_CPOX)/len(female2_no_CPOX)

    result = {"male":ratio_male,
               "female":ratio_female}
    
    return result

print(chickenpox_by_sex())

# assert len(chickenpox_by_sex())==2, "Return a dictionary with two items, the first for males and the second for females."



def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    
    df = pd.read_csv('./csvFiles/NISPUF17.csv')
    df=df[['HAD_CPOX','P_NUMVRC']][ ( (df['HAD_CPOX'] == 1) | (df['HAD_CPOX'] == 2) ) & (df['P_NUMVRC']>0) ]
    had_chickenpox_column=df['HAD_CPOX']
    num_chickenpox_vaccine_column=df['P_NUMVRC']
    

    df=pd.DataFrame({"had_chickenpox_column":had_chickenpox_column,
                   "num_chickenpox_vaccine_column":num_chickenpox_vaccine_column})


    corr,  pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])
    # corr,  pval=df

   
    return corr

print(corr_chickenpox())
    



assert -1<=corr_chickenpox()<=1, "You must return a float number between -1.0 and 1.0."
