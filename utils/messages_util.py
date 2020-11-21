from utils.sql_connect_utils import connect
import pandas as pd


def set_push_notification_message(is_written: bool) -> str:
    push_message = None
    db = connect()

    if is_written:
        query = "SELECT CONTENT FROM CORE_PUSHNOTIFICATIONMESSAGE WHERE TYPE = 'h' ORDER BY RANDOM() LIMIT 1"
    else:
        query = "SELECT CONTENT FROM CORE_PUSHNOTIFICATIONMESSAGE WHERE TYPE = 'r' ORDER BY RANDOM() LIMIT 1"
    try:
        push_message = str(pd.read_sql_query(query, db)['content'][0])
    except IndexError:
        push_message = "[서버알림] 리마인더 문구를 등록하세요!"

    return push_message
