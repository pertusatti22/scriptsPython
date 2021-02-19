#minha primeira  API
import pandas as pd
from nba_api.stats.static import teams

def oneDict(listDict):
    keys = listDict[0].keys()
    outDict = {key:[] for key in keys}
    for dict_ in listDict:
        for key, value in dict_.items():
            outDict[key].append(value)
        return outDict
    dictNbaTeam = oneDict(nbaTeams)
    dfTeams = pd.DataFrame(dictNbaTeam)
    dfTeams.head()


nbaTeams = teams.get_teams()
nbaTeams[:5]

print(nbaTeams)

