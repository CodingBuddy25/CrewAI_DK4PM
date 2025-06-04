import pandas as pd
import pm4py

class CSV_format_O2C:
    case = "Case id"
    activity = "Activity name"
    timestamp = "Timestamp"
    sep = ';'

class CSV_format_P2P:
    case = "case_id"
    activity = "activity"
    timestamp = "timestamp"
    sep = ','


class CSV_format_AP:
    case = "Case ID"
    activity = "Activity"
    timestamp = "Timestamp"
    sep = ','

def Event_log_readings(file_path: str, file: str) -> str:
    """ basically the function is that of the Process discovery of Max in Tools, process mining, process mining tool
Event_log_readings is called a tool right now but I want to change it to a normal function, it is not a tool per se
"""
    # Distinction between CSV and XES file formats
    if file == "O2C.csv":
        used_class = CSV_format_O2C
        formatvariable = ('mixed')
    elif file == "purchase_to_pay_event_log.csv":
        used_class = CSV_format_P2P
        formatvariable = 'ISO8601'
    elif file == "AP_event_log_26052023.csv":
        used_class = CSV_format_AP
        formatvariable = 'mixed'

    if "csv" in file_path:
        # For CSV file formats paramters for 3 columns have to be set manually here
        df = pd.read_csv(file_path, sep=used_class.sep)

        # If required, convert time format
        df[used_class.timestamp] = pd.to_datetime(df[used_class.timestamp], format=formatvariable)
        df = pm4py.format_dataframe(df, case_id=used_class.case, activity_key=used_class.activity,
                                    timestamp_key=used_class.timestamp)

        event_log = pm4py.convert_to_event_log(df)
    else:
        # Reading the event log directly from XES file
        event_log = pm4py.read_xes(file_path)
    return event_log
