import random

#Each team is assigned a certain amount of 4-ball combinations
#14 teams in the lottery -> 14 choose 4 == 1001
#For simplicity, only 1000 combinations are assigned
#If the 1 combination is selected, they re-roll


def main():
    teams = []
    addTeams(teams)
    print(calcDraftPosition(teams))
    
#2024 draft lottery teams
#add in the teams with the amount of 4-ball combinations they would
#receive accordign to nba.com
def addTeams(teams):
    for i in range(140):
        teams.append("DET")
    for i in range(140):
        teams.append("WSH")
    for i in range(133):
        teams.append("CHA")
    for i in range(132):
        teams.append("POR")
    for i in range(105):
        teams.append("SAN")
    for i in range(90):
        teams.append("TOR")
    for i in range(75):
        teams.append("MEM")
    for i in range(60):
        teams.append("UTA")
    for i in range(45):
        teams.append("BKN")
    for i in range(30):
        teams.append("ATL")
    for i in range(20):
        teams.append("CHI")
    for i in range(15):
        teams.append("HOU")
    for i in range(8):
        teams.append("SAC")
    for i in range(7):
        teams.append("GSW")

#calculating which pick the pistons will receive
def calcDraftPosition(teams):
    selected = ["", "", "", ""]
    detPostion = 0
    for i in range(4):
        #this random int represents one of the 1001 possible 4-ball combinations
        n = random.randint(1, 1001)
        #check for re-rolls
        while n==1001 or teams[n] in selected:
            n = random.randint(1, 1001)
        #assign team to first pick through fourth pick
        selected[i] = teams[n]
        #check if Detriot was the team selected
        if selected[i] == "DET":
            detPosition = i + 1
    #under current lottery rules, the team with the worst record will have
    #the fifth pick at worst
    if "DET" not in selected:
        detPosition = 5
    return detPosition




main()