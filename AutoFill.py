# Autofill Google Form

import requests
import datetime
import time
import sys

# URL to the form you want to fill. formResponse should be used instead of viewform
url = 'https://docs.google.com/forms/d/e/1FAIpQLScDT-xtsF9eViroPOgaSkjayQTrVwk8H8An-i2nH5JbX8F-PQ/formResponse'


def get_values():
    """It returns a list of different form data to be submitted by send_attendance method.
    subjects_time is a dictionary with Day as keys and time and subjects in a list as values.
    value_list is a list of lectures' subject and time of current_day."""

    values_list = []
    now = datetime.datetime.now()
    day_name = now.strftime("%A")

    subjects_time = {
        "Monday": [["10", "30", "AJ(HC)"], ["11", "30", "DCDR(PC)"], ["1", "00", "WT(AM)"], ["2", "00", "SE(KD)"]],
        "Tuesday": [["11", "30", "SE(KD)"], ["1", "00", "AJ(HC)"]],
        "Wednesday": [["11", "30", ".NET(PC)"], ["1", "00", "SE(KD)"], ["2", "00", ".NET(PC)"]],
        "Thursday": [["10", "30", "WT(AM)"], ["11", "30", "DCDR(PC)"], ["1", "00", "AJ(HC)"]],
        "Friday": [["10", "30", "AJ(HC)"], ["11", "30", ".NET(PC)"], ["1", "00", "SE(KD)"], ["2", "00", ".NET(PC)"]],
    }

    date = str(now).split('-')

    for i in subjects_time[day_name]:
        '''keys are the value of 'name' element of the '''
        values = {
            # Email Address
            "emailAddress": str(sys.argv[1]),
            # Enrollment Number
            "entry.33987362": str(sys.argv[2]),
            # Course
            "entry.363926033": "BE",
            # Branch
            "entry.733518766": "IT",
            # Semester
            "entry.114626584": "Sem-6",
            # Subject
            "entry.609979780": i[2],
            # Date
            "entry.1916623197_year": date[0],
            "entry.1916623197_month": date[1],
            "entry.1916623197_day": date[2][0:2],
            # Time
            "entry.125609755_hour": i[0],
            "entry.125609755_minute": i[1],
        }

        values_list.append(values)

    return values_list


def send_attendance(url, data):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the form iteratively."""

    for d in data:
        try:
            requests.post(url, data=d)
            print("Form Submitted.")
            time.sleep(10)
        except:
            print("Error Occured!")


final_data = get_values()

send_attendance(url, final_data)
