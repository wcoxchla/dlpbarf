# DLP Batch Automatic Record Faker

import csv
import names
import random
import datetime
import string
from faker import Faker

fake = Faker()
print(fake.credit_card_number(card_type=None))

barf = []
barfcount = 0
print('Welcome to the DLP (Data Loss Prevention) B.A.R.F - Batch Automatic Record Faker')
print('#############################')

# Import wordlists for datapoints
conditionslist = open("conditionslistv2.txt", "r").read().splitlines()
cancertestslist = open("cancertestslist.txt", "r").read().splitlines()
stdtestslist = open("stdtestslist.txt", "r").read().splitlines()
drugslist = open("drugslist.txt", "r").read().splitlines()

# Get configuration counts
barfcount = int(input('How many barfs we talkin here? '))
datapointcount= int(input('Oh and how many datapoints per record?'))

# Memes
if barfcount>=100 :
    print("Dang that's a lot of barfs, hold my beer...")
else: print("Easy. Hold tight.")

# Define functions for datapoints generation
def dob():
    fake = Faker()
    #fake.date_between(start_date='today', end_date='+30y')
    # datetime.date(2025, 3, 12)
    #dob = fake.date_time_between(start_date='-15y', end_date='now')
    dob = fake.date_between(start_date='-15y', end_date='now')
    # datetime.datetime(2007, 2, 28, 11, 28, 16)


    # Or if you need a more specific date boundaries, provide the start
    # and end dates explicitly.
    #start_date = datetime.date(year=2015, month=1, day=1)
    #fake.date_between(start_date=start_date, end_date='+30y')
    return dob

def condition (datapointcount):
    conditions =''
    for i in range(datapointcount):
        conditions += conditionslist[random.randint(0, len(conditionslist)-1)] + ' '
    return conditions

def stdtests (datapointcount):
    stdtests =''
    for i in range(datapointcount):
        stdtests += stdtestslist[random.randint(0, len(stdtestslist)-1)] + ' '
    return stdtests

def cancertests (datapointcount):
    cancertests =''
    for i in range(datapointcount):
        cancertests += cancertestslist[random.randint(0, len(cancertestslist)-1)] + ' '
    return cancertests

def ssn():
    ssn = fake.ssn(taxpayer_identification_number_type="SSN")
    return ssn

def creditcard():
    creditcard = fake.credit_card_number(card_type=None)
    return creditcard

def dlnumber():
    dlnumber = random.choice(string.ascii_letters) + str(random.randint(1000000,9999999))
    return dlnumber

def drugs():
    drugs =''
    for i in range(datapointcount):
        drugs += drugslist[random.randint(0, len(drugslist)-1)] + ' '
    return drugs

def mrn():
    mrn = 'MRN: ' + str(random.randint(1000000,9999999))
    return mrn

# Generate names
for i in range(barfcount):
    barf.append([names.get_full_name(),dob(),creditcard(),ssn(), dlnumber(), mrn(), drugs(), condition(datapointcount), stdtests(datapointcount), cancertests(datapointcount)])

# Debug


# Output
print('Generated ' + str(len(barf)) + ' fake patient records with ' + str(datapointcount) + ' datapoints each record.')
print('Exporting fake data to \"Fake MRN Data Count ' + str(barfcount) + '.csv\"')

# Save to CSV
with open('Fake MRN Data Count ' + str(barfcount) + '.csv ', 'w', newline='') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['Fake record Name', 'Date of birth', 'Fake Credit Card', 'SSN', 'Fake Driver\'s License Number', 'Fake MRN','Prescriptions and drugs', 'Condition Notes','STD Tests','Cancer Tests'])
    for row in barf:
        csv_out.writerow(row)
