import ssaw, os
from dotenv import load_dotenv

# PyDantic
# https://github.com/vavalomi/ssaw/issues/4
from ssaw.models import Group
Group.model_rebuild()

load_dotenv()

"""

steps:

1 pip install ssaw

2 pip install pydantic==1.10.11

or:

1 pip install -r requirements.txt

"""

# parameters, changed them to match yours
# change .env (clone it from .env.dummy)

# First, initialize connection with the server
client = ssaw.Client(
    os.getenv("DB_HOST"), api_user=os.getenv("DB_USER"), api_password=os.getenv("DB_PWRD"), workspace=os.getenv("SS_WORK")
)


# Get list of questionnaires
for q in ssaw.QuestionnairesApi(client).get_list():
    print(q.title)
    print(q.id)

    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, q.id)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    print("folder:", final_directory)
    # Download the latest exported data in Tabular format
    filename = ssaw.ExportApi(client).get(
        export_type="Tabular", # Format of the export data: Tabular, STATA, SPSS, Binary, DDI, Paradata
        export_path=final_directory, 
        questionnaire_identity=q.id,
        interview_status='All', # What interviews to include in the export
        generate=True #  generate new export if no existing result setisfies the specified filters
    )
