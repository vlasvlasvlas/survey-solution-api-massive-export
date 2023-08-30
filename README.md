# survey-solution-api-massive-export
 
Just a simple masive export tabular data download for Survey Solutions using an API User (https://github.com/surveysolutions/surveysolutions).

It uses ssaw library : https://github.com/vavalomi/ssaw

## Reqs:

- Python3

- ssaw

- must install pydantic==1.10.11 or it will not work (issue opened at ssaw) 

- or you can just pip install -r requirements!

- clone .env.dummy -> .env & fill with your connection strings (must have an API user created at SSolution)

## Run

Python ./export_masivo_ssolution.py

## Result

This script will create results per Questionnaire created at SSolution server, using QuestionnairesApi (https://ssaw.readthedocs.io/en/latest/)
