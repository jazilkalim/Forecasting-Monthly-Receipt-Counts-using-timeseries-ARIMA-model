import pickle
from datetime import date
from dateutil.relativedelta import relativedelta
from custom_arima import custom_ARIMA
import sys
import os

current_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

# Change the current working directory to the script's directory
os.chdir(current_directory)
#print(os.getcwd())
#print(os.getcwd())
#print(os.getcwd())

def load_saved_artifacts():
    print("Loading saved artifiacts")
    global _model
    with open('model.pickle','rb') as f:
        _model=pickle.load(f)
    print("Loading saved artificats - DONE")



def get_prediction(year,month):
    date1 = date(2021, 12, 1)
    prediction_year = year
    prediction_month = month
    date2 = date(prediction_year, prediction_month, 1)

    years_difference = prediction_year - date1.year
    months_difference = years_difference * 12 + (date2.month - date1.month)

    #months_difference = relativedelta(date2, date1).months

    prediction_values=_model.predict(months_difference)

    numberofdays=days_in_month(prediction_year)[prediction_month]
    final_answer=int(prediction_values[-1]*numberofdays)

    return final_answer

def days_in_month(year):
    # Dictionary with month and the number of days
    days_in_month_dict = {
        1: 31,  # January
        2: 28,  # February (default)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31, # October
        11: 30, # November
        12: 31  # December
    }

    # Function to check leap year
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # Adjust February for leap years
    if is_leap_year(year):
        days_in_month_dict[2] = 29

    return days_in_month_dict

if __name__ == '__main__':
    print(os.getcwd())
    load_saved_artifacts()
    print(get_prediction(2022,12))
