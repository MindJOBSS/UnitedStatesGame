import pandas as pd

class States:
    def __init__(self):
        self.states_file = pd.read_csv("./50_states.csv")
        self.states_names = self.states_file["state"].to_list()

    def is_in_states(self , guess_name):
        if guess_name in self.states_names:
            return True
        return  False

    def get_coordinates(self , state_name):
        coordinates = self.states_file.loc[self.states_file["state"] == state_name]
        x = coordinates["x"].item()
        y = coordinates["y"].item()
        return (x , y)

    def get_missing_file(self , list_of_known):
        missing_list = [state for state in self.states_names if state not in list_of_known]
        return missing_list

