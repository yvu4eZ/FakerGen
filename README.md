# FakerGen
FakerGen is a Python script I wrote that allows you to quickly and easily generate fake data. I initialy created the script to anonymize data taken from a production service but the script also has other use cases like stress testing and database seeding. 

## Installation
As a requirement, the Faker library needs to be installed.
```bash
pip install Faker
```

## Usage
To use the script, you will need to:
1. Input a locale IE ('en_CA')
2. Input the number of records in fake_date()
3. Execute the python script

The fake data will then be generated onto a csv file in the local directory.

## Ideas for next steps
- Execute the script via command line while passing the locale, number of records and output file as arguments
- Ability to select what kind of fake data would be included in the export
