from typing import List

from utils.users_util import get_users_who_set_notification_time_as_now
from utils.push_notification_util import set_push_notification_infos, send_push_notification


def send_push_notification_for_reminder_or_happy_words(event, context):
    """
    # TODO
    매 분 마다 유저가 지정한 시각에 특정 푸시 알림을 보낸다.
    현재 시각과 같은 유저들이 지정한 시각의 데이터를 가져온다.
    유저들의 일기 작성 여부를 나누어 작업한다.
    작성한 경우 : 행복 문구를 푸시알림으로 보내준다
    작성하지 않은 경우 : 일기 작성을 유도하는 푸시알림으로 보낸다.
    """
    user_infos: List = get_users_who_set_notification_time_as_now()
    push_notification_infos: List = [
        set_push_notification_infos(user_info) for user_info in user_infos
    ]
    [
        send_push_notification(
            set_push_notification_infos.message, set_push_notification_infos.push_notification_token
        )
        for push_notification_info in push_notification_infos
    ]
