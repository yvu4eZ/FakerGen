from faker import Faker
import pandas as Panda
import os
from datetime import datetime

Fake = Faker('en_CA')

def input_data(x):
    Df = Panda.DataFrame()
    for _ in range(0, x):
        Df.loc[_,'uuid']= Fake.unique.uuid4(cast_to = None)
        Df.loc[_,'type']= Fake.random_element(elements = ('subscriber', 'customer'))
        Df.loc[_,'country']= Fake.current_country_code()
        Df.loc[_,'first_name']= Fake.first_name()
        Df.loc[_,'last_name']= Fake.last_name()
        Df.loc[_,'email']= Fake.unique.ascii_company_email()
        Df.loc[_,'phone']= Fake.unique.phone_number()
        Df.loc[_,'job']= Fake.job()
        Df.loc[_,'company']= Fake.unique.company()
        Df.loc[_,'last_login_ip']= Fake.unique.ipv4()
        Df.loc[_,'last_login']= Fake.date_time_between(start_date = "-1y", end_date = "now")
        Df.loc[_,'created']= Fake.date_time_between(start_date = "-5y", end_date = "-1y")
        Df.loc[_,'modified']= Fake.date_time_between(start_date = "-3y", end_date = "-1y")
    return Df

Df = input_data(10)

Df.to_csv(os.getcwd() + "/output_" + datetime.now().strftime("%Y-%m-%dT%H_%M_%S.%fZ") + '.csv')