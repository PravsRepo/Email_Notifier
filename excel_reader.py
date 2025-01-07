import pandas as pd
from datetime import date
import logging



class DataReader(): 

    def __init__(self, **kwargs) -> None:
        """Initiated..."""
        print("Datareader Initiated")
        self.file_name = kwargs['file_name']
        self.sheet_name = kwargs['sheet_name']
        self.log_filename = kwargs['log_filename']
        self.log_level = kwargs['log_level']
        self.date_format = kwargs['date_format']
        self.log_format = kwargs['log_format']
        logging.basicConfig(filename=self.log_filename, format=self.log_format,
                            level=self.log_level, datefmt=self.date_format, filemode='w') # Configure the logging module
        self.log = kwargs['excel_log']
        self.log.info("All variable are Initiated")

    # Reading the excel file using pandas
    def read_file(self):
        try:
            df = pd.read_excel(self.file_name, self.sheet_name)
            self.log.info('Read the file successfully')
            return df
        except FileNotFoundError:
            # print("File not found!")
            self.log.error('File not found') # Has to check e.message()
    
    def read_modified(self, modified_file_name):
        try:
            df = pd.read_excel(modified_file_name, self.sheet_name)
            self.log.info('Read the file successfully')
            return df
        except FileNotFoundError:
            # print("File not found!")
            self.log.error('File not found') # Has to check e.message()

    # Rename the columns(Replace space with underscore)
    def change_col_names(self, df):
        for i in df.columns:
            all_df = df.rename(columns=lambda i: i.replace(' ', '_'))
        self.log.info("Changed the column names")
        return all_df

    # Filtering the activity column and find the lecture is exist or not
    def check_date(self, df):
        mask_na = df[df['Activity_Type'].notna()]
        activity_df = mask_na[mask_na['Activity_Type'].str.contains(
            'Lecture')]  # Separate only Lecture activities
        practical_df = mask_na[mask_na['Activity_Type'].str.contains(
            'Practical')]

        # Getting only Mail_notification_date to compare with Present date
        date_values = activity_df['Mail_notification_date'].dt.date
        for i in date_values:
            if i == date.today():
                row_df = activity_df.loc[lambda activity_df: activity_df['Mail_notification_date'] == pd.Timestamp(
                    i)]
                return row_df
        else:
            return None

    # Get the data from the date filtered dataframe. If the dataframe is none, it returns none.
    def get_data_bs(self, df):
        if df is not None:
            df = df[['Phase', 'Theme', 'Activity', 'Activity_Type', 'Mode', 'Responsibilities',
                     'Mail_notification_date', 'Planned/Rescheduled_Start_Date', 'Planned/Rescheduled_End_Date', 'Duration']]
            mail_dict = df.to_dict(orient='records')
            return (mail_dict[0])
        else:
            self.log.info("None of the sessions aren't scheduled today")
            print("None of the sessions aren't scheduled today")
            return None


