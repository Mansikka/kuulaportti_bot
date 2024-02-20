import urllib.request
import json
from datetime import datetime as DateTime


#Team ID here
team_id = 165

        
def main():
    
    #Fetch JSON data
    page = urllib.request.urlopen(f'https://kuulaportti.fi/ajax.php?request=events&type=team&id={team_id}')
    contents = page.read()
    json_data = json.loads(contents)
    data = json_data['data']
    
    
    today = DateTime.now()
    next_id = 0
    next_date = today
    name = ''
    #Go through data
    for entry in data:
        id = entry['id']
        start_d = entry['event_start_d']
        start_date = DateTime.fromisoformat(start_d['date'])
        
        #Skip all old
        if start_date < today:
            continue
        
        if next_id == 0 or start_date < next_date:
            next_id = id
            next_date = start_date
    
    
main()