import json 
import requests
import ast

file = open('gg2013.json')
tweets = json.load(file)
file.close()

golden_globes_2013_url = "https://www.imdb.com/event/ev0000292/2013/1/?ref_=gg_eh"
golden_globes_2015_url = "https://www.imdb.com/event/ev0000292/2015/1/?ref_=ev_eh"

golden_globes_2013_html = requests.get(golden_globes_2013_url).text

start_index_of_golden_globes_2013_info = golden_globes_2013_html.index("IMDbReactWidgets.NomineesWidget.push") + len("IMDbReactWidgets.NomineesWidget.push") + 19
end_index_of_golden_globes_2013_info = golden_globes_2013_html.index("true}}") + len("true}}")
golden_globes_2013_info = golden_globes_2013_html[start_index_of_golden_globes_2013_info:end_index_of_golden_globes_2013_info]
golden_globes_2013_info = golden_globes_2013_info.replace("null", "None")
golden_globes_2013_info = golden_globes_2013_info.replace("true", "True")
golden_globes_2013_info = golden_globes_2013_info.replace("false", "False")
golden_globes_2013_info_dict = ast.literal_eval(golden_globes_2013_info)

golden_globe_2013_data_str = ""

for i, category in enumerate(golden_globes_2013_info_dict["nomineesWidgetModel"]["eventEditionSummary"]["awards"][0]["categories"]):
    golden_globe_2013_data_str += category['categoryName']
    for nomination in golden_globes_2013_info_dict["nomineesWidgetModel"]["eventEditionSummary"]["awards"][0]["categories"][i]["nominations"]:
        golden_globe_2013_data_str += "\n"
        golden_globe_2013_data_str += nomination["primaryNominees"][0]["name"] 
    golden_globe_2013_data_str += "\n\n"
    
def get_2013_award_data():
	return golden_globe_2013_data_str
