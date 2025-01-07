import schedule
import time
from excel_reader import DataReader
from mail_bs_as import Send_mail
import logging


def do_schedule():
    print("Scheduler Initiated")
    create_obj()
    while True:
        schedule.run_pending(decide_flag())
        time.sleep(1)


def new_job(file_path, data_obj, mail_obj):
    if file_path.endswith('Test_file.xlsx'):
        all_df = data_obj.read_modified(file_path)
        altered_df = data_obj.change_col_names(all_df)
        filtered_df = data_obj.check_date(altered_df)
        mail_data = data_obj.get_data_bs(filtered_df)
        mail_obj.send_mail_before_session(mail_data)
        return schedule.CancelJob
    else:
        return None


def job_works_daily(data_obj, mail_obj):
    # Do some work that only needs to happen once...
    print("Initiated...")
    all_df = data_obj.read_file()
    altered_df = data_obj.change_col_names(all_df)
    filtered_df = data_obj.check_date(altered_df)
    mail_data = data_obj.get_data_bs(filtered_df)
    mail_obj.send_mail_before_session(mail_data)
    print("cancel the job")
    return schedule.CancelJob


def decide_flag(get_flag, file_path):
    if get_flag == True:
        schedule.every().minute.at(":30").do(new_job(file_path))
    else:
        schedule.every().minute.at(":30").do(job_works_daily())


def create_obj():
    file_name = 'data/Test_file.xlsx'
    sheet_name = 'Schedule'
    mail_log_filename = 'my_mail.log'
    excel_log_filename = 'excel.log'
    log_level = logging.DEBUG
    log_format = '%(levelname)s:%(message)s %(asctime)s'
    date_format = '%d/%m/%Y %I:%M:%S %p'
    mail_log = logging.getLogger(__name__)
    excel_log = logging.getLogger(__name__)

    data_obj = DataReader(file_name=file_name, sheet_name=sheet_name, log_filename=excel_log_filename,
                          log_level=log_level, date_format=date_format, log_format=log_format, excel_log=excel_log)

    mail_obj = Send_mail(log_filename=mail_log_filename, log_level=log_level,
                         date_format=date_format, log_format=log_format, mail_log=mail_log)

    return data_obj, mail_obj