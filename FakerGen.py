from faker import Faker
import pandas as Panda
import os
from datetime import datetime

Fake = Faker('en_CA')

def fake_data(x):
    FakerDf = Panda.DataFrame()
    for _ in range(0, x):
        FakerDf.loc[_,'uuid']= Fake.unique.uuid4(cast_to = None)
        FakerDf.loc[_,'type']= Fake.random_element(elements = ('subscriber', 'customer'))
        FakerDf.loc[_,'country']= Fake.current_country_code()
        FakerDf.loc[_,'first_name']= Fake.first_name()
        FakerDf.loc[_,'last_name']= Fake.last_name()
        FakerDf.loc[_,'email']= Fake.unique.ascii_company_email()
        FakerDf.loc[_,'phone']= Fake.unique.phone_number()
        FakerDf.loc[_,'address']= Fake.address()
        FakerDf.loc[_,'job']= Fake.job()
        FakerDf.loc[_,'company']= Fake.unique.company()
        FakerDf.loc[_,'last_login_ip']= Fake.unique.ipv4()
        FakerDf.loc[_,'last_login']= Fake.date_time_between(start_date = "-1y", end_date = "now")
        FakerDf.loc[_,'created']= Fake.date_time_between(start_date = "-5y", end_date = "-1y")
        FakerDf.loc[_,'modified']= Fake.date_time_between(start_date = "-3y", end_date = "-1y")
    return FakerDf

FakerDf = fake_data(1000)

FakerDf.to_csv(os.getcwd() + "/output_" + datetime.now().strftime("%Y-%m-%dT%H_%M_%S.%fZ") + '.csv', index = False)
