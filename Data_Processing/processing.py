import pandas as pd
def extract_data(filename):
    data = pd.read_excel(filename, sheet_name="Data")
    meta = pd.read_excel(filename, sheet_name="Metadata")
    data_processed = pd.DataFrame([data["Time [s]"],data["Average [m/s]"]]).transpose().rename(columns={'Time [s]': 't', 'Average [m/s]': 'v'})
    
    return {"data":data_processed, "metadata":meta}

def cut_to_start(sim1):
    start = sim1["data"].where(sim1["data"]["v"]>0.001)["t"].idxmin()
    data =  sim1["data"].iloc[start:]
    time_shifted = data['t'] -  data['t'].min()
    data = pd.DataFrame([time_shifted,data['v']]).transpose()
    return data 