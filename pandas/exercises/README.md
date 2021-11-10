
## First exercise
Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

This function should return a dictionary in the form of (use the correct numbers, do not round numbers):

    {"less than high school":0.2,
    "high school":0.4,
    "more than high school but not college":0.2,
    "college":0.2}

## Second exercise
Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

This function should return a tuple in the form (use the correct numbers:

(2.5, 0.1)

## Third exercise
It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.

This function should return a dictionary in the form of (use the correct numbers):

    {"male":0.2,
    "female":0.4}
Note: To aid in verification, the chickenpox_by_sex()['female'] value the autograder is looking for starts with the digits 0.0077.
## Fourth exercise
A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease. In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).

Some notes on interpreting the answer. If the had_chickenpox_column is either 1 (for yes) or 2 for no, and that the num_chickenpox_vaccine_column is the number of doses a child has been given of the varicella vaccine, then a positive correlation (e.g. corr > 0) would mean that an increase in had_chickenpox_column (which means more no's) would mean an increase in the num_chickenpox_vaccine_column (which means more doses of vaccine). If corr < 0 then there is a negative correlation, indicating that having had chickenpox is related to an increase in the number of vaccine doses. Also, pval refers to the probability the relationship observed is significant. In this case pval should be very very small (will end in e-18 indicating a very small number), which means the result unlikely to be by chance.

#### For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this assignment is in csvFiles/NISPUF17.csv. A data users guide for this, which you'll need to map the variables in the data to the questions being asked, is available at csvFiles/NIS-PUF17-DUG.pdf.