import ssaw,os

"""

steps:

1 pip install ssaw

2 pip install pydantic==1.10.11

or:

1 pip install -r requirements.txt

"""

# parameters
host='http://127.0.0.1:9700'
api_user='apiuser1'
api_password='Abcde12345'
workspace='primary'

# First, initialize connection with the server
client = ssaw.Client(host, api_user=api_user, api_password=api_password, workspace=workspace)


# Get list of questionnaires
for q in ssaw.QuestionnairesApi(client).get_list():
    print(q.title)
    print(q.id)

    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, q.id)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    
    print("folder:",final_directory)
    # Download the latest exported data in Tabular format
    filename = ssaw.ExportApi(client).get(export_type="Tabular",export_path=final_directory,
    questionnaire_identity=q.id)

