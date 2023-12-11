import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.content

    def program_school(self):
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])
        return programs_list

# Comment out the line programs = GetPrograms.get_programs()
# print(programs)

# Create an instance of GetPrograms
programs_instance = GetPrograms()

# Fetch and process program data
programs_schools = programs_instance.program_school()

# Print out the unique list of schools
for school in set(programs_schools):
    print(school)